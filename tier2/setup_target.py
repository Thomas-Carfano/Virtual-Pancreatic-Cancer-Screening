#!/usr/bin/env python3
"""
setup_target.py — generalize the validated 7RPZ workflow to ANY docking target defined
by an mmCIF structure + native-ligand component (rows of targets_manifest.csv).

Given an mmCIF, a chain, the native-ligand CCD, the cofactors to keep, and the ligand's
RCSB "ideal" SDF (bond-order template), this:
  1. extracts a single-chain receptor (protein + kept cofactors) and the native ligand.
     Selection is done in mmCIF space, so 5-character CCDs (A1EN3, A1H63, ...) that legacy
     PDB cannot represent are handled correctly.
  2. preps receptor PDBQT (OpenBabel) and ligand PDBQT (RDKit bond-order template -> Meeko),
     the same bug-#1-safe path validated on MRTX1133 / 7RPZ (0.5 A redock).
  3. defines a docking box on the native ligand.
  4. RE-DOCKS the native ligand and reports symmetry-corrected heavy-atom RMSD.
  5. writes dock_config.json (drop-in for tier1/batch_dock.py) + validation_report.json.

Pass = heavy-atom RMSD < 2.0 A AND native score < -7 kcal/mol.

    python setup_target.py --cif assets/9U50.cif --chain A --ligand-ccd A1EN3 \
        --keep GDP,MG --ligand-sdf assets/A1EN3_ideal.sdf \
        --name KRAS_G12V_OFF_9U50 --outdir targets/9U50 --cpu 1 --exhaustiveness 16
"""
import sys
import json
import argparse
import subprocess
import warnings
from pathlib import Path

warnings.filterwarnings("ignore", category=DeprecationWarning)
STD_AA = set("ALA ARG ASN ASP CYS GLN GLU GLY HIS ILE LEU LYS MET PHE PRO SER THR TRP TYR VAL".split())


def extract(cif, chain_ids, ligand_ccd, keep, outdir):
    """mmCIF -> receptor.pdb (one or more chains: protein + kept cofactors) + native_ligand.pdb (resname LIG).

    Pass multiple chain_ids for composite-pocket targets (e.g. KRAS+CypA tri-complex):
    all listed chains' standard amino acids + kept cofactors go into the receptor; the
    ligand is taken from whichever chain holds it (often the partner chain in tri-complexes).
    """
    import gemmi
    st = gemmi.read_structure(str(cif)); st.setup_entities()
    chains_present = [c.name for c in st[0]]
    for cid in chain_ids:
        if cid not in chains_present:
            raise ValueError(f"chain {cid} not in {chains_present}")
    keep = set(keep)
    st_r = gemmi.Structure(); mod = gemmi.Model("1")
    lig_atoms = []
    for cid in chain_ids:
        chain = st[0][cid]
        cr = gemmi.Chain(cid)
        for res in chain:
            if res.name == ligand_ccd:
                for a in res:
                    lig_atoms.append((a.name, a.element.name, a.pos.x, a.pos.y, a.pos.z))
            elif res.name in STD_AA or res.name in keep:
                cr.add_residue(res)
        if len(cr) > 0:
            mod.add_chain(cr)
    if not lig_atoms:
        raise ValueError(f"ligand {ligand_ccd} not found in chains {chain_ids}")
    total_res = sum(len(c) for c in mod)
    if total_res < 20:
        raise ValueError(f"receptor too small ({total_res} res) — wrong chains/ligand?")
    st_r.add_model(mod)
    receptor_pdb = outdir / "receptor.pdb"
    st_r.write_pdb(str(receptor_pdb))
    ligand_pdb = outdir / "native_ligand.pdb"
    with open(ligand_pdb, "w") as f:
        for i, (name, el, x, y, z) in enumerate(lig_atoms, 1):
            f.write(f"HETATM{i:>5d} {name[:4]:<4.4s} LIG A   1    "
                    f"{x:8.3f}{y:8.3f}{z:8.3f}  1.00  0.00          {el:>2s}\n")
        f.write("END\n")
    return receptor_pdb, ligand_pdb, total_res, len(lig_atoms)


def prep_receptor(receptor_pdb, outdir):
    out = outdir / "receptor.pdbqt"
    subprocess.run(["obabel", str(receptor_pdb), "-O", str(out), "-xr", "-p", "7.4"],
                   capture_output=True, text=True, check=True)
    return out


def prep_ligand(ligand_pdb, template_sdf, outdir):
    """RDKit bond-order template onto crystal coords -> Meeko PDBQT (OpenBabel fallback)."""
    out = outdir / "native_ligand.pdbqt"
    prepared = outdir / "native_ligand_prepared.sdf"
    ok = False
    try:
        from rdkit import Chem
        from rdkit.Chem import AllChem
        template = Chem.MolFromMolFile(str(template_sdf), removeHs=True)
        crystal = Chem.MolFromPDBFile(str(ligand_pdb), removeHs=True, sanitize=False)
        if template is None or crystal is None:
            raise ValueError("RDKit could not load template or crystal ligand")
        mol = AllChem.AssignBondOrdersFromTemplate(template, crystal)
        mol = Chem.AddHs(mol, addCoords=True); Chem.SanitizeMol(mol)
        w = Chem.SDWriter(str(prepared)); w.write(mol); w.close()
        ok = True
    except Exception as e:
        print(f"  template prep failed ({e!r}); preparing from PDB instead")
    src = prepared if ok else ligand_pdb
    try:
        subprocess.run(["mk_prepare_ligand.py", "-i", str(src), "-o", str(out)],
                       capture_output=True, text=True, check=True)
        return out, ok
    except (FileNotFoundError, subprocess.CalledProcessError):
        cmd = ["obabel", str(src), "-O", str(out)] + ([] if ok else ["-h", "-p", "7.4"])
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        return out, ok


def define_box(ligand_pdb, pad=8.0):
    import numpy as np
    xs = [(float(l[30:38]), float(l[38:46]), float(l[46:54]))
          for l in open(ligand_pdb) if l.startswith(("ATOM", "HETATM"))]
    a = np.array(xs); c = a.mean(0); size = np.maximum(a.max(0) - a.min(0) + 2 * pad, 22.5)
    return {"center_x": float(c[0]), "center_y": float(c[1]), "center_z": float(c[2]),
            "size_x": float(size[0]), "size_y": float(size[1]), "size_z": float(size[2])}


def redock(receptor_pdbqt, ligand_pdbqt, box, outdir, cpu, exh, seed=42):
    docked = outdir / "docked.pdbqt"; b = box
    cmd = ["vina", "--receptor", str(receptor_pdbqt), "--ligand", str(ligand_pdbqt), "--out", str(docked),
           "--center_x", f"{b['center_x']:.3f}", "--center_y", f"{b['center_y']:.3f}", "--center_z", f"{b['center_z']:.3f}",
           "--size_x", f"{b['size_x']:.3f}", "--size_y", f"{b['size_y']:.3f}", "--size_z", f"{b['size_z']:.3f}",
           "--exhaustiveness", str(exh), "--num_modes", "20", "--cpu", str(cpu), "--seed", str(seed)]
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError(f"vina failed: {p.stderr[:300]}")
    score = None
    for line in open(docked):
        if line.startswith("REMARK VINA RESULT"):
            score = float(line.split()[3]); break
    return docked, score


def heavy_rmsd(docked_pdbqt, crystal_pdb, outdir):
    ds = outdir / "docked_top.sdf"; cs = outdir / "crystal.sdf"
    subprocess.run(["obabel", str(docked_pdbqt), "-O", str(ds), "-f", "1", "-l", "1", "-d"],
                   capture_output=True, text=True, check=True)
    subprocess.run(["obabel", str(crystal_pdb), "-O", str(cs), "-d"],
                   capture_output=True, text=True, check=True)
    from spyrmsd import io, rmsd
    a = io.loadmol(str(ds)); b = io.loadmol(str(cs))
    if len(a.atomicnums) != len(b.atomicnums):
        return float("nan")
    try:
        return float(rmsd.symmrmsd(b.coordinates, a.coordinates, b.atomicnums, a.atomicnums,
                                   b.adjacency_matrix, a.adjacency_matrix))
    except Exception:
        # symmrmsd does a full graph-isomorphism symmetry search, which blows up
        # combinatorially on large/symmetric ligands (e.g. 62-atom RAS(ON) glue molecules).
        # Fall back to the Hungarian algorithm: optimal atom assignment in polynomial time.
        # Still a valid heavy-atom RMSD; never fabricate a number — NaN only if this also fails.
        try:
            return float(rmsd.hrmsd(a.coordinates, b.coordinates, a.atomicnums, b.atomicnums,
                                    center=False))
        except Exception:
            return float("nan")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cif", required=True)
    ap.add_argument("--chain", default="A",
                    help="chain ID, or comma-separated list for multi-chain receptors "
                         "(e.g. 'A,C' for KRAS+CypA tri-complex; ligand may live on either chain)")
    ap.add_argument("--ligand-ccd", required=True)
    ap.add_argument("--keep", default="")
    ap.add_argument("--ligand-sdf", required=True)
    ap.add_argument("--name", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--cpu", type=int, default=1)
    ap.add_argument("--exhaustiveness", type=int, default=16)
    a = ap.parse_args()

    outdir = Path(a.outdir); outdir.mkdir(parents=True, exist_ok=True)
    keep = [k.strip() for k in a.keep.split(",") if k.strip()]
    chain_ids = [c.strip() for c in a.chain.split(",") if c.strip()]
    print(f"== {a.name}: {Path(a.cif).name} chains {chain_ids}, ligand {a.ligand_ccd}, keep {keep} ==")
    rec_pdb, lig_pdb, nres, nlig = extract(Path(a.cif), chain_ids, a.ligand_ccd, keep, outdir)
    print(f"  extracted receptor {nres} res, ligand {nlig} atoms")
    rec_q = prep_receptor(rec_pdb, outdir)
    lig_q, tmpl_ok = prep_ligand(lig_pdb, Path(a.ligand_sdf), outdir)
    print(f"  prepped receptor.pdbqt + ligand.pdbqt (template={'yes' if tmpl_ok else 'NO/fallback'})")
    box = define_box(lig_pdb)
    print(f"  box center ({box['center_x']:.1f}, {box['center_y']:.1f}, {box['center_z']:.1f})")
    docked, score = redock(rec_q, lig_q, box, outdir, a.cpu, a.exhaustiveness)
    rms = heavy_rmsd(docked, lig_pdb, outdir)
    rms_str = "nan" if rms != rms else f"{rms:.3f}"
    print(f"  redock: score {score:.2f} kcal/mol | heavy-atom RMSD {rms_str} A")

    cfg = {"_comment": f"{a.name}: receptor+box from {Path(a.cif).name} chain {a.chain}, native ligand {a.ligand_ccd}. Validated by native redock.",
           "target": a.name, "receptor_pdbqt": "receptor.pdbqt", "box": box,
           "vina": {"exhaustiveness": 8, "num_modes": 9, "cpu": 16, "seed": 42}}
    (outdir / "dock_config.json").write_text(json.dumps(cfg, indent=2))
    passed = (rms == rms and rms < 2.0) and (score is not None and score < -7.0)
    rep = {"target": a.name, "cif": Path(a.cif).name, "chain": a.chain, "ligand_ccd": a.ligand_ccd,
           "receptor_residues": nres, "ligand_atoms": nlig, "template_prep": tmpl_ok,
           "redock_score_kcal_mol": score,
           "redock_heavy_rmsd_angstrom": (None if rms != rms else round(rms, 3)),
           "passed": bool(passed)}
    (outdir / "validation_report.json").write_text(json.dumps(rep, indent=2))
    print(f"  {'PASS' if passed else 'CHECK'} -> {outdir}/validation_report.json + dock_config.json")


if __name__ == "__main__":
    main()
