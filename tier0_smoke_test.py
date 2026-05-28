#!/usr/bin/env python3
"""
PancScan Tier 0 smoke test — re-dock MRTX1133 against PDB 7RPZ and recover the crystal pose.

Steps:
  1. Verify the conda environment has the tools we need
  2. Download PDB 7RPZ from RCSB
  3. Inspect the PDB to identify HETATM components (expect: 6IC = MRTX1133, GDP, MG)
  4. Split into receptor (protein + GDP + Mg²⁺) and native ligand (6IC = MRTX1133)
  5. Prepare PDBQT files (Meeko preferred; OpenBabel fallback)
  6. Define a docking box centered on the native ligand position
  7. Run AutoDock Vina (exhaustiveness 32, fixed seed)
  8. Compute symmetry-corrected RMSD of the top docked pose vs the crystal pose
  9. Parse all Vina scores
 10. Write a structured JSON + human-readable Markdown report

Run from `/Volumes/Storage April 2026/PancreaticCancer/pancscan/` with the `pancscan` conda env active:

    mamba activate pancscan
    python tier0_smoke_test.py

End state: `reports/tier0_report.json` and `reports/tier0_report.md` ready to share.
"""

import os
import sys
import json
import subprocess
import urllib.request
from pathlib import Path
from datetime import datetime


# -----------------------------------------------------------------------------
# Paths
# -----------------------------------------------------------------------------
HERE = Path(__file__).parent.resolve()
DATA_DIR = HERE / "data"
REPORTS_DIR = HERE / "reports"
DATA_DIR.mkdir(exist_ok=True)
REPORTS_DIR.mkdir(exist_ok=True)


# -----------------------------------------------------------------------------
# Step 1 — Environment check
# -----------------------------------------------------------------------------
def check_env() -> dict:
    """Verify the tools the script needs are present. Returns a dict of {tool: status}."""
    print("== Step 1: Environment check ==")
    results = {}

    # Python version
    results["python"] = sys.version.split()[0]

    # Vina CLI
    try:
        out = subprocess.run(["vina", "--version"], capture_output=True, text=True, check=True)
        results["vina"] = out.stdout.strip() or out.stderr.strip() or "found"
    except (FileNotFoundError, subprocess.CalledProcessError) as e:
        results["vina"] = f"MISSING ({e})"

    # OpenBabel CLI
    try:
        out = subprocess.run(["obabel", "-V"], capture_output=True, text=True, check=True)
        results["obabel"] = out.stdout.strip().split("\n")[0]
    except (FileNotFoundError, subprocess.CalledProcessError) as e:
        results["obabel"] = f"MISSING ({e})"

    # Python imports
    for mod in ("rdkit", "Bio", "numpy", "spyrmsd"):
        try:
            m = __import__(mod)
            ver = getattr(m, "__version__", "installed")
            results[mod] = ver
        except ImportError as e:
            results[mod] = f"MISSING ({e})"

    # Meeko (CLI is optional — script falls back to obabel)
    try:
        out = subprocess.run(
            ["mk_prepare_receptor.py", "--help"],
            capture_output=True, text=True, timeout=10,
        )
        results["meeko_cli"] = "found" if out.returncode == 0 else "found (returncode != 0)"
    except (FileNotFoundError, subprocess.TimeoutExpired):
        results["meeko_cli"] = "not on PATH (will use obabel fallback)"

    for tool, status in results.items():
        print(f"  {tool:14s}: {status}")

    missing_critical = [k for k, v in results.items()
                        if k in ("vina", "obabel", "rdkit", "Bio", "numpy", "spyrmsd")
                        and "MISSING" in str(v)]
    if missing_critical:
        print(f"\nERROR: missing critical tools: {missing_critical}")
        print("Try: mamba env create -f environment.yml && mamba activate pancscan")
        sys.exit(1)
    return results


# -----------------------------------------------------------------------------
# Step 2 — Download PDB
# -----------------------------------------------------------------------------
def download_pdb(target: str = "7RPZ") -> Path:
    print(f"\n== Step 2: Download PDB {target} ==")
    out_path = DATA_DIR / f"{target.lower()}.pdb"
    if out_path.exists() and out_path.stat().st_size > 1000:
        print(f"  {out_path.name} already exists ({out_path.stat().st_size} bytes), skipping")
        return out_path
    url = f"https://files.rcsb.org/download/{target}.pdb"
    print(f"  downloading {url}")
    try:
        urllib.request.urlretrieve(url, out_path)
        print(f"  wrote {out_path.name} ({out_path.stat().st_size} bytes)")
    except Exception as e:
        print(f"  ERROR: download failed: {e}")
        print(f"  Try downloading manually from https://www.rcsb.org/structure/{target}")
        sys.exit(1)
    return out_path


# -----------------------------------------------------------------------------
# Step 3 — Inspect HETATMs
# -----------------------------------------------------------------------------
def inspect_hetatms(pdb_path: Path) -> dict:
    """List every HETATM residue type in the PDB, with atom counts."""
    print("\n== Step 3: Inspect HETATM components ==")
    from Bio import PDB
    parser = PDB.PDBParser(QUIET=True)
    structure = parser.get_structure("S", str(pdb_path))
    components: dict[str, int] = {}
    for model in structure:
        for chain in model:
            for residue in chain:
                if residue.id[0] == " ":
                    continue  # standard amino acid
                resname = residue.resname.strip()
                components[resname] = components.get(resname, 0) + sum(1 for _ in residue)
    print("  HETATM components found:")
    for name, count in sorted(components.items(), key=lambda kv: -kv[1]):
        print(f"    {name:6s}: {count} atoms")
    return components


# -----------------------------------------------------------------------------
# Step 4 — Split receptor / native ligand
# -----------------------------------------------------------------------------
def split_receptor_ligand(pdb_path: Path, ligand_code: str = "6IC") -> tuple[Path, Path]:
    """Write receptor.pdb (protein + GDP + Mg) and native_ligand.pdb (just the named ligand)."""
    print(f"\n== Step 4: Split receptor + native ligand ({ligand_code}) ==")
    from Bio import PDB

    parser = PDB.PDBParser(QUIET=True)
    structure = parser.get_structure("S", str(pdb_path))

    keep_for_receptor = {"GDP", "MG"}  # cofactors that stay with the receptor

    class ReceptorSelect(PDB.Select):
        def accept_residue(self, residue):
            # keep standard amino acids
            if residue.id[0] == " ":
                return True
            # keep GDP + Mg cofactors
            if residue.resname.strip() in keep_for_receptor:
                return True
            return False

    class LigandSelect(PDB.Select):
        def __init__(self, code):
            self.code = code
        def accept_residue(self, residue):
            return residue.resname.strip() == self.code

    io = PDB.PDBIO()
    io.set_structure(structure)

    receptor_path = DATA_DIR / "receptor.pdb"
    ligand_path = DATA_DIR / "native_ligand.pdb"

    io.save(str(receptor_path), ReceptorSelect())
    io.save(str(ligand_path), LigandSelect(ligand_code))

    if ligand_path.stat().st_size < 100:
        print(f"  WARNING: native_ligand.pdb is suspiciously small ({ligand_path.stat().st_size} bytes)")
        print(f"  did the PDB use a different code for MRTX1133? See Step 3 output.")
    print(f"  receptor       -> {receptor_path.name} ({receptor_path.stat().st_size} bytes)")
    print(f"  native ligand  -> {ligand_path.name} ({ligand_path.stat().st_size} bytes)")
    return receptor_path, ligand_path


# -----------------------------------------------------------------------------
# Step 5a — Receptor PDBQT (OpenBabel: reliable, and keeps GDP + Mg cofactors)
# -----------------------------------------------------------------------------
def prepare_receptor_pdbqt(receptor_pdb: Path) -> Path:
    """Receptor -> PDBQT via OpenBabel.

    Deliberately OpenBabel, not Meeko: Meeko's polymer-based receptor prep needs
    explicit templates for non-standard residues and tends to drop or choke on the
    bound GDP + Mg2+ cofactors — which sit right next to the MRTX1133 pocket and must
    stay in the receptor. OpenBabel's rigid-receptor prep (-xr) keeps them and
    protonates at pH 7.4. The receptor is not where bug #1 lives (that's the ligand);
    a protein is well-behaved under distance-based bond perception.
    """
    print("\n== Step 5a: Prepare receptor PDBQT (OpenBabel) ==")
    receptor_pdbqt = DATA_DIR / "receptor.pdbqt"
    try:
        subprocess.run(
            ["obabel", str(receptor_pdb), "-O", str(receptor_pdbqt), "-xr", "-p", "7.4"],
            capture_output=True, text=True, check=True,
        )
        print(f"  receptor PDBQT -> {receptor_pdbqt.name}")
    except subprocess.CalledProcessError as e:
        print(f"  ERROR: obabel receptor prep failed: {e.stderr}")
        sys.exit(1)
    return receptor_pdbqt


# -----------------------------------------------------------------------------
# Step 5b — Ligand bond-order template (RCSB "ideal" SDF for the component)
# -----------------------------------------------------------------------------
def download_ligand_template(ligand_code: str) -> Path:
    """Fetch the RCSB Chemical Component 'ideal' SDF, which carries correct bond orders."""
    print("\n== Step 5b: Fetch ligand bond-order template ==")
    out = DATA_DIR / f"{ligand_code}_ideal.sdf"
    if out.exists() and out.stat().st_size > 200:
        print(f"  template {out.name} already present, skipping download")
        return out
    url = f"https://files.rcsb.org/ligands/download/{ligand_code}_ideal.sdf"
    print(f"  downloading {url}")
    try:
        urllib.request.urlretrieve(url, out)
        print(f"  wrote {out.name} ({out.stat().st_size} bytes)")
    except Exception as e:
        print(f"  WARNING: template download failed ({e}); ligand prep will fall back to OpenBabel")
    return out


# -----------------------------------------------------------------------------
# Step 5c — Ligand PDBQT (RDKit template -> Meeko): the bug-#1 fix
# -----------------------------------------------------------------------------
def prepare_ligand_pdbqt(ligand_pdb: Path, template_sdf: Path) -> Path:
    """Ligand -> PDBQT the robust way.

    Bug #1 was: preparing a drug-like ligand from a bare PDB lets the tool *guess*
    bond orders and protonation from 3D coordinates — unreliable for a molecule like
    MRTX1133 (fused heteroaromatics, an alkyne, three basic amines).

    Fix: stamp KNOWN bond orders from the RCSB ideal SDF onto the crystal coordinates
    via RDKit AssignBondOrdersFromTemplate, add explicit H, then hand the correct
    molecule to Meeko for PDBQT (correct rotatable bonds + charges). OpenBabel stays as
    a fallback so the script still runs if RDKit/Meeko/template are unavailable.

    NOTE: this reproduces the *deposited* protonation state (right for pose recovery).
    Physiological (pH 7.4) protonation of the basic centers is a Tier-1 refinement
    (e.g. Dimorphite-DL) and matters more for the score than for this self-dock.
    """
    print("\n== Step 5c: Prepare ligand PDBQT (RDKit template -> Meeko) ==")
    ligand_pdbqt = DATA_DIR / "native_ligand.pdbqt"
    prepared_sdf = DATA_DIR / "native_ligand_prepared.sdf"

    # --- Build a correct RDKit molecule: crystal coords + template bond orders + H
    prepared_ok = False
    try:
        from rdkit import Chem
        from rdkit.Chem import AllChem

        template = Chem.MolFromMolFile(str(template_sdf), removeHs=True)
        crystal = Chem.MolFromPDBFile(str(ligand_pdb), removeHs=True, sanitize=False)
        if template is None or crystal is None:
            raise ValueError("could not load template or crystal ligand into RDKit")

        mol = AllChem.AssignBondOrdersFromTemplate(template, crystal)
        mol = Chem.AddHs(mol, addCoords=True)
        Chem.SanitizeMol(mol)
        writer = Chem.SDWriter(str(prepared_sdf))
        writer.write(mol)
        writer.close()
        print(f"  bond orders assigned from {template_sdf.name}; wrote {prepared_sdf.name} "
              f"({mol.GetNumAtoms()} atoms incl. H)")
        prepared_ok = True
    except Exception as e:
        print(f"  template-based prep failed ({e!r}); preparing directly from PDB instead")

    meeko_input = prepared_sdf if prepared_ok else ligand_pdb

    # --- Meeko (works now that gemmi is installed) on the correct molecule
    try:
        subprocess.run(
            ["mk_prepare_ligand.py", "-i", str(meeko_input), "-o", str(ligand_pdbqt)],
            capture_output=True, text=True, check=True,
        )
        print(f"  ligand PDBQT (Meeko) -> {ligand_pdbqt.name}")
        return ligand_pdbqt
    except (FileNotFoundError, subprocess.CalledProcessError) as e:
        msg = e.stderr if hasattr(e, "stderr") and e.stderr else str(e)
        print(f"  Meeko ligand prep failed: {msg[:200]}")
        print(f"  falling back to OpenBabel")

    # --- OpenBabel fallback
    try:
        ob_cmd = ["obabel", str(meeko_input), "-O", str(ligand_pdbqt)]
        if not prepared_ok:
            ob_cmd += ["-h", "-p", "7.4"]   # only let obabel add H if we have no prepared SDF
        subprocess.run(ob_cmd, capture_output=True, text=True, check=True)
        print(f"  ligand PDBQT (OpenBabel) -> {ligand_pdbqt.name}")
    except subprocess.CalledProcessError as e:
        print(f"  ERROR: OpenBabel ligand prep also failed: {e.stderr}")
        sys.exit(1)
    return ligand_pdbqt


# -----------------------------------------------------------------------------
# Step 6 — Docking box
# -----------------------------------------------------------------------------
def define_box(ligand_pdb: Path, padding: float = 8.0) -> dict:
    """Center the docking box on the native ligand; size = ligand bbox + 2*padding."""
    print(f"\n== Step 6: Define docking box (padding {padding} Å) ==")
    coords = []
    with open(ligand_pdb) as f:
        for line in f:
            if line.startswith(("ATOM", "HETATM")):
                try:
                    x = float(line[30:38]); y = float(line[38:46]); z = float(line[46:54])
                    coords.append((x, y, z))
                except ValueError:
                    pass
    if not coords:
        print(f"  ERROR: no coordinates found in {ligand_pdb}")
        sys.exit(1)
    import numpy as np
    arr = np.array(coords)
    center = arr.mean(axis=0)
    extents = arr.max(axis=0) - arr.min(axis=0)
    size = extents + 2 * padding
    # Vina recommends each dim ≥ 22.5 Å for reliability; clamp upward
    size = np.maximum(size, 22.5)
    box = {
        "center_x": float(center[0]),
        "center_y": float(center[1]),
        "center_z": float(center[2]),
        "size_x":   float(size[0]),
        "size_y":   float(size[1]),
        "size_z":   float(size[2]),
        "n_ligand_atoms": len(coords),
    }
    print(f"  ligand center: ({box['center_x']:.2f}, {box['center_y']:.2f}, {box['center_z']:.2f})")
    print(f"  box size:      ({box['size_x']:.2f}, {box['size_y']:.2f}, {box['size_z']:.2f}) Å")
    return box


# -----------------------------------------------------------------------------
# Step 7 — Vina
# -----------------------------------------------------------------------------
def run_vina(receptor_pdbqt: Path, ligand_pdbqt: Path, box: dict,
             exhaustiveness: int = 32, num_modes: int = 20, cpu: int = 16, seed: int = 42) -> tuple[Path, Path]:
    print(f"\n== Step 7: Run AutoDock Vina (exhaustiveness {exhaustiveness}, cpu {cpu}, seed {seed}) ==")
    docked = DATA_DIR / "docked.pdbqt"
    log = DATA_DIR / "docking.log"
    cmd = [
        "vina",
        "--receptor", str(receptor_pdbqt),
        "--ligand",   str(ligand_pdbqt),
        "--out",      str(docked),
        "--center_x", f"{box['center_x']:.3f}",
        "--center_y", f"{box['center_y']:.3f}",
        "--center_z", f"{box['center_z']:.3f}",
        "--size_x",   f"{box['size_x']:.3f}",
        "--size_y",   f"{box['size_y']:.3f}",
        "--size_z",   f"{box['size_z']:.3f}",
        "--exhaustiveness", str(exhaustiveness),
        "--num_modes",      str(num_modes),
        "--cpu",            str(cpu),
        "--seed",           str(seed),
    ]
    print(f"  cmd: {' '.join(cmd[:6])} ... (full command in docking.log)")
    print("  (Vina is running; expect 1–5 min on M4 Max...)")
    result = subprocess.run(cmd, capture_output=True, text=True)
    with open(log, "w") as f:
        f.write("# Command:\n")
        f.write(" ".join(cmd) + "\n\n")
        f.write("# STDOUT:\n")
        f.write(result.stdout)
        f.write("\n# STDERR:\n")
        f.write(result.stderr)
    if result.returncode != 0:
        print(f"  ERROR: Vina returned non-zero ({result.returncode})")
        print(f"  stderr (first 800 chars):\n{result.stderr[:800]}")
        sys.exit(1)
    print(f"  docked poses -> {docked.name}")
    print(f"  log -> {log.name}")
    return docked, log


# -----------------------------------------------------------------------------
# Step 8 — RMSD vs crystal pose
# -----------------------------------------------------------------------------
def compute_rmsd(docked_pdbqt: Path, crystal_ligand_pdb: Path) -> float:
    """Symmetry-corrected, HEAVY-ATOM RMSD between docked top pose and crystal pose.

    Both molecules are stripped of hydrogens (obabel -d) before comparison. Vina's
    PDBQT output carries only polar H (united-atom model), so adding all H to the
    crystal side would create a hydrogen-count mismatch that breaks spyrmsd's graph
    matching. Heavy-atom RMSD is the standard re-docking metric anyway.

    Returns NaN (never a fabricated number) if the two heavy-atom graphs don't match,
    so an un-measurable test fails loudly instead of passing on garbage.
    """
    print("\n== Step 8: RMSD top-pose vs crystal (heavy atoms) ==")
    # Top docked pose (mode 1) -> heavy-atom-only SDF
    docked_sdf = DATA_DIR / "docked_top.sdf"
    subprocess.run(
        ["obabel", str(docked_pdbqt), "-O", str(docked_sdf), "-f", "1", "-l", "1", "-d"],
        capture_output=True, text=True, check=True,
    )
    # Crystal native ligand -> heavy-atom-only SDF (strip H so the graphs match)
    crystal_sdf = DATA_DIR / "crystal.sdf"
    subprocess.run(
        ["obabel", str(crystal_ligand_pdb), "-O", str(crystal_sdf), "-d"],
        capture_output=True, text=True, check=True,
    )

    from spyrmsd import io, rmsd
    docked_mol = io.loadmol(str(docked_sdf))
    crystal_mol = io.loadmol(str(crystal_sdf))

    if len(docked_mol.atomicnums) != len(crystal_mol.atomicnums):
        print(f"  INVALID TEST: heavy-atom counts differ "
              f"({len(docked_mol.atomicnums)} docked vs {len(crystal_mol.atomicnums)} crystal).")
        print(f"  The two structures are not the same species — RMSD is undefined.")
        return float("nan")

    try:
        val = rmsd.symmrmsd(
            crystal_mol.coordinates, docked_mol.coordinates,
            crystal_mol.atomicnums,   docked_mol.atomicnums,
            crystal_mol.adjacency_matrix, docked_mol.adjacency_matrix,
        )
    except Exception as e:
        print(f"  INVALID TEST: symmetry-corrected RMSD could not be computed ({e!r}).")
        print(f"  Heavy-atom graphs are not isomorphic (bond-perception mismatch).")
        print(f"  Fix: prep the ligand from a bond-order template (RCSB 6IC ideal SDF)")
        print(f"  so connectivity is identical on both sides. This is NOT a docking failure.")
        return float("nan")
    print(f"  heavy-atom RMSD = {val:.3f} Å")
    return float(val)


# -----------------------------------------------------------------------------
# Step 9 — Parse Vina log
# -----------------------------------------------------------------------------
def parse_vina_log(log_path: Path) -> list[dict]:
    """Pull the scoring table from Vina's stdout."""
    print("\n== Step 9: Parse Vina scores ==")
    scores: list[dict] = []
    with open(log_path) as f:
        in_table = False
        for line in f:
            s = line.strip()
            if s.startswith("mode |"):
                in_table = True
                continue
            if in_table:
                parts = s.split()
                if len(parts) >= 4 and parts[0].isdigit():
                    try:
                        scores.append({
                            "mode": int(parts[0]),
                            "affinity_kcal_mol": float(parts[1]),
                            "rmsd_lb": float(parts[2]),
                            "rmsd_ub": float(parts[3]),
                        })
                    except ValueError:
                        pass
                elif s == "":
                    if scores:
                        break
                elif s.startswith(("Writing", "----")):
                    continue
    print(f"  parsed {len(scores)} modes; top score: {scores[0]['affinity_kcal_mol']:.2f} kcal/mol")
    for s in scores[:5]:
        print(f"    mode {s['mode']}: {s['affinity_kcal_mol']:.2f}")
    return scores


# -----------------------------------------------------------------------------
# Step 10 — Report
# -----------------------------------------------------------------------------
def write_report(env: dict, hetatms: dict, ligand_code: str, box: dict,
                 scores: list[dict], rmsd: float) -> dict:
    print("\n== Step 10: Generate report ==")
    criteria = {
        "ligand_code_6IC_present_in_pdb": "6IC" in hetatms,
        "GDP_cofactor_present": "GDP" in hetatms,
        "Mg_cofactor_present": "MG" in hetatms,
        "rmsd_under_2_angstrom": rmsd < 2.0,
        "top_score_under_minus_8": scores and scores[0]["affinity_kcal_mol"] < -8.0,
    }
    passed = all(criteria.values())
    report = {
        "tier": 0,
        "target_pdb": "7RPZ",
        "target_description": "KRAS G12D + MRTX1133 + GDP + Mg²⁺",
        "ligand_code_used": ligand_code,
        "date_run": datetime.now().isoformat(),
        "environment": env,
        "pdb_hetatms": hetatms,
        "docking_box": box,
        "vina_scores": scores,
        "top_pose_score_kcal_mol": scores[0]["affinity_kcal_mol"] if scores else None,
        "rmsd_top_pose_vs_crystal_angstrom": rmsd,
        "acceptance_criteria": criteria,
        "passed": passed,
    }
    # JSON
    json_path = REPORTS_DIR / "tier0_report.json"
    with open(json_path, "w") as f:
        json.dump(report, f, indent=2)
    print(f"  JSON -> {json_path}")

    # Markdown
    md = []
    md.append(f"# PancScan Tier 0 Smoke Test Report\n")
    md.append(f"- **Date:** {report['date_run']}")
    md.append(f"- **Target:** PDB 7RPZ ({report['target_description']})")
    md.append(f"- **Ligand code used:** {ligand_code}")
    md.append(f"\n## Verdict\n")
    md.append(f"### {'✅ PASS' if passed else '❌ FAIL'}\n")
    md.append(f"## Acceptance criteria\n")
    md.append(f"| # | Criterion | Pass? |")
    md.append(f"|---|---|---|")
    for k, v in criteria.items():
        md.append(f"| | {k} | {'✅' if v else '❌'} |")
    md.append(f"\n## Key numbers\n")
    md.append(f"- Top-pose Vina score: **{scores[0]['affinity_kcal_mol']:.2f} kcal/mol**")
    md.append(f"- Top-pose RMSD vs crystal: **{rmsd:.3f} Å**\n")
    md.append(f"## HETATM components in PDB 7RPZ\n")
    md.append(f"| Component | Atom count |")
    md.append(f"|---|---|")
    for name, count in sorted(hetatms.items(), key=lambda kv: -kv[1]):
        md.append(f"| {name} | {count} |")
    md.append(f"\n## Docking box\n")
    md.append(f"- Center: ({box['center_x']:.2f}, {box['center_y']:.2f}, {box['center_z']:.2f})")
    md.append(f"- Size: ({box['size_x']:.2f}, {box['size_y']:.2f}, {box['size_z']:.2f}) Å")
    md.append(f"- Native ligand atoms: {box['n_ligand_atoms']}\n")
    md.append(f"## All Vina poses\n")
    md.append(f"| Mode | Affinity (kcal/mol) | RMSD LB | RMSD UB |")
    md.append(f"|---|---|---|---|")
    for s in scores:
        md.append(f"| {s['mode']} | {s['affinity_kcal_mol']:.2f} | {s['rmsd_lb']:.2f} | {s['rmsd_ub']:.2f} |")
    md.append(f"\n## Environment\n")
    for k, v in env.items():
        md.append(f"- {k}: {v}")
    md_path = REPORTS_DIR / "tier0_report.md"
    with open(md_path, "w") as f:
        f.write("\n".join(md) + "\n")
    print(f"  Markdown -> {md_path}")

    return report


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
def main():
    print(f"PancScan Tier 0 smoke test")
    print(f"Working directory: {HERE}")
    print(f"Started: {datetime.now().isoformat()}\n")

    env = check_env()
    pdb_path = download_pdb("7RPZ")
    hetatms = inspect_hetatms(pdb_path)

    # MRTX1133 in PDB 7RPZ should be component 6IC
    LIGAND_CODE = "6IC"
    if LIGAND_CODE not in hetatms:
        print(f"\nWARNING: expected component {LIGAND_CODE} (MRTX1133) not in HETATMs")
        print(f"  PDB contains: {sorted(hetatms.keys())}")
        # Pick the largest non-cofactor / non-water HETATM as candidate
        candidates = [n for n in hetatms if n not in ("GDP", "MG", "HOH", "ZN", "NA", "CL", "K")]
        if candidates:
            LIGAND_CODE = max(candidates, key=lambda n: hetatms[n])
            print(f"  using largest non-cofactor HETATM '{LIGAND_CODE}' instead")
        else:
            print(f"  no candidate ligand found; aborting")
            sys.exit(1)

    receptor_pdb, ligand_pdb = split_receptor_ligand(pdb_path, ligand_code=LIGAND_CODE)
    receptor_pdbqt = prepare_receptor_pdbqt(receptor_pdb)
    template_sdf = download_ligand_template(LIGAND_CODE)
    ligand_pdbqt = prepare_ligand_pdbqt(ligand_pdb, template_sdf)
    box = define_box(ligand_pdb, padding=8.0)
    docked, log = run_vina(receptor_pdbqt, ligand_pdbqt, box)
    rmsd = compute_rmsd(docked, ligand_pdb)
    scores = parse_vina_log(log)
    report = write_report(env, hetatms, LIGAND_CODE, box, scores, rmsd)

    print(f"\n{'='*60}")
    if report["passed"]:
        print(f"✅ Tier 0 PASSED")
    else:
        print(f"❌ Tier 0 FAILED — check reports/tier0_report.md for details")
    print(f"{'='*60}")
    print(f"\nSend these files back for validation:")
    print(f"  {REPORTS_DIR / 'tier0_report.json'}")
    print(f"  {REPORTS_DIR / 'tier0_report.md'}")
    print(f"  {DATA_DIR / 'docking.log'}")
    print()


if __name__ == "__main__":
    main()
