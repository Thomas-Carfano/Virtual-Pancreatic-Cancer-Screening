# PancScan — repurposing candidates

These are the ranked results: existing approved/clinical drugs scored by how well they fit two
validated pancreatic-cancer targets. They are **prioritized leads for laboratory testing — not
confirmed binders, and not medical advice.** (See the main project [README](../README.md) for
how this works and its limitations.)

The drug library screened was the **Broad Drug Repurposing Hub** (~6,400 approved/clinical drugs).

## Targets screened

| Target | Structure (PDB) | Pose-recovery accuracy | Fairness score (ROC-AUC) | Top-1% enrichment | Confidence |
|---|---|---|---|---|---|
| **KRAS G12D** | 7RPZ | 0.51 Å | 0.690 | 6.6× | Modest — rankings are noisy; treat as starting points. |
| **PARP1** | 9ETQ | 0.90 Å | **0.874** | **15.3×** | Strong — the engine cleanly separates known PARP drugs from look-alikes. |

## Files in this folder

| File | What it is |
|---|---|
| `<target>/top50.csv` | The 50 best-scoring drugs for that target. |
| `<target>/top25_selective.csv` | Hits high on *this* target but **not** the other — the more target-specific leads. |
| `<target>/HANDOFF.md` | A one-page summary a laboratory can act on (target background + suggested first experiment). |
| `cross_target_overlap.csv` | Drugs that score well on **both** targets — mostly generic "fits-many-pockets" molecules (includes olaparib and EB-47, which act as built-in sanity checks). |

## How to read these results

- **Trust the cluster, not the exact rank.** The scoring has ~±3 kcal/mol of error, so #5 vs #15
  is mostly noise. What matters is *which kinds of drugs* land at the top and whether that makes
  biological sense.
- **The target-selective lists are the most interesting** — a drug specific to one target is a
  cleaner lead than one that sticks to everything.
- **Every hit is a hypothesis,** to be confirmed (or ruled out) in a lab. See each `HANDOFF.md`
  for the recommended first experiment.

## How these were produced (reproducibility)

- **Code:** the `pancscan/` pipeline in this repository (open source).
- **Drug library:** Broad Drug Repurposing Hub samples (free, non-commercial use).
- **Protein structures:** RCSB Protein Data Bank. **Validation data:** ChEMBL (CC BY-SA 3.0).
- **Hardware:** an ordinary 16-core laptop CPU — AutoDock Vina, RDKit/Meeko, scikit-learn, all open-source.

## Honest framing

This is the **computational first step** of drug discovery. KRAS G12D rankings are *modest*
(treat as starting points); PARP1 rankings are *strong* (more trustworthy, still hypotheses).
Laboratory confirmation is required before any biological claim.

## Contact

Self-funded open project. Lead: **Thomas Carfano** (tomcarfano@gmail.com). Laboratory
collaborators welcome — each `HANDOFF.md` lists a recommended first assay.
