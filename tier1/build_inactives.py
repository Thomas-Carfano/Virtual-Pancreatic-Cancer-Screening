#!/usr/bin/env python3
"""
build_inactives.py — fetch CONFIRMED-INACTIVE compounds for a target from ChEMBL.

Decoys (property-matched, topologically dissimilar molecules) are PRESUMED inactive — they were
never actually tested against the target. This builds a STRONGER negative set: compounds that
were EXPERIMENTALLY measured against the target and found weak/inactive (true negatives). Use it
to run a tougher enrichment gate (actives vs confirmed-inactives) than the decoy gate.

Confirmed-inactive = has a measured activity vs the target with pChEMBL <= --max-inactive-pchembl
(default 5.0, i.e. potency weaker than ~10 uM) AND is NOT also a known active (pChEMBL >=
--active-pchembl in any assay — those are excluded so we don't mislabel a real binder).

    python build_inactives.py --target-chembl-id CHEMBL3105 --target-name PARP1 \
        --actives ../tier2/targets/9ETQ/enrichment/actives.csv \
        --out ../tier2/targets/9ETQ/confirmed_inactives.csv \
        --gate-out ../tier2/targets/9ETQ/gate_confirmed_compounds.csv

Honest caveat: "measured weak vs this target" is a far stronger negative than a decoy, but it is
still assay/condition-dependent (a compound weak in one assay could bind in another context).
"""
import csv
import time
import argparse
import urllib.request
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
from rdkit import Chem
from rdkit.Chem import Descriptors, rdMolDescriptors

CHEMBL = "https://www.ebi.ac.uk/chembl/api/data"


def chembl_get(url, tries=4):
    for k in range(tries):
        try:
            req = urllib.request.Request(url, headers={"Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=60) as r:
                import json
                return json.loads(r.read())
        except Exception:
            if k == tries - 1:
                raise
            time.sleep(2 * (k + 1))


def fetch_active_ids(target_id, active_pchembl, hard_cap=100000):
    """Molecule ids with pChEMBL >= active_pchembl (any assay) — these get EXCLUDED from inactives.
    Must be EXHAUSTIVE: a missed active could leak into the 'confirmed inactive' set as a false
    negative. The cap is only a runaway guard, set far above any single target's activity count;
    if it is ever hit, warn loudly that exclusion may be incomplete."""
    print(f"[exclude] fetching known actives (pChEMBL >= {active_pchembl}) to exclude ...")
    url = (f"{CHEMBL}/activity.json?target_chembl_id={target_id}"
           f"&pchembl_value__gte={active_pchembl}&limit=1000&offset=0")
    ids, fetched = set(), 0
    while url:
        d = chembl_get(url)
        for a in d["activities"]:
            fetched += 1
            if a.get("molecule_chembl_id"):
                ids.add(a["molecule_chembl_id"])
        nxt = d["page_meta"]["next"]
        url = ("https://www.ebi.ac.uk" + nxt) if nxt else None
        if fetched >= hard_cap:
            print(f"  WARNING: hit hard_cap={hard_cap} fetching actives — exclusion may be "
                  f"INCOMPLETE; an active could leak into the inactive set. Raise hard_cap.")
            break
    print(f"[exclude] {len(ids)} active molecule ids to exclude")
    return ids


def fetch_inactives(target_id, max_inactive_pchembl, exclude_ids, hard_cap=12000):
    """Distinct molecules measured weak (pChEMBL <= threshold) vs target, minus known actives."""
    print(f"[inactives] fetching measured-weak compounds (pChEMBL <= {max_inactive_pchembl}) ...")
    url = (f"{CHEMBL}/activity.json?target_chembl_id={target_id}"
           f"&pchembl_value__lte={max_inactive_pchembl}&pchembl_value__isnull=false"
           f"&order_by=pchembl_value&limit=1000&offset=0")     # weakest first
    out, fetched = {}, 0
    while url:
        d = chembl_get(url)
        for a in d["activities"]:
            fetched += 1
            cid, smi = a.get("molecule_chembl_id"), a.get("canonical_smiles")
            if not cid or not smi or cid in exclude_ids:
                continue
            try:
                pc = float(a.get("pchembl_value"))
            except (TypeError, ValueError):
                continue
            rec = out.setdefault(cid, {"smiles": smi, "weakest_pchembl": pc})
            rec["weakest_pchembl"] = min(rec["weakest_pchembl"], pc)
        nxt = d["page_meta"]["next"]
        url = ("https://www.ebi.ac.uk" + nxt) if nxt else None
        if fetched >= hard_cap:
            break
    print(f"[inactives] {fetched} weak activity rows -> {len(out)} distinct candidate inactives")
    return out


def drug_like(smi):
    m = Chem.MolFromSmiles(smi)
    if m is None:
        return False
    return 250 <= Descriptors.MolWt(m) <= 650 and rdMolDescriptors.CalcNumRotatableBonds(m) <= 15


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--target-chembl-id", required=True)
    ap.add_argument("--target-name", default="target")
    ap.add_argument("--actives", help="actives.csv (id column) — also excluded from inactives")
    ap.add_argument("--out", required=True, help="confirmed_inactives.csv")
    ap.add_argument("--gate-out", help="optional: actives + confirmed-inactives, ready for the gate")
    ap.add_argument("--max-inactive-pchembl", type=float, default=5.0)
    ap.add_argument("--active-pchembl", type=float, default=6.0)
    ap.add_argument("--cap", type=int, default=600)
    args = ap.parse_args()

    exclude = fetch_active_ids(args.target_chembl_id, args.active_pchembl)
    # also exclude ids already in the provided actives.csv (belt and suspenders)
    actives_rows = []
    if args.actives and Path(args.actives).exists():
        actives_rows = list(csv.DictReader(open(args.actives)))
        exclude |= {r["id"] for r in actives_rows}

    cand = fetch_inactives(args.target_chembl_id, args.max_inactive_pchembl, exclude)
    rows = []
    for cid, rec in cand.items():
        if drug_like(rec["smiles"]):
            rows.append((cid, rec["smiles"], round(rec["weakest_pchembl"], 2)))
    rows.sort(key=lambda r: r[2])          # weakest (most clearly inactive) first
    rows = rows[:args.cap]

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", newline="") as f:
        w = csv.writer(f); w.writerow(["id", "smiles", "label", "measured_weakest_pchembl"])
        for cid, smi, pc in rows:
            w.writerow([cid, smi, "confirmed_inactive", pc])
    print(f"\n[inactives] {len(rows)} drug-like confirmed-inactives -> {out}")

    if args.gate_out and actives_rows:
        gate = Path(args.gate_out)
        with open(gate, "w", newline="") as f:
            w = csv.writer(f); w.writerow(["id", "smiles", "label"])
            for r in actives_rows:
                w.writerow([r["id"], r["smiles"], "active"])
            for cid, smi, pc in rows:
                w.writerow([cid, smi, "decoy"])     # 'decoy' label so analyze_enrichment treats as negative
        print(f"[gate] {len(actives_rows)} actives + {len(rows)} confirmed-inactives -> {gate}")
        print(f"       (screen this with batch_dock, then analyze_enrichment for the confirmed-inactive gate)")


if __name__ == "__main__":
    main()
