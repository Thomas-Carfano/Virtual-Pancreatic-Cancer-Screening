# Audit: 14_immunotherapy.md

**Source:** `/Volumes/Storage April 2026/PancreaticCancer/PROJECT/14_immunotherapy.md`
**Audit date:** 2026-05-22
**Auditor stance:** Ruthless. Every specific numeric/clinical claim verified against primary sources where reachable.

---

## Summary table

| # | Status | Claim | Note |
|---|---|---|---|
| 1 | Verified | PDAC TMB ~2–3 mut/Mb | Median 2.13 mut/Mb in literature |
| 2 | Verified | CD8+ T cells 1–5% of TME | Consistent with literature on "cold" PDAC |
| 3 | Verified | KEYNOTE-028: 24 PDAC patients, 0% ORR | Confirmed |
| 4 | Verified | KEYNOTE-158 MSI-H PDAC: 22 patients, ORR ~18% | Confirmed (18%, the doc says 18.2% which is the literal published value) |
| 5 | Verified | Algenpantucel-L IMPRESS Phase 3 failed | Confirmed, 2016 |
| 6 | Verified | GVAX + CRS-207 ECLIPSE Phase IIb did not beat chemo | Confirmed (Clin Cancer Res 2019, mOS 6.28 mo) |
| 7 | Verified | TeloVac GV1001 Phase 3 failed | Confirmed Lancet Oncol 2014 |
| 8 | Verified | Autogene cevumeran 8/16 responders, MSKCC, BioNTech/Genentech, atezolizumab + mFOLFIRINOX | Confirmed Rojas Nature 2023 |
| 9 | Verified | NCT04161755 is the trial number | Confirmed |
| 10 | Verified | 3-yr follow-up: responders RFS not reached, non-responders 13.4 mo, P=0.007 | Nature 2024 (Sethna et al., follow-up paper) |
| 11 | Verified | T-cell clone estimated lifespan 7.7 yr | Confirmed in Nature 2024 follow-up |
| 12 | Partial | "98% of expanded clones not present pre-vaccination" — doc says "not present pre-vaccination" | Verified |
| 13 | Verified | Leidner/Rosenberg NEJM 2022, 71-yr-old woman, KRAS G12D, HLA-C*08:02, 16.2×10⁹ cells, 72% PR | Fully confirmed |
| 14 | Verified | Tran NEJM 2016 = colorectal patient (original source of the TCRs) | Confirmed (patient 4095, CRC, 1.11×10¹¹ TIL) |
| 15 | Partial / misleading | ELI-002 7P "AMPLIFY-201 and AMPLIFY-7P" presented as a single results block | AMPLIFY-201 was the **2P** version (G12D, G12R only), not 7P. The 99% / 145-fold / 85% / 86% numbers come from AMPLIFY-7P Phase 2 (89/90 patients), NOT AMPLIFY-201. The doc conflates two distinct trials. |
| 16 | Verified | 99% (89/90) mKRAS T-cell response, 145.3× mean baseline, 85% combined CD4/CD8, Phase 2 AMPLIFY-7P | Confirmed via Elicio press release |
| 17 | Partial | "86% of target antigens elicited responses" | Elicio reports "67% responded to all seven epitopes, >80% response rate to each individual KRAS mutation, 88% generated responses to their own tumor-specific mutation." The 86% figure is close to but not exactly the published number; appears the doc misremembered "88% to own mutation" or ">80% per epitope" as 86%. |
| 18 | Verified | IDMC recommended continue unmodified; DFS readout Q4 2025 | Confirmed in Elicio press release |
| 19 | Partial | Pelareorep GOBLET "62% ORR in first-line metastatic PDAC at ASCO 2025" | Verified that 62% ORR was reported (13 evaluable patients in Cohort 1). But this is a small Phase 1/2 single-arm cohort — the doc should make the n=13 explicit. Also later updates reported 69% ORR (SITC) — there are multiple ORR numbers floating around for the same cohort at different timepoints. |
| 20 | False (as stated) | "Phase 3 cleared by FDA" | The FDA aligned with Oncolytics on a Phase 3 trial **design** in 2025; trial launch is **first half of 2026** (per Oncolytics announcements). Pelareorep also entered the Precision Promise platform trial. "Phase 3 cleared by FDA" implies the trial has been authorized to begin enrollment, which is true in the design-alignment sense but not in the sense of an active Phase 3. Misleading. |
| 21 | False / misleading | T-DXd / Enhertu: "Tissue-agnostic FDA approval for HER2+ solid tumors (**including PDAC if HER2 3+**)" — "Most clinically validated ADC across solid tumors" applied to PDAC table | The April 2024 FDA tissue-agnostic accelerated approval (HER2 IHC 3+) does technically cover PDAC, BUT the DESTINY-PanTumor02 PDAC cohort showed **0% ORR in the first 15 patients and was closed for futility** at 25 patients enrolled. Presenting Enhertu as a credible PDAC therapy is misleading — the underlying clinical data in PDAC is null. |
| 22 | Verified | Anetumab ravtansine: mesothelin ADC, Phase II in MSLN+ PDAC | Trial NCT03023722, completed 2019. Published outcomes are weak; "modest activity" is a generous description. |
| 23 | Verified | PT886 Fast Track for CLDN18.2+ metastatic PDAC | Confirmed (Phanes Therapeutics, granted March 2024). Note: PT886 (spevatamig) is actually a **bispecific antibody (CLDN18.2 × CD47)**, not an ADC. The doc lists it in the ADC table with "MMAE payload" — **THIS IS WRONG**. PT886 has no payload. |
| 24 | Verified | CT041 / satricabtagene autoleucel / CARsgen | Confirmed |
| 25 | Verified | Gastric/GEJ Phase 2 published in The Lancet 2025 (CT041-ST-01) | Confirmed (median PFS 3.25 vs 1.77 mo, OS 7.92 vs 5.49 mo) |
| 26 | Partial / misleading | "5/6 PDAC patients had significant CA19-9 decreases at ESMO 2025" | CARsgen ESMO 2025: "Significant decline in CA19-9 levels post infusion was observed in **five (83.3%) patients, with reductions ranging from 51.3% to 96.1%**." So 5/6 is verified literally, but the trial is CT041-ST-05 (NCT05911217), not "CT041-ST-05 (PDAC adjuvant) Phase 1b" — the doc's identifier is correct. The bigger issue is the doc's enthusiasm: 6 patients is tiny; "World's first proof-of-concept for adjuvant CAR-T in solid tumors" is CARsgen's marketing, not independent assessment. |
| 27 | Verified | PEGPH20 HALO-301 Phase 3 failed (mentioned in §12.3) | Confirmed (11.2 vs 11.5 mo mOS, futility) |
| 28 | Verified | Lifileucel FDA approval Feb 2024, melanoma post-checkpoint | Confirmed (Iovance, ORR ~31.5%) |
| 29 | Verified | IMCODE003 = follow-on Phase 2 randomized trial for autogene cevumeran (NCT05968326) | Confirmed (not in the doc body but in the trial registry — the doc just says "Phase 2 ongoing" which is fine) |

---

## Top errors / problems (ranked by severity)

### 1. **PT886 mis-classified as an ADC with MMAE payload** [FALSE]
Document Section 10 ADC table lists:
> **PT886** | Claudin 18.2 / **MMAE** | FDA Fast Track for CLDN18.2+ metastatic PDAC

PT886 (spevatamig, Phanes Therapeutics) is a **bispecific antibody** targeting CLDN18.2 × CD47 — it has no cytotoxic payload. Sources:
- https://www.phanesthera.com/news/phanes-therapeutics-pt886-granted-fast-track-designation-for-the-treatment-of-patients-with-metastatic-claudin-18-2-positive-pancreatic-adenocarcinoma-by-the-fda/
- https://www.prnewswire.com/news-releases/phanes-therapeutics-announces-positive-phase-2-results-of-spevatamig-pt886-in-combination-with-chemotherapy-in-frontline-1l-treatment-of-metastatic-pdac-at-asco-gi-2026-302656945.html

Quote: "PT886 is a first-in-class native IgG-like bispecific antibody targeting claudin 18.2 and CD47."

**Action:** Move PT886 out of the ADC table into the bispecific section, and correct the mechanism. There ARE genuine CLDN18.2 ADCs in development (e.g., LM-302, AZD0901/CMG901) — those would be appropriate to list as ADCs.

### 2. **Enhertu in PDAC misleadingly framed** [MISLEADING]
Document Section 10:
> **Trastuzumab deruxtecan (T-DXd / Enhertu)** | HER2 / DXd | Tissue-agnostic FDA approval for HER2+ solid tumors (**including PDAC if HER2 3+**) | **Most clinically validated ADC across solid tumors**

The FDA's April 2024 tissue-agnostic accelerated approval (IHC 3+, prior therapy, no satisfactory alternative) does technically include PDAC. But the underlying PDAC data is null:
> "In the pancreatic cohort, no objective response was observed in the first 15 patients, and the cohort was closed for further recruitment according to prespecified futility criterion, by which time 25 patients had been enrolled." (DESTINY-PanTumor02, J Clin Oncol)

Source: https://ascopubs.org/doi/10.1200/JCO.23.02005 and https://pmc.ncbi.nlm.nih.gov/articles/PMC10730032/

**Action:** Note explicitly that DESTINY-PanTumor02 PDAC cohort was closed for futility (0/15) — the formal approval applies but the empirical PDAC data does not support use.

### 3. **Pelareorep "Phase 3 cleared by FDA" overstated** [PARTIALLY FALSE]
Document Section 11:
> "62% ORR in first-line metastatic PDAC at ASCO 2025; **Phase 3 cleared by FDA**"

What actually happened: Oncolytics announced **alignment with FDA on Phase 3 trial design** in 2025; trial launch is planned for **first half of 2026**. Pelareorep was selected for the Precision Promise platform Phase 3. "FDA cleared" implies clearance to begin enrolling, which is true for trial design but not for activation. Also the 62% ORR is from n=13 evaluable patients in a Cohort 1 of GOBLET — should disclose the small denominator.

Sources:
- https://oncolyticsbiotech.com/press_releases/oncolytics-biotech-aligns-with-fda-on-pivotal-study-design-for-pelareorep-in-first-line-pancreatic-cancer/
- https://www.prnewswire.com/news-releases/oncolytics-biotechs-pelareorep-selected-for-inclusion-in-precision-promisesm-pivotal-phase-3-platform-trial-301857678.html

**Action:** Rephrase as "FDA-aligned Phase 3 trial design, anticipated launch 2026; n=13 evaluable patients in GOBLET cohort 1."

### 4. **ELI-002 2P vs 7P conflation** [PARTIAL]
Document Section 6 presents AMPLIFY-201 and AMPLIFY-7P results as a single bullet list, implying the 99% / 145-fold / 85% numbers come from both. They do NOT:
- **AMPLIFY-201** = Phase 1 of **ELI-002 2P** (G12D + G12R only) in MRD-positive adjuvant patients (PDAC + CRC). Published in Nature Medicine 2024 / 2025. Different and smaller patient numbers.
- **AMPLIFY-7P** = Phase 1/2 of **ELI-002 7P** (G12D/V/R/A/C/S + G13D). The 99% (89/90), 145-fold, 85% CD4+CD8 figures are from Phase 2 AMPLIFY-7P (Sept 2025 readout).

Sources:
- https://elicio.com/press_releases/elicio-therapeutics-reports-eli-002-7p-achieved-robust-mkras-specific-t-cell-responses-in-99-of-evaluable-patients-in-ongoing-phase-2-amplify-7p-trial/
- https://elicio.com/press_releases/elicio-therapeutics-announces-publication-of-eli-002-updated-amplify-201-phase-1-follow-up-data-in-nature-medicine-for-minimal-residual-disease-mrd-positive-adjuvant-stage-patient/

**Action:** Separate the AMPLIFY-201 and AMPLIFY-7P sections cleanly; attribute the 99% figure exclusively to AMPLIFY-7P Phase 2 (n=89/90).

### 5. **"86% of target antigens elicited responses"** [PARTIAL — likely wrong number]
Elicio's published figures are:
- 67% of patients responded to all seven mKRAS epitopes
- >80% per individual KRAS mutation
- 88% generated responses to their own tumor-specific mutation

There is no "86% of target antigens" figure in the public Elicio releases I can find. Likely the doc's author mis-transcribed 88% → 86%, or conflated multiple metrics.

**Action:** Replace with the exact wording above ("88% generated responses to their own tumor-specific mutation").

---

## Other minor notes

- **§5** says "Three-year follow-up presented in 2024–2025: vaccine-induced T cells persisted up to 3 years in responders." This is accurate but the **Nature 2024** follow-up paper (Sethna et al., Nature 2024) is the canonical reference (https://www.nature.com/articles/s41586-024-08508-4) — worth citing it directly rather than just "updates 2024-2025." The 7.7-year average estimated T-cell lifespan claim **is supported** by this paper.

- **§5** says "Patients received: Atezolizumab, Autogene cevumeran (8 priming doses + boosts), Modified FOLFIRINOX." The actual protocol per Nature 2023 was **sequential**: atezolizumab → autogene cevumeran (8 priming IV doses + booster ~6 months later) → mFOLFIRINOX. The doc lists this as a numbered list with no sequencing emphasis. Minor.

- **§8** "16.2 × 10⁹ autologous T cells engineered to express two HLA-C*08:02–restricted TCRs targeting the KRAS G12D 9-mer peptide GADGVGKSA" — peptide sequence and HLA verified. Note: the canonical published KRAS G12D 9-mer for HLA-C*08:02 is GADGVGKSA (residues 5–13 of KRAS with G12D substitution). Verified.

- **§3.5** "CCR2 + chemo. PF-04136309 plus FOLFIRINOX" — the company name (Pfizer) is correct; PF-04136309 is a Pfizer CCR2 inhibitor. The Phase Ib data was published in Lancet Oncol 2016 (Nywening et al.) — the doc cites "Wainberg et al." which is the wrong first-author attribution. The original report is **Nywening TM et al., Lancet Oncol 2016**. (Wainberg has written related work but is not the Phase Ib first author.)

- **§4 table** for Algenpantucel-L says "Failed 2016; program terminated" — correct, NewLink Genetics IMPRESS readout May 2016.

- **§7 table** describes CT041 trial as "CT041-ST-05 (PDAC adjuvant) Phase 1b; CT041-ST-01 (gastric) Phase 2 positive." Both NCT identifiers and phase labels are correct.

- **§12.3** PEGPH20 / HALO-301 mentioned as failed — verified.

- **§10 bispecifics table** ASP2138 (CLDN18.2 × CD3) NCT05365581 — trial number plausible but not independently verified in this audit.

- **§9** TIL therapy / Lifileucel approval (Feb 2024, ORR 31.5–35%) — verified.

---

## Trial NCT identifiers — quick verification status

| Trial | Doc says | Verified? |
|---|---|---|
| Autogene cevumeran Phase 1 | NCT04161755 | ✅ Verified |
| Autogene cevumeran Phase 2 IMCODE003 | (not stated by NCT) | ✅ NCT05968326 (would be useful to add) |
| CT041 gastric Phase 2 | NCT04581473 | ✅ Verified |
| CT041 PDAC adjuvant | CT041-ST-05 (NCT05911217) | ✅ Verified |
| Mesothelin TCR-T (FH) | NCT04809766 | ✅ Verified |
| Anetumab ravtansine PDAC | NCT03023722 | ✅ Verified |
| KRAS G12V TCR-T | NCT04146298 | ✅ Verified (exists for G12V) |
| ASP2138 CLDN18.2×CD3 | NCT05365581 | 🔵 Plausible, not directly verified |
| PT886 TWINPEAK | NCT05482893 | ✅ Verified |
| Mesothelin neoadjuvant | NCT06054308 | 🔵 Not verified independently |

---

## Total counts

- **Total specific claims audited:** ~29 distinct verifiable claims (numbers, trial IDs, mechanisms, outcomes)
- **Verified:** ~20
- **Partial / needs nuance:** ~6
- **False / misleading as written:** 3 (PT886 mechanism, Enhertu PDAC validation, "Phase 3 cleared")

---

## Recommended fixes

1. **PT886** — re-classify as bispecific (CLDN18.2 × CD47), remove "MMAE payload."
2. **Enhertu / T-DXd** — explicitly disclose DESTINY-PanTumor02 PDAC futility (0/15) alongside the tissue-agnostic approval.
3. **Pelareorep** — change "Phase 3 cleared by FDA" to "FDA-aligned Phase 3 trial design, launch H1 2026; Cohort 1 ORR 62% in n=13 evaluable patients."
4. **ELI-002 §6** — separate AMPLIFY-201 (2P) from AMPLIFY-7P (7P) results clearly; attribute 99% / 145× / 85% to AMPLIFY-7P Phase 2 specifically.
5. **ELI-002 §6** — fix "86%" to "88% generated responses to their own tumor-specific mutation."
6. **§3.5 CCR2** — correct citation to Nywening et al. (Lancet Oncol 2016), not Wainberg.
7. **§5** — cite Sethna et al. Nature 2024 follow-up directly.
8. **GOBLET §11** — disclose n=13 evaluable; note 69% ORR in later SITC update for transparency.
9. **CT041 PDAC §7** — note explicitly that the "5/6 patients had significant CA19-9 decrease" is from a 6-patient cohort — small n.
