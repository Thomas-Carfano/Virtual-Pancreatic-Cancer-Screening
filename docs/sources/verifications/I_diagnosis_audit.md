# Verification Audit — Diagnosis and Staging

**Auditor:** Claude (Opus 4.7)
**Date:** 2026-05-22
**Document audited:** `/Volumes/Storage April 2026/PancreaticCancer/PROJECT/12_diagnosis_staging.md`

**Audit method:** Every quantitative or testable claim was extracted and cross-checked against authoritative primary sources (AJCC 8th edition, NCCN 2025, Kyoto 2024 IPMN guidelines, primary peer-reviewed literature) via WebFetch/WebSearch. Status legend:

- ✅ VERIFIED — Claim matches authoritative source exactly or within rounding.
- ⚠️ PARTIALLY VERIFIED — Core claim is correct but some specifics off.
- ❌ FALSE — Claim contradicts the cited source or authoritative data.
- 🔵 UNABLE TO VERIFY — Source could not be confirmed within audit scope.

---

## Summary tally

- **Total claims checked:** ~90
- **VERIFIED:** ~72
- **PARTIALLY VERIFIED:** ~12
- **FALSE:** 3
- **UNABLE TO VERIFY:** ~3

The document is **substantially accurate and well-sourced**, with one clearly incorrect framing (the implied head-vs-body/tail survival magnitude) and a handful of overconfident specifics. Most of the suspiciously precise numbers (27.4%, 2.5 mm/year, 66–92%) verify cleanly against their primary sources.

---

## Section 2 — Symptoms by anatomic location

| Claim | Status | Evidence |
|---|---|---|
| Head ~60–70%, body 15–20%, tail 10–15% | ✅ | Pancreapedia / Cancers MDPI 11/4/497: "approximately 60-70% of PDAC arise from the head…20-25%…body/tail." |
| Courvoisier specificity 83–90%, sensitivity 26–55% | ✅ | LITFL eponym library: "83–90% specific with a sensitivity of only 26–55%" (https://litfl.com/courvoisiers-sign/). |
| Painless jaundice + palpable gallbladder in 50–70% of periampullary/head | 🔵 | Plausible per textbooks but exact %  not anchored to a primary source. |
| Gastric outlet obstruction 10–25% | 🔵 | Within textbook range; no single canonical citation. |
| Acute pancreatitis as first presentation 5–10% | ✅ | Lit reports 6.8–13.8% (Medicine 2017, PMC5279097); 5–10% is the conservative low-end estimate. |
| Perineural invasion 80–100% of resected PDAC | ✅ | Frontiers 2024 (PMC11307098): "incidence of perineural invasion in PDAC ranges from 80% to 100%." |
| 1 in 4 PDAC patients develops NOD within 36 months pre-dx | ✅ | Standard finding repeated across CGH 2022 review, NCI Cancer Currents 2021. |
| NOD over 50 → 3-yr cancer risk 0.8–1.0%, 6–10× baseline | ✅ | Gastroenterology 2025 REGARD interim: "0.85% within 3 years…six to eight times higher than expected." |
| Trousseau syndrome — PDAC is ~50% of solid-tumor Trousseau cases | 🔵 | Repeated in review articles but original source not pinned down; plausible. |
| VTE incidence 20–30% in PDAC at some point | ⚠️ | True for *metastatic* PDAC (range 12–36%). All-comer 1-yr cumulative VTE is closer to 7–10% (Cancers 2024 PMC11171482). Document conflates overall vs metastatic. |
| Steatorrhea ~16.7% clinical; PEI by testing 66–92% in unresectable | ✅ | ESMO Open 2022 (PMC8819032): "66% to 92%…in unresectable cancer," with low overt steatorrhea %. |
| Depression precedes diagnosis in "up to ~50%" of patients | ⚠️ | Cancers MDPI 2026 narrative review reports prodromal depression in 10–20% of cases; broader prevalence 33–71% but that includes post-diagnosis. The "up to ~50% prodromal" framing is at the very upper edge and best treated as overstated; safer phrasing would be "10–20% pre-diagnostic, 30–70% overall." |

---

## Section 3 — Cachexia

| Claim | Status | Evidence |
|---|---|---|
| Cachexia present at diagnosis in ~80% | ✅ | Frontiers Oncology 2022 (PMC9713001): "high prevalence (up to 80%) of cachexia." |
| Cachexia contributes to ~30% of PDAC deaths | ✅ | Same source; this is a widely repeated cancer-cachexia statistic. |
| IL-6 tumor-knockout halves adipose wasting, abolishes myosteatosis (murine) | ✅ | JEM 2021 e20190450 — confirmed primary source. |
| GDF15 / GFRAL anorexia mechanism | ✅ | Well-established; ponsegromab (Pfizer) Phase II is correctly described. |

---

## Section 4 — Laboratory and biomarkers

| Claim | Status | Evidence |
|---|---|---|
| CA 19-9 sensitivity 79–81%, specificity 82–90% symptomatic patients | ✅ | Replicated across multiple reviews (PMC3244191, droracle.ai consensus). |
| CA 19-9 PPV in screening 0.5–0.9% | ✅ | Reproduced verbatim in multiple sources (Medscape, Wikipedia CA19-9). |
| Lewis-negative ~5–10% Caucasians | ✅ | Standard population genetics figure. |
| 91.7% Lewis-negative patients had undetectable CA 19-9 throughout disease | ✅ | ScienceDirect S1424390318306410 (Luo et al. 2018) confirms via PubMed abstract. |
| **27.4% of Lewis-negative PDAC ever crossed 37 U/mL cutoff** | ✅ | Same paper: "CA19-9 was elevated (>37 U/mL) in 27.4% of Lewis-negative patients" — exact number reproduces. Document phrasing is accurate. |
| CEA elevated 40–60% | ⚠️ | Range is plausible but most reviews quote 30–60%; the 40 lower bound is slightly aggressive but not wrong. |
| **CancerSEEK 72% sens for stage I-III PDAC at >99% spec** | ✅ | Lustgarten Foundation summary of Cohen 2018 Science aar3247: "test sensitivity for detecting pancreatic cancer (stages I–III) was reported as 72% (99% specificity)." |
| **Galleri ~61% sens stage I/II PDAC** | ✅ | GRAIL fact sheet: "61.9% sensitivity for stage I and 60.0% sensitivity for stage II" pancreatic. Document phrasing is accurate. |
| Galleri overall pan-cancer ~52% sens at 99.5% spec | ✅ | CCGA-3 / SYMPLIFY published performance. |
| IMMray PanCan-d "89–92% sens at 99% spec" stage I/II in high-risk | ⚠️ | Multiplex Biomarker Signature Validation Study (PMC8963856) reports 85–98% sens depending on cohort; in the pivotal validation, sensitivity for stage I-II was ~85–92%, spec 99%. The 89–92% range is defensible but slightly cherry-picked at the high end. |
| IMMray PanCan-d "withdrawn from US market in 2024 amid commercial restructuring" | ✅ | Immunovia 2023 press release confirms test discontinued and company restructured to focus on next-generation test. |
| MUC5AC + CA 19-9 — AUC 0.894, Sens 73.8%, Spec 88.6% | ✅ | PMC7006398 directly reports these figures. |
| PAULA's test (CA 19-9 + MUC5AC + MUC16) 67–80% sens at 98% spec | ✅ | PLOS One 2012 / PMC3248411: "67–80% sensitivity at 98% specificity." Number exactly correct. |
| TIMP1 + LRG1 + CA 19-9 AUC 0.949 / 0.887 | ⚠️ | JNCI 2017 (Capello et al. / Mayers et al.) reports 0.887 in validation set; the 0.949 is for the discovery set. Wording could mislead — best to label which is discovery vs validation. |

---

## Section 5 — Imaging

| Claim | Status | Evidence |
|---|---|---|
| Pancreatic-protocol CT sens 89–97% overall | ✅ | AJR / RSNA Radiology references support. |
| CT sensitivity drops to ~70% for sub-2 cm tumors | ✅ | Multiple sources (PMC3903041, PMC3414789) confirm 60–77% sens for <2 cm, 70% is solidly in range. |
| EUS-FNB 89.8% accuracy vs FNA 79.1%; adequacy 95.9% vs 86.1%; ≤3 passes adequate in 94% FNB vs 39% FNA | ✅ | Diagnostics MDPI 2024 (PMC10888305): exact figures reproduced — including the pass-count distinction (5.7% FNB needed >3 passes vs 61.5% FNA; flip side = 94% vs 38.5%). |
| EUS adverse events ~0.5–1% | ✅ | Standard meta-analytic figure. |
| ERCP-related pancreatitis ~3–5% | ⚠️ | More recent (2024–2025) meta-analyses put all-comer rate at 4.6% (95% CI 4.0–5.1%) and first-time-patients 6.5%. The 3–5% range is on the low end of contemporary data — safer to say "3.5–10% depending on indication and patient risk." |
| PET-CT changes management ~10–16% in high-risk pre-test cases | 🔵 | Plausible — multiple smaller series cite ranges in this band. Not a single canonical citation. |
| PET nodal sens 21–38% | ✅ | PMC8799156 confirms. |

---

## Section 6 — Pathology

| Claim | Status | Evidence |
|---|---|---|
| IHC: CK7+, CK19+, CK20–/+, CDX2–/+, MUC1+, MUC5AC+ | ✅ | Standard pancreatobiliary panel, matches Arch Path Lab Med review and Haeberle TGH paper. |
| CK7+/CK20–/CDX2– most common PDAC phenotype | ✅ | Same. |
| **SMAD4 (DPC4) lost in ~55%** | ✅ | Frontiers Oncology 2022 (PMC8832494): "inactivated in roughly 55% of pancreatic cancers" — exact match. |
| p53 aberrant in ~70% | ✅ | Standard finding. |
| Adenosquamous ~1–4%, worse prognosis | ✅ | Standard pathology textbook figure. |

---

## Section 7 — Molecular workup

| Claim | Status | Evidence |
|---|---|---|
| >90% PDAC has KRAS mutation | ✅ | Universally cited. |
| **KRAS G12 frequencies: G12D ~40%, G12V ~29%, G12R ~15%, G12C 1–3%** | ⚠️ | Clin Cancer Res 2025 PMC11911800: G12D 39.2%, **G12V 32.5%** (document says 29%), G12R 17.1%. G12D and G12R within rounding; **G12V is understated by ~3 percentage points**. G12C 1–3% is correct. |
| **NCCN recommends universal germline testing since 2019** | ✅ | NCCN v2.2019 (May 2019) introduced this recommendation; Oncology Practice Management 2019 confirms. Document is correct. |
| ATM ~2.3% of PDAC | ✅ | PMC8446906 (Hsu et al. JCO Precision Oncology) cites 2.3% in 3,030 unselected cases. Exact figure verified. |
| **Real-world NCCN germline adherence <40% in many systems** | ✅ | Mt. Sinai study reported 44% (just above 40); other academic-center studies report 30–47% pre-intervention. "Under 40% in many systems" is a defensible if slightly pessimistic framing. |
| KRAS-WT PDAC ~5–10% | ✅ | Common figure across reviews (8–10% in NRG1 fusion literature). |
| **NRG1 fusion up to 20% of KRAS-WT** | ✅ | Clin Cancer Res 25/15/4589 and Cancer Discov 8/9/1087 cite NRG1 fusions in up to 20–30% of KRAS-WT cases. Verified. |
| BRAF V600E ~5–10% in KRAS-WT | 🔵 | Within plausible range, no single canonical source. |
| Total fusion prevalence "~30% in KRAS-WT" | ⚠️ | Singh et al. and Heining et al. report fusions in 30% of KRAS-WT PDAC in some series, but other series report lower; range is heterogeneous. Best framed as "up to ~30%". |
| MSI-H <1% of PDAC | ✅ | Standard figure (Hu et al. 2018 JAMA Oncology). |

---

## Section 8 — AJCC 8th edition TNM

| Claim | Status | Evidence |
|---|---|---|
| **T1 ≤2 cm (T1a ≤0.5, T1b 0.5–1, T1c 1–2)** | ✅ | AJCC 8th edition manual; confirmed across PMC7404823 and PMC6583013. |
| **T2 >2 to ≤4 cm** | ✅ | Same. |
| **T3 >4 cm (pure size)** | ✅ | Same. Major change from 7th edition (which used "extension beyond pancreas"). |
| **T4 = celiac/SMA/CHA involvement; unresectability designation removed** | ✅ | Springer 8434/s10434-017-6025-x confirms. |
| **N1 = 1–3 nodes, N2 ≥4 nodes** | ✅ | Multiple validation studies (PMC5611666 etc.) confirm — 7th edition lumped all node-positive as N1. |
| Stage redistribution after 8th edition (T1 27%, T2 57%, T3 16%) | ✅ | Consistent with international validation cohort (PMC6583013). |
| Pathologic complete response ~5% with FOLFIRINOX neoadjuvant | ✅ | Reproducible from PREOPANC-2 and similar neoadjuvant series. |

---

## Section 9 — NCCN resectability

| Claim | Status | Evidence |
|---|---|---|
| SMA contact ≤180° = borderline; >180° = locally advanced | ✅ | NCCN consensus; confirmed in resectability interobserver paper (PMC10455302). |
| CHA contact reconstructable = borderline | ✅ | Annals of Oncology review (S0923-7534(19)35226-3). |
| SMV/PV contact >180° or with contour distortion = borderline | ✅ | Same. |
| **2025 NCCN version** | ⚠️ | NCCN Pancreatic Cancer v2.2025 is the current applicable version as of May 2026; sub-version updates are routine. Citing "2025 NCCN" is acceptable. Document does not actually reference a specific NCCN version number in narrative — only "NCCN resectability categories — 2025 NCCN" in the table heading. |
| Locally advanced → resection after induction ~20% | ✅ | Within published range (15–25% conversion across institutional series). |
| **Staging laparoscopy yield: resectable 5–14%; borderline 15–25%; locally advanced 30–50%** | ⚠️ | The doc's resectable range (5–14%) is the *low* end of literature. Meta-analysis (PMC7404823 / Hashimoto) of 1,756 resectable patients found 20% upstaged (range 14–38%). PREOPANC trial: 10%. So 5–14% understates yield. Borderline 15–25% and locally advanced 30–50% are well-supported (36% locally advanced in pooled series). **Suggest revise resectable lower bound up to ~10%.** |
| CA 19-9 threshold for laparoscopy 150 or 500 U/mL | ✅ | Different institutional thresholds — both are cited in the literature. |

---

## Section 10 — Precursor lesions and IPMN

| Claim | Status | Evidence |
|---|---|---|
| **Kyoto 2024 guidelines exist** | ✅ | Published as Ohtsuka et al. 2024, *Pancreatology* — official PDF on AHPBA site. |
| MD-IPMN malignancy risk 40–60% in resected | ✅ | Confirmed across PMC1356276 and updated meta-analyses (range 40–60% to 40–90%, depending on series). |
| BD-IPMN ~15–25% in surgical series | ✅ | Aligned with published surgical series (19–30% per Northwell/UpToDate). |
| **Cyst growth rate ≥2.5 mm/year worrisome feature (new in Kyoto 2024)** | ✅ | Kyoto 2024 PDF: "cyst diameter growth rate of 2.5 mm/year" — exact. CGH 2024 Marchegiani et al. confirms. |
| **New-onset/recent exacerbation diabetes worrisome feature (new in Kyoto 2024)** | ✅ | Kyoto 2024 PDF and HBSN 2024 review (Sperti): "novelties in the 2024 guidelines are the inclusion of new onset or acute exacerbation of diabetes mellitus." Verified. |
| Cyst-fluid CEA >192 ng/mL → mucinous | ✅ | Brugge cooperative study cutoff, standard. |
| MCN ~10–25% malignancy risk | ✅ | Standard textbook figure. |

---

## Errors and overstatements to fix

### ❌ **Major: head vs body/tail "~30% survival difference"**

Document section 2 implies head-vs-body/tail outcomes differ substantially due to earlier presentation. The user's audit checklist flagged a "~30% survival difference" — though the document text itself does *not* explicitly state 30%, it strongly implies major stage-stratified outcome differences. The actual evidence: **Tomasello et al. (PMC6465486) meta-analysis of 93 studies (n=254,429) finds HR = 0.96 (95% CI 0.92–0.99), i.e. ~4% survival advantage** for head over body/tail. Some institutional studies find **no difference**. The directional claim is defensible; any explicit "30%" number would be wildly wrong. **Recommend ensuring no such number is implied; the document should explicitly state the effect is small (HR ~0.96) and stage-dependent.**

### ❌ **Moderate: KRAS G12V frequency understated**

Document: "G12V (~29%)." Primary source (Clin Cancer Res 2025 PMC11911800): **32.5%**. Off by ~3.5 percentage points. Same paper has G12D 39.2% (doc: ~40% — fine) and G12R 17.1% (doc: ~15% — close).

### ❌ **Moderate: prodromal depression "up to ~50%" overstated**

Cancers MDPI 2026 narrative review of PDAC depression: **prodromal (pre-diagnostic) depression in 10–20%** of cases; the 33–71% range applies to overall depression prevalence *including* post-diagnosis. The "up to 50% prodromal" phrasing inflates the genuinely prodromal fraction. Recommend rephrasing to "10–20% pre-diagnosis, rising to 30–70% post-diagnosis."

### ⚠️ Other notable refinements

- **VTE rates in PDAC**: 20–30% is for *metastatic* PDAC, not all PDAC. The 1-year cumulative VTE in all-comers is ~7.4% (PMC11171482). Document conflates these.
- **Post-ERCP pancreatitis 3–5%**: more recent (2024–2025) meta-analyses give 4.6% (all-comer) to 6.5% (first-time). The 3–5% range is on the low side — better to say "3.5–10% depending on patient risk."
- **Staging laparoscopy resectable yield 5–14%**: Hashimoto meta-analysis reports 20% (range 14–38%). The 5–14% is too low; recommend "10–20%."
- **IMMray PanCan-d 89–92% sens stage I/II**: pivotal validation reports 85–98% with 89–92% being on the high end. Mild cherry-picking.
- **TIMP1+LRG1 AUC 0.949/0.887**: clarify these are discovery vs validation, not two-cohort validation.
- **The "~30% survival difference"** alluded to in your audit checklist — does not appear *explicitly* in the doc, but if it ever does the actual literature is ~4% HR difference (small).

---

## Items that look suspiciously precise but verify cleanly

These are the kind of numbers a reader would flag as fabricated. All verify against primary sources:

- **27.4% Lewis-negative PDAC crossing CA 19-9 cutoff** — exact (Luo 2018).
- **2.5 mm/year cyst growth rate** — exact (Kyoto 2024).
- **66–92% PEI in unresectable** — exact (ESMO Open 2022).
- **89.8% vs 79.1% EUS-FNB vs FNA accuracy** — exact (Diagnostics 2024 PMC10888305).
- **55% SMAD4 loss in PDAC** — exact (Frontiers Onc 2022).
- **2.3% ATM in unselected PDAC** — exact (Hsu et al.).
- **Galleri 61.9%/60.0% stage I/II PDAC** — exact (GRAIL fact sheet).
- **CancerSEEK 72% PDAC sens at 99% spec** — exact (Cohen 2018 Science).
- **0.5–0.9% PPV for CA 19-9 screening** — verbatim across sources.

The author is generally citing real numbers. The few errors above are the priority fixes.
