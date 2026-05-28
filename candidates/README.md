# PancScan@home — repurposing candidate handoff

An open virtual-screening pipeline pointed at two validated pancreatic-cancer targets,
then run against the **Broad Drug Repurposing Hub** (~6,400 approved/clinical drugs).
The output is *prioritized hypotheses* for wet-lab follow-up — not confirmed binders.

## Targets

| Target | PDB | Redock RMSD | Gate ROC-AUC | EF 1% | Strength |
|---|---|---|---|---|---|
| **KRAS G12D** | 7RPZ | 0.506 Å | 0.690 | 6.56× | Modest — Vina scoring-limited; rankings noisy |
| **PARP1 catalytic** | 9ETQ | 0.898 Å | **0.874** | **15.25×** | Strong — engine cleanly discriminates known PARP inhibitors |

Engine: AutoDock Vina 1.2.5, exhaustiveness 8, Meeko/OpenBabel prep with Dimorphite-DL pH-7.4 protonation.

## Files

| File | Description |
|---|---|
| `G12D/top50.csv` · `G12D/HANDOFF.md` | Top 50 ranked candidates against KRAS G12D + 1-page wet-lab handoff |
| `G12D/top25_selective.csv` | KRAS-selective hits (NOT in PARP1 top-200) — the real repurposing leads |
| `PARP1/top50.csv` · `PARP1/HANDOFF.md` | Top 50 vs PARP1 + 1-page handoff |
| `PARP1/top25_selective.csv` | PARP1-selective hits (NOT in G12D top-200) |
| `cross_target_overlap.csv` | 20 drugs in top-100 of *both* — mostly generic shape-fitters (incl. olaparib/EB-47 as sanity controls) |

## How to read these

- **Trust the cluster, not the rank.** Vina has ±3 kcal/mol error (per the original paper). A drug at rank 5 vs 15 is mostly noise. What matters: which drugs cluster at the top, do they share chemistry, do any have plausible biology?
- **Target-selective lists are the most interesting.** A drug high on *only one* target is a more specific lead than one high on both (those are typically generic kinase-ATP chemotypes).
- **Hits = hypotheses.** The next steps are (1) better scoring via GNINA (GPU), (2) short MD simulation, (3) wet-lab binding/cell assay. See per-target `HANDOFF.md` for the suggested first assay.

## Reproducibility

- Code: `pancscan/` (open source, Apache 2.0 spirit).
- Library: Broad Drug Repurposing Hub samples (free, non-commercial).
- Structures: RCSB PDB. Validation actives/decoys: ChEMBL (CC BY-SA 3.0).
- Hardware: M4 Max (16 cores), AutoDock Vina, RDKit/Meeko, scikit-learn — all open-source.

## Honest framing

This is the *computational top-of-funnel*. KRAS G12D rankings are *modest* (AUC 0.69) — treat as starting points, not endpoints. PARP1 rankings are *strong* (AUC 0.87) — more trustworthy, still hypotheses. Wet-lab confirmation is required before any biological claim. **Step 1 of 5** in a drug-discovery pipeline.

## Contact

Open self-funded project. Lead: Thomas Carfano (tcarfano@kixie.com). Wet-lab collaborators welcome — see per-target `HANDOFF.md` for the recommended first assay.
