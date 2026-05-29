# N — Final Verification Pass (pre-publication audit)

Date: 2026-05-22. Verifier: Claude Opus 4.7 (1M).
Scope: spot-check ~50 corrections from prior audits + 5 replacement PDB IDs + 8 outstanding ⚠️ items.

Status legend: ✅ Confirmed / ⚠️ Partial / ❌ False / 🔵 Unable to verify

---

## Part A — Spot-check recent corrections

### 1. Folding@home KRAS-VHL paper (Tu / Qiu et al. JACS Au 2024)
**Status:** ⚠️ Partial — affiliation correct, first-author attribution wrong, numerical specifics nearly correct.

- **Affiliation:** ✅ Huang is at **University of Wisconsin–Madison** (Hirschfelder Chair, joined September 2021). Previously at HKUST.
  - Evidence: https://huang.chem.wisc.edu/xuhui-huang/ ("Prof. Xuhui Huang … UW–Madison")
- **First author / paper title:** ❌ I have been calling this "Tu et al." It is **Qiu et al.** (Yunrui Qiu is first author; Weiping Tang is a middle author, not first/corresponding). Title: *"Non-Markovian Dynamic Models Identify Non-Canonical KRAS-VHL Encounter Complex Conformations for Novel PROTAC Design"* — JACS Au 2024, 4, 3857–3868, DOI 10.1021/jacsau.4c00503.
  - Evidence: https://pmc.ncbi.nlm.nih.gov/articles/PMC11522902/
- **Numerical claims:**
  - "~1.5 ms total MD" → ✅ Paper states "**~1.51 ms in total**" from 2,492 trajectories at ~605 ns avg.
  - "6 metastable encounter states" → ✅ Paper: "**six metastable states each containing a different PPI interface**" (100 microstates lumped into 6 macrostates).
  - "3 with favorable PROTAC linker geometries" → ✅ Paper: "**three metastable states** (States II, III, and V)" deemed promising; States I/IV excluded for distance, VI for kinetic instability.
- **Blog URL:** ✅ https://foldingathome.org/2025/09/18/ resolves to "Catching KRAS in the Act: Simulations Reveal New Paths for Targeted Protein Degradation," author Xuhui Huang, dated September 18, 2025.

**Correction needed:** Change "Tu et al." → **"Qiu et al."** everywhere in the plan.

---

### 2. OpenMM platforms on Apple Silicon
**Status:** ✅ Confirmed.

- Upstream OpenMM supports CUDA, HIP, OpenCL, CPU, Reference. **No native Metal.** On macOS, OpenMM uses Apple's OpenCL implementation.
  - Evidence: https://docs.openmm.org/latest/userguide/application/01_getting_started.html — "On macOS, OpenCL is included with the operating system."
- `philipturner/openmm-metal` is a third-party plugin by Philip Turner (MIT-licensed) that adds a Metal platform (currently labeled "HIP" internally as a workaround for the energy-minimizer hard-coded platform checks).
  - Evidence: https://github.com/philipturner/openmm-metal — "adds the Metal platform that accelerates OpenMM on Metal 3 GPUs"
- **No correction needed.**

---

### 3. Miniforge install via Homebrew Cask
**Status:** ⚠️ Partial — Cask syntax is correct, but the "conda-forge recommends PKG over Homebrew" framing needs softening.

- `brew install --cask miniforge` is valid. Cask page exists: https://formulae.brew.sh/cask/miniforge
- Upstream conda-forge miniforge README **explicitly discourages Homebrew** ("we do not recommend using Homebrew to install Miniforge"). It does **not** explicitly recommend PKG over other methods; it lists PKG installers alongside shell scripts and Windows executables. Shell installers are emphasized for unattended/CI use.
  - Evidence: https://github.com/conda-forge/miniforge

**Correction needed:** Replace "conda-forge recommends the PKG installer over Homebrew" with **"conda-forge explicitly does not recommend Homebrew; their preferred methods are the signed/notarized PKG installer or shell script from GitHub releases."**

---

### 4. OpenFE on Apple Silicon
**Status:** ❌ False as stated.

- OpenFE installation docs explicitly list `osx-arm64` as a supported CPU architecture. Single-file installer for "MacOS (arm64)" is published. Native ARM support.
  - Evidence: https://docs.openfree.energy/en/stable/installation.html — "We currently support the following CPU architectures: linux-64 [and] osx-arm64"
- Production runs are recommended on Linux x86_64 + NVIDIA GPU (because GPU MD via CUDA is required for the FEP perturbations to run at scale), but that is a *practical* recommendation, not a *Rosetta 2 requirement*.

**Correction needed:** Replace "OpenFE requires Rosetta 2 emulation on Apple Silicon" with **"OpenFE installs natively on osx-arm64 via conda-forge, but the GPU-accelerated FEP backend (OpenMM CUDA) does not run on Apple Silicon — production FEP runs must target Linux x86_64 + NVIDIA. M4 Max is fine for ligand prep, network construction, and analysis only."**

---

### 5. fpocket license
**Status:** ❌ False as corrected.

- fpocket is **MIT License**, NOT GPL-3. Copyright (c) 2020 Peter Schmidtke & Vincent Le Guilloux. Verified directly from raw GitHub.
  - Evidence: https://raw.githubusercontent.com/Discngine/fpocket/master/LICENSE — full MIT text quoted.

**Correction needed:** Revert this correction. The original claim of MIT was correct; my "GPL-3" replacement is wrong. Restore **MIT License**.

---

### 6. PMV Pharmaceuticals (PMVP) status
**Status:** ✅ Confirmed.

- PMV Pharmaceuticals remains an independent NASDAQ-listed entity (ticker PMVP) as of May 12, 2026 (Q1 2026 earnings).
- March 2, 2026: FDA granted Orphan Drug Designation for rezatapopt in TP53 Y220C ovarian/fallopian/peritoneal cancers.
- NDA submission targeted Q1 2027 for platinum-resistant/refractory ovarian.
- OrbiMed exited stake in Feb–Mar 2026 at $1.62/share (which is consistent with PMV being publicly traded, not acquired).
- No 8-K or press release indicates Pfizer or any other acquisition.
  - Evidence: https://www.biospace.com/press-releases/pmv-pharmaceuticals-reports-first-quarter-2026-financial-results-and-corporate-highlights
- **No correction needed.**

---

### 7. MRTX1133 / NCT05737706 termination
**Status:** ⚠️ Partial — timing and reason both need slight refinement.

- **When:** Trial was terminated in **January 2025**, not "January 2025" as a generic statement — ClinicalTrials.gov verification status April 2025, primary completion March 10, 2025.
- **Reason on ClinicalTrials.gov:** "**Formulation challenges**" — that is the official record.
- **Reason per BMS spokesperson (via ApexOnco):** "no safety concerns; PK data **highly variable and suboptimal**."
- **Phase 1 status:** Phase 1 was **completed**; the phase 1/2 study was terminated before phase 2 dose expansion.
  - Evidence: https://www.oncologypipeline.com/apexonco/bristol-exits-kras-g12d
  - Evidence: https://clinicaltrials.gov/study/NCT05737706 (status TERMINATED, reason "Formulation challenges")

**Correction needed:** Phrase as **"NCT05737706 was terminated by BMS in January 2025 after completing Phase 1; ClinicalTrials.gov lists 'formulation challenges' as the reason and a BMS spokesperson cited 'highly variable and suboptimal' pharmacokinetics — no safety signal."** Cite both sources.

---

### 8. ACS Cancer Facts & Figures 2026 (US PDAC numbers)
**Status:** ✅ Confirmed.

- 67,530 new US cases; 52,740 deaths estimated for 2026.
- PDAC remains 3rd leading cause of cancer death, projected to be 2nd by 2030.
- 5-year relative survival = 13% (Lustgarten / ACS press release).
  - Evidence: https://www.cancer.org/content/dam/cancer-org/research/cancer-facts-and-statistics/annual-cancer-facts-and-figures/2026/2026-cancer-facts-and-figures.pdf
  - Evidence: https://lustgarten.org/new-report-acs-cancer-facts-figures-2026-report-five-year-relative-survival-rate-for-pancreatic-cancer-remains-at-13/
- **No correction needed.**

---

### 9. Sotorasib & Adagrasib FDA approvals
**Status:** ✅ Confirmed.

- **Sotorasib (Lumakras, Amgen):**
  - NSCLC accelerated approval May 28, 2021 → traditional approval 2023.
  - CRC + panitumumab: **January 15, 2025** for KRAS G12C mCRC after FOLFOX/FOLFIRI failure (CodeBreaK-300).
  - Not approved for PDAC.
  - Evidence: https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-sotorasib-panitumumab-kras-g12c-mutated-colorectal-cancer
- **Adagrasib (Krazati, originally Mirati → BMS):**
  - NSCLC accelerated approval December 12, 2022.
  - CRC + cetuximab: **June 21, 2024** for KRAS G12C mCRC (KRYSTAL-1, ORR 34%).
  - Not approved for PDAC.
  - Evidence: https://www.fda.gov/drugs/resources-information-approved-drugs/fda-grants-accelerated-approval-adagrasib-cetuximab-kras-g12c-mutated-colorectal-cancer
- **No correction needed.**

---

### 10. Divarasib (GDC-6036) status
**Status:** ✅ Confirmed.

- Investigational; Phase 3 ongoing (Krasensa-Lung-302 vs SoC and head-to-head trials).
- Wikipedia + Genentech IR + ClinicalTrials.gov show Phase 3 enrolling; no FDA approval as of May 2026.
- 5–20x more potent than sotorasib/adagrasib in preclinical models.
- **No correction needed.**

---

## Part B — Replacement PDB IDs (the ones we'll cite in the plan)

### 11. PDB 9BR3 + 9BR4 — rezatapopt + Y220C
**Status:** ✅ Both confirmed as p53 Y220C + rezatapopt-class ligands.

- **9BR3:** p53 Y220C + PC-10709 (compound A1ARO). Depositors: Abendroth/Lorimer/Vu/Tanaka. Note: PC-10709 is a rezatapopt-series compound (intermediate / analogue), not rezatapopt itself.
- **9BR4:** p53 Y220C + **PC-9859** = **rezatapopt (PC14586)**. Same depositor set. 1.70 Å resolution. **This is the authoritative rezatapopt+Y220C co-crystal.**
  - Evidence: https://www.rcsb.org/structure/9BR4

**Verdict:** Cite **9BR4 as the rezatapopt co-crystal** (canonical). 9BR3 is a related rezatapopt-class structure — useful as a secondary reference, but do not call it "rezatapopt" without the PC-10709 qualifier.

---

### 12. PDB 4DSO — claimed KRAS G12D apo
**Status:** ❌ Wrong on "apo." Partially correct on G12D.

- **Mutation:** Yes, 4DSO carries G12D (confirmed via downstream literature that explicitly states "the G12D mutation present in the [4DSO] PDB structure").
- **Apo?** **No.** 4DSO is **not apo** — it has **GSP** (GMP-PNP-thiophosphate, a non-hydrolyzable GTP analog), **benzamidine, glycerol, and Mg²⁺** bound. From the Maurer 2012 PNAS fragment-screen paper.
- This is a perfectly fine reference KRAS G12D structure for docking pipelines, but **must not be described as "apo."**

**Verdict:** Either (a) rename in the plan to **"KRAS G12D · GSP (GTP analog)"** — a usable active-state reference — or (b) replace with a true apo entry like **6QUU** (also G12D GCP-bound, also not strictly apo) or **7ACQ** (G12D · GDP). There is no widely-cited *fully apo* KRAS G12D entry; the field universally uses nucleotide-bound G12D as the "reference" state.

**Correction needed:** Re-label 4DSO as "KRAS G12D · GTP-analog (GSP), Maurer 2012" — drop the word "apo." If the plan needs an apo proxy, note that pure apo KRAS structures don't exist in the PDB and the standard reference is GDP/GTP-bound.

---

### 13. PDB 9DMM — divarasib + KRAS G12C
**Status:** ✅ Confirmed (legitimate).

- KRAS G12C covalently bound to divarasib (GDC-6036). Deposited 2024-09-13, released 2025-05-21. Paper: Fernando, Craven, Shokat 2024 in *Small GTPases*.
  - Evidence: https://www.rcsb.org/structure/9DMM
- Note: the listed author affiliations are **UCSF + UC Berkeley + HHMI (Shokat lab)**, not Genentech. So 9DMM is the academic/Shokat-lab co-crystal of divarasib + G12C, not the original Genentech industrial structure. This is fine — it's the publicly available divarasib-G12C structure — but the plan should not imply Genentech deposited it.

**Verdict:** Cite 9DMM as **"Shokat lab divarasib + KRAS G12C co-crystal (Fernando et al. 2024)"** rather than as a Genentech deposition.

---

### 14. PDB 2VUK — Boeckler 2008 PhiKan083 + Y220C
**Status:** ✅ Confirmed (deposit-perfect).

- p53 core domain with Y220C mutation + **PhiKan083** (carbazole derivative, ~150 μM affinity).
- Depositors: Joerger, Boeckler, Fersht (Centre for Protein Engineering, Cambridge).
- Deposited 2008-05-26, released 2008-07-22.
- Publication: Boeckler et al. *PNAS* 2008, 105:10360 — "Targeted Rescue of a Destabilized Mutant of P53 by an in Silico Screened Drug."
  - Evidence: https://www.rcsb.org/structure/2VUK

**Verdict:** Safe to cite as-is for external review. Canonical PhiKan083 + Y220C reference.

---

### 15. PDB 8A32 — claimed JC769 + Y220C
**Status:** ⚠️ Right on Y220C and depositor lineage, but the **ligand ID is wrong**.

- Protein: p53 Y220C. Correct.
- Depositors: Joerger, Baud, Knapp, Stephenson Clarke, Balourdas, plus **Structural Genomics Consortium (SGC)**. Correct.
- **Ligand: KVA, not JC769.** Per RCSB the bound compound code is "KVA" (which is a Baud/Joerger-series Y220C stabilizer, related to but not identical to the published JC744 / JC769 compounds).
  - Evidence: https://www.rcsb.org/structure/8A32

**Verdict:** Citing 8A32 is fine as a "Joerger/SGC Y220C stabilizer co-crystal," but **do not call the ligand "JC769"** — call it by the PDB code KVA or describe it as "a Joerger-series Y220C stabilizer (KVA)." The doc's prior claim that 8A32 contained rezatapopt was already correctly flagged as wrong; the new claim of JC769 is also wrong.

---

## Part C — Outstanding ⚠️ items

### 16. TP53 frequency in PDAC
**Status:** ✅ ~70% is correct; "13–50%" is wrong.

- Literature consensus: TP53 mutated in **~50–90% of PDAC** depending on cohort; modern integrated genomics (TCGA-PAAD, COSMIC, ICGC, advanced metastatic series) center around **60–75%**. A recent 100-pt PDAC cohort: 63%. A 2025 71-pt metastatic series: KRAS 86%, TP53 next-most-common.
- The doc's prior **"13–50%"** range is **wrong** — almost certainly a typo where "13%" referred to *5-year survival* and got mashed into the TP53 row.
  - Evidence: https://pmc.ncbi.nlm.nih.gov/articles/PMC11815932/

**Correction needed:** Replace "13–50%" with **"~65–75% (TCGA-PAAD: ~72%)"** in the mutation-frequency table.

---

### 17. PEGPH20 HALO-301
**Status:** ✅ Confirmed.

- HALO-301 failed in late 2019 (announcement November 4, 2019). PEGPH20 + gem/nab-pac OS 11.2 mo vs gem/nab-pac alone 11.5 mo — futility.
- Halozyme **discontinued PEGPH20 and closed oncology operations**, cut ~160 jobs (55% workforce), pivoted entirely to **ENHANZE** subcutaneous drug-delivery platform (royalty/licensing model).
  - Evidence: https://www.biospace.com/halozyme-announces-halo-301-phase-3-study-fails-to-meet-primary-endpoint
- **No correction needed.**

---

### 18. Enamine REAL Space size (mid-2026)
**Status:** ✅ ~94.5 billion (mid-2026 figure).

- Current Enamine official site: **94.5 billion** make-on-demand molecules.
- Trajectory: was ~31B → ~64B → 76.9B (June 2025 LinkedIn announcement) → 83B (Alipheron) → **94.5B (Enamine official, mid-2026)**.
- Plus xREAL Space (extension) ~4 trillion compounds.
  - Evidence: https://enamine.net/compound-collections/real-compounds/real-space-navigator

**Correction needed:** Use **"~94.5 billion (Enamine REAL Space, mid-2026)"** as the citation number. Old stale numbers (6B, 11B, 21B, 38B, 64B) should all be updated.

---

### 19. ZINC22 size — peer-reviewed source
**Status:** ✅ ~37B (2D) / ~4.5B (3D dock-ready) per the Tingle 2023 paper.

- Tingle et al. *J Chem Inf Model* 2023 (JCIM, the ZINC-22 paper): **"over 37 billion enumerated, searchable, commercially available compounds in 2D, over 4.5 billion of which have been built in biologically relevant ready-to-dock 3D formats."**
- The "~55 billion 2D" alternative is NOT in the peer-reviewed text. (Newer informal ZINC site numbers may differ, but the published source says 37B / 4.5B.)
  - Evidence: https://pubs.acs.org/doi/10.1021/acs.jcim.2c01253
  - Evidence: https://pmc.ncbi.nlm.nih.gov/articles/PMC9976280/

**Correction needed:** Cite **"~37 billion 2D / ~4.5 billion 3D dock-ready (Tingle et al. 2023)"** — drop the "~55B" claim.

---

### 20. GLOBOCAN 2022 pancreatic numbers (Bray 2024)
**Status:** ✅ Confirmed.

- **510,992 new cases globally; 467,409 deaths** in 2022.
- ASR (World) incidence = 4.7 per 100k.
- Source: Bray F. et al. *CA Cancer J Clin* 2024, 74:229–263 (and the IARC GCO factsheet).
  - Evidence: https://gco.iarc.who.int/media/globocan/factsheets/cancers/13-pancreas-fact-sheet.pdf
- (Minor: a parallel IARC export gives 510,566 / 467,005 — both are acceptable; the Bray paper itself uses the 510,992 figure.)

**Correction needed:** Use **510,992 incidence / 467,409 mortality, ASR 4.7/100k, Bray 2024**.

---

### 21. R175H frequency in PDAC
**Status:** ✅ Audit L's ~3% pan-PDAC / ~5–6% of TP53-mut PDAC is correct.

- R175H is **~5.3% of TP53-mutated PDAC** (PNAS 2021, Maddalena et al.).
- R175 + R248 + R273 (the three classic GoF hotspots) **together account for ~17% of all TP53-mutated PDAC**.
- If TP53-mutation prevalence in PDAC is ~70%, then R175H absolute frequency in PDAC is roughly 0.70 × 0.053 = **~3.7%** of all PDAC. So the "~3% PDAC overall / ~5–6% of TP53-mutant PDAC" framing in audit L is good.
  - Evidence: https://www.pnas.org/doi/10.1073/pnas.2025631118

**No correction needed**; keep audit L's numbers.

---

### 22. NCCN universal germline testing for PDAC
**Status:** ✅ Confirmed for 2019.

- NCCN updated the Pancreatic Adenocarcinoma Guidelines (Version 1.2019) to **recommend germline testing for all patients with pancreatic cancer regardless of family history**.
- Rationale: family history is a poor predictor (only ~9% of patients with deleterious germline mutations had significant family history in the 854-pt study).
- BRCA1/2/PALB2-positive patients direct first-line therapy choice (platinum-containing regimens) and maintenance olaparib (POLO trial → FDA approval 2019).
  - Evidence: https://www.oncpracticemanagement.com/issues/2019/june-2019-vol-9-no-6/updated-nccn-guideline-strongly-recommends-germline-testing-for-all-patients-with-pancreatic-cancer

**No correction needed**; the "since 2019" attribution is accurate.

---

### 23. KRAS G12V frequency in PDAC: 29% vs 32.5%
**Status:** ⚠️ Both are reported; "29%" is older/lower-end, "32–36%" is the modern consensus.

- TCGA-PAAD: G12V ~29–30% of KRAS-mutant PDAC.
- Recent (2024–2026) advanced-PDAC cohorts: G12V **32–36% of KRAS-mutant PDAC**, making it #2 after G12D (~40%).
- "32.5%" is well within the modern reported range; "29%" is also defensible if the citation is TCGA.
  - Evidence: https://aacrjournals.org/clincancerres/article/31/6/1082/753262/Distinct-Molecular-and-Clinical-Features-of

**Correction needed:** Pick one of two framings — either (a) **"~30% (TCGA-PAAD)"** or (b) **"~32–36% of KRAS-mutant PDAC (modern advanced-disease cohorts)"**. The mixed 29% / 32.5% in two places of the same doc looks like an internal inconsistency the reviewer will catch.

---

## Summary table of changes required before publication

| # | Item | Severity | Action |
|---|------|----------|--------|
| 1 | "Tu et al." attribution | High | Change to **"Qiu et al."** |
| 3 | Miniforge / conda-forge framing | Low | Soften wording per #3 above |
| 4 | OpenFE Apple Silicon | High | Reverse claim — OpenFE installs natively; FEP backend is the gating issue |
| 5 | fpocket license | High | **Restore MIT** (not GPL-3) |
| 7 | MRTX1133 termination | Low | Use both "formulation challenges" (CT.gov) + "PK suboptimal/variable" (BMS quote); date January 2025 |
| 12 | PDB 4DSO "apo" | High | Drop "apo" — it's G12D · GSP nucleotide-bound |
| 13 | PDB 9DMM provenance | Low | Re-attribute to Shokat lab/UCSF, not Genentech |
| 15 | PDB 8A32 ligand "JC769" | High | Ligand code is **KVA**, not JC769 |
| 16 | TP53 freq in PDAC "13–50%" | High | Replace with **~65–75%** |
| 18 | Enamine REAL size | Low | Update to **~94.5B (mid-2026)** |
| 19 | ZINC22 size "~55B" | Medium | Replace with **~37B 2D / ~4.5B 3D (Tingle 2023)** |
| 23 | KRAS G12V freq 29 vs 32.5% | Low | Pick one framing, cite consistently |

Items 2, 6, 8, 9, 10, 11 (re 9BR4 specifically), 14, 17, 20, 21, 22 — **passed without changes**.
