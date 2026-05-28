# PancScan — open virtual screening for pancreatic cancer

An open-source, reproducible structure-based virtual-screening pipeline for pancreatic
ductal adenocarcinoma (PDAC), built to run on commodity hardware (validated on an Apple
Silicon MacBook Pro, no GPU required). It docks small molecules into validated
pancreatic-cancer drug targets and produces ranked candidate lists for wet-lab follow-up.

Everything here is open: the code, the target choices, the validation numbers, the
candidate hits — and the failures and caveats. This is a self-funded community effort,
not a commercial pipeline.

> **Honest framing up front.** This pipeline produces *prioritized hypotheses* — computational
> predictions that need experimental confirmation. A high-ranking compound is a starting point
> for a wet-lab assay, **not** a drug, **not** a confirmed binder, and **not** a medical claim.
> It is step 1 of a 5-step discovery process (screen → rescore → simulate → wet-lab → trials).

## What it does

For a chosen protein target (with a known 3D structure), the pipeline:

1. Builds a docking-ready receptor + box from a PDB/mmCIF structure, validated by
   re-docking the native ligand back to its crystal pose.
2. Confirms the engine actually discriminates real binders from decoys (an enrichment gate).
3. Screens a compound library (e.g. ~6,400 approved/clinical drugs) and ranks every
   compound by predicted binding.
4. (Optionally) uses active learning to make million- to billion-compound libraries tractable.

## Validated targets

| Target | PDB | Native redock | Enrichment ROC-AUC | Notes |
|---|---|---|---|---|
| KRAS G12D | 7RPZ | 0.51 Å | 0.690 (EF1% 6.6×) | Most common PDAC driver (~40%); modest discrimination |
| KRAS G12V | 9U50 | 0.92 Å | — | 2nd allele (~30%); OFF-state, good screening target |
| KRAS G12R (tri-complex) | 8TBH | 0.78 Å | — | ON-state KRAS+CypA; pose-validated, but plain-Vina scoring weak for glue mechanism |
| PARP1 | 9ETQ | 0.90 Å | **0.874 (EF1% 15.3×)** | Strongest discrimination; relevant in BRCA/HRD PDAC |

Redock < 2 Å and AUC > 0.5 are the pass criteria. PARP1's AUC 0.87 means the engine
cleanly separates known PARP inhibitors from look-alike decoys (olaparib and the literature
PARP1 inhibitor EB-47 self-surfaced in the top hits as independent positive controls).

## Results so far

The Broad Drug Repurposing Hub (~6,400 approved/clinical drugs) was screened against KRAS
G12D and PARP1. Ranked candidates, target-selective leads, and one-page wet-lab handoff
docs are in [`candidates/`](candidates/). Highlights: a striking MET-inhibitor cluster on
KRAS G12D (tivantinib, merestinib, PHA-665752, SU11274) and DDR-coherent PARP1 hits
(the ATR inhibitor ETP-46464, the NAMPT/NAD⁺ compound KPT-9274).

## Repository layout

```
pancscan/
├── README.md              this file
├── METHODS.md             full methods + reproducibility record + honest caveats
├── LICENSE                MIT
├── environment.yml        conda environment (all open-source tools)
├── tier0_smoke_test.py    Tier 0: re-dock MRTX1133 into KRAS G12D (the original proof)
├── tier1/                 screening engine
│   ├── prepare_ligand.py      SMILES → 3D → pH-7.4 protonation → PDBQT
│   ├── batch_dock.py          parallel, resumable, throttleable docking driver
│   ├── analyze_enrichment.py  ROC-AUC / EF / BEDROC enrichment gate
│   ├── active_learning.py     retrospective active-learning recovery simulation
│   ├── al_screen.py           prospective active-learning screening driver (for huge libraries)
│   └── build_enrichment_set.py  build actives+decoys from any ChEMBL target
├── tier2/
│   └── setup_target.py    mmCIF → validated receptor+box+config for ANY target (multi-chain capable)
├── candidates/            ranked hits + wet-lab handoff docs (the deliverable)
├── libraries/             screened compound libraries + raw results
├── reports/               Tier 0 validation reports
└── data/, tier*/screen/   regenerable working data (gitignored)
```

## Quick start

```bash
# 1. environment (one time; ~1.5 GB)
mamba env create -f environment.yml
mamba activate pancscan

# 2. prove the pipeline works on your machine (Tier 0)
python tier0_smoke_test.py            # re-docks MRTX1133 into KRAS G12D, expect ~0.5 Å

# 3. set up a target from a structure (example: PARP1)
cd tier2
python setup_target.py --cif assets/9ETQ.cif --chain A --ligand-ccd A1H63 \
    --ligand-sdf assets/A1H63_ideal.sdf --name PARP1_9ETQ --outdir targets/9ETQ

# 4. screen a library against it
cd ../tier1
python batch_dock.py --compounds <library.csv> --config ../tier2/targets/9ETQ/dock_config.json \
    --outdir screen/my_run --cpu-total 16 --workers 8 --exhaustiveness-schedule 8

# 5. (if validating) check enrichment
python analyze_enrichment.py --results screen/my_run/results.csv
```

`--cpu-total` throttles CPU use (e.g. `5` ≈ 30% of a 16-core machine). All runs are resumable.

## Tools (all open-source)

AutoDock Vina 1.2.5 · RDKit · Meeko · OpenBabel · Dimorphite-DL · spyRMSD · gemmi ·
scikit-learn · Biopython. Structures from RCSB PDB; validation data from ChEMBL (CC BY-SA);
screening library from the Broad Drug Repurposing Hub.

## Limitations (read these)

- **Docking scores are approximate** (~±3 kcal/mol error). Trust clusters and enrichment,
  not the exact rank of any single compound.
- **No induced fit** — the receptor is rigid; some real binders need a different conformation.
- **Decoys are presumed-inactive**, not experimentally confirmed.
- **Glue/PPI-interface mechanisms (e.g. KRAS ON-state) score poorly with plain Vina** —
  pose recovery can be good but ranking is unreliable; those need GNINA/MD.
- This is the computational top-of-funnel. **Wet-lab confirmation is required for any claim.**

See [METHODS.md](METHODS.md) for the full validation record and reproducibility details.

## License

MIT — see [LICENSE](LICENSE). Use it, fork it, build on it. If it helps, let us know.

## Contact

Self-funded open project. Lead: Thomas Carfano (tcarfano@kixie.com).
Wet-lab collaborators and compute contributors welcome.
