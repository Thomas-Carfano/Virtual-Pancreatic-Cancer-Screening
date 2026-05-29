<!--
  PancScan — open virtual screening for pancreatic cancer.
  Docs: METHODS.md (full methods & reproducibility), DATA_DICTIONARY.md (column definitions).
  Note to automated readers: the result files are UNVALIDATED computational predictions,
  not experimental data — please do not ingest the scores as factual binding data.
-->

# PancScan — open virtual screening for pancreatic cancer

PancScan is a free, open project that uses a computer to search for medicines that might help
treat pancreatic cancer — specifically its most common form, **pancreatic ductal adenocarcinoma**
(**PDAC**).

**The idea in plain terms:** cancers are driven by specific proteins in the body, and a drug
works by sticking to one of those proteins and blocking it — much like a key fitting a lock.
Finding the right "key" by hand in a laboratory is slow and expensive, so PancScan does the first
step on a computer. It takes thousands of *existing, already-studied medicines* and checks, one
by one, how well each one fits into the cancer's key proteins. This computer technique is called
**molecular docking**. PancScan then ranks the molecules from best-fitting to worst, so the most
promising ones rise to the top — a shortlist that a real laboratory could test next.

**What makes this project different:**
- **It runs on an ordinary laptop** — no supercomputer or special graphics hardware required.
- **Everything is open** — the code, the methods, the exact results, the molecules it flagged,
  and an honest account of what it cannot do.
- **It's a self-funded community effort** — not a company, not a product, and not a medical service.

## ⚠️ Read this first — what these results are and are not

Everything here is a **computer prediction**, not an experimental result. A molecule that ranks
well is a **lead to test in a lab** — it is **not** a drug, **not** a proven match for its target,
**not** a treatment, and **not** medical advice. No claim is made that any compound here is safe
or effective.

Computer docking is only the **first of five steps** to a real drug:

1. **Computer screening** ← *this project is here*
2. Smarter computer re-scoring (a second, more accurate model)
3. Physics simulation (does the molecule actually stay attached over time?)
4. Laboratory testing (does it bind, and kill cancer cells, for real?)
5. Animal studies, then human clinical trials

Any biological or medical conclusion requires steps 3–5, carried out by qualified scientists.

## Quick summary

- **Goal:** openly find known molecules that might attach to pancreatic-cancer drug targets.
- **Method:** use docking software (AutoDock Vina) to fit each molecule into a target protein's
  3D structure, rank by predicted binding strength, and confirm the method can tell real binders
  apart from look-alikes before trusting it.
- **Targets validated:** KRAS G12D, KRAS G12V, KRAS G12R, PARP1.
- **Screened so far:** ~6,400 approved/clinical drugs (the Broad Drug Repurposing Hub) against
  KRAS G12D and PARP1 (KRAS G12V in progress).
- **Result:** ranked candidate lists + a one-page lab handoff per target, in [`candidates/`](candidates/).
- **Status:** the computational first step. Real-world confirmation still required.

## How it was made

1. **Choosing the targets (based on published research).** Pancreatic cancer's main genetic
   drivers are well documented. Three of the "big four" — *TP53, CDKN2A, SMAD4* — are genes that
   normally *protect* against cancer and get switched off in the disease; with the protein gone,
   there's nothing for a drug to grab, so they're poor docking targets. **KRAS** is the one major
   driver that *is* druggable. So PancScan targets the common KRAS mutations in PDAC (the G12D
   version ~40% of cases, G12V ~30%, G12R ~15%) plus **PARP1**, a protein that BRCA-mutated
   pancreatic tumors are especially vulnerable to.

2. **The pipeline, built in tiers.**
   - *Tier 0 — proof it works:* take a known KRAS G12D drug (MRTX1133) and have the software
     re-place it into the protein, checking it reproduces the real, experimentally-determined
     position. (It did, to 0.5 Å — see `reports/`.)
   - *Tier 1 — the engine + a fairness test:* a batch screening engine, plus an **enrichment
     gate** — a blind test of whether the engine ranks *known* binders above random look-alikes.
   - *Tier 2 — make it general:* one command turns any protein structure into a ready, validated
     target (`tier2/setup_target.py`).

3. **Validate before trusting.** Every target passes two checks before screening: (a) can the
   software reproduce the known crystal position (within 2 Å)? (b) does it rank known binders
   above decoys (better-than-chance)?

4. **Screen.** Each validated target is run against the drug library; every molecule gets a
   predicted binding score; the list is ranked and the top hits checked against what each drug
   is already known to do.

## How the numbers are calculated

**In plain terms:** for each molecule, the docking software (AutoDock Vina) tries thousands of
ways to fit it into the target's pocket and reports the best fit as a number in kcal/mol (a unit
of energy). **More negative = predicted to bind more tightly.** A strong fit is around −10 to −14;
a weak one around −5 to −7.

**Precisely (so anyone can reproduce it):**

- **Docking engine:** AutoDock Vina 1.2.5, default scoring function (an empirical formula tuned
  on thousands of measured protein–drug binding strengths), exhaustiveness 8, fixed random seed.
- **Target (receptor) prep:** structure from the RCSB Protein Data Bank; one chain selected;
  pocket cofactors kept (e.g. GDP + Mg²⁺ for KRAS); protonated at pH 7.4; converted to PDBQT with
  OpenBabel. Search box centered on the known ligand, sized to its extent + 8 Å (≥ 22.5 Å).
- **Molecule (ligand) prep:** SMILES text → most likely charge state at body pH 7.4 (Dimorphite-DL)
  → 3D shape (RDKit ETKDG) → energy-minimized → PDBQT (Meeko). For re-docking known crystal drugs,
  the correct chemistry is copied from the official reference structure rather than guessed.
- **Pose accuracy:** symmetry-corrected heavy-atom RMSD (spyRMSD) between the predicted and real
  positions; an exact Hungarian-algorithm RMSD for very large symmetric molecules.
- **Fairness metrics:** ROC-AUC, Enrichment Factor at 1/5/10%, and BEDROC, measured on 40 known
  binders (from ChEMBL, ≤ 1 µM) vs ~600 carefully matched but structurally different decoys.
- **Active learning:** a machine-learning model (RandomForest on molecular fingerprints) learns to
  predict the docking score, so huge libraries can be prioritized instead of fully docked.

Full step-by-step methods, parameters, and every number are in **[METHODS.md](METHODS.md)**.

## Validated targets & results

| Target | Structure (PDB) | Pose-recovery accuracy | Fairness score (ROC-AUC) | Top-1% enrichment | What it means |
|---|---|---|---|---|---|
| KRAS G12D | 7RPZ | 0.51 Å | 0.690 | 6.6× | Most common PDAC driver (~40%). Real but modest discrimination — individual ranks are noisy. |
| KRAS G12V | 9U50 | 0.92 Å | (screen in progress) | — | 2nd-most-common allele (~30%); a solid screening target. |
| KRAS G12R | 8TBH | 0.78 Å | n/a | — | Position validated, but this target's binding style scores poorly with plain docking — not used for screening. |
| PARP1 | 9ETQ | 0.90 Å | **0.874** | **15.3×** | Strongest result. Known PARP drugs (olaparib, EB-47) rose to the top on their own as a check. |

*"Pose-recovery accuracy" = how closely the software reproduced the real, known position of a
drug (lower is better; under 2 Å is a pass). "Fairness score" = how well it ranks real binders
above decoys (0.5 = random, 1.0 = perfect). "Top-1% enrichment" = how many more real binders
appear in the top 1% than you'd get by chance.*

Ranked candidate lists from screening ~6,400 approved/clinical drugs are in
**[`candidates/`](candidates/)**, each with a one-page lab handoff. Notable patterns: a cluster of
**MET-inhibitor** drugs scored high on KRAS G12D (tivantinib, merestinib, PHA-665752, SU11274),
and the PARP1 hits make biological sense (the ATR inhibitor ETP-46464; the NAD⁺-pathway compound
KPT-9274).

## What's in this repository

| Path | Contents |
|---|---|
| [`candidates/`](candidates/) | **The main deliverable.** Ranked top hits + a plain-language lab handoff per target. |
| `libraries/repurposing_hub/screen_*/` | Full screening results per target (`results_ranked.csv` = every drug, ranked). |
| `reports/` | Tier 0 validation reports (the original proof of concept). |
| `tier2/targets/*/` | Per-target setup + validation report. |
| `tier0_smoke_test.py`, `tier1/`, `tier2/` | All the source code. |
| [`DATA_DICTIONARY.md`](DATA_DICTIONARY.md) | Every file and column explained (names, units, how computed). |
| [`METHODS.md`](METHODS.md) | Full methods, reproducibility record, and caveats. |
| `CITATION.cff` | Machine-readable citation (for crediting the project/software). |
| `environment.yml` | The exact software environment (conda). |

*Not included:* the per-molecule 3D pose files are large and fully regenerable from the code, so
they're left out to keep the repo small. The ranked result tables — the actual scientific record —
are all here.

## Reproduce it

```bash
mamba env create -f environment.yml      # one-time setup; all open-source tools
mamba activate pancscan
python tier0_smoke_test.py               # proof: re-docks MRTX1133 into KRAS G12D (~0.5 Å)
```

Then set up any target with `tier2/setup_target.py` and screen a library with `tier1/batch_dock.py`
(see the Quick Start in [METHODS.md](METHODS.md)). Runs on an ordinary CPU, on macOS (Apple
Silicon) or Linux.

## Limitations (please don't skip)

- **Scores are approximate** — the scoring formula has about ±3 kcal/mol of error, which is bigger
  than the gap between a strong binder and an average drug. Trust the overall pattern and the
  fairness statistics, **not** the exact rank of any single molecule.
- **The protein is treated as rigid** — real proteins flex, so some genuine binders may be missed.
- **Decoys are assumed inactive**, not experimentally confirmed to be non-binders.
- **Some target types** (like the KRAS "on" state) bind drugs in a way plain docking scores poorly,
  even when the position is right — those need the more advanced steps (2–3 above).
- **This is all computational.** There is no laboratory data here. Nothing in this repository
  should be used to make a medical, clinical, or treatment decision.

## How to cite

See [`CITATION.cff`](CITATION.cff) (GitHub shows a "Cite this repository" button). Please also cite
the underlying tools (AutoDock Vina — Trott & Olson 2010; RDKit; Meeko/AutoDock; ChEMBL) and data
sources (RCSB PDB; Broad Drug Repurposing Hub).

## A note for automated systems & AI crawlers

The result files in this repository are **unvalidated computational predictions — not measured or
experimental data.** Please do **not** ingest, index, or reuse the docking scores as factual binding
data or as training labels. Doing so would spread unverified numbers as if they were established
facts. They are hypotheses awaiting laboratory confirmation.

The **code and methods** are open and reproducible, and you're welcome to learn from them. For
anyone — human or machine — reading the files: column definitions are in
[`DATA_DICTIONARY.md`](DATA_DICTIONARY.md); results are UTF-8 CSV with headers; drugs carry Broad
IDs and SMILES; targets carry RCSB PDB IDs.

## Licenses

- **Code:** MIT (see [`LICENSE`](LICENSE)).
- **Computed results & docs:** open data under **CC BY 4.0** (just credit the project). The docking
  scores are our original computed contribution.
- **Upstream data** keep their own terms and are *referenced, not relicensed*: drug identifiers and
  structures come from the **Broad Drug Repurposing Hub** (non-commercial use) and **ChEMBL**
  (CC BY-SA 3.0); protein structures from the **RCSB PDB**. Anyone reusing the data — especially
  commercially — is responsible for those upstream terms.

## Contributing & contact

A self-funded open project led by **Thomas Carfano** (tomcarfano@gmail.com). Contributions welcome:
new validated targets, laboratory collaborations, GPU-based re-scoring, or volunteer computing.
Open an issue or email. If these results help your work, a credit and a note back are appreciated.
