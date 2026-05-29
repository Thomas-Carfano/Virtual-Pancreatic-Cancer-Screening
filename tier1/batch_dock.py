#!/usr/bin/env python3
"""
batch_dock.py — PancScan Tier 1 screening engine (multi-pass, escalating exhaustiveness).

Docks a list of SMILES into the validated 7RPZ (KRAS G12D) switch-II pocket and ranks
them by AutoDock Vina affinity. CPU workhorse of pipeline Stage 2.

WHY MULTI-PASS: empirically Vina's seed-to-seed variance at fixed CPU is negligible
(~0.01 kcal/mol), so re-seeding adds no information. The real uncertainty is whether
the conformational search was thorough enough. So each ligand is docked over a
schedule of INCREASING exhaustiveness (default 8,16,32):
  - affinity          = best-of-passes (deepest pose found) -> consensus ranking score
  - affinity_mean     = mean over passes
  - affinity_std      = spread across passes (large => low exhaustiveness was undersampling)
  - affinities_by_pass = the raw per-pass scores
The best pass's pose is kept; intermediate pose files are removed.

Input  : CSV with `id,smiles` (optional `label` carried through, e.g. active/decoy).
Output : <outdir>/results.csv, results_ranked.csv, run_manifest.json, ligands/, poses/

Robust + resumable: failed ligand logged and skipped; re-running the same --outdir
skips ids already in results.csv.

    PATH="/opt/homebrew/Caskroom/miniforge/base/envs/pancscan/bin:$PATH" \
      python batch_dock.py --compounds c.csv --outdir screen/run1 --exhaustiveness-schedule 8,16,32
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
from datetime import datetime

HERE = Path(__file__).parent.resolve()
sys.path.insert(0, str(HERE))
from prepare_ligand import prepare_ligand

FIELDNAMES = ["id", "smiles", "label", "prep_ok", "dock_ok", "affinity",
              "affinity_mean", "affinity_std", "n_passes", "affinities_by_pass", "error"]


def parse_best_affinity(out_pdbqt: Path):
    """Top-pose affinity (kcal/mol) from the first 'REMARK VINA RESULT' in a PDBQT."""
    try:
        with open(out_pdbqt) as f:
            for line in f:
                if line.startswith("REMARK VINA RESULT"):
                    return float(line.split()[3])
    except FileNotFoundError:
        pass
    return None


def dock_one(smiles, cid, label, cfg, dirs, receptor_pdbqt, cpu, exh_list, base_seed):
    lig_pdbqt = dirs["ligands"] / f"{cid}.pdbqt"
    pose_pdbqt = dirs["poses"] / f"{cid}.pdbqt"
    row = {"id": cid, "smiles": smiles, "label": label, "prep_ok": False, "dock_ok": False,
           "affinity": "", "affinity_mean": "", "affinity_std": "", "n_passes": 0,
           "affinities_by_pass": "", "error": ""}

    pr = prepare_ligand(smiles, cid, lig_pdbqt)
    if not pr.ok:
        row["error"] = f"prep: {pr.error}"
        return row
    row["prep_ok"] = True

    b, v = cfg["box"], cfg["vina"]
    affs, exh_done, best, last_err = [], [], None, ""
    for i, exh in enumerate(exh_list):
        tmp = dirs["poses"] / f"{cid}.p{i}.pdbqt"
        cmd = ["vina",
               "--receptor", str(receptor_pdbqt), "--ligand", str(lig_pdbqt), "--out", str(tmp),
               "--center_x", str(b["center_x"]), "--center_y", str(b["center_y"]), "--center_z", str(b["center_z"]),
               "--size_x", str(b["size_x"]), "--size_y", str(b["size_y"]), "--size_z", str(b["size_z"]),
               "--exhaustiveness", str(exh), "--num_modes", str(v["num_modes"]),
               "--cpu", str(cpu), "--seed", str(base_seed + i)]
        try:
            proc = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
        except subprocess.TimeoutExpired:
            last_err = "vina timeout (>900s)"
            continue
        if proc.returncode != 0:
            last_err = f"vina rc={proc.returncode}: {proc.stderr.strip()[:120]}"
            continue
        a = parse_best_affinity(tmp)
        if a is None:
            last_err = "no VINA RESULT parsed"
            continue
        affs.append(a)
        exh_done.append(exh)
        if best is None or a < best[0]:
            best = (a, i)

    if best is not None:
        try:
            shutil.move(str(dirs["poses"] / f"{cid}.p{best[1]}.pdbqt"), str(pose_pdbqt))
        except Exception:
            pass
    for i in range(len(exh_list)):
        leftover = dirs["poses"] / f"{cid}.p{i}.pdbqt"
        if leftover.exists():
            try:
                leftover.unlink()
            except Exception:
                pass

    if not affs:
        row["error"] = last_err or "all passes failed"
        return row
    row["dock_ok"] = True
    row["affinity"] = min(affs)                                   # best-of-passes consensus
    row["affinity_mean"] = round(statistics.fmean(affs), 3)
    row["affinity_std"] = round(statistics.pstdev(affs), 3) if len(affs) > 1 else 0.0
    row["n_passes"] = len(affs)
    row["affinities_by_pass"] = ";".join(f"{e}:{a:.3f}" for e, a in zip(exh_done, affs))
    # Flag partial multi-pass runs: if the deepest pass(es) failed/timed out, the best-of
    # consensus came from shallower search only. Keep dock_ok=True but record it, so ligands
    # aren't silently ranked against each other at inconsistent search depth.
    if len(affs) < len(exh_list):
        missing = [e for e in exh_list if e not in exh_done]
        row["error"] = f"partial: {len(affs)}/{len(exh_list)} passes ok, missing exh={missing} ({last_err[:50]})"
    return row


def write_ranked(results_csv: Path, ranked_csv: Path):
    rows = []
    with open(results_csv) as f:
        for r in csv.DictReader(f):
            if r["dock_ok"] == "True" and r["affinity"] not in ("", None):
                r["affinity"] = float(r["affinity"])
                rows.append(r)
    rows.sort(key=lambda r: r["affinity"])           # most negative (best) first
    with open(ranked_csv, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDNAMES)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    return rows


def main():
    ap = argparse.ArgumentParser(description="PancScan Tier 1 multi-pass batch docker")
    ap.add_argument("--compounds", required=True, help="CSV with id,smiles[,label]")
    ap.add_argument("--config", default=str(HERE / "dock_config.json"))
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--limit", type=int, default=0, help="only the first N compounds (debug)")
    ap.add_argument("--workers", type=int, default=0,
                    help="ligands docked concurrently (0 = auto: cpu//4). Each Vina uses cpu//workers cores.")
    ap.add_argument("--cpu-total", type=int, default=0,
                    help="cap total cores used (0 = use config). Throttle: 5 ~= 30%% of a 16-core machine.")
    ap.add_argument("--exhaustiveness-schedule", default="8,16,32",
                    help="comma list; one pass per value, best-of taken. e.g. '8,16,32'")
    ap.add_argument("--base-seed", type=int, default=-1, help="first seed (-1 = use config vina.seed)")
    args = ap.parse_args()

    cfg_path = Path(args.config)
    cfg = json.loads(cfg_path.read_text())
    rp = Path(cfg["receptor_pdbqt"])
    # relative receptor paths are relative to the CONFIG file's dir, not this script's dir
    receptor_pdbqt = rp if rp.is_absolute() else (cfg_path.parent / rp)
    if not receptor_pdbqt.exists():
        print(f"ERROR: receptor not found: {receptor_pdbqt}")
        sys.exit(1)
    base_seed = args.base_seed if args.base_seed >= 0 else int(cfg["vina"]["seed"])
    exh_list = [int(x) for x in args.exhaustiveness_schedule.split(",") if x.strip()]

    outdir = Path(args.outdir)
    dirs = {"ligands": outdir / "ligands", "poses": outdir / "poses"}
    for d in dirs.values():
        d.mkdir(parents=True, exist_ok=True)
    results_csv = outdir / "results.csv"

    compounds = []
    with open(args.compounds) as f:
        for r in csv.DictReader(f):
            compounds.append((r["id"], r["smiles"], r.get("label", "")))
    if args.limit:
        compounds = compounds[:args.limit]

    done = set()
    if results_csv.exists():
        with open(results_csv) as f:
            done = {r["id"] for r in csv.DictReader(f)}
    todo = [c for c in compounds if c[0] not in done]

    cpu_total = args.cpu_total if args.cpu_total > 0 else int(cfg["vina"]["cpu"])
    workers = args.workers or max(1, cpu_total // 4)
    cpu_per = max(1, cpu_total // workers)
    print(f"compounds={len(compounds)}  already_done={len(done)}  todo={len(todo)}")
    print(f"receptor={receptor_pdbqt.name}  exhaustiveness_schedule={exh_list}  base_seed={base_seed}")
    print(f"workers={workers}  cpu/worker={cpu_per}  (cpu_total={cpu_total})")

    from concurrent.futures import ProcessPoolExecutor, as_completed
    t0 = time.time()
    n_ok = n_fail = 0
    with open(results_csv, "a", newline="") as fout:
        w = csv.DictWriter(fout, fieldnames=FIELDNAMES)
        if not done:
            w.writeheader()
        with ProcessPoolExecutor(max_workers=workers) as ex:
            futures = {ex.submit(dock_one, smi, cid, label, cfg, dirs, receptor_pdbqt,
                                 cpu_per, exh_list, base_seed): cid
                       for (cid, smi, label) in todo}
            for i, fut in enumerate(as_completed(futures), 1):
                row = fut.result()
                w.writerow(row)
                fout.flush()
                if row["dock_ok"]:
                    n_ok += 1
                    status = f"{row['affinity']:.2f} (passes {row['affinities_by_pass']})"
                else:
                    n_fail += 1
                    status = f"FAIL({row['error'][:28]})"
                el = time.time() - t0
                rate = el / i
                eta_min = rate * (len(todo) - i) / 60
                print(f"[{i}/{len(todo)}] {row['id']:16s} {status:34s} {rate:4.1f}s/lig ETA {eta_min:5.1f}m")

    ranked = write_ranked(results_csv, outdir / "results_ranked.csv")
    manifest = {
        "date": datetime.now().isoformat(), "config": cfg,
        "exhaustiveness_schedule": exh_list, "base_seed": base_seed,
        "compounds_total": len(compounds), "attempted_this_run": len(todo),
        "succeeded_this_run": n_ok, "failed_this_run": n_fail, "ranked_total": len(ranked),
        "wall_seconds_this_run": round(time.time() - t0, 1),
        "best": ranked[0] if ranked else None,
    }
    (outdir / "run_manifest.json").write_text(json.dumps(manifest, indent=2))
    print(f"\nDone. ok={n_ok} fail={n_fail} ranked={len(ranked)} wall={manifest['wall_seconds_this_run']}s")
    if ranked:
        print(f"Top hit: {ranked[0]['id']} @ {ranked[0]['affinity']:.2f} kcal/mol")
    print(f"-> {outdir/'results_ranked.csv'}")


if __name__ == "__main__":
    main()
