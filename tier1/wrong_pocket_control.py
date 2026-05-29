#!/usr/bin/env python3
"""
wrong_pocket_control.py — negative control: enrichment should COLLAPSE at the wrong pocket.

The enrichment gate shows actives rank above decoys at the real binding site. But is that real
molecular recognition, or just the scoring function liking the actives' physicochemistry
everywhere? This control re-docks the SAME actives + decoys at a WRONG site and checks the
discrimination disappears:
  - default: an OFF-SITE box on the same receptor, centered on the surface atom farthest from
    the real pocket — controls for everything except pocket location.
  - --decoy-config: dock into a DIFFERENT target's pocket entirely (cross-target control).

PASS (enrichment is pocket-specific / real): wrong-site AUC collapses toward 0.5 and is well
below the true-site AUC. FAIL (artifact): it stays high even at the wrong site.

    python wrong_pocket_control.py --config ../tier2/targets/9ETQ/dock_config.json \
        --compounds ../tier2/targets/9ETQ/enrichment/enrichment_compounds.csv \
        --true-results ../tier2/targets/9ETQ/screen/results.csv \
        --outdir ../tier2/targets/9ETQ/_wrongpocket
"""
import sys
import csv
import json
import shutil
import argparse
import subprocess
import random
from pathlib import Path

HERE = Path(__file__).parent.resolve()
sys.path.insert(0, str(HERE))
from analyze_enrichment import roc_auc
BATCH_DOCK = HERE / "batch_dock.py"


def load_labeled(results_csv, id_subset=None, fail_score=1e9):
    """actives/decoys affinity lists from a results.csv (failed docks -> worst), optional id filter."""
    actives, decoys = [], []
    for r in csv.DictReader(open(results_csv)):
        if id_subset is not None and r.get("id") not in id_subset:
            continue
        lab = (r.get("label") or "").lower()
        ok = r.get("dock_ok") == "True" and r.get("affinity") not in ("", None)
        a = float(r["affinity"]) if ok else fail_score
        if lab == "active":
            actives.append(a)
        elif lab == "decoy":
            decoys.append(a)
    return actives, decoys


def build_offsite_config(true_config_path, outdir):
    """Off-site box centered on the receptor atom farthest from the real pocket (far surface)."""
    import numpy as np
    cfg = json.loads(Path(true_config_path).read_text())
    rp = Path(cfg["receptor_pdbqt"])
    receptor = (rp if rp.is_absolute() else (Path(true_config_path).parent / rp)).resolve()
    box = cfg["box"]
    pc = np.array([box["center_x"], box["center_y"], box["center_z"]])
    coords = []
    for line in open(receptor):
        if line.startswith(("ATOM", "HETATM")):
            try:
                coords.append((float(line[30:38]), float(line[38:46]), float(line[46:54])))
            except ValueError:
                pass
    arr = np.array(coords)
    d = np.linalg.norm(arr - pc, axis=1)
    far = arr[d.argmax()]
    off_box = {"center_x": float(far[0]), "center_y": float(far[1]), "center_z": float(far[2]),
               "size_x": box["size_x"], "size_y": box["size_y"], "size_z": box["size_z"]}
    # Overlap fraction with the true pocket box (axis-aligned). The off-site box reuses the
    # true box size, so depending on geometry it can clip the real pocket; record it so a
    # compromised control is visible (a big overlap lets ligands reach the real site).
    ov = 1.0
    for c, s in (("center_x", "size_x"), ("center_y", "size_y"), ("center_z", "size_z")):
        lo = max(box[c] - box[s] / 2, off_box[c] - off_box[s] / 2)
        hi = min(box[c] + box[s] / 2, off_box[c] + off_box[s] / 2)
        ov *= max(0.0, hi - lo)
    true_vol = box["size_x"] * box["size_y"] * box["size_z"]
    overlap_frac = ov / true_vol if true_vol else 0.0
    off = dict(cfg)
    off["receptor_pdbqt"] = str(receptor)   # absolute so it resolves from the off-site outdir
    off["box"] = off_box
    p = Path(outdir) / "_offsite_config.json"
    p.write_text(json.dumps(off, indent=2))
    return p, float(d.max()), overlap_frac


def main():
    ap = argparse.ArgumentParser(description="Wrong-pocket negative control")
    ap.add_argument("--config", required=True, help="true target dock_config.json")
    ap.add_argument("--compounds", required=True, help="enrichment_compounds.csv (id,smiles,label active/decoy)")
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--true-results", help="true-site results.csv (to compute true-site AUC on the same molecules)")
    ap.add_argument("--decoy-config", help="dock into THIS other target's pocket instead of an off-site box")
    ap.add_argument("--max-decoys", type=int, default=150, help="subsample decoys for speed (0 = all)")
    ap.add_argument("--cpu-total", type=int, default=16)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--exhaustiveness", default="8")
    ap.add_argument("--collapse-margin", type=float, default=0.15,
                    help="wrong-site AUC must be at least this far below true-site AUC")
    args = ap.parse_args()

    outdir = Path(args.outdir); outdir.mkdir(parents=True, exist_ok=True)

    rows = list(csv.DictReader(open(args.compounds)))
    acts = [r for r in rows if r["label"] == "active"]
    decs = [r for r in rows if r["label"] == "decoy"]
    if args.max_decoys and len(decs) > args.max_decoys:
        decs = random.Random(42).sample(decs, args.max_decoys)
    sub = acts + decs
    subset_ids = {r["id"] for r in sub}
    sub_csv = outdir / "wrongpocket_compounds.csv"
    with open(sub_csv, "w", newline="") as f:
        w = csv.writer(f); w.writerow(["id", "smiles", "label"])
        for r in sub:
            w.writerow([r["id"], r["smiles"], r["label"]])

    overlap_frac = None
    if args.decoy_config:
        wp_config, far_d, mode = args.decoy_config, None, f"cross-target ({Path(args.decoy_config).parent.name})"
    else:
        wp_config, far_d, overlap_frac = build_offsite_config(args.config, outdir)
        mode = f"off-site box ({far_d:.0f} A from real pocket, {overlap_frac*100:.0f}% box overlap)"
        if overlap_frac > 0.15:
            print(f"  WARNING: off-site box overlaps the true pocket by {overlap_frac*100:.0f}% — "
                  f"control may be compromised (ligands could reach the real site).")
    print(f"wrong pocket: {mode}")
    print(f"docking {len(acts)} actives + {len(decs)} decoys at the wrong pocket ...")

    # fresh dock
    for p in (outdir / "results.csv", outdir / "results_ranked.csv", outdir / "run_manifest.json"):
        if p.exists():
            p.unlink()
    for d in (outdir / "ligands", outdir / "poses"):
        if d.exists():
            shutil.rmtree(d, ignore_errors=True)

    cmd = [sys.executable, "-u", str(BATCH_DOCK), "--compounds", str(sub_csv),
           "--config", str(wp_config), "--outdir", str(outdir),
           "--cpu-total", str(args.cpu_total), "--workers", str(args.workers),
           "--exhaustiveness-schedule", args.exhaustiveness]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        print("ERROR: batch_dock failed:\n" + proc.stdout[-400:] + proc.stderr[-400:]); sys.exit(1)

    wa, wd = load_labeled(outdir / "results.csv")
    wrong_auc = roc_auc(wa, wd)

    true_auc = None
    if args.true_results and Path(args.true_results).exists():
        ta, td = load_labeled(args.true_results, id_subset=subset_ids)
        if ta and td:
            true_auc = roc_auc(ta, td)

    if true_auc is not None:
        collapsed = wrong_auc < (true_auc - args.collapse_margin)
    else:
        collapsed = wrong_auc < 0.62
    passed = collapsed and wrong_auc < 0.65

    report = {
        "mode": mode, "true_site_auc": round(true_auc, 3) if true_auc is not None else None,
        "wrong_site_auc": round(wrong_auc, 3), "collapse_margin": args.collapse_margin,
        "offsite_box_overlap_frac": round(overlap_frac, 3) if overlap_frac is not None else None,
        "n_actives": len(wa), "n_decoys": len(wd), "passed": bool(passed),
    }
    (outdir / "wrong_pocket_report.json").write_text(json.dumps(report, indent=2))

    print(f"\n{'='*56}")
    print(f"  true-site AUC : {report['true_site_auc']}")
    print(f"  wrong-site AUC: {report['wrong_site_auc']}   (0.5 = no discrimination)")
    if passed:
        print(f"  >>> PASS — enrichment COLLAPSES at the wrong pocket, so the real-site signal is pocket-specific.")
    else:
        print(f"  >>> FAIL — actives still enrich at the wrong pocket; the signal may be a property/scoring artifact.")
    print(f"{'='*56}")
    print(f"-> {outdir/'wrong_pocket_report.json'}")
    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
