#!/usr/bin/env python3
"""
al_screen.py — prospective active-learning screening driver (Stage-2 production tool).

For libraries too big to fully dock (10^5 - 10^9), the brute-force approach is intractable.
This driver uses a cheap RandomForest surrogate (RDKit ECFP4 -> Vina affinity) to PRIORITIZE
which compounds to dock next:

  Iter 0 (seed)  : random sample of `seed_frac` of the library -> dock with batch_dock.
  Iter 1..N      : train RF on docked, predict scores for undocked, dock the top
                   `batch_frac` greedy (most negative predicted score), repeat.
  Stop           : when `max_frac` of the library has been docked.

The cumulative docked set is the screen output (ranked); the surrogate's predictions for
the un-docked rest are written as a bonus ranking. With r~0.83 surrogates (per the
retrospective demo) we recover most top hits at a fraction of compute.

Reuses tier1/batch_dock.py as the underlying docker (subprocess) — correctness, --cpu-total
throttle, receptor-path fix, and resumability all inherited. Re-running with the same
--outdir picks up where the last run stopped (reads existing results.csv).

    python al_screen.py \
        --compounds ../libraries/repurposing_hub/compounds.csv \
        --config ../tier2/targets/9ETQ/dock_config.json \
        --outdir ../libraries/repurposing_hub/al_screen_PARP1 \
        --seed-frac 0.02 --batch-frac 0.05 --max-frac 0.30 \
        --cpu-total 16 --workers 8

Honest scope: AL pays off most at 10^6+ libraries. On a 6 k library you'd just full-dock.
This tool is the bridge to ZINC22 / Enamine REAL screens (millions to billions).
"""
import sys
import csv
import json
import time
import argparse
import subprocess
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
import numpy as np
from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem
from sklearn.ensemble import RandomForestRegressor

HERE = Path(__file__).parent.resolve()
BATCH_DOCK = HERE / "batch_dock.py"


def load_library(path):
    rows = []
    with open(path) as f:
        for r in csv.DictReader(f):
            rows.append((r["id"], r["smiles"], r.get("label", "")))
    return rows


def featurize(smiles_list, nbits=2048, radius=2):
    """ECFP4 fingerprints. Returns (X, bad_indices)."""
    X = np.zeros((len(smiles_list), nbits), dtype=np.int8)
    bad = []
    for i, s in enumerate(smiles_list):
        m = Chem.MolFromSmiles(s)
        if m is None:
            bad.append(i)
            continue
        fp = AllChem.GetMorganFingerprintAsBitVect(m, radius, nBits=nbits)
        DataStructs.ConvertToNumpyArray(fp, X[i])
    return X, bad


def load_docked(results_csv):
    """Return {id: affinity} for successfully docked compounds."""
    out = {}
    if not Path(results_csv).exists():
        return out
    with open(results_csv) as f:
        for r in csv.DictReader(f):
            if r.get("dock_ok") == "True" and r.get("affinity") not in ("", None):
                try:
                    out[r["id"]] = float(r["affinity"])
                except ValueError:
                    pass
    return out


def write_batch_csv(path, rows):
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "smiles", "label"])
        for r in rows:
            w.writerow(r)


def run_batch_dock(batch_csv, config, outdir, cpu_total, workers, exh_schedule):
    """Invoke tier1/batch_dock.py as a subprocess; raises on non-zero exit."""
    cmd = [sys.executable, "-u", str(BATCH_DOCK),
           "--compounds", str(batch_csv), "--config", str(config), "--outdir", str(outdir),
           "--cpu-total", str(cpu_total), "--workers", str(workers),
           "--exhaustiveness-schedule", str(exh_schedule)]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        sys.stderr.write(proc.stderr[-800:])
        raise RuntimeError(f"batch_dock failed (rc={proc.returncode})")
    return proc.stdout


def main():
    ap = argparse.ArgumentParser(description="PancScan prospective active-learning screening driver")
    ap.add_argument("--compounds", required=True, help="library CSV with id,smiles[,label]")
    ap.add_argument("--config", required=True, help="dock_config.json for the target (e.g. tier2/targets/9ETQ/dock_config.json)")
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--seed-frac", type=float, default=0.02, help="initial random seed fraction (default 2%)")
    ap.add_argument("--batch-frac", type=float, default=0.05, help="per-iteration AL batch fraction (default 5%)")
    ap.add_argument("--max-frac", type=float, default=0.30, help="stop after this fraction docked (default 30%)")
    ap.add_argument("--cpu-total", type=int, default=16)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--exhaustiveness-schedule", default="8")
    ap.add_argument("--n-estimators", type=int, default=200, help="RandomForest trees")
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    al_dir = outdir / "_al"
    al_dir.mkdir(exist_ok=True)
    log_path = outdir / "al_log.json"
    results_csv = outdir / "results.csv"

    library = load_library(args.compounds)
    n = len(library)
    ids = [r[0] for r in library]
    id2idx = {cid: k for k, cid in enumerate(ids)}
    smiles = [r[1] for r in library]
    print(f"library: {n} compounds")
    print(f"featurizing (ECFP4, 2048 bits) ...")
    X, bad = featurize(smiles)
    if bad:
        print(f"  {len(bad)} compounds unparseable -> excluded from selection")

    seed_n = max(2, int(round(args.seed_frac * n)))
    batch_n = max(1, int(round(args.batch_frac * n)))
    max_n = int(round(args.max_frac * n))

    docked = load_docked(results_csv)
    print(f"start: {len(docked)} already docked, budget {max_n}/{n} ({100*args.max_frac:.0f}%)")

    rng = np.random.default_rng(args.seed)
    log = json.loads(log_path.read_text()) if log_path.exists() else []
    iter_i = len(log)

    while len(docked) < max_n:
        is_seed = (len(docked) == 0)
        undocked_idx = [i for i, cid in enumerate(ids) if cid not in docked and i not in bad]
        if not undocked_idx:
            print("no undocked compounds left.")
            break
        take = min((seed_n if is_seed else batch_n), max_n - len(docked), len(undocked_idx))

        if is_seed:
            sel = rng.choice(undocked_idx, size=take, replace=False).tolist()
            strategy = "random_seed"
            iter_meta = {}
        else:
            d_idx = [id2idx[cid] for cid in docked if cid in id2idx]
            y_tr = np.array([docked[ids[i]] for i in d_idx])
            X_tr = X[d_idx]
            model = RandomForestRegressor(
                n_estimators=args.n_estimators, n_jobs=-1, random_state=args.seed + iter_i,
            )
            model.fit(X_tr, y_tr)
            pred = model.predict(X[undocked_idx])
            order = np.argsort(pred)            # ascending: most negative (best predicted) first
            sel = [undocked_idx[k] for k in order[:take]]
            strategy = "greedy_top_predicted"
            iter_meta = {"surrogate_train_n": int(len(d_idx)),
                         "predicted_top_batch_mean": round(float(np.mean(pred[order[:take]])), 3)}

        batch_csv = al_dir / f"batch_iter{iter_i}.csv"
        write_batch_csv(batch_csv, [library[i] for i in sel])
        print(f"\n=== iter {iter_i}: {strategy} | docking {len(sel)} | progress {len(docked)}/{max_n} ===")

        t0 = time.time()
        run_batch_dock(batch_csv, args.config, outdir, args.cpu_total, args.workers, args.exhaustiveness_schedule)
        wall = time.time() - t0

        prev = docked
        docked = load_docked(results_csv)
        new_ok = len(docked) - len(prev)
        new_actuals = [docked[ids[i]] for i in sel if ids[i] in docked and ids[i] not in prev]

        iter_log = {"iter": iter_i, "strategy": strategy,
                    "submitted": len(sel), "newly_docked_ok": new_ok,
                    "cumulative_docked": len(docked), "wall_s": round(wall, 1),
                    "batch_mean_actual": round(float(np.mean(new_actuals)), 3) if new_actuals else None,
                    **iter_meta}
        log.append(iter_log)
        log_path.write_text(json.dumps(log, indent=2))
        print(f"   iter {iter_i} done: +{new_ok} docked ({wall:.0f}s); "
              f"batch mean actual = {iter_log['batch_mean_actual']}")
        iter_i += 1

    # ---- final outputs ----
    print(f"\nfinal: {len(docked)}/{n} docked ({100*len(docked)/n:.1f}% of library)")
    final_ranked = sorted(docked.items(), key=lambda kv: kv[1])
    out_ranked = outdir / "final_ranked.csv"
    with open(out_ranked, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "smiles", "label", "affinity"])
        for cid, aff in final_ranked:
            i = id2idx[cid]; _, smi, label = library[i]
            w.writerow([cid, smi, label, aff])
    print(f"-> {out_ranked} (ranked docked compounds)")

    if 0 < len(docked) < n:
        d_idx = [id2idx[cid] for cid in docked if cid in id2idx]
        y_tr = np.array([docked[ids[i]] for i in d_idx])
        model = RandomForestRegressor(n_estimators=args.n_estimators, n_jobs=-1, random_state=args.seed)
        model.fit(X[d_idx], y_tr)
        und_idx = [i for i, cid in enumerate(ids) if cid not in docked and i not in bad]
        pred = model.predict(X[und_idx])
        ord_p = np.argsort(pred)
        top_n = max(200, len(und_idx) // 20)
        out_pred = outdir / "undocked_predicted_top.csv"
        with open(out_pred, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["id", "smiles", "label", "predicted_affinity"])
            for k in ord_p[:top_n]:
                i = und_idx[k]; cid, smi, label = library[i]
                w.writerow([cid, smi, label, round(float(pred[k]), 3)])
        print(f"-> {out_pred} (top {top_n} predicted-best un-docked, by surrogate)")


if __name__ == "__main__":
    main()
