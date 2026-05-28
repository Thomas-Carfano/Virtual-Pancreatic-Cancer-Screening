<!--
  PancScan — open virtual screening for pancreatic cancer
  Machine-readable metadata: see dataset_metadata.jsonld (schema.org/Dataset) and CITATION.cff
  Column-level data definitions: see DATA_DICTIONARY.md
  Full methods & reproducibility: see METHODS.md
  Keywords: pancreatic cancer, PDAC, KRAS G12D, KRAS G12V, KRAS G12R, PARP1, molecular docking,
  AutoDock Vina, virtual screening, drug repurposing, structure-based drug discovery, open science,
  cheminformatics, RDKit, enrichment, active learning, MRTX1133, olaparib
-->

# PancScan — open virtual screening for pancreatic cancer

PancScan is an **open-source, fully reproducible computational pipeline** that searches for
candidate small-molecule drugs against pancreatic ductal adenocarcinoma (PDAC). It runs
**molecular docking** on commodity hardware (validated on an Apple Silicon laptop, no GPU),
screens libraries of compounds against validated drug targets, and publishes **ranked
candidate lists** that wet-labs can pick up and test.

Everything is open: the code, the methods, the exact numbers, the candidate hits, **and the
limitations**. This is a self-funded community science project — not a commercial product and
not a medical service.

> ## ⚠️ Read this first — what these results are and are not
> The outputs in this repository are **computational predictions (hypotheses)**, produced by
> molecular docking. A high-ranking compound is a **starting point for a laboratory experiment**.
> It is **NOT** a drug, **NOT** a confirmed binder, **NOT** a treatment, and **NOT** medical advice.
> No claim of therapeutic efficacy or safety is made or implied. Docking is **step 1 of a 5-step
> discovery process** (screen → ML rescore → physics simulation → wet-lab assay → clinical trials).
> Any biological or clinical conclusion requires experimental validation by qualified scientists.

---

## TL;DR

- **Goal:** find existing/known molecules that might bind pancreatic-cancer drug targets, openly.
- **Method:** dock molecules into the 3D structure of a target protein with AutoDock Vina; rank by predicted binding energy; validate that the method actually distinguishes real binders from look-alikes.
- **Targets validated:** KRAS G12D, KRAS G12V, KRAS G12R (tri-complex), PARP1.
- **Screened so far:** ~6,400 approved/clinical drugs (Broad Drug Repurposing Hub) vs KRAS G12D and PARP1 (KRAS G12V in progress).
- **Deliverable:** ranked candidate lists + per-target wet-lab handoff docs in [`candidates/`](candidates/).
- **Status:** computational top-of-funnel. Wet-lab confirmation required for any claim.

---

## How this was created

1. **Target selection (grounded in the literature).** Pancreatic cancer's biggest genetic
   drivers were reviewed (TCGA, recent reviews). Three of the "big four" — TP53, CDKN2A, SMAD4 —
   are *lost* tumor-suppressor genes with no protein pocket to drug, so they are poor docking
   targets. **KRAS** is the dominant *druggable* driver. We therefore target the KRAS mutant
   alleles common in PDAC (G12D ~40%, G12V ~30%, G12R ~15%) plus **PARP1** (a validated synthetic-
   lethal target in BRCA/HRD pancreatic cancer).

2. **Pipeline built in tiers of increasing scale.**
   - *Tier 0 — proof:* re-dock a known drug (MRTX1133) into its target (KRAS G12D) and confirm we
     reproduce the experimental crystal structure pose. (Achieved 0.5 Å — see `reports/`.)
   - *Tier 1 — engine + validation:* a batch docking engine, plus an **enrichment gate** that blind-
     tests whether the engine ranks known binders above decoys.
   - *Tier 2 — generalization:* one command turns any protein structure (PDB/mmCIF) into a validated
     docking target (`tier2/setup_target.py`).

3. **Validation before trust.** Every target is checked two ways before screening: (a) **native
   redock** — does the engine reproduce the known crystal pose (<2 Å)? (b) **enrichment gate** —
   does it rank known actives above property-matched decoys (ROC-AUC > 0.5)?

4. **Screening.** Validated targets are screened against a compound library; every compound gets a
   predicted binding score; results are ranked and the top hits cross-referenced with each drug's
   known mechanism.

## How it was calculated (the computation, in plain terms then precisely)

**In plain terms:** for each molecule, the docking program (AutoDock Vina) tries thousands of
ways to fit it into the target protein's binding pocket, then reports the best fit's predicted
binding strength as a number in kcal/mol. **More negative = predicted to bind more tightly.** A
typical strong fit is around −10 to −14; a weak one is around −5 to −7.

**Precisely (so it can be reproduced):**

- **Docking engine:** AutoDock Vina 1.2.5, default Vina scoring function (an empirical function
  fitted to thousands of measured protein–ligand affinities), exhaustiveness 8, fixed random seed.
- **Target (receptor) prep:** structure downloaded from the RCSB Protein Data Bank; one chain
  selected; the binding-pocket cofactors (e.g. GDP + Mg²⁺ for KRAS) kept; protonated at pH 7.4;
  converted to PDBQT with OpenBabel. Docking box centered on the native ligand, sized to its
  bounding box + 8 Å (minimum 22.5 Å per Vina's recommendation).
- **Molecule (ligand) prep:** SMILES string → dominant protonation state at pH 7.4 (Dimorphite-DL)
  → 3D structure (RDKit ETKDG) → energy-minimized → PDBQT (Meeko). For re-docking known crystal
  ligands, correct bond orders are stamped from the PDB "ideal" reference (RDKit template) — this
  avoids mis-guessing chemistry from coordinates alone.
- **Pose accuracy metric:** symmetry-corrected heavy-atom RMSD (spyRMSD) between the docked pose
  and the crystal pose; for very large symmetric molecules, an exact Hungarian-algorithm RMSD.
- **Enrichment metrics:** ROC-AUC, Enrichment Factor at 1/5/10%, BEDROC (α=20), computed on 40
  known actives (from ChEMBL, ≤1 µM) vs ~600 property-matched, topologically dissimilar decoys.
- **Active learning:** a RandomForest model (scikit-learn) learns to predict docking score from
  molecular fingerprints (ECFP4), so large libraries can be prioritized instead of fully docked.

Full step-by-step methodology, parameters, and every validation number are in **[METHODS.md](METHODS.md)**.

## Validated targets & results

| Target | PDB | Native redock RMSD | Enrichment ROC-AUC | EF 1% | Interpretation |
|---|---|---|---|---|---|
| KRAS G12D | 7RPZ | 0.51 Å | 0.690 | 6.6× | Most common PDAC driver (~40%). Modest, real discrimination — rankings noisy. |
| KRAS G12V | 9U50 | 0.92 Å | (screen in progress) | — | 2nd allele (~30%); good OFF-state screening target. |
| KRAS G12R + CypA | 8TBH | 0.78 Å | n/a | — | ON-state glue mechanism: pose validated, but plain-Vina *scoring* weak → not used for screening. |
| PARP1 | 9ETQ | 0.90 Å | **0.874** | **15.3×** | Strongest discrimination. Known PARP inhibitors (olaparib, EB-47) self-surfaced as controls. |

Ranked candidate lists from screening ~6,400 approved/clinical drugs are in **[`candidates/`](candidates/)**,
with one-page wet-lab handoff docs per target. Notable patterns: a MET-inhibitor cluster on
KRAS G12D (tivantinib, merestinib, PHA-665752, SU11274) and DDR-coherent PARP1 hits (the ATR
inhibitor ETP-46464; the NAD⁺-pathway compound KPT-9274).

## What's in this repository (data & file guide)

| Path | Contents |
|---|---|
| [`candidates/`](candidates/) | **The deliverable.** Ranked top hits + wet-lab handoff docs per target. |
| `libraries/repurposing_hub/screen_*/` | Full screening results per target (`results_ranked.csv` = every compound ranked). |
| `reports/` | Tier 0 validation reports (the original proof-of-concept). |
| `tier2/targets/*/` | Per-target receptor config + native-redock validation report. |
| `tier0_smoke_test.py`, `tier1/`, `tier2/` | All pipeline source code. |
| [`DATA_DICTIONARY.md`](DATA_DICTIONARY.md) | **Every file and every column explained** (names, units, how computed). |
| [`METHODS.md`](METHODS.md) | Full methods + reproducibility record + caveats. |
| `dataset_metadata.jsonld` | Machine-readable dataset metadata (schema.org/Dataset). |
| `CITATION.cff` | Machine-readable citation. |
| `environment.yml` | Exact software environment (conda). |

**Note on what's *not* committed:** per-compound 3D pose files (`poses/`, `ligands/`, `*.pdbqt`)
are excluded to keep the repo small — they are large and fully regenerable from the code. The
ranked result tables (the scientific record) are included.

## Reproduce it

```bash
mamba env create -f environment.yml      # one-time; all open-source tools
mamba activate pancscan
python tier0_smoke_test.py               # proof: re-docks MRTX1133 into KRAS G12D (~0.5 Å)
```
Then set up any target with `tier2/setup_target.py` and screen with `tier1/batch_dock.py`.
See the Quick Start in [METHODS.md](METHODS.md). The pipeline is CPU-only and runs on macOS
(Apple Silicon) or Linux.

## Limitations (please don't skip)

- **Docking scores are approximate** — the Vina scoring function has ~±3 kcal/mol error, which is
  larger than the gap between a potent binder and an average drug. Trust **clusters and enrichment
  statistics**, not the exact rank of any single compound.
- **Rigid receptor** — no induced-fit; some genuine binders need a protein conformation we don't model.
- **Decoys are *presumed* inactive**, not experimentally confirmed non-binders.
- **Molecular-glue / protein-protein-interface targets** (e.g. KRAS ON-state) score poorly with
  plain Vina even when the pose is right — those need ML rescoring (GNINA) or physics simulation (MD).
- **This is computational.** No wet-lab data is contained here. Nothing in this repository should be
  used to make a medical, clinical, or treatment decision.

## How to cite

See [`CITATION.cff`](CITATION.cff) (GitHub will render a "Cite this repository" button). Please also
cite the underlying tools (AutoDock Vina: Trott & Olson 2010; RDKit; Meeko/AutoDock; ChEMBL) and
data sources (RCSB PDB; Broad Drug Repurposing Hub).

## For machines, crawlers & data-search engines

- **Structured metadata:** [`dataset_metadata.jsonld`](dataset_metadata.jsonld) follows the
  [schema.org/Dataset](https://schema.org/Dataset) vocabulary (indexable by Google Dataset Search
  and general crawlers). It declares creator, license, keywords, variables measured, and file
  distributions.
- **Column definitions:** [`DATA_DICTIONARY.md`](DATA_DICTIONARY.md) defines every field, with units.
- **Formats:** results are UTF-8 CSV with header rows; metadata reports are JSON; docs are Markdown.
- **Stable identifiers:** compounds carry Broad Institute IDs (`BRD-...`) and SMILES; targets carry
  RCSB PDB IDs and ChEMBL target IDs; ligand components carry PDB CCD codes.

## Licenses

- **Code:** MIT (see [`LICENSE`](LICENSE)).
- **Computed results & documentation in this repo:** released as open data under
  **CC BY 4.0** (attribution). The docking scores are our original computed contribution.
- **Upstream data carry their own terms** and are *referenced*, not relicensed: compound
  identifiers/SMILES derive from the **Broad Drug Repurposing Hub** (non-commercial use) and
  **ChEMBL** (CC BY-SA 3.0); structures from the **RCSB PDB**. Downstream users are responsible
  for complying with those upstream terms, especially for commercial use.

## Contributing & contact

Self-funded open project led by **Thomas Carfano** (tcarfano@kixie.com). Contributions welcome:
new validated targets, wet-lab collaborations, GPU rescoring, or volunteer compute. Open an issue
or email. If these results help your work, attribution and a note back are appreciated.
