# PancScan — methods & reproducibility record

This is the scientific record: exact tools, decisions, validation numbers, and honest
caveats. It exists so anyone can reproduce, audit, or build on the work.

## Pipeline

Structure-based virtual screening with AutoDock Vina, in stages of increasing scale:

- **Tier 0 — proof.** Re-dock the co-crystallized inhibitor back into its target and
  confirm we recover the experimental pose. Falsifiable mechanics check.
- **Tier 1 — engine + gate.** Screen a compound library; validate with an enrichment gate
  (do known binders rank above property-matched decoys?); active learning for scale.
- **Tier 2 — generalization.** Reduce any PDB/mmCIF structure to a validated receptor+box
  with one command (`setup_target.py`), so new targets are cheap to add.

## Ligand & receptor preparation (the parts that matter)

- **Receptor:** OpenBabel `-xr -p 7.4` (rigid receptor, protonated at pH 7.4). Cofactors that
  line the pocket (GDP, Mg²⁺ for KRAS) are deliberately retained — Meeko's polymer receptor
  prep tends to drop them.
- **Native ligand (redock):** RDKit `AssignBondOrdersFromTemplate` stamps correct bond orders
  from the RCSB "ideal" SDF onto the crystal coordinates, then `AddHs` → Meeko PDBQT. This
  avoids the classic failure of perceiving bond orders/protonation from coordinates alone.
- **Novel ligand (screening):** SMILES → Dimorphite-DL protonation at pH 7.4
  (`precision=0.0` for the dominant microspecies) → RDKit ETKDGv3 3D embed + MMFF/UFF →
  Meeko PDBQT. Protonation is load-bearing: it sets formal charge, which drives Vina's
  electrostatic/H-bond terms.
- **mmCIF targets:** newer structures use 5-character ligand codes (e.g. A1EN3, A1H63) that
  legacy PDB format cannot represent — `.pdb` downloads return error stubs. We select chains
  and ligands in mmCIF space via gemmi. Multi-chain receptors (e.g. KRAS+CypA tri-complexes)
  are supported by passing `--chain A,C`.

## Validation: native redocking

Pass = symmetry-corrected heavy-atom RMSD < 2 Å (spyRMSD), and native score < −7 kcal/mol.
RMSD that cannot be computed returns NaN (never a fabricated number). For large symmetric
ligands where full graph-isomorphism symmetry search blows up combinatorially, we fall back
to the Hungarian algorithm (optimal atom assignment, polynomial time).

| Target | PDB | Native ligand | Redock RMSD | Native score |
|---|---|---|---|---|
| KRAS G12D | 7RPZ | MRTX1133 (6IC) | 0.51 Å | −14.7 |
| KRAS G12V | 9U50 | MCB-294 (A1EN3) | 0.92 Å | −14.9 |
| KRAS G12R + CypA | 8TBH | RMC-7977 (ZNI) | 0.78 Å | −7.5 |
| PARP1 | 9ETQ | AZD5305 (A1H63) | 0.90 Å | −12.3 |

## Validation: enrichment gate

Blind test: dock 40 known actives (ChEMBL, pChEMBL ≥ 6, drug-like) + ~600 property-matched
decoys (DUD-E-style: matched MW/logP/HBD/HBA/rotatable bonds, ECFP4 Tanimoto < 0.35 to every
active → topologically dissimilar → presumed inactive). Metrics: ROC-AUC, enrichment factor
at 1/5/10%, BEDROC (α=20).

| Target | ROC-AUC | EF 1% | EF 5% | BEDROC | Read |
|---|---|---|---|---|---|
| KRAS G12D | 0.690 | 6.56× | 1.97× | 0.18 | Modest — real signal, scoring-limited |
| PARP1 | 0.874 | 15.25× | 11.31× | 0.76 | Strong — clean discrimination |

Independent positive controls auto-surfaced: olaparib (top 1.4%) and the literature PARP1
inhibitor EB-47 (#12 of 6,309) in the PARP1 run — the engine recognizes real binders without
being told which they are.

> **Benchmark policy:** DUD-E-style property-matched decoys only. LIT-PCBA is explicitly NOT
> used as a gate — the 2025 audit (arXiv:2507.21404) documented severe data leakage making it
> exploitable by a memorization baseline.

## Active learning

A RandomForest surrogate (ECFP4 fingerprints → Vina score) prioritizes which compounds to
dock, making large libraries tractable. Retrospective simulation on the 612-compound KRAS set:
surrogate holdout Spearman **0.83**; recovered **89% of true top-hits at 50% docked** (vs 55%
random), 64% at 30%. `al_screen.py` productionizes this as an iterative dock→train→predict→dock
loop for million/billion-scale libraries (ZINC22, Enamine REAL).

## Key empirical findings about the method itself

- **Vina is converged at exhaustiveness 8 for these pockets** (8 ≈ 16 ≈ 32, Δ < 0.1 kcal/mol;
  seed-to-seed variance ~0.01 at fixed CPU). Multi-pass re-seeding adds no information.
  Apparent score scatter across runs was a CPU-count effect, not randomness.
- **Scoring-function ceiling:** the Vina paper (Trott & Olson 2010) reports ±2.85 kcal/mol
  standard error — larger than the gap between a potent binder and a random drug. This is why
  enrichment (group-level) is the meaningful metric and why GNINA rescoring (Stage 3, GPU) is
  the motivated next step, not more docking.
- **Plain Vina underscores molecular-glue / PPI-interface ligands** (KRAS ON-state tri-complex):
  pose recovery good (0.78 Å), score weak (−7.5 for a sub-nM glue). Such targets need GNINA/MD,
  not plain-Vina screening.

## Environment

conda env `pancscan` (see `environment.yml`): Python 3.11, AutoDock Vina 1.2.5, smina, RDKit
2023.09, Meeko 0.7.1, gemmi, OpenBabel 3.1, Dimorphite-DL 2.0.2, spyRMSD, scikit-learn,
Biopython, NumPy/SciPy/pandas. Native on macOS arm64; works on Linux x86-64. CPU-only.
Note: the conda package for Vina is `vina` (NOT `autodock-vina`, which has no osx-arm64 build).

## The honest pipeline (where this sits)

1. **Computational screen** ← *this project* (hours, commodity CPU)
2. ML rescoring — GNINA (GPU, ~$10–30 cloud)
3. Short MD — does the pose hold? (GPU)
4. Wet-lab binding / cell assay (CRO ~$1–5k/compound, or academic/SGC collaboration)
5. Optimization → animals → clinical trials

Steps 1–2 are achievable by an open volunteer-compute effort. Steps 3–5 require partners. The
deliverable of this project is an openly-published, reproducible, ranked candidate list that a
qualified lab can pick up at step 2 or 4. That is a real research contribution — and explicitly
not a medical claim.
