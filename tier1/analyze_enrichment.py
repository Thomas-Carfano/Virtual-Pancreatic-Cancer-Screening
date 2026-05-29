#!/usr/bin/env python3
"""
analyze_enrichment.py — does the docking engine rank known KRAS binders above decoys?

Reads a batch_dock results.csv (needs columns: label in {active,decoy}, affinity, dock_ok)
and computes standard virtual-screening enrichment metrics:

  - ROC-AUC          (rank-based; 0.5 = random, 1.0 = perfect)
  - Enrichment Factor at 1% / 5% / 10%   (EF1% etc.; 1.0 = random)
  - BEDROC (alpha=20)                    (early-recognition weighted; 0..1)
  - score separation (mean affinity, actives vs decoys)

A more-negative Vina affinity = better binder, so the ranking score is -affinity.

    python analyze_enrichment.py --results screen/enrichment_run/results.csv
"""
import sys
import csv
import json
import math
import argparse
from pathlib import Path


def load(results_csv, score_col="affinity", fail_score=1e9):
    """Load actives/decoys by label. Failed docks are ranked WORST (sentinel score), not
    dropped — dropping them silently biases AUC/EF if actives and decoys fail at different
    rates (a failed dock is a failed prediction and should count against the method)."""
    actives, decoys = [], []
    n_fail_active = n_fail_decoy = 0
    for r in csv.DictReader(open(results_csv)):
        lab = (r.get("label") or "").lower()
        ok = r.get("dock_ok") == "True" and r.get(score_col) not in ("", None)
        aff = float(r[score_col]) if ok else fail_score   # fail_score => ranks last
        if not ok:
            if lab == "active":
                n_fail_active += 1
            elif lab == "decoy":
                n_fail_decoy += 1
        if lab == "active":
            actives.append(aff)
        elif lab == "decoy":
            decoys.append(aff)
    return actives, decoys, n_fail_active, n_fail_decoy


def roc_auc(actives, decoys):
    """AUC via the Mann-Whitney U relationship. score = -affinity (higher better)."""
    na, nd = len(actives), len(decoys)
    if na == 0 or nd == 0:
        return float("nan")
    scored = [(-a, 1) for a in actives] + [(-d, 0) for d in decoys]
    scored.sort(key=lambda x: x[0])            # ascending score
    # average ranks (1-based), handling ties
    ranks = [0.0] * len(scored)
    i = 0
    while i < len(scored):
        j = i
        while j + 1 < len(scored) and scored[j + 1][0] == scored[i][0]:
            j += 1
        avg = (i + 1 + j + 1) / 2.0
        for k in range(i, j + 1):
            ranks[k] = avg
        i = j + 1
    sum_ranks_active = sum(rk for rk, (_, lab) in zip(ranks, scored) if lab == 1)
    u = sum_ranks_active - na * (na + 1) / 2.0
    return u / (na * nd)


def enrichment_factor(actives, decoys, frac):
    na, nd = len(actives), len(decoys)
    total = na + nd
    n_top = max(1, math.ceil(frac * total))
    scored = [(-a, 1) for a in actives] + [(-d, 0) for d in decoys]
    scored.sort(key=lambda x: (x[0], -x[1]), reverse=True)   # best first; ties broken against actives
    top_active = sum(lab for _, lab in scored[:n_top])
    return (top_active / n_top) / (na / total)


def _bedroc_clean(scored, na, n, alpha):
    ra = na / n
    sum_exp = sum(math.exp(-alpha * (i + 1) / n) for i, (_, lab) in enumerate(scored) if lab == 1)
    rand = (na / n) * (1 - math.exp(-alpha)) / (math.exp(alpha / n) - 1)
    rie = sum_exp / rand
    return rie * (ra * math.sinh(alpha / 2)) / (math.cosh(alpha / 2) - math.cosh(alpha / 2 - alpha * ra))


def verdict(auc, ef1):
    if auc >= 0.75 and ef1 >= 5:
        return "STRONG enrichment — the engine discriminates known binders well."
    if auc >= 0.60:
        return "MODEST enrichment — real signal; GNINA rescoring (Stage 3) recommended before trusting hits."
    if auc >= 0.55:
        return "WEAK enrichment — marginal; Vina-alone is not a reliable filter on this target."
    return "NO meaningful enrichment — Vina-alone is insufficient here; lean on Stage-3 rescoring / ensemble."


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", required=True)
    ap.add_argument("--out", default="")
    ap.add_argument("--score-col", default="affinity",
                    help="rank by 'affinity' (best-of-N consensus) or 'affinity_mean'")
    args = ap.parse_args()

    actives, decoys, n_fail_active, n_fail_decoy = load(args.results, args.score_col)
    n_fail = n_fail_active + n_fail_decoy
    na, nd = len(actives), len(decoys)
    if na == 0 or nd == 0:
        print(f"ERROR: need both actives and decoys (got {na} actives, {nd} decoys).")
        sys.exit(1)

    auc = roc_auc(actives, decoys)
    ef = {f: enrichment_factor(actives, decoys, f) for f in (0.01, 0.05, 0.10)}
    bed = _bedroc_clean(
        sorted([(-a, 1) for a in actives] + [(-d, 0) for d in decoys], key=lambda x: (x[0], -x[1]), reverse=True),
        na, na + nd, 20.0)
    real_a = [a for a in actives if a < 1e8]   # exclude failed-dock sentinels from the mean
    real_d = [d for d in decoys if d < 1e8]
    mean_a = sum(real_a) / len(real_a) if real_a else float("nan")
    mean_d = sum(real_d) / len(real_d) if real_d else float("nan")
    v = verdict(auc, ef[0.01])

    rep = {
        "n_actives": na, "n_decoys": nd, "n_failed_docks": n_fail,
        "failed_docks_active": n_fail_active, "failed_docks_decoy": n_fail_decoy,
        "roc_auc": round(auc, 3),
        "ef_1pct": round(ef[0.01], 2), "ef_5pct": round(ef[0.05], 2), "ef_10pct": round(ef[0.10], 2),
        "bedroc_alpha20": round(bed, 3),
        "mean_affinity_actives": round(mean_a, 2), "mean_affinity_decoys": round(mean_d, 2),
        "separation_kcal_mol": round(mean_d - mean_a, 2),
        "verdict": v,
    }

    print("\n================ Tier 1 Enrichment Gate ================")
    print(f"actives : {na}  ({n_fail_active} failed dock, ranked worst)")
    print(f"decoys  : {nd}  ({n_fail_decoy} failed dock, ranked worst)")
    print(f"ROC-AUC        : {auc:.3f}   (0.5 random, 1.0 perfect)")
    print(f"EF  1%         : {ef[0.01]:.2f}x")
    print(f"EF  5%         : {ef[0.05]:.2f}x")
    print(f"EF 10%         : {ef[0.10]:.2f}x")
    print(f"BEDROC (a=20)  : {bed:.3f}")
    print(f"mean affinity  : actives {mean_a:.2f} vs decoys {mean_d:.2f}  (sep {mean_d-mean_a:+.2f} kcal/mol)")
    print(f"\nVERDICT: {v}")
    print("========================================================\n")

    outdir = Path(args.out) if args.out else Path(args.results).parent
    (outdir / "enrichment_report.json").write_text(json.dumps(rep, indent=2))
    print(f"-> {outdir/'enrichment_report.json'}")


if __name__ == "__main__":
    main()
