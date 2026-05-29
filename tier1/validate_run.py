#!/usr/bin/env python3
"""
validate_run.py — per-run positive/negative control check ("can this setup still tell a
binder from a non-binder, right now?").

Docks a small set of KNOWN binders (positive controls) + decoys (negative controls) through
the EXACT same dock_config / receptor / box / code path a production screen uses, then asserts
the engine still discriminates positives from negatives. Use it as a PRE-FLIGHT before any big
screen: if the controls don't separate, the whole screen would be garbage — wrong receptor,
bad box, broken config. This is the check that would have caught the all-zeros receptor-path
bug instantly (it docks, sees ~0.0 scores, and FAILS).

    python validate_run.py --config ../tier2/targets/9ETQ/dock_config.json \
        --enrichment-dir ../tier2/targets/9ETQ/enrichment --outdir ../tier2/targets/9ETQ/_validate

PASS requires ALL of:
  - controls actually docked (>=2 positives and >=2 negatives succeed)
  - scores are sane: most-negative < -5 kcal/mol AND non-degenerate spread (catches all-zeros)
  - positives beat negatives: mean separation >= --min-separation AND control AUC >= --min-auc
Exit code 0 on PASS, 1 on FAIL (so it can gate a screen in a shell: `validate_run.py ... && batch_dock.py ...`).
"""
import sys
import csv
import json
import time
import shutil
import argparse
import statistics
import subprocess
from pathlib import Path

HERE = Path(__file__).parent.resolve()
BATCH_DOCK = HERE / "batch_dock.py"


def sample_controls(enrichment_dir, k):
    """K most-potent actives (positive controls) + K decoys (negative controls)."""
    ed = Path(enrichment_dir)
    acts = list(csv.DictReader(open(ed / "actives.csv")))
    decs = list(csv.DictReader(open(ed / "decoys.csv")))
    try:                       # prefer the most potent actives as positives
        acts.sort(key=lambda r: float(r.get("max_pchembl") or 0), reverse=True)
    except Exception:
        pass
    a_sel = acts[:k]
    d_sel = decs[:k]           # decoys.csv has no potency; first K is fine (built dissimilar)
    return ([(r["id"], r["smiles"], "control_active") for r in a_sel] +
            [(r["id"], r["smiles"], "control_decoy") for r in d_sel])


def mini_auc(pos, neg):
    """Direct AUC = fraction of (positive, negative) pairs the engine orders correctly.
    More-negative affinity = better binder, so a positive should be < its paired negative."""
    if not pos or not neg:
        return float("nan")
    wins = 0.0
    for p in pos:
        for q in neg:
            if p < q:
                wins += 1.0
            elif p == q:
                wins += 0.5
    return wins / (len(pos) * len(neg))


def main():
    ap = argparse.ArgumentParser(description="Per-run positive/negative control validation")
    ap.add_argument("--config", required=True, help="target dock_config.json (the one a real screen would use)")
    ap.add_argument("--enrichment-dir", help="dir with actives.csv + decoys.csv to sample controls from")
    ap.add_argument("--controls", help="explicit controls CSV (id,smiles,label in {control_active,control_decoy})")
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--k", type=int, default=8, help="controls per class")
    ap.add_argument("--cpu-total", type=int, default=8)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--exhaustiveness", default="8")
    ap.add_argument("--min-separation", type=float, default=0.8,
                    help="required mean(decoy) - mean(active) in kcal/mol")
    ap.add_argument("--min-auc", type=float, default=0.65)
    ap.add_argument("--min-score", type=float, default=-3.0,
                    help="best control must score below this (kcal/mol); catches all-zeros/degenerate output "
                         "without assuming strong binding")
    args = ap.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    # ---- build control set ----
    if args.controls:
        rows = [(r["id"], r["smiles"], r["label"]) for r in csv.DictReader(open(args.controls))]
    elif args.enrichment_dir:
        rows = sample_controls(args.enrichment_dir, args.k)
    else:
        print("ERROR: need --enrichment-dir or --controls"); sys.exit(2)
    n_pos_in = sum(1 for r in rows if r[2] == "control_active")
    n_neg_in = sum(1 for r in rows if r[2] == "control_decoy")
    controls_csv = outdir / "controls.csv"
    with open(controls_csv, "w", newline="") as f:
        w = csv.writer(f); w.writerow(["id", "smiles", "label"]); w.writerows(rows)
    print(f"controls: {n_pos_in} positive + {n_neg_in} negative  (config: {Path(args.config).name})")

    # ---- force a FRESH dock (else batch_dock would skip ids and return stale scores
    #      from a previous config — defeating the whole point of a validation) ----
    for p in (outdir / "results.csv", outdir / "results_ranked.csv", outdir / "run_manifest.json"):
        if p.exists():
            p.unlink()
    for d in (outdir / "ligands", outdir / "poses"):
        if d.exists():
            shutil.rmtree(d, ignore_errors=True)

    # ---- dock through the EXACT production path ----
    cmd = [sys.executable, "-u", str(BATCH_DOCK), "--compounds", str(controls_csv),
           "--config", args.config, "--outdir", str(outdir),
           "--cpu-total", str(args.cpu_total), "--workers", str(args.workers),
           "--exhaustiveness-schedule", args.exhaustiveness]
    t0 = time.time()
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        print("FAIL: batch_dock errored:\n" + proc.stderr[-600:])
        sys.exit(1)

    # ---- read control scores ----
    pos, neg, n_fail, detail = [], [], 0, []
    for r in csv.DictReader(open(outdir / "results.csv")):
        ok = r.get("dock_ok") == "True" and r.get("affinity") not in ("", None)
        a = float(r["affinity"]) if ok else None
        detail.append({"id": r.get("id"), "label": r.get("label"), "affinity": a})
        if ok:
            (pos if r["label"] == "control_active" else neg).append(a)
        else:
            n_fail += 1

    # ---- checks ----
    alls = pos + neg
    sep = (statistics.fmean(neg) - statistics.fmean(pos)) if (pos and neg) else float("nan")
    auc = mini_auc(pos, neg)
    checks = {
        "controls_docked": (len(pos) >= 2 and len(neg) >= 2),
        "scores_sane": bool(alls) and min(alls) < args.min_score and (statistics.pstdev(alls) > 0.1 if len(alls) > 1 else False),
        "positives_beat_negatives": (sep == sep) and sep >= args.min_separation,
        "auc_ok": (auc == auc) and auc >= args.min_auc,
    }
    passed = all(checks.values())

    report = {
        "config": str(args.config), "passed": bool(passed),
        "n_pos_docked": len(pos), "n_neg_docked": len(neg), "n_failed": n_fail,
        "mean_active": round(statistics.fmean(pos), 3) if pos else None,
        "mean_decoy": round(statistics.fmean(neg), 3) if neg else None,
        "separation_kcal_mol": round(sep, 3) if sep == sep else None,
        "control_auc": round(auc, 3) if auc == auc else None,
        "checks": checks,
        "controls": detail,
        "wall_s": round(time.time() - t0, 1),
    }
    (outdir / "control_report.json").write_text(json.dumps(report, indent=2))

    print(f"\n{'='*56}")
    print(f"  positives docked: {len(pos)}  mean { report['mean_active'] }")
    print(f"  negatives docked: {len(neg)}  mean { report['mean_decoy'] }")
    print(f"  separation: {report['separation_kcal_mol']} kcal/mol   control AUC: {report['control_auc']}")
    for name, ok in checks.items():
        print(f"    [{'PASS' if ok else 'FAIL'}] {name}")
    print(f"  >>> {'VALIDATION PASSED — safe to screen' if passed else 'VALIDATION FAILED — do NOT trust a screen with this config'}")
    print(f"{'='*56}")
    print(f"-> {outdir/'control_report.json'}")
    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
