#!/usr/bin/env python3
"""
build_library.py — assemble a large drug-like screening library from the ChEMBL bulk
"chemical representations" file (one reliable download, ~2.4M molecules with clean SMILES).

Streams the gzip, keeps drug-like molecules (MW 250-650, parseable), and writes the first
N to a compounds CSV ready for batch_dock / al_screen. Stops as soon as N are kept, so it
does NOT have to process all 2.4M.

    python build_library.py --n 500000 --out ../libraries/chembl_druglike/compounds.csv
"""
import gzip
import csv
import argparse
import urllib.request
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
from rdkit import Chem
from rdkit.Chem import Descriptors

URL = "https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/chembl_37_chemreps.txt.gz"
GZ = "/tmp/chembl_37_chemreps.txt.gz"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=500000, help="number of drug-like molecules to keep")
    ap.add_argument("--out", required=True)
    ap.add_argument("--mw-min", type=float, default=250.0)
    ap.add_argument("--mw-max", type=float, default=650.0)
    args = ap.parse_args()

    gz = Path(GZ)
    if not gz.exists() or gz.stat().st_size < 100_000_000:
        print(f"downloading {URL} ...")
        urllib.request.urlretrieve(URL, GZ)
        print(f"  downloaded {gz.stat().st_size // 1048576} MB")
    else:
        print(f"using cached {GZ} ({gz.stat().st_size // 1048576} MB)")

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    scanned = kept = bad = 0
    with gzip.open(GZ, "rt") as f, open(out, "w", newline="") as fo:
        w = csv.writer(fo)
        w.writerow(["id", "smiles", "label"])
        header = f.readline()  # chembl_id \t canonical_smiles \t standard_inchi \t standard_inchi_key
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 2:
                continue
            cid, smi = parts[0], parts[1]
            scanned += 1
            if not smi or smi == "None":
                continue
            m = Chem.MolFromSmiles(smi)
            if m is None:
                bad += 1
                continue
            mw = Descriptors.MolWt(m)
            if not (args.mw_min <= mw <= args.mw_max):
                continue
            w.writerow([cid, smi, cid])
            kept += 1
            if kept % 50000 == 0:
                print(f"  kept {kept:,} / scanned {scanned:,}")
            if kept >= args.n:
                break
    print(f"\nDONE: kept {kept:,} drug-like molecules (scanned {scanned:,}, {bad:,} unparseable)")
    print(f"-> {out}")


if __name__ == "__main__":
    main()
