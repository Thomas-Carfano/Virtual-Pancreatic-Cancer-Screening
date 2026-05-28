#!/usr/bin/env python3
"""
build_enrichment_set.py — assemble an actives + property-matched decoys set for the
enrichment gate, for ANY ChEMBL protein target.

WHY: before screening unknown compounds, we must show the engine RANKS KNOWN binders
above presumed-inactive look-alikes. DUD-E-style property-matched decoys are the right
control (per the project's benchmark policy + the 2025 LIT-PCBA audit that ruled
LIT-PCBA out as a primary gate).

ACTIVES: real inhibitors from a ChEMBL target (e.g. CHEMBL2189121 = KRAS, CHEMBL3105 =
         PARP1) with pChEMBL >= threshold (<= ~1 uM). Filtered to drug-like small
         molecules (peptides / PPI-disruptors removed). Optionally tag/prioritize actives
         whose assay description contains a keyword (e.g. "G12D").
DECOYS : drug-like molecules sampled from ChEMBL, property-matched to each active
         (MW/logP/HBD/HBA/rotatable bonds) but topologically DISSIMILAR
         (ECFP4 Tanimoto < 0.35 to every active) -> presumed inactive.

Outputs into --out-dir: actives.csv, decoys.csv, enrichment_compounds.csv, provenance.md

    # KRAS:
    python build_enrichment_set.py --target-chembl-id CHEMBL2189121 \
        --target-name "KRAS (GTPase KRas)" --assay-keyword G12D --prefer-keyword --out-dir enrichment
    # PARP1:
    python build_enrichment_set.py --target-chembl-id CHEMBL3105 \
        --target-name "PARP1" --out-dir ../tier2/targets/9ETQ/enrichment
"""
import csv
import json
import time
import argparse
import urllib.request
from pathlib import Path
from datetime import datetime

import warnings
warnings.filterwarnings("ignore")
from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem, Descriptors, Crippen, rdMolDescriptors

CHEMBL = "https://www.ebi.ac.uk/chembl/api/data"


def chembl_get(url, tries=4):
    for k in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return json.loads(r.read())
        except Exception:
            if k == tries - 1:
                raise
            time.sleep(2 * (k + 1))


def fetch_actives(target_id, pchembl_min=6.0, keyword="", hard_cap=4000):
    """All distinct molecules for the target with pChEMBL >= threshold. Returns {id: {...}}."""
    print(f"[actives] fetching {target_id} activities (pChEMBL >= {pchembl_min}) ...")
    kw = keyword.lower()
    url = (f"{CHEMBL}/activity.json?target_chembl_id={target_id}"
           f"&pchembl_value__gte={pchembl_min}&limit=1000&offset=0")
    out, fetched = {}, 0
    while url:
        d = chembl_get(url)
        for a in d["activities"]:
            fetched += 1
            cid, smi = a.get("molecule_chembl_id"), a.get("canonical_smiles")
            if not cid or not smi:
                continue
            kw_match = bool(kw) and kw in (a.get("assay_description") or "").lower()
            rec = out.setdefault(cid, {"smiles": smi, "max_pchembl": 0.0, "kw": False})
            try:
                rec["max_pchembl"] = max(rec["max_pchembl"], float(a.get("pchembl_value") or 0))
            except (TypeError, ValueError):
                pass
            rec["kw"] = rec["kw"] or kw_match
        nxt = d["page_meta"]["next"]
        url = ("https://www.ebi.ac.uk" + nxt) if nxt else None
        if fetched >= hard_cap:
            break
    print(f"[actives] {fetched} activity rows -> {len(out)} distinct molecules")
    return out


def fetch_decoy_pool(target_count, mw_min, mw_max):
    """Sample drug-like molecules from ChEMBL (MW bracketing the actives) as decoy candidates."""
    print(f"[decoys] fetching ~{target_count} decoy candidates (MW {mw_min:.0f}-{mw_max:.0f}) ...")
    url = (f"{CHEMBL}/molecule.json?molecule_properties__full_mwt__gte={mw_min:.0f}"
           f"&molecule_properties__full_mwt__lte={mw_max:.0f}&limit=1000&offset=0")
    pool = {}
    while url and len(pool) < target_count:
        d = chembl_get(url)
        for m in d["molecules"]:
            cid = m.get("molecule_chembl_id")
            smi = (m.get("molecule_structures") or {}).get("canonical_smiles")
            if cid and smi:
                pool[cid] = smi
        nxt = d["page_meta"]["next"]
        url = ("https://www.ebi.ac.uk" + nxt) if nxt else None
    print(f"[decoys] decoy candidate pool: {len(pool)} molecules")
    return pool


def props(smiles):
    """RDKit physchem descriptors + ECFP4 fingerprint. None if unparseable."""
    m = Chem.MolFromSmiles(smiles)
    if m is None:
        return None
    return {
        "mw": Descriptors.MolWt(m), "logp": Crippen.MolLogP(m),
        "hbd": rdMolDescriptors.CalcNumHBD(m), "hba": rdMolDescriptors.CalcNumHBA(m),
        "rtb": rdMolDescriptors.CalcNumRotatableBonds(m), "charge": Chem.GetFormalCharge(m),
        "n_amide": len(m.GetSubstructMatches(Chem.MolFromSmarts("C(=O)N"))),
        "fp": AllChem.GetMorganFingerprintAsBitVect(m, 2, nBits=2048),
    }


def is_drug_like_active(p):
    """Keep small-molecule actives; drop peptides / PPI-disruptors / oversized."""
    return 250 <= p["mw"] <= 650 and p["rtb"] <= 15 and p["n_amide"] <= 4


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--target-chembl-id", default="CHEMBL2189121")
    ap.add_argument("--target-name", default="KRAS (GTPase KRas)")
    ap.add_argument("--assay-keyword", default="",
                    help="tag actives whose assay description contains this (e.g. G12D)")
    ap.add_argument("--prefer-keyword", action="store_true",
                    help="rank keyword-matching actives first when capping")
    ap.add_argument("--out-dir", default="enrichment")
    ap.add_argument("--pchembl-min", type=float, default=6.0)
    ap.add_argument("--actives-cap", type=int, default=40)
    ap.add_argument("--decoys-per-active", type=int, default=15)
    ap.add_argument("--decoy-pool", type=int, default=15000)
    ap.add_argument("--max-tanimoto", type=float, default=0.35)
    args = ap.parse_args()

    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    # ---- Actives ----
    raw = fetch_actives(args.target_chembl_id, args.pchembl_min, args.assay_keyword)
    actives = []
    for cid, rec in raw.items():
        p = props(rec["smiles"])
        if p and is_drug_like_active(p):
            actives.append((cid, rec["smiles"], rec["max_pchembl"], rec["kw"], p))
    actives.sort(key=lambda r: ((1 if (args.prefer_keyword and r[3]) else 0), r[2]), reverse=True)
    n_kw = sum(1 for a in actives if a[3])
    print(f"[actives] drug-like actives: {len(actives)}"
          + (f" (assay-keyword '{args.assay_keyword}': {n_kw})" if args.assay_keyword else ""))
    actives = actives[:args.actives_cap]
    active_fps = [a[4]["fp"] for a in actives]
    print(f"[actives] using top {len(actives)} actives")
    if not actives:
        print("ERROR: no drug-like actives found — check target id / filters."); return

    # ---- Decoys: property-match each active, enforce topological dissimilarity ----
    a_mw = [a[4]["mw"] for a in actives]
    pool = fetch_decoy_pool(args.decoy_pool, min(a_mw) - 30, max(a_mw) + 30)
    active_ids = {a[0] for a in actives}
    used, decoys = set(), []
    TOL = dict(mw=35.0, logp=1.5, hbd=1, hba=3, rtb=3)
    pool_items = [(cid, smi) for cid, smi in pool.items() if cid not in active_ids]
    pool_props = {}

    def get_pp(cid, smi):
        if cid not in pool_props:
            pool_props[cid] = props(smi)
        return pool_props[cid]

    for (acid, asmi, apc, akw, ap) in actives:
        picked = 0
        for cid, smi in pool_items:
            if picked >= args.decoys_per_active:
                break
            if cid in used:
                continue
            pp = get_pp(cid, smi)
            if pp is None:
                continue
            if (abs(pp["mw"] - ap["mw"]) <= TOL["mw"] and abs(pp["logp"] - ap["logp"]) <= TOL["logp"]
                    and abs(pp["hbd"] - ap["hbd"]) <= TOL["hbd"] and abs(pp["hba"] - ap["hba"]) <= TOL["hba"]
                    and abs(pp["rtb"] - ap["rtb"]) <= TOL["rtb"]):
                if max(DataStructs.BulkTanimotoSimilarity(pp["fp"], active_fps)) < args.max_tanimoto:
                    decoys.append((cid, smi, acid)); used.add(cid); picked += 1
        if picked < args.decoys_per_active:
            print(f"  [warn] only {picked}/{args.decoys_per_active} decoys for {acid}")
    print(f"[decoys] matched {len(decoys)} decoys total")

    # ---- Write outputs ----
    with open(out / "actives.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(["id", "smiles", "max_pchembl", "keyword_assay"])
        for a in actives:
            w.writerow([a[0], a[1], f"{a[2]:.2f}", a[3]])
    with open(out / "decoys.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(["id", "smiles", "matched_active"])
        for d in decoys:
            w.writerow(d)
    with open(out / "enrichment_compounds.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(["id", "smiles", "label"])
        for a in actives:
            w.writerow([a[0], a[1], "active"])
        for d in decoys:
            w.writerow([d[0], d[1], "decoy"])

    kw_line = (f"- {n_kw} of the actives come from an assay whose description mentions "
               f"'{args.assay_keyword}'.\n" if args.assay_keyword else "")
    prov = f"""# {args.target_name} enrichment set — provenance & limitations

Built {datetime.now().isoformat()} by build_enrichment_set.py

## Actives ({len(actives)})
- Source: ChEMBL target {args.target_chembl_id} ({args.target_name}), pChEMBL >= {args.pchembl_min} (<= ~1 uM).
- Filtered to drug-like small molecules: MW 250-650, rotatable bonds <= 15, amide groups <= 4
  (removes peptides / PPI-disruptor macrocycles).
{kw_line}
## Decoys ({len(decoys)})
- Source: drug-like ChEMBL molecules (MW bracketing the actives), excluding any known active.
- DUD-E-style property matching per active (tolerances: MW +/-{TOL['mw']}, logP +/-{TOL['logp']},
  HBD +/-{TOL['hbd']}, HBA +/-{TOL['hba']}, rotatable +/-{TOL['rtb']}).
- Topological dissimilarity enforced: ECFP4 Tanimoto < {args.max_tanimoto} to EVERY active.
- Target {args.decoys_per_active} decoys/active.

## Honest limitations
- This is an ENGINE SANITY CHECK, not a publication-grade selectivity benchmark.
- Decoys are PRESUMED inactive (not experimentally confirmed non-binders).
- Property matching reduces, but does not eliminate, trivial-feature enrichment bias.
"""
    (out / "provenance.md").write_text(prov)
    print(f"\nWrote: {out}/ (actives.csv, decoys.csv, enrichment_compounds.csv, provenance.md)")
    print(f"TOTAL to screen: {len(actives)} actives + {len(decoys)} decoys = {len(actives)+len(decoys)}")


if __name__ == "__main__":
    main()
