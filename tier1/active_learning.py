#!/usr/bin/env python3
"""
active_learning.py — the load-bearing piece of PancScan Stage 2.

Brute-force docking does not scale: 10^9 compounds x seconds each = CPU-millennia.
Deep-Docking / MolPAL-style active learning fixes this: dock a small SEED fraction,
train a cheap surrogate to predict docking score from molecular fingerprints, use it to
PRIORITIZE which compounds to dock next, and iterate. You recover most of the true top
hits while docking only a small fraction of the library.

This script runs a RETROSPECTIVE simulation: it takes a completed screen (where every
compound's Vina score is known) and replays the AL loop, pretending scores are hidden
until a compound is "docked". It measures how many of the true top hits AL recovers vs
fraction docked, against a random-selection baseline.

    python active_learning.py --results screen/run_full/results.csv --out screen/run_full/al

Honest scope: on a 640-compound set the absolute numbers are coarse/noisy — the real
100x payoff is at 10^7-10^9. This is a correctness + behavior demo on real Vina scores,
and the exact code scales to a production library.
"""
import sys
import csv
import json
import argparse
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
import numpy as np
from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem
from sklearn.ensemble import RandomForestRegressor
from scipy.stats import spearmanr


def load_and_featurize(results_csv, nbits=2048, radius=2):
    """Return ids, X (fingerprints), y (Vina affinity) for all successfully docked compounds."""
    ids, smis, aff = [], [], []
    for r in csv.DictReader(open(results_csv)):
        if r.get("dock_ok") == "True" and r.get("affinity") not in ("", None):
            m = Chem.MolFromSmiles(r["smiles"])
            if m is None:
                continue
            ids.append(r["id"]); smis.append(r["smiles"]); aff.append(float(r["affinity"]))
    X = np.zeros((len(ids), nbits), dtype=np.int8)
    for i, s in enumerate(smis):
        fp = AllChem.GetMorganFingerprintAsBitVect(Chem.MolFromSmiles(s), radius, nBits=nbits)
        DataStructs.ConvertToNumpyArray(fp, X[i])
    return ids, X, np.array(aff)


def true_top_sets(y, fracs):
    """Indices of the true best compounds (most negative affinity) for each top-fraction."""
    order = np.argsort(y)                      # ascending: best (most negative) first
    n = len(y)
    return {f: set(order[:max(1, int(round(f * n)))].tolist()) for f in fracs}


def simulate(X, y, strategy, rng, seed_frac, batch_frac, max_frac, top_sets, n_estimators):
    """One AL (or random) run. Returns list of (frac_docked, {topfrac: recovery})."""
    n = len(y)
    seed_n = max(2, int(round(seed_frac * n)))
    batch_n = max(1, int(round(batch_frac * n)))
    max_n = int(round(max_frac * n))

    docked = set(rng.choice(n, size=seed_n, replace=False).tolist())
    curve = []

    def record():
        frac = len(docked) / n
        rec = {f: len(docked & s) / len(s) for f, s in top_sets.items()}
        curve.append((frac, rec))

    record()
    while len(docked) < max_n:
        undocked = np.array([i for i in range(n) if i not in docked])
        take = min(batch_n, max_n - len(docked))
        if strategy == "random":
            pick = rng.choice(undocked, size=take, replace=False)
        else:  # active learning: train surrogate, dock predicted-best
            d = np.array(sorted(docked))
            model = RandomForestRegressor(n_estimators=n_estimators, n_jobs=-1,
                                          random_state=int(rng.integers(1e9)))
            model.fit(X[d], y[d])
            pred = model.predict(X[undocked])         # predicted affinity (lower = better)
            pick = undocked[np.argsort(pred)[:take]]  # greedily dock predicted-best
        docked.update(pick.tolist())
        record()
    return curve


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", required=True)
    ap.add_argument("--out", default="")
    ap.add_argument("--seed-frac", type=float, default=0.10)
    ap.add_argument("--batch-frac", type=float, default=0.10)
    ap.add_argument("--max-frac", type=float, default=0.60)
    ap.add_argument("--replicates", type=int, default=12)
    ap.add_argument("--top-fracs", default="0.05,0.10")
    ap.add_argument("--n-estimators", type=int, default=200)
    args = ap.parse_args()

    ids, X, y = load_and_featurize(args.results)
    n = len(y)
    if n < 30:
        print(f"ERROR: only {n} docked compounds — need a completed screen first.")
        sys.exit(1)
    fracs = [float(x) for x in args.top_fracs.split(",")]
    top_sets = true_top_sets(y, fracs)
    print(f"loaded {n} docked compounds; true top sets: "
          + ", ".join(f"top{int(f*100)}%={len(s)}" for f, s in top_sets.items()))

    # quick surrogate sanity: 5-fold-ish holdout Spearman (does FP predict Vina score at all?)
    rng0 = np.random.default_rng(0)
    perm = rng0.permutation(n); cut = int(0.7 * n)
    tr, te = perm[:cut], perm[cut:]
    m = RandomForestRegressor(n_estimators=args.n_estimators, n_jobs=-1, random_state=0).fit(X[tr], y[tr])
    rho = spearmanr(y[te], m.predict(X[te])).correlation
    print(f"surrogate holdout Spearman (FP -> Vina score): {rho:.3f}")

    # AL vs random, averaged over replicates
    results = {"al": {}, "random": {}}
    for strat in ("al", "random"):
        agg = {}  # frac -> {topfrac -> [recoveries]}
        for rep in range(args.replicates):
            rng = np.random.default_rng(1000 + rep)
            curve = simulate(X, y, strat, rng, args.seed_frac, args.batch_frac,
                             args.max_frac, top_sets, args.n_estimators)
            for frac, rec in curve:
                key = round(frac, 3)
                agg.setdefault(key, {f: [] for f in fracs})
                for f in fracs:
                    agg[key][f].append(rec[f])
        results[strat] = agg

    # align fractions (use AL's keys) and print comparison
    keys = sorted(results["al"].keys())
    print(f"\n{'docked%':>8} | " + " | ".join(
        f"AL top{int(f*100)}%  rand top{int(f*100)}%" for f in fracs))
    print("-" * (10 + 26 * len(fracs)))
    rows = []
    for k in keys:
        line = f"{k*100:7.0f}% |"
        row = {"frac_docked": k}
        for f in fracs:
            al = float(np.mean(results["al"][k][f]))
            rd = float(np.mean(results["random"].get(k, {f: [k]})[f])) if k in results["random"] else k
            line += f"  {al*100:5.0f}%      {rd*100:5.0f}%   "
            row[f"al_top{int(f*100)}"] = round(al, 3)
            row[f"rand_top{int(f*100)}"] = round(rd, 3)
        print(line)
        rows.append(row)

    # headline: AL recovery of best top-frac at the smallest "early" budget >= 20%
    early = min([k for k in keys if k >= 0.20], default=keys[-1])
    f_hi = max(fracs)
    al_e = float(np.mean(results["al"][early][f_hi]))
    rd_e = early
    verdict = (f"At {early*100:.0f}% of the library docked, active learning recovered "
               f"{al_e*100:.0f}% of the true top-{int(f_hi*100)}% hits "
               f"(random selection would get ~{rd_e*100:.0f}%).")
    print(f"\nVERDICT: {verdict}")
    if al_e > rd_e + 0.15:
        print("=> AL clearly beats random: the surrogate is a useful prioritizer.")
    else:
        print("=> AL edge is modest here (expected on a small/!diverse set); scales with library size.")

    out = Path(args.out) if args.out else Path(args.results).parent / "al"
    out.mkdir(parents=True, exist_ok=True)
    cols = list(rows[0].keys())          # ordered: frac_docked, al_topX, rand_topX, ...
    (out / "al_recovery.csv").write_text(
        ",".join(cols) + "\n" +
        "\n".join(",".join(str(r[k]) for k in cols) for r in rows) + "\n")
    (out / "al_report.json").write_text(json.dumps({
        "n_compounds": n, "surrogate_holdout_spearman": round(float(rho), 3),
        "seed_frac": args.seed_frac, "batch_frac": args.batch_frac,
        "replicates": args.replicates, "top_fracs": fracs,
        "verdict": verdict, "curve": rows,
    }, indent=2))
    print(f"\n-> {out}/al_recovery.csv, al_report.json")


if __name__ == "__main__":
    main()
