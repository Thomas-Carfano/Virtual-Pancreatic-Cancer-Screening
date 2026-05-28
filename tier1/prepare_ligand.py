#!/usr/bin/env python3
"""
prepare_ligand.py — turn a SMILES string into a docking-ready PDBQT.

This is the bug-#1-safe prep path for NOVEL molecules. Unlike Tier 0 (which had a
crystal structure to use as a bond-order template), screening compounds come as bare
SMILES, so we build them up explicitly:

    SMILES
      -> Dimorphite-DL protonation at pH 7.4   (dominant microspecies; basic amines
                                                 get protonated, acids deprotonated)
      -> RDKit parse + AddHs
      -> ETKDGv3 3D embedding (fixed seed) + MMFF (UFF fallback) optimization
      -> Meeko PDBQT  (correct rotatable bonds + Gasteiger charges)

Protonation is load-bearing here: it changes formal charge and therefore the Vina
electrostatics/H-bond terms. Getting it from coordinates (the Tier 0 OpenBabel path)
is unreliable for drug-like molecules — hence Dimorphite-DL.

Use as a library (batch_dock imports `prepare_ligand`) or as a one-off CLI:

    python prepare_ligand.py --smiles "CC(=O)Oc1ccccc1C(=O)O" --name aspirin -o aspirin.pdbqt
"""
import sys
import argparse
import warnings
from pathlib import Path
from dataclasses import dataclass

# Dimorphite-DL imports a deprecated rdkit.Chem.MolStandardize submodule; silence the noise.
warnings.filterwarnings("ignore", category=DeprecationWarning)


@dataclass
class PrepResult:
    ok: bool
    name: str
    smiles_in: str
    smiles_protonated: str = ""
    pdbqt_path: str = ""
    error: str = ""


def _protonate(smiles: str, ph: float = 7.4) -> str:
    """Return the dominant protonation state at the given pH (or the input on failure)."""
    import dimorphite_dl
    try:
        # precision=0.0 -> the single DOMINANT microspecies at this pH. (The default
        # precision=1.0 enumerates near-pKa variants and does not reliably put the
        # dominant state first, which silently left basic amines un-protonated.)
        out = dimorphite_dl.protonate_smiles(smiles, ph_min=ph, ph_max=ph,
                                             precision=0.0, max_variants=1)
        return out[0] if out else smiles
    except Exception:
        return smiles


def prepare_ligand(smiles: str, name: str, out_pdbqt, ph: float = 7.4, seed: int = 42) -> PrepResult:
    """SMILES -> protonate -> 3D embed -> Meeko PDBQT. Never raises; returns PrepResult."""
    from rdkit import Chem
    from rdkit.Chem import AllChem
    from meeko import MoleculePreparation, PDBQTWriterLegacy

    res = PrepResult(ok=False, name=name, smiles_in=smiles)
    try:
        prot = _protonate(smiles, ph)
        res.smiles_protonated = prot

        mol = Chem.MolFromSmiles(prot)
        if mol is None:                       # protonated SMILES unparseable -> try the original
            mol = Chem.MolFromSmiles(smiles)
            res.smiles_protonated = smiles
        if mol is None:
            res.error = "RDKit could not parse SMILES"
            return res

        mol = Chem.AddHs(mol)
        params = AllChem.ETKDGv3()
        params.randomSeed = seed
        if AllChem.EmbedMolecule(mol, params) != 0:
            params.useRandomCoords = True     # retry path for awkward geometries
            if AllChem.EmbedMolecule(mol, params) != 0:
                res.error = "3D embedding failed"
                return res

        try:
            if AllChem.MMFFHasAllMoleculeParams(mol):
                AllChem.MMFFOptimizeMolecule(mol, maxIters=500)
            else:
                AllChem.UFFOptimizeMolecule(mol, maxIters=500)
        except Exception:
            pass                              # ETKDG geometry is usually fine even if min. hiccups

        setups = MoleculePreparation().prepare(mol)
        if not setups:
            res.error = "Meeko produced no molecule setups"
            return res
        pdbqt, ok, err = PDBQTWriterLegacy.write_string(setups[0])
        if not ok:
            res.error = f"Meeko PDBQT write failed: {err}"
            return res

        out_pdbqt = Path(out_pdbqt)
        out_pdbqt.parent.mkdir(parents=True, exist_ok=True)
        out_pdbqt.write_text(pdbqt)
        res.pdbqt_path = str(out_pdbqt)
        res.ok = True
        return res
    except Exception as e:
        res.error = f"{type(e).__name__}: {e}"
        return res


def main():
    ap = argparse.ArgumentParser(description="SMILES -> docking-ready PDBQT")
    ap.add_argument("--smiles", required=True)
    ap.add_argument("--name", default="ligand")
    ap.add_argument("-o", "--out", required=True)
    ap.add_argument("--ph", type=float, default=7.4)
    ap.add_argument("--seed", type=int, default=42)
    a = ap.parse_args()
    r = prepare_ligand(a.smiles, a.name, Path(a.out), ph=a.ph, seed=a.seed)
    if r.ok:
        print(f"OK   {r.name}: {r.pdbqt_path}")
        print(f"     protonated @ pH {a.ph}: {r.smiles_protonated}")
    else:
        print(f"FAIL {r.name}: {r.error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
