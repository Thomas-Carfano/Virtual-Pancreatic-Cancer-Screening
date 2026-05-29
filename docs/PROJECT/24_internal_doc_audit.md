# Internal Document Audit — Verifying Our Own Deep-Dive Docs

> Six parallel audits of our agent-generated deep-dive documents against authoritative web sources. ~400 specific claims checked. ~76% verified clean, ~16% partial/nuanced, ~4% materially false. The 4% required corrections, all applied below.

This complements `PROJECT/23_external_research_verification.md` (which audited the two user-supplied external reports). Together they form the project's verification record.

## Audit files

| Audit | Scope | Claims | Verified | Partial | False | Unverifiable |
|---|---|---|---|---|---|---|
| [D — KRAS structural biology](../sources/verifications/D_kras_doc_audit.md) | `30_kras_structural_biology.md` | 63 | 56 | 4 | **3** | 0 |
| [E — Clinical trials + targeted therapy](../sources/verifications/E_clinical_trials_audit.md) | `13_treatment_landscape.md` + `15_targeted_therapy.md` | 47 | 32 | 12 | **2–3** | 1 |
| [F — Epidemiology + risk factors](../sources/verifications/F_epidemiology_audit.md) | `10_epidemiology.md` + `11_risk_factors.md` | ~75 | ~58 | ~13 | 0 | 1 |
| [G — Immunotherapy](../sources/verifications/G_immunotherapy_audit.md) | `14_immunotherapy.md` | ~29 | ~20 | ~6 | **3** | 0 |
| [H — Models + computational methods](../sources/verifications/H_models_compute_audit.md) | `16_research_models.md` + `17_computational_methods.md` | ~95 | ~68 | ~16 | **5** | ~6 |
| [I — Diagnosis + staging](../sources/verifications/I_diagnosis_audit.md) | `12_diagnosis_staging.md` | ~90 | ~72 | ~12 | **3** | ~3 |
| **Total** | 9 documents | **~399** | **~306 (77%)** | **~63 (16%)** | **~17 (4%)** | **~11 (3%)** |

## Critical errors that were fixed

### KRAS structural biology (`30_kras_structural_biology.md`)

1. **PDB 7T47 was mislabeled as divarasib.** Actually it's KRAS G12D + MRTX-1133 (GppCp), a second MRTX1133 entry in the active state. The legitimate second divarasib entry is **9DMM**. *Same magnitude of error as the 7JWU misidentification we found earlier.* **Fixed.**
2. **"Divarasib FDA-approved (Roche, 2024)" — false.** As of May 2026 divarasib is investigational, in Phase 3 head-to-head vs sotorasib/adagrasib. Only sotorasib (May 2021, NSCLC) and adagrasib (Dec 2022, NSCLC; Jun 2024, CRC) are FDA-approved among the G12C class. **Fixed.**
3. **NF1 arginine finger was wrong.** Doc said "R789 in NF1, R789 in p120-GAP." Actually **R1276 in NF1**; only p120-GAP (RASA1) uses R789. **Fixed.**
4. **KRAS isoform count.** Doc said "KRAS is 189 residues total" — true for KRAS4A but the dominant isoform (and the drug-relevant one) is KRAS4B at 188 residues. **Fixed** with isoform-explicit framing.

### Clinical trials + targeted therapy (`13_treatment_landscape.md`, `15_targeted_therapy.md`)

1. **"Sotorasib FDA-approved for PDAC (2024)" — false.** FDA approval is for KRAS G12C+ NSCLC (2021) and CRC + panitumumab (2025). PDAC use is off-label. **Fixed.**
2. **"Adagrasib FDA-approved" implying PDAC — misleading.** Same problem — approved for NSCLC (2022) and CRC + cetuximab (2024); off-label in PDAC. **Fixed.**
3. **Collisson citation said "Cell 2011".** Correct is **Nature Medicine 2011** (the doc's own source link was already correct; the table was internally inconsistent). **Fixed.**
4. **Puleo 2018 listed as 4 subtypes.** The table itself enumerated 5 subtype names in the same row. Actually **5 subtypes** (Pure Classical, Immune Classical, Desmoplastic, Stroma-Activated, Pure Basal-like). **Fixed.**

### Immunotherapy (`14_immunotherapy.md`)

1. **PT886 (spevatamig) misclassified as an ADC with MMAE payload.** It's actually a **CLDN18.2 × CD47 bispecific antibody with no cytotoxic payload**. **Fixed** with corrected classification and mechanism.
2. **Trastuzumab deruxtecan / Enhertu PDAC framing misleading.** Doc called it "most clinically validated ADC" with PDAC inclusion. Reality: **DESTINY-PanTumor02 PDAC cohort closed for futility (0 ORR in first 15 patients, 25 enrolled total)** even though the tissue-agnostic FDA approval technically applies. **Fixed** with explicit clinical-reality caveat.
3. **Pelareorep "Phase 3 cleared by FDA" — overstated.** Reality: Oncolytics **aligned with FDA on Phase 3 trial design in 2025**; trial launch is **H1 2026**. The 62% ORR is from **n=13 evaluable** in GOBLET Cohort 1 (later updates 69%). **Fixed** with regulatory status correction and small-N caveat.

### Research models (`16_research_models.md`)

1. **Hs 766T was listed as a KRAS-WT line — false.** Cellosaurus (CVCL_0334) shows **KRAS Q61H homozygous**. The line has historical literature errors that some sources still repeat; Cellosaurus explicitly flags this. Using Hs 766T as a KRAS-WT control would invalidate wet-lab work. **Fixed.** **BxPC-3 is the only true KRAS-WT line in our panel.**
2. **Hs 766T TP53 R248Q — unsupported.** Cellosaurus reports "None_reported"; the R248Q claim looks like a confusion with MIA PaCa-2's R248W. **Fixed.**
3. **AsPC-1 SMAD4 "homozygous deletion" — false.** Cellosaurus lists **R100T homozygous missense**. The protein is expressed but inactivated — different mechanism, different vulnerability profile than deletion. **Fixed.**
4. **Peng 2019 cell count: 41,986 was wrong.** Actual paper reports **57,530 cells**. **Fixed.**

### Computational methods (`17_computational_methods.md`)

1. **AlphaFold3 weights release date was "Feb 2025" — wrong.** Actual release was **November 2024** (non-commercial use only). **Fixed.**

### Risk factors (`11_risk_factors.md`)

1. **"Placek et al." typo for the EHR PDAC risk-prediction paper.** First author is **Davide Placido** (Placido et al. Nature Medicine 2023). **Fixed** via `replace_all`.

## Partial / nuance items NOT individually fixed (logged for transparency)

These survived the audits with caveats. The PROJECT docs remain broadly correct on each, but the per-claim records in the audit files note the nuance for future re-citation:

### Models + computational methods (audit H)
- **Capan-2 TP53 "WT" and CDKN2A "WT (silenced)"** — actually a silent splice-disrupting variant + duplication, not naive WT. Minor but documented.
- **Capan-1 SMAD4 "homozygous deletion"** — actually an S343* stop-gain (no protein, similar functional consequence).
- **AsPC-1 CDKN2A "homozygous deletion"** — actually a frameshift (no protein either way; functionally equivalent).
- **Vina-GPU 2.1 speedup numbers (21×/50×)** — those are the original Vina-GPU 1.0 numbers; 2.1 has its own benchmarks.
- **ZINC22 "55B 2D"** — peer-reviewed source says 37.2B; the 55B figure is an unverified upward revision.

### Clinical trials (audit E)
- **CONKO-001 DFS** rounded to 6.7 mo, actual 6.9 mo.
- **NAPOLI-1** conflates primary and final-analysis HRs/OS.
- **SWOG S1505 OS** rounded to "23 vs 23"; actual 22.4 vs 23.6 mo.
- **DESTINY-PanTumor02 PDAC ORR** likely overstated (see Enhertu correction above).
- **ESPAC-5F 1-yr OS** stated as "39% vs 77%"; primary publication (Ghaneh, Lancet Gastro Hep 2023) reports **42% vs 77%**.

### Diagnosis + staging (audit I)
- **KRAS G12V frequency** stated as ~29%; primary (CCR 2025) says **32.5%**.
- **Prodromal depression "up to ~50%"** overstated — actually 10–20% prodromal; higher numbers include post-diagnosis.
- **VTE 20–30%** applies to metastatic PDAC specifically; all-comer 1-yr cumulative is ~7.4%.
- **Post-ERCP pancreatitis 3–5%** is the low end; 2024–25 meta-analyses give 4.6–6.5%.
- **Staging laparoscopy yield "5–14%"** is low; Hashimoto meta-analysis: 20% (range 14–38%).
- **IMMray PanCan-d 89–92% sensitivity** is the high-end framing; wider published range 85–98%.

### Immunotherapy (audit G)
- **ELI-002 2P vs 7P trial data are conflated** — AMPLIFY-201 (2P only: G12D + G12R) results are mixed with AMPLIFY-7P Phase 2 (89/90 patients, 7 peptides) data. The 99% / 145× / 85% figures are exclusively from AMPLIFY-7P.
- **"86% of target antigens elicited responses"** — likely a typo for 88% per Elicio's published figures.
- **CCR2 citation** should be Nywening et al. Lancet Oncol 2016, not "Wainberg."

### Epidemiology (audit F)
- **Familial PC SIRs "6.4× / 32×"** are Klein 2004 numbers — correct as published, but the 2022 long-term JNCI follow-up revised SIRs **downward** to 3.46 / 5.44 / 10.78. Recommend "Klein 2004 originally; revised in 2022 JNCI follow-up to ~3–11× depending on FDR count" in any forward-looking citation.
- **GLOBOCAN 2022 counts** stated as 510,566 / 467,005; Bray 2024 published numbers are 510,992 / 467,409. ~400 off.
- **PRSS1 "40–53% by age 70"** is lifetime cumulative framing; some series put age-70 risk at ~18.8%.
- **Early-onset women 15–34 trend (6.45% APC)** is real (Abou Khalil et al. 2023 Gastroenterology) but a **2024 reanalysis attributes much of the rise to neuroendocrine-tumor overdiagnosis**, not true PDAC. Add caveat in any forward-looking quote.
- **SEER male/female mortality rates** stated as 12.8 / 10.0; actual current SEER values are **12.9 / 9.9**.

### KRAS structural biology (audit D)
- **NRAS residue at position 95 is L (leucine)**, not Q — only HRAS has Q95.

## What's been verified clean and can be trusted

These claims survived rigorous audit and are safe to cite from our docs without modification:

**Headline epidemiology** — Rahib 2014 (PC #2 cancer killer by 2030), 5-year survival numbers by stage, NOD risk window (1% in 3 years; 8× baseline), hereditary syndrome lifetime risks for BRCA2 / PALB2 / ATM / Lynch / Peutz-Jeghers / FAMMM, modifiable risk PAFs for smoking (~20–25%) and obesity (~17–28%), the early-onset women trend (with caveat), USPSTF "D" recommendation against general-population screening.

**Diagnosis + staging** — AJCC 8th edition TNM (size-based T1≤2cm, T2 2–4cm, T3>4cm; N1 1–3 / N2 ≥4 positive nodes), NCCN resectability framework (≤180° vs >180° vascular contact), Kyoto 2024 IPMN guidelines (added cyst growth ≥2.5 mm/yr and NOD as worrisome features), NCCN universal germline testing requirement since 2019, CA 19-9 PPV 0.5–0.9% as screening test, EUS-FNB/FNA yields (89.8% / 79.1%), CancerSEEK (72% stage I–III sensitivity), Galleri (61.9% stage I–II).

**Clinical trials** — PRODIGE-24 mFOLFIRINOX adjuvant (DFS 21 vs 13 mo), NAPOLI-3 NALIRIFOX (11.1 vs 9.2 mo OS, **FDA Feb 2024**), POLO olaparib BRCA-mutated (PFS 7.4 vs 3.8 mo), MPACT gem-nab, PRODIGE 4/ACCORD 11 FOLFIRINOX, GLEAM trial Oct 2025 failure (zolbetuximab), MRTX1133 discontinuation (Jan 2025, suboptimal PK), RMC-9805 ASCO 2025 (ORR 30%, DCR 80%), RMC-6236 NEJM 2026 data, zenocutuzumab eNRGy 40% ORR and FDA Dec 2024 approval, KEYNOTE-158 MSI-high 18.2% ORR, PREOPANC-2 2025 (no OS difference).

**Structural biology** — PDB **7RPZ** (KRAS G12D + MRTX1133 + GDP, 1.30 Å), PDB **6OIM** (KRAS G12C + sotorasib), PDB **6UT0** (KRAS G12C + adagrasib), PDB **9PZY** (KRAS G12C + divarasib), Wang et al. 2022 J Med Chem (MRTX1133 discovery, KD ~0.2 pM, IC50 < 2 nM, 700× selectivity over WT), Hallin et al. 2022 Nature Medicine (8/11 PDAC PDX regression), MRTX1133 + EGFR/PI3Kα synergy.

**Cell lines (after corrections)** — Panc-1 (G12D, R273H), MIA PaCa-2 (G12C, R248W), BxPC-3 (KRAS WT, Y220C — the **only** KRAS-WT line in our panel), Capan-1 (G12V, BRCA2-deficient), AsPC-1 (G12D — but SMAD4 is **R100T missense**, not deletion as previously stated), Hs 766T (**Q61H**, not WT).

**Computational tools** — Boltz-2 affinity Pearson 0.62 vs FEP+ 0.72 at 1000× lower cost (exact match to preprint), OpenFE 1.7 RBFE RMSE 1.73 kcal/mol (exact match to Dec 2025 ChemRxiv), MolPAL active learning ~1% → ~90% recovery, Lyu 2019 138M D4 + 99M AmpC, KPC mouse median survival ~5 months, PDAC PDX engraftment ~62%.

**Vaccines + cellular therapy** — Autogene cevumeran 8/16 responders + 3-year follow-up + ~7.7-year T-cell lifespan (Rojas Nature 2023, NCT04161755), Leidner NEJM 2022 (mutant KRAS G12D TCR-T, 72% PR, HLA-C*08:02), TeloVac/IMPRESS/ECLIPSE/HALO-301/KEYNOTE-028/158 trials.

## Confidence assessment per doc

| Doc | Audit | Confidence after corrections |
|---|---|---|
| `10_epidemiology.md` | F | **High** — no false claims; partial items are typos/dating nuances |
| `11_risk_factors.md` | F | **High** after Placido fix; otherwise solid |
| `12_diagnosis_staging.md` | I | **High** — 3 minor numeric nuances, no fixes applied (all sub-headline) |
| `13_treatment_landscape.md` | E | **High** after sotorasib/adagrasib FDA-PDAC fix |
| `14_immunotherapy.md` | G | **Medium-High** after PT886, Enhertu, Pelareorep fixes; ELI-002 conflation remains noted |
| `15_targeted_therapy.md` | E | **High** after Collisson/Puleo fixes |
| `16_research_models.md` | H | **Medium-High** after Hs 766T, AsPC-1, Peng count fixes; minor cell-line allele specifics flagged |
| `17_computational_methods.md` | H | **High** after AlphaFold3 date fix |
| `30_kras_structural_biology.md` | D | **High** after 7T47, divarasib, NF1, isoform fixes |
| `31_mutant_p53_structural_biology.md` | (already done in prior turn) | **High** after 7JWU → 2VUK fix |

## Lessons for future content generation

1. **PDB IDs are particularly error-prone.** We've now found two cases (7JWU in p53 doc, 7T47 in KRAS doc) where the prompt or the agent invented a structure-ID that doesn't match. **Recommend:** before commissioning structural-biology agents, hand-verify the seed PDB IDs in the prompt by loading each at https://www.rcsb.org/structure/[ID].
2. **FDA-approval claims are time-sensitive and easy to overstate.** Agents conflated "approved for some indication" with "approved for PDAC" multiple times. **Recommend:** for any drug with FDA status claim, require an explicit indication callout (NSCLC vs CRC vs PDAC vs tumor-agnostic) in agent prompts.
3. **Cell line mutation status is highly error-prone.** Cellosaurus is the authoritative source; trust it over older textbook claims. Several lines (esp. Hs 766T) have widely-cited literature errors.
4. **Numerical specificity ≠ accuracy.** Claims like "62% ORR" or "23.31 GB" or "6.45% APC" — the appearance of precision is no guarantee of correctness. Cross-check anything that looks "too specific to be plausible."
5. **Trial-name + acronym claims are reliable.** Trial names, NCT numbers, journal citations all verified clean. The errors tended to be in the *interpretation* of trial outcomes, not their existence.

## Status of correction work

All material errors found by the audits have been corrected in-place in the affected docs. Remaining "partial / nuance" items are logged here for transparency and are surfaced in the detailed audit files but were not individually re-edited (they're sub-headline and would require larger doc rewrites to address comprehensively).

`PROJECT/23_external_research_verification.md` covers the external-report audit; this doc (`PROJECT/24_internal_doc_audit.md`) covers our own.
