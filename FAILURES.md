# Failures, dead ends & negative results

This file is here on purpose. Most computational drug-discovery work only ever shows what
worked — the bugs, dead ends, and "we tried it and it doesn't work" results stay private, so
everyone privately rediscovers the same problems. This is our running, honest record of what
went **wrong** and what **didn't pan out**. It's as much a part of the project as the successes.

Nothing here is a finished conclusion — it's a lab notebook kept in the open.

---

## A. Bugs we caught (and what they teach)

These produced *wrong numbers* before we noticed. They're logged because anyone building a
docking pipeline will likely hit the same ones.

| Bug | What it did | How it was caught | Lesson |
|---|---|---|---|
| **All-H vs polar-H RMSD** | Tier 0's first run reported an 8 Å "FAIL" re-docking MRTX1133 — but the docking was fine. The RMSD compared an all-hydrogen crystal pose against a polar-hydrogen docked pose, so the atom sets didn't match. | The score (−14) looked too good for a "failed" pose; inspecting the RMSD code revealed the mismatch. Heavy-atom-only comparison gave 0.5 Å. | A validation metric can fail while the thing it's testing is correct. Compare heavy atoms only; never trust a single failing number without checking the metric itself. |
| **Receptor-path bug** | The batch docker resolved the receptor file path relative to the *script's* folder, not the *config's* folder — so a PARP1 run silently used the KRAS receptor. ~530 compounds "docked" into empty space, every score 0.0. | A glance at the live results showed `dock_ok=True` with `affinity=0.0` for everything — physically impossible. | "Succeeded" is not "correct." Sanity-check that scores are in a plausible range, not just that the program exited cleanly. Caught before it polluted any saved results. |
| **Silent protonation bug** | The pH-7.4 protonation tool, on its default setting, returned several charge states and we took the first — which wasn't reliably the dominant one. Basic amines were silently left uncharged → wrong formal charge → wrong docking electrostatics. | Test molecules (propranolol, imatinib) came back neutral when they should be positively charged at body pH. | Defaults aren't always what you assume. Verify charge states on known molecules before trusting them at scale. |
| **RMSD blows up on big symmetric molecules** | The symmetry-corrected RMSD did a full graph-isomorphism search that exploded combinatorially on a 62-atom "molecular glue" ligand and returned NaN — which read as a validation failure. | The pose looked right by eye (centroid 0.19 Å) but RMSD said NaN. | Added a polynomial-time fallback (Hungarian algorithm). A tool failing to *measure* success isn't the same as failure. |
| **Active-learning seed skipped on resume** | A 500k-compound active-learning run was restarted after a tiny aborted attempt had docked just 3 compounds. The code inferred "the seed is done" from "results aren't empty," skipped the random seed phase, and trained the surrogate on those **3 molecules** — so the first 10,000-compound batch was picked near-arbitrarily instead of by active learning. | The run log showed `iter 0: greedy_top_predicted, surrogate_train_n: 3`. A model trained on 3 molecules can't prioritize anything. | Track phase completion *explicitly* (keep seeding until N seeds are docked) — never infer it from "is the output non-empty." Resume/restart paths are a classic home for silent bugs. The dockings themselves stayed valid; only the *selection* was degraded. |

**Meta-lesson:** in this project alone, several bugs produced confidently-wrong numbers. That is
exactly why every result here is treated as unvalidated until a lab confirms it.

---

## B. Negative scientific results (things that genuinely don't work this way)

| Finding | Detail |
|---|---|
| **Plain docking fails for the KRAS "ON-state" (tri-complex) mechanism.** | We validated the KRAS G12R structure (8TBH) — the ligand's *position* reproduced to 0.78 Å. But the *score* for a known sub-nanomolar inhibitor was only −7.5 kcal/mol (weak). These "molecular glue" drugs work at a protein–protein interface that plain AutoDock Vina scores poorly. **Conclusion: don't use plain docking to screen this target type** — it needs more advanced methods (ML rescoring / physics simulation). A real, useful dead end. |
| **KRAS G12D screening is only modestly reliable.** | The enrichment test (do known binders rank above decoys?) scored AUC 0.69 — real signal, but noisy. KRAS's large, floppy inhibitors sit near the edge of what this scoring function can resolve. Treat any individual KRAS G12D rank with skepticism. |
| **The recurring "MET-inhibitor cluster" might be an artifact.** | Several MET-targeting drugs (tivantinib, merestinib, etc.) consistently scored high on both KRAS alleles. That's either a real pocket-shape affinity *or* just a flat chemotype that fits many pockets. We can't tell which without a lab. Logged as an open question, not a finding. |

---

## C. Tooling / setup dead ends (saving others the time)

- **`autodock-vina` does not exist as a conda package for Apple Silicon**, and there's no Homebrew
  formula either — both "standard" install routes are dead ends on a Mac. The working package is
  named **`vina`** on conda-forge. (Cost an hour to discover.)
- **Newer PDB structures (mmCIF, 5-character ligand codes) break the legacy `.pdb` format** —
  `.pdb` downloads return tiny error stubs. Must use `.cif` and select ligands in mmCIF space.
- **LIT-PCBA is unusable as a benchmark** — a 2025 audit (arXiv:2507.21404) documented severe data
  leakage that lets a trivial memorization baseline match state-of-the-art models. We use DUD-E-style
  property-matched decoys instead. (A negative result from the literature we chose to respect.)
- **Re-seeding docking runs is wasted compute** — AutoDock Vina is effectively converged at its
  default search depth for these pockets (results barely change from exhaustiveness 8 → 16 → 32, and
  seed-to-seed variance is ~0.01 kcal/mol). Earlier "score scatter" was a CPU-count effect, not
  randomness. Don't pay for multi-pass re-seeding.

---

## D. Per-screen failure counts (the routine attrition)

Every screen of an unfiltered drug library loses a small fraction of compounds to un-parseable
chemistry, 3D-embedding failures, or malformed docking inputs. These are logged per run (the
`error` column in each `results.csv`) rather than hidden:

| Screen | Attempted | Failed prep/dock | Rate |
|---|---|---|---|
| KRAS G12D (repurposing) | 6,389 | ~78 | ~1% |
| PARP1 (repurposing) | 6,389 | ~91 | ~1.4% |
| KRAS G12V (repurposing) | 6,389 | ~80 | ~1.3% |

These failures aren't errors in the science — they're the normal cost of running real, messy
chemical libraries, and they're reported for completeness.

---

*If you reproduce this work and hit a failure we didn't list — or show that one of our "negative
results" is actually wrong — that's a contribution. Open an issue.*
