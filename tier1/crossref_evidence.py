#!/usr/bin/env python3
"""
crossref_evidence.py — corroborate docking candidates against REAL measured experimental data.

A docking score is a prediction. The most honest, cheapest way to make it more credible is to
ask: has this molecule *actually been measured* binding the target before? ChEMBL aggregates
literature-reported bioactivities (IC50/Ki/Kd/EC50…), so for each candidate we:

  1. SMILES -> standard InChIKey -> connectivity skeleton (first 14 chars)
  2. skeleton -> ALL ChEMBL structure variants of that compound (salt/stereo/parent forms)
  3. aggregate measured activities of ANY variant against the EXACT target
  4. classify the evidence:
       DIRECT   — a measured activity vs THIS target exists in ChEMBL  (strong corroboration)
       none     — compound is in ChEMBL but has no measured activity vs this target
       no-map   — compound not found in ChEMBL

Why the skeleton (not the exact InChIKey): ChEMBL files a drug's measured activity under a
specific salt/stereo/parent entry, which often differs from the salt-stripped structure we
docked. Matching on connectivity and aggregating across variants is what actually recovers the
data (verified: EB-47's PARP1 Ki is filed under a variant the exact key misses).

This does NOT prove a candidate works — it shows whether an independent experiment already
touched the same target. Known binders should light up DIRECT (built-in sanity check); most
repurposed drugs will be 'none' (expected — approved for other diseases).

    python crossref_evidence.py --candidates ../candidates/PARP1/top50.csv \
        --target-chembl-id CHEMBL3105 --target-name PARP1 --out ../candidates/PARP1/top50_evidence.csv
"""
import csv
import json
import time
import argparse
import urllib.request
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
from rdkit import Chem

CHEMBL = "https://www.ebi.ac.uk/chembl/api/data"
MAX_VARIANTS = 25   # cap structure variants checked per compound (covers heavily-salted scaffolds)


def chembl_get(url, tries=4):
    for k in range(tries):
        try:
            req = urllib.request.Request(url, headers={"Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if k == tries - 1:
                return None
            time.sleep(1.5 * (k + 1))
        except Exception:
            if k == tries - 1:
                return None
            time.sleep(1.5 * (k + 1))
    return None


def skeleton_from_smiles(smiles):
    """Standard-InChIKey connectivity block (first 14 chars). Ignores salt/stereo/protonation."""
    m = Chem.MolFromSmiles(smiles)
    if m is None:
        return None
    try:
        return Chem.MolToInchiKey(m)[:14]
    except Exception:
        return None


def chembl_variants_by_skeleton(skel):
    """All ChEMBL molecules whose standard InChIKey starts with this connectivity block."""
    url = (f"{CHEMBL}/molecule.json?molecule_structures__standard_inchi_key__istartswith={skel}"
           f"&limit={MAX_VARIANTS}")
    d = chembl_get(url)
    if not d or not d.get("molecules"):
        return []
    out = []
    for m in d["molecules"]:
        out.append((m.get("molecule_chembl_id"), m.get("pref_name"), m.get("max_phase")))
    return out


def aggregate_activity(mol_ids, target_id):
    """Aggregate measured activities (with pChEMBL) across all variant molecules vs the target."""
    n_total, best, types = 0, None, set()
    for mid in mol_ids:
        url = (f"{CHEMBL}/activity.json?molecule_chembl_id={mid}"
               f"&target_chembl_id={target_id}&pchembl_value__isnull=false&limit=200")
        d = chembl_get(url)
        if not d or not d.get("activities"):
            continue
        for a in d["activities"]:
            n_total += 1
            try:
                v = float(a["pchembl_value"])
                best = v if best is None else max(best, v)
            except (TypeError, ValueError, KeyError):
                pass
            if a.get("standard_type"):
                types.add(a["standard_type"])
        time.sleep(0.05)
    return {"n": n_total, "best_pchembl": best, "types": "|".join(sorted(types))}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidates", required=True)
    ap.add_argument("--target-chembl-id", required=True)
    ap.add_argument("--target-name", default="target")
    ap.add_argument("--out", required=True)
    ap.add_argument("--top", type=int, default=50)
    ap.add_argument("--smiles-col", default="smiles")
    ap.add_argument("--name-col", default="drug_name")
    args = ap.parse_args()

    rows = list(csv.DictReader(open(args.candidates)))[:args.top]
    name_col = args.name_col if rows and args.name_col in rows[0] else ("label" if rows and "label" in rows[0] else "id")
    print(f"cross-referencing {len(rows)} candidates vs {args.target_name} ({args.target_chembl_id}) ...")

    out_rows = []
    n_direct = n_none = n_nomap = 0
    for i, r in enumerate(rows, 1):
        name = r.get(name_col, "?")
        smi = r.get(args.smiles_col, "")
        score = r.get("affinity_kcal_mol") or r.get("affinity") or ""
        skel = skeleton_from_smiles(smi)
        evidence, rep_name, best, n_act, types, n_variants = "no-map", "", None, 0, "", 0
        if skel:
            variants = chembl_variants_by_skeleton(skel)
            n_variants = len(variants)
            if variants:
                rep_name = next((p for _, p, _ in variants if p), "")
                act = aggregate_activity([v[0] for v in variants], args.target_chembl_id)
                n_act, best, types = act["n"], act["best_pchembl"], act["types"]
                evidence = "DIRECT" if act["n"] > 0 else "none"
            time.sleep(0.05)
        if evidence == "DIRECT": n_direct += 1
        elif evidence == "none": n_none += 1
        else: n_nomap += 1
        out_rows.append({
            "rank": i, "drug_name": name, "predicted_score": score,
            "evidence_vs_target": evidence,
            "measured_pchembl_vs_target": f"{best:.2f}" if isinstance(best, float) else "",
            "n_measured_activities": n_act, "assay_types": types,
            "chembl_variants_checked": n_variants, "chembl_pref_name": rep_name or "",
        })
        if evidence == "DIRECT":
            bs = f"{best:.2f}" if isinstance(best, float) else "n/a"
            tag = f"*** DIRECT  measured vs {args.target_name}: pChEMBL {bs} ({types})"
        elif evidence == "none":
            tag = "    none"
        else:
            tag = "    (not in ChEMBL)"
        print(f"  [{i:>2}] {str(name)[:24]:<25}{tag}")

    out = Path(args.out)
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out_rows[0].keys()))
        w.writeheader()
        w.writerows(out_rows)
    print(f"\n=== {args.target_name}: {n_direct} DIRECT, {n_none} none, {n_nomap} not-in-ChEMBL (of {len(rows)}) ===")
    print(f"-> {out}")


if __name__ == "__main__":
    main()
