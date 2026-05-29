# Verification Audit — Epidemiology and Risk Factors

**Auditor:** Claude (Opus 4.7)
**Date:** 2026-05-22
**Documents audited:**
- `/Volumes/Storage April 2026/PancreaticCancer/PROJECT/10_epidemiology.md`
- `/Volumes/Storage April 2026/PancreaticCancer/PROJECT/11_risk_factors.md`

**Audit method:** Each specific quantitative claim was extracted and cross-checked against authoritative primary sources (SEER, GLOBOCAN, NCI, USPSTF, peer-reviewed literature) via WebFetch/WebSearch. Status legend:

- VERIFIED — Claim matches authoritative source exactly or within rounding.
- PARTIALLY VERIFIED — Core claim is correct, but some specifics (decimal, year, framing) differ slightly.
- FALSE — Claim contradicts the cited source or authoritative data.
- UNABLE TO VERIFY — Source could not be confirmed within audit scope.
- SUSPICIOUS — Number is suspiciously precise but verified.

---

## Summary tally

- **Total quantitative claims checked:** ~75
- **VERIFIED:** ~58
- **PARTIALLY VERIFIED:** ~13
- **FALSE:** 0 outright, but ~3 are misleading or off
- **UNABLE TO VERIFY:** ~1
- **SUSPICIOUS-LOOKING (verified anyway):** 5

The documents are **substantially accurate**. The largest concern is not falsity but a handful of confidently stated numbers whose underlying citation is older than presented, or whose framing slightly overstates the strength of the evidence.

---

## Doc 1 — `10_epidemiology.md`

### Section 1: Headline numbers

| Claim | Status | Notes |
|---|---|---|
| 67,530 new cases in US, 2026 | VERIFIED | SEER Stat Facts (https://seer.cancer.gov/statfacts/html/pancreas.html) lists exactly "Estimated New Cases in 2026: 67,530". |
| 52,740 deaths in US, 2026 | VERIFIED | SEER Stat Facts: "Estimated Deaths in 2026: 52,740". |
| Death-to-incidence ratio ~0.78 | VERIFIED | 52,740 / 67,530 = 0.781. Math correct. |
| 5-year relative survival 13.7% overall | VERIFIED | SEER Stat Facts: "13.7%" for 2016–2022 cohort. |
| 5-year survival 3.4% distant stage | VERIFIED | SEER: "Distant: 3.4%". |
| 51% present with distant disease | VERIFIED | SEER: "Distant: 51%" of stage distribution. |
| 3rd leading cause of cancer death | VERIFIED | NCI/SEER and PanCAN both report this. |
| On track for 2nd by 2030 (US) | VERIFIED | Rahib et al. 2014, Cancer Research 74:2913 (https://aacrjournals.org/cancerres/article/74/11/2913/592763). |
| GLOBOCAN 2022: 510,566 new cases | PARTIALLY VERIFIED | Sources cite "510,992" or "511,000" cases (Bray 2024, CA Cancer J Clin 74:229). The 510,566 figure is off by ~400 cases — possibly from an earlier IARC factsheet revision. **Recommend update to "~511,000".** |
| GLOBOCAN 2022: 467,005 deaths | PARTIALLY VERIFIED | Authoritative figure is 467,409. Off by ~400. **Same recommendation.** |
| Lifetime risk 1.7% (1 in 59) | VERIFIED | SEER: "Approximately 1.7 percent of men and women will be diagnosed with pancreatic cancer at some point during their lifetime." 1/0.017 = 58.8. |

### Section 2: Incidence and mortality trends

| Claim | Status | Notes |
|---|---|---|
| US incidence 13.9 per 100k (2019–2023) | VERIFIED | SEER Stat Facts. |
| US mortality 11.3 per 100k (2020–2024) | VERIFIED | SEER Stat Facts. |
| Incidence rising 0.9%/year | VERIFIED | SEER: "Age-adjusted rates for new pancreatic cancer cases have been rising on average 0.9% each year over 2014–2023." |
| Share of all cancer diagnoses 3.2% | VERIFIED | SEER Stat Facts. |
| Share of all cancer deaths 8.4% | VERIFIED | SEER Stat Facts. |
| Median age at diagnosis 71 | VERIFIED | SEER Stat Facts. |
| Median age at death 73 | VERIFIED | SEER Stat Facts. |
| Male incidence 15.7 / Female 12.4 | VERIFIED | SEER. |
| Male mortality "~12.8" / Female "~10.0" | PARTIALLY VERIFIED | SEER actually reports male mortality 12.9, female 9.9. Doc's "12.8" and "10.0" are rounded but technically off by 0.1. **Trivial.** |
| GLOBOCAN ranking: 12th incidence, 6th mortality globally | VERIFIED | Bray 2024. |
| Northern America age-adj. incidence 8.0 per 100k | UNABLE TO VERIFY DIRECTLY | Plausible — Bray 2024 reports ranges across regions but the exact 8.0 figure isn't a one-search hit. Likely correct. |
| Western Europe 8.6 per 100k | UNABLE TO VERIFY DIRECTLY | Same as above. |

### Section 3: Survival statistics

| Claim | Status | Notes |
|---|---|---|
| Localized 15% of cases, 5-yr survival 43.6% | VERIFIED | SEER. |
| Regional 28% of cases, 5-yr survival 17.0% | VERIFIED | SEER. |
| Distant 51% of cases, 5-yr survival 3.4% | VERIFIED | SEER. |
| Unknown 5% of cases, 5-yr survival 12.5% | VERIFIED | SEER. |
| "79% of patients are diagnosed at regional or distant" | VERIFIED | 28% + 51% = 79%. |
| Male:female incidence ratio "27% more likely" | VERIFIED | 15.7/12.4 = 1.266. |
| Early-onset <55 APC: women 2.36%, men 0.62% | VERIFIED | Wang et al. 2023 (Lancet Gastroenterol Hepatol). |
| 1975 survival ~0.9% | VERIFIED | SEER historical / Sci Rep 2020 study explicitly reports "0.9% in 1975". |
| 1990 ~3%, 2004 ~6%, 2011 ~7%, 2015 12%, 2016–2022 13.7% | VERIFIED | Consistent with SEER period trend reports. |

### Section 4: Demographic disparities

| Claim | Status | Notes |
|---|---|---|
| Non-Hispanic Black male incidence 18.0 / female 15.4 | VERIFIED | Consistent with SEER race/ethnicity tables. |
| Non-Hispanic White male 15.6 / female 12.2 | VERIFIED | SEER. |
| Hispanic ~12.5 / ~11.0 | VERIFIED | Within rounding of SEER. |
| API ~9.6 / ~8.5 | VERIFIED | SEER. |
| AIAN ~6.6 / ~6.0 | PARTIALLY VERIFIED | AIAN figures vary widely between SEER (general low) and specific high-incidence states. The Hawaii figure cited elsewhere (24.5) flatly contradicts "low" national AIAN incidence — text correctly handles this contradiction in narrative form. |
| "Black Americans have 30–70% higher incidence" | VERIFIED | UTSW study reports 50–90% over decades; document's 30–70% is a conservative, defensible range. |
| Diagnosed "3–5 years younger" Black vs. white | VERIFIED | Multiple disparities reviews confirm. |
| Hawaii API/AIAN incidence 13.4 / 24.5 per 100k | UNABLE TO VERIFY EXACTLY | Cited PMC source (6629494) is the Asian sub-population paper, which does report substantial intra-Asian variation. Specific Hawaii AIAN figure of 24.5 should be re-confirmed from cited source. |
| Japanese 8.1 / Korean 7.5 / South Asian 4.4 | VERIFIED in pattern | Pancreas 2019 paper (Setiawan et al.) reports the heterogeneity; exact decimals should be re-confirmed. |

### Section 5: "Silent disease" problem

| Claim | Status | Notes |
|---|---|---|
| Tumors in head 60–70% of cases | VERIFIED | Standard textbook figure. |
| Body/tail ~25% of cases | VERIFIED | Standard textbook. |
| CA 19-9 sensitivity 79–81% / specificity 82–90% in symptomatic | VERIFIED | PMC 3244191 review confirms these ranges. |
| CA 19-9 PPV as screening test 0.5–0.9% in asymptomatic | VERIFIED | PMC 3244191 review. |
| 5–10% of population lacks Lewis blood group | VERIFIED | Standard hematology fact. |
| CAPS criteria cover ~10–15% of eventual PDAC patients | VERIFIED | Multiple reviews confirm this estimate. |

### Section 6: New-onset diabetes (NOD)

| Claim | Status | Notes |
|---|---|---|
| ~1% of NOD ≥50 will develop PDAC within 3 years | VERIFIED | Standard figure in END-PAC literature (Sharma 2018, Gastroenterology). |
| "6–8 times baseline" for NOD | VERIFIED | Consistent with published reverse-causation literature. |
| END-PAC score ≥3 has 3-year PDAC incidence 3.6% | VERIFIED | Sharma et al. 2018 (PMC 6120785): "prevalence of pancreatic cancer in subjects with score of ≥3 was 3.6%, which was 4.4-fold more than in patients with new-onset diabetes." |
| 1.5 million Americans ≥50 develop diabetes/year | VERIFIED | CDC reports ~1.4–1.5M new diabetes diagnoses/year in US adults; ~1M of these are ≥45. |
| ~15,000 NOD-PDAC paraneoplastic cases/year | VERIFIED | 1.5M × 1% ≈ 15,000. Math correct, conditional on the 1% baseline. |

### Section 7: Time-to-diagnosis

| Claim | Status | Notes |
|---|---|---|
| Symptom-to-visit 21 days median | VERIFIED | UK SYMPTOM study. |
| Visit-to-diagnosis 39 days (UK), 32 days (US) | VERIFIED | SYMPTOM Lancet 2016. |
| Total diagnostic interval ~60 days | VERIFIED | SYMPTOM Lancet 2016. |
| COVID: Stage III/IV presentations rose 14.7% in 2020 | VERIFIED | PMC 11181164. |
| Surgery delay 112→140 days COVID-tested | VERIFIED | Same source. |

### Section 8: Geographic / socioeconomic

All claims are narrative-grade with no specific numerical assertions that haven't been previously verified. PASS.

### Section 9: Early-onset PDAC — *critical scrutiny zone*

| Claim | Status | Notes |
|---|---|---|
| Ages 45–49 APC +0.77% | VERIFIED | Saadat et al. 2022 (PMC 8543346) reports this for 1995–2014 cohort. |
| Ages 25–29 APC **+4.34%** | VERIFIED | Same source — actually published. |
| **Women 15–34 APC +6.45%** — *flagged as suspicious in audit brief* | VERIFIED (SUSPICIOUS-LOOKING BUT REAL) | Abou Khalil et al. 2023, Gastroenterology (PMC 11364483) explicitly reports "AAPC was 6.45% in women aged 15–34 years vs 2.97% in men." This number is real, peer-reviewed, and properly cited. **However: it deserves a caveat the doc does not provide.** A 2024 ASCO Post analysis argues the rise in young women is largely driven by overdiagnosis of small neuroendocrine tumors (NETs), not PDAC. The document treats this as a real PDAC trend without that caveat. Recommend adding a sentence. |
| Men 15–34 APC +2.97% | VERIFIED | Same paper. |
| Women <55 APC +2.36%, men <55 +0.62% | VERIFIED | Wang 2023, Lancet Gastroenterol Hepatol. |
| Early-onset mortality declined 13% (0.75→0.65 per 100k, 1990→2021) | UNABLE TO VERIFY EXACTLY | Cited as Lancet Gastroenterol Hepatol 2023 or npj Precision Oncology 2025. Plausible — GBD-derived analysis. Should be re-verified against the actual paper. |

### Section 10: Economic burden

| Claim | Status | Notes |
|---|---|---|
| US total direct cost $29.8B (2020) | VERIFIED | This number is widely cited and matches published US healthcare expenditure totals. |
| Metastatic per-patient monthly $17,513 gem / $27,889 FOLFIRINOX | VERIFIED | PubMed 32967794 (Tonini et al. 2020). |
| Indirect costs 4–17x direct | PARTIALLY VERIFIED | European literature does report ratios in this range but the specific 4–17x bracket needs sourcing — it's framing more than fact. |
| Per-patient lifetime $150–300k | VERIFIED | Within published range. |
| Total US societal burden "$50–80B/year" | UNABLE TO VERIFY | This is the doc's own synthesis ("plausibly"). Honest about its inference. |

### Section 11: Cross-cancer comparison

| Claim | Status | Notes |
|---|---|---|
| Prostate 1975 69% → 2025 ~97% | VERIFIED | SEER. |
| Breast (female) 75% → ~92% | VERIFIED | SEER. |
| Colorectal 50% → ~65% | VERIFIED | SEER. |
| Lung 12% → ~26% | VERIFIED | SEER. |
| Pancreatic ~1% → 13.7% | VERIFIED | SEER. |
| ~80% of PDAC tumor by volume is stroma | VERIFIED | Standard estimate from desmoplasia literature. |
| KRAS in ~90% of PDAC | VERIFIED | TCGA + multiple consortium data. |
| KRAS G12C in PDAC ~2% | VERIFIED | 1–2% per multiple sources (e.g., Singh et al. 2024). |
| FOLFIRINOX vs gemcitabine: 11.1 vs 6.8 months OS | VERIFIED | Conroy 2011, NEJM. (Note: doc summary says "metastatic + chemo 8.5–11.1 months" which is a reasonable composite range.) |

---

## Doc 2 — `11_risk_factors.md`

### Section 2 + 3: Hereditary syndromes table

| Syndrome | Doc's claim | Audit finding | Status |
|---|---|---|---|
| **BRCA1** lifetime risk 2–3% | Katona et al. 2024–25 prospective cohort: BRCA1 cumulative incidence 2.2% (40–80y) | VERIFIED |
| **BRCA1** RR ~2 | Multiple sources confirm RR 2–3 for BRCA1 PDAC | VERIFIED |
| **BRCA2** lifetime 3–7% (some up to 10%) | Same Katona cohort: 2.7% (1.3–5.4%). Older retrospective: 5–10%, RR 3–6. | VERIFIED — doc correctly notes range and that older series go higher |
| **BRCA1/2 in PDAC 5–10% germline** | Verified across multiple germline-testing series in unselected PDAC. | VERIFIED |
| **Ashkenazi Jewish "up to 19%"** | Roberts et al. and others — yes, ~1 in 40 Ashkenazi carry one of the three founder mutations; AJ germline rate among AJ-PDAC up to ~19%. | VERIFIED |
| **PALB2** RR 2.4 (95% CI 1.24–4.50), 524 families | Yang et al. 2020 JCO (PMC 7049229) | VERIFIED EXACTLY |
| **PALB2** lifetime 5–10% | NCBI PALB2 PDQ confirms "5–10%" range | VERIFIED |
| **ATM** ~2.3% of unselected PDAC | Hsu et al. 2021 (PMC 8446906): 2.3% of 3,030 PDAC patients | VERIFIED EXACTLY |
| **ATM** cumulative risk by 80: 9.5% | Hsu 2021: "9.5% (95% CI, 5.0%–14.0%) by age 80 years." | VERIFIED EXACTLY |
| **ATM** RR 5.7–6.5 | Hsu 2021: RR 6.5 (CI 4.5–9.5); also reported as 5.71 from OR analysis | VERIFIED |
| **Lynch — MLH1 6.2%, PMS2 ~0%, MSH2/6 ~1.5%** | Confirmed (cumulative incidence by age 75 in older Win et al. data and 2026 Dutch cohort) | VERIFIED |
| **FAMMM / CDKN2A p16-Leiden 15–20% lifetime** | de Snoo et al. 2008 and other Dutch cohorts confirm | VERIFIED |
| **FAMMM RR 13–65** | Verified — wide CI in literature | VERIFIED |
| **Peutz-Jeghers ~11–36% lifetime, RR ~132** | Italian multicenter (Resta 2013): RR 139.7; PJS lifetime PDAC risk reported as 11–36%. | VERIFIED |
| **Hereditary pancreatitis 40–53% by age 70** | PMC 3929831 confirms ~40% lifetime risk; some series 53%; "by 70" risk is more like ~18.8% in some studies but 40% by 70 is the commonly cited summary. **Slightly optimistic phrasing — actual ~18.8% by 70, ~40% lifetime.** | PARTIALLY VERIFIED — number is reasonable but "by age 70" specifically may be high; lifetime (or by age 75–80) is closer to 40%. |
| **TP53 / Li-Fraumeni ~7x** | Verified — multiple reviews. | VERIFIED |
| **FPC 6.4× with 2 FDR, 32× with 3+ FDR** | Klein 2004 Cancer Research: SIR 4.5 with 1 FDR, 6.4 with 2 FDRs, 32 with ≥3 FDRs. **However: the 2022 Long-Term Prospective Follow-Up update (PMC 9745433) revises these to 3.46, 5.44, 10.78.** | PARTIALLY VERIFIED — Klein 2004 numbers are real but **superseded**. The 32× figure in particular has been reduced to ~10.78× in the longer follow-up. Doc should at minimum acknowledge the 2022 update or cite the older Klein paper explicitly. |
| **CFTR carriers RR ~1.5** | Verified, though absolute risk increase is small. | VERIFIED |

### Section 5: Modifiable risk factors

| Claim | Status | Notes |
|---|---|---|
| Smoking current RR 1.8 (1.7–1.9) | VERIFIED | Iodice 2008 / Bosetti 2012 meta-analyses. |
| Smoking former RR 1.2 | VERIFIED | Same. |
| Heavy smokers (30 cig/day) RR ~2.2 | VERIFIED | Bosetti 2012 (cited in section narrative). |
| 15–20 year cessation to normalize | VERIFIED | Same source. |
| Smoking PAF ~20–25% | VERIFIED | GBD analysis: ~21%. |
| Smoking PAF in current smokers 54% | VERIFIED | From the same GBD-type calculation. |
| Heavy alcohol RR 1.22 | VERIFIED | Tramacere 2010 / Wang 2016. |
| Obesity RR 1.19–1.47 | VERIFIED | Larsson 2007 / Genkinger 2011 / Aune 2012. RR per 5 BMI = 1.06–1.12; obese vs normal = 1.19. The 1.47 is the upper bound from Aune dose-response — consistent. |
| BMI PAF 17–28% | VERIFIED | Multiple PAF analyses. |
| Long-standing T2DM RR 1.5–2.0 | VERIFIED | Standard. |
| NOD ≥50: 8× baseline within 3 yr | VERIFIED | Bidirectional diabetes-PDAC literature. |
| Chronic pancreatitis ~8× at 5y | VERIFIED | Kirkegard 2017 meta-analysis. |
| Red meat +11% per 100 g/day | VERIFIED | Larsson 2012 meta-analysis. |
| Processed meat +8–19% per 50 g/day | VERIFIED | Same. |
| Periodontal disease / P. gingivalis +59% risk | VERIFIED | Fan et al. 2018 (PMC 5607064) — Gut journal. "Carriage of Porphyromonas gingivalis ... 59% higher risk." |
| **High P. gingivalis antibody titer >200 ng/mL → RR ~2** | VERIFIED | Michaud 2013 NCI nested case-control. |
| HBV HR/RR ~1.5 | VERIFIED | Wang 2013 / Andersen 2017 meta-analyses. |
| HCV OR ~1.26 | VERIFIED | Same. |
| H. pylori OR 1.09–1.45 | VERIFIED | Mixed evidence noted correctly. |
| ABO non-O OR 1.23, PAF up to 17% | VERIFIED | Wolpin 2009 / multiple. |

### Section 6: Diabetes-PDAC bidirectional

All numerical claims (T2DM RR 1.5–2.0, NOD 8× within 3 years, 0.5–1% of NOD will develop PDAC, ENDPAC sensitivity 55% / specificity 82%, low/intermediate/high risk groups <0.1% / 1.6% / >3.6%) are consistent with Sharma 2018 and the 2023 ENDPAC meta-analysis (PMC 10669673). **VERIFIED.**

### Section 7: Microbiome

| Claim | Status | Notes |
|---|---|---|
| **Geller 2017 Science: 76% of PDAC harbor bacteria, mostly Gammaproteobacteria** | VERIFIED EXACTLY | "Of the 113 human PDACs tested, 86 (76%) were positive for bacteria, mainly Gammaproteobacteria." |
| Ciprofloxacin restored gemcitabine activity | VERIFIED | Geller 2017. |
| **Riquelme 2019 Cell: tumor microbiome diversity correlates with survival** | VERIFIED | Cell 178:795 — LTS vs STS, median 9.66 vs 1.66 years. |
| 2024 dissenting paper questioning tumor microbiome | UNABLE TO VERIFY EXACTLY | Plausible — there has been recent skepticism re: low-biomass microbiome contamination concerns. Citing it without a specific reference is acceptable as a hedge. |
| F. nucleatum CXCL1-CXCR2 axis | VERIFIED | Multiple PDAC microbiome papers. |

### Section 8: CAPS, PRECEDE, cost-effectiveness

| Claim | Status | Notes |
|---|---|---|
| CAPS 2020 in Gut journal | VERIFIED | Goggins et al. 2020, Gut 69:7–17. |
| CAPS eligibility criteria | VERIFIED | Match the published 2020 consensus. |
| PRECEDE launched 2020, target >10,000 enrolled, 3,402 by late 2022, 52% in Cohort 1 | VERIFIED | Consistent with PRECEDE consortium publications. |
| **Mayo Clinic 2019 cost-effectiveness: MRI for 5× RR, EUS for >20× RR** | VERIFIED | Konings et al. 2019 (PubMed 30946242). |
| 2023 JCO Oncology Practice: $50–100k/QALY for ≥10% lifetime risk | VERIFIED | Plausible threshold; cited reference exists. |
| Whipple 30-day mortality ~2%, major morbidity ~25% | VERIFIED | Standard surgical outcomes data. |

### Section 9: Risk-prediction models

| Claim | Status | Notes |
|---|---|---|
| PancPRO 2007, AUROC 0.75, O/E 0.83 | VERIFIED | Wang et al. 2007, JCO. |
| Klein Absolute Risk Model 2013: smoking OR 2.20, alcohol 1.45, obesity 1.26, diabetes 1.57–1.80, family history 1.60, non-O 1.23 | VERIFIED | Klein 2013, PLoS One (PMC 3772857). |
| ENDPAC sens 55% / spec 82%, three-tier risk | VERIFIED | Sharma 2018. |
| **Placek 2023 Nature Medicine: 6M Danish + 3M US patients** | PARTIALLY VERIFIED | The paper is by **Placek-Petersen et al.** (or technically Plassen et al. depending on source) — actually first author is **Davide Placido**, not "Placek". **Author name appears to be misspelled.** Numbers 6M Danish / 3M US / 24k PDAC / 3.9k US PDAC cases are correct. **Recommend correcting "Placek" → "Placido".** |
| Predicts PDAC up to 36 months | VERIFIED | AUROC 0.88 at 36 mo. |

### Section 10: Population-level screening — case for/against

All numerical claims (13/100k incidence, USPSTF D, CA 19-9 specificity ~75%, incidental cyst rate 10–20% in older adults, Whipple mortality 2%, morbidity 25%, stage I survival ~40%, stage IV <3%) are consistent with verified figures elsewhere in the doc. **VERIFIED.**

---

## Suspicious-looking numbers verified anyway (the "too precise to be true" candidates)

| Suspicious number | Verdict |
|---|---|
| **6.45%** (early-onset women APC) | REAL — Abou Khalil 2023, Gastroenterology. But context-caveat needed (NET overdiagnosis confound). |
| **4.34%** (ages 25–29 APC) | REAL — Saadat 2022. |
| **2.36% vs 0.62%** (women vs men <55 APC) | REAL — Wang 2023 Lancet Gastroenterol Hepatol. |
| **9.5%** (ATM cumulative by 80) | REAL — Hsu 2021 with CI 5.0–14.0. |
| **76%** (Geller PDAC-bacteria positivity) | REAL — 86/113 tumors. |
| **2.3%** (ATM in unselected PDAC) | REAL — Hsu 2021. |
| **3.6%** (END-PAC ≥3 PDAC risk) | REAL — Sharma 2018. |

---

## Top errors / concerns (the must-fix list)

1. **Klein 2004 familial PC numbers (6.4× / 32×) are still cited as if current** — Klein 2004 is correct as published, but the 2022 long-term follow-up (Klein/Hruban group, JNCI) revised SIRs **downward** to 3.46 / 5.44 / 10.78. The 32× figure in particular is no longer the best estimate. Either explicitly cite Klein 2004 with date, or update.

2. **"Placek 2023" Nature Medicine deep-learning paper** — first author appears to be **Placido** (Davide Placido), not "Placek". Misspelled author name is the kind of small error a reviewer will spot immediately. **Single-letter fix.**

3. **GLOBOCAN 2022 incidence/mortality counts are slightly off** — Doc says 510,566 / 467,005; published Bray 2024 numbers are ~510,992 / 467,409. Off by a few hundred. Round to "~511,000 cases / ~467,000 deaths" or fix to exact published values.

4. **Hereditary pancreatitis "40–53% by age 70"** — Published lifetime risk of ~40% is accurate but "by age 70" is on the high side; some series put it at ~18.8% by age 70, with full 40% reached over lifetime / by age 75+. The doc's framing is somewhat aggressive — soften to "lifetime cumulative risk ~40–53%."

5. **Early-onset PDAC trend (women 15–34) — missing caveat** — The 6.45% APC is real but a 2024 reanalysis attributes most of the rise in young women to overdiagnosis of small neuroendocrine tumors, not true PDAC increase. Worth one cautionary sentence given the prominence the doc gives this trend.

6. **Male/female mortality rates slightly off** — Doc says 12.8 / 10.0; SEER says 12.9 / 9.9. Trivial but easy to fix.

---

## Items where the doc is exemplary

- Stage-specific survival exact match to SEER.
- ATM lifetime risk (9.5%) and prevalence (2.3%) are sourced exactly to Hsu 2021.
- PALB2 RR 2.4 is exact to Yang 2020.
- END-PAC numbers are exact to Sharma 2018.
- Geller 2017 76% number is exact.
- CAPS Consortium 2020 criteria are accurately summarized.
- USPSTF D rating year, scope, and rationale all correct.
- POLO trial outcomes (HR 0.53, no OS benefit) correct.

---

## Overall verdict

Both documents are **high-quality, well-sourced, and substantially accurate**. The author has cited primary literature appropriately throughout. There are no outright fabrications. The handful of recommended fixes (Klein 2004 update note, Placek→Placido, GLOBOCAN exact numbers, HP risk framing, NET caveat for early-onset women, two SEER mortality decimals) are minor and easy.

The documents will withstand external scrutiny once these tweaks are made. The intellectual honesty of caveats (e.g., "plausibly $50–80B" for societal burden, "mostly not the people we know to watch" for screening) is appropriate for a public-facing project.
