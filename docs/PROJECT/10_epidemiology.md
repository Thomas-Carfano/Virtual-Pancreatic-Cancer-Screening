# Pancreatic Cancer Epidemiology and the Late-Diagnosis Problem

*A deep look at who gets pancreatic cancer, who dies from it, when it gets caught, and why almost everything about it is harder than the cancers we have learned to fight.*

**Author:** Thomas Carfano
**Date:** 2026-05-21
**Status:** Working draft for the PancScan volunteer-compute project
**Scope:** Pancreatic ductal adenocarcinoma (PDAC) unless otherwise noted. PDAC is roughly 90% of all pancreatic cancers; the rest are mostly neuroendocrine tumors with very different (much better) prognosis.

---

## 1. Headline numbers

In the United States in 2026, an estimated **67,530 people** will be diagnosed with pancreatic cancer and **52,740 will die from it** — a death-to-incidence ratio of about 0.78, the worst of any common cancer. The five-year relative survival rate is **13.7%** overall and just **3.4%** once the cancer has spread to distant organs, which is how **51% of patients** first present. Pancreatic cancer is the **3rd leading cause of cancer death** in the US and is on track to be the **2nd by 2030**, ahead of breast and colorectal cancer. Globally, **510,566 new cases** and **467,005 deaths** were recorded in 2022 (the most recent GLOBOCAN year), with the burden concentrated in high-income countries but rising fastest in the developing world. The lifetime risk for an American is about **1.7%** — roughly 1 in 59 people. ([SEER](https://seer.cancer.gov/statfacts/html/pancreas.html), [GLOBOCAN 2022 / Bray et al.](https://acsjournals.onlinelibrary.wiley.com/doi/10.3322/caac.21834), [Rahib et al. 2014](https://aacrjournals.org/cancerres/article/74/11/2913/592763))

---

## 2. Incidence and mortality — trends over time

### United States

The US incidence rate is **13.9 new cases per 100,000 people per year** (2019–2023, age-adjusted). The mortality rate is **11.3 per 100,000**. Incidence is rising **0.9% per year** and has been climbing steadily since the early 2000s; mortality has been roughly flat for the last decade (a small win — survival gains are barely keeping up with rising case counts). ([SEER](https://seer.cancer.gov/statfacts/html/pancreas.html))

| Metric (US, 2026 projected) | Value |
|---|---|
| New cases | 67,530 |
| Deaths | 52,740 |
| Share of all cancer diagnoses | 3.2% |
| Share of all cancer deaths | 8.4% |
| Incidence rate (per 100k, age-adj.) | 13.9 |
| Mortality rate (per 100k, age-adj.) | 11.3 |
| Lifetime risk | ~1.7% (1 in 59) |
| Median age at diagnosis | 71 |
| Median age at death | 73 |

**Jargon note:** *Age-adjusted* means the rate is normalized to a standard age distribution so we can compare across populations of different ages. *Relative survival* compares cancer patients' survival to that of a similar uncancered population — it isolates the cancer's effect from normal mortality.

### Global

GLOBOCAN 2022 reported **510,566 new pancreatic cancer cases** worldwide (2.6% of all cancers) and **467,005 deaths** (4.8% of all cancer deaths). It ranks 12th in global incidence but **6th in cancer mortality** — because almost everyone who gets it dies. By 2021 GBD figures, that climbed to **508,532 incident cases**, **53.8% in males**. ([GLOBOCAN 2022](https://acsjournals.onlinelibrary.wiley.com/doi/10.3322/caac.21834), [GBD 2021 analysis](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2024.1521788/full))

| Region | Incidence (per 100k, age-adj.) |
|---|---|
| Global average | 4.9 |
| Northern America | 8.0 |
| Western Europe | 8.6 |
| Eastern Asia | high (China alone has more cases than US) |
| Sub-Saharan Africa | <2 |

Incidence is highest in high-income countries, but the **rate of increase** is now fastest in middle-income countries adopting Western diets, smoking, obesity, and longer life expectancies. By 2050, global pancreatic cancer cases are projected to grow substantially — one GBD-based projection estimates roughly a doubling by 2050. ([BMC Cancer GBD 2025](https://link.springer.com/article/10.1186/s12885-025-13597-z))

### The 2030 projection

The widely-cited **Rahib et al. (2014)** model projected that pancreatic cancer would surpass breast, prostate, and colorectal cancer to become the **second leading cause of cancer death in the US by 2030**, behind only lung cancer. As of 2026, that trajectory is on track. Breast and colorectal mortality have fallen due to screening and treatment advances; pancreatic mortality has not. ([Rahib et al., Cancer Research 2014](https://aacrjournals.org/cancerres/article/74/11/2913/592763), [PanCAN](https://pancan.org/press-releases/rankings-of-most-common-and-deadly-cancer-types-will-shift-over-next-two-decades/))

---

## 3. Survival statistics

### Overall and by stage

Five-year relative survival has roughly **tripled** since the 1970s — from about **0.9% in 1975 to 13.7% in 2016–2022**. That sounds like progress, but it remains the worst of any common cancer, and most of the improvement is concentrated in patients diagnosed early or who can have surgery. ([SEER](https://seer.cancer.gov/statfacts/html/pancreas.html), [Pancreas journal 2025](https://journals.lww.com/pancreasjournal/fulltext/2025/07000/factors_driving_pancreatic_cancer_survival_rates.5.aspx))

| Stage at diagnosis | % of cases | 5-year survival |
|---|---|---|
| Localized (confined to pancreas) | 15% | 43.6% |
| Regional (spread to nearby nodes/tissue) | 28% | 17.0% |
| Distant (metastatic) | 51% | 3.4% |
| Unknown / not staged | 5% | 12.5% |

The brutal arithmetic: **79% of patients are diagnosed at regional or distant stages**, where treatment is almost never curative. Among the lucky 15% diagnosed early, survival is nearly **13x higher** than among the 51% diagnosed late. Stage at diagnosis is by far the single biggest survival predictor — bigger than any drug, any surgery, any institution. ([SEER](https://seer.cancer.gov/statfacts/html/pancreas.html))

### By sex

| Sex | Incidence (per 100k) | Mortality (per 100k) |
|---|---|---|
| Male | 15.7 | ~12.8 |
| Female | 12.4 | ~10.0 |

Men are about **27% more likely** to develop pancreatic cancer than women, partly explained by higher historical smoking rates and possibly hormonal effects. The gap has been narrowing — early-onset incidence (under 55) is rising **faster in women than in men** (2.36% vs. 0.62% annual percentage change). ([SEER](https://seer.cancer.gov/statfacts/html/pancreas.html), [Lancet Gastroenterol Hepatol 2023](https://www.thelancet.com/journals/langas/article/PIIS2468-1253(23)00039-0/fulltext))

### By age

Pancreatic cancer is overwhelmingly a disease of older adults:

- **<45**: rare (<3% of cases)
- **45–54**: ~8%
- **55–64**: ~24%
- **65–74**: **32.7%** (peak)
- **75–84**: ~22%
- **85+**: ~10%

Median age at diagnosis is **71**. But — and this is one of the most concerning trends in the field — early-onset pancreatic cancer (under 50) is rising sharply (see §9). ([SEER](https://seer.cancer.gov/statfacts/html/pancreas.html))

### Historical survival trajectory (US)

| Era | 5-year survival (all stages) |
|---|---|
| 1975 | ~0.9% |
| 1990 | ~3% |
| 2004 | ~6% |
| 2011 | ~7% |
| 2015 | 12% |
| 2016–2022 | 13.7% |

The improvement is real but slow: roughly **0.3 percentage points per year**. Compare with breast cancer, which gained from ~75% to ~92% over the same period via screening + tamoxifen + HER2 inhibitors + better imaging. ([Pancreas journal 2025](https://journals.lww.com/pancreasjournal/fulltext/2025/07000/factors_driving_pancreatic_cancer_survival_rates.5.aspx), [PanCAN](https://pancan.org/news/pancreatic-cancer-five-year-survival-rate-increases-to-13/))

---

## 4. Demographic disparities

### Race and ethnicity (US, per 100k, age-adjusted)

| Group | Male incidence | Female incidence |
|---|---|---|
| Non-Hispanic Black | **18.0** | **15.4** |
| Non-Hispanic White | 15.6 | 12.2 |
| Hispanic | ~12.5 | ~11.0 |
| Non-Hispanic Asian/Pacific Islander | ~9.6 | ~8.5 |
| American Indian/Alaska Native | ~6.6 | ~6.0 |

Black Americans have a **30–70% higher pancreatic cancer incidence** than other racial groups and are diagnosed roughly **3–5 years younger** on average. They are **less likely** to be offered surgery or chemotherapy, **more likely** to live in low-resource areas, and have higher mortality rates even after adjusting for stage. ([SEER](https://seer.cancer.gov/statfacts/html/pancreas.html), [Racial disparities in PDAC treatment, PMC 11824320](https://pmc.ncbi.nlm.nih.gov/articles/PMC11824320/))

**Hypothesized drivers:**

1. **Higher prevalence of risk factors** — diabetes, obesity, smoking history, chronic pancreatitis.
2. **Reduced access to specialty care** — high-volume pancreatic surgical centers cluster in urban academic medical centers.
3. **Lower clinical trial enrollment** — under 5% of trial participants are Black.
4. **Cachexia disparities** — emerging evidence of more severe cancer-associated muscle wasting in Black patients.
5. **Possible genetic/ancestry factors** — under-studied; biology may interact with environment.

Geographic patterns reinforce these disparities: in Hawaii, **API and AIAN incidence is 13.4 and 24.5 per 100k respectively** — more than double the mainland Asian rate. Sub-population resolution matters: Japanese (8.1) and Korean (7.5) Americans have rates roughly twice South Asian (4.4) rates. Treating "Asian" or "AIAN" as monolithic groups obscures real, actionable variation. ([Pancreas journal Asian subgroups](https://pmc.ncbi.nlm.nih.gov/articles/PMC6629494/), [JCO disparities abstract](https://ascopubs.org/doi/abs/10.1200/JCO.2023.41.16_suppl.e16275))

### Sex disparity

Beyond raw incidence, treatment patterns differ: women are slightly less likely to receive aggressive surgical resection in some series, though survival outcomes after surgery are similar to men.

---

## 5. The "silent disease" problem

Pancreatic cancer's signature is its absence of signature. Most patients have no symptoms until the cancer is already advanced. There are three layered reasons for this. ([Capital Health Cancer Center](https://capitalhealthcancer.org/the-silent-risks-what-causes-pancreatic-cancer-to-go-undetected/))

### 5.1 Anatomic reasons

The pancreas is **retroperitoneal** — it sits behind the stomach, deep against the spine, surrounded by other organs (duodenum, spleen, liver, bile duct, kidneys). This means:

- It **cannot be palpated** during a routine physical exam. A breast lump or a thyroid nodule can be felt; a pancreatic mass cannot.
- A small tumor causes **no structural distortion** that anything else notices — there's no airway it obstructs, no skin it visibly changes.
- Tumors in the **body or tail** of the pancreas (about 25% of cases) are particularly silent because they don't compress the bile duct and so don't cause jaundice. By the time they cause symptoms, they often have already invaded the celiac axis or splenic vessels.
- Tumors in the **head** of the pancreas (about 60–70% of cases) may eventually compress the common bile duct and cause jaundice — but only once they're 2–3 cm or larger.

Compare with skin (visible), breast (palpable), colon (screenable via colonoscopy), cervix (screenable via Pap smear), prostate (palpable + PSA test). The pancreas has no easy access path.

### 5.2 Symptom non-specificity

When symptoms do appear, they are systemic and easily attributed to other things:

| Symptom | Why it's missed |
|---|---|
| **Vague abdominal/back pain** | Attributed to indigestion, muscle strain, GERD, or "stress" |
| **Unintentional weight loss** | Attributed to aging, diet, depression |
| **Fatigue** | Attributed to almost anything |
| **New-onset diabetes** | Attributed to lifestyle; almost never triggers cancer workup |
| **Jaundice (yellowing)** | Usually appears late; specific but often the first clue |
| **Pale stools / dark urine** | Specific but late and often unmentioned by patients |
| **Loss of appetite, nausea** | Generic GI complaints |
| **Steatorrhea (fatty stools)** | Specific to pancreatic insufficiency but rarely volunteered |

A 2025 EHR/NLP study of symptom trajectories found that the symptoms most predictive of PDAC (back pain, fatigue, GI complaints) appeared in patient records **months to over a year before diagnosis** but were almost never investigated as cancer because they look like dozens of more common conditions. Back pain had a median pre-diagnosis interval of **11.5 months**, fatigue **7.1 months**. ([EHR symptom trajectories preprint](https://www.medrxiv.org/content/10.1101/2023.02.13.23285861), [ScienceDirect 2025 NLP study](https://www.sciencedirect.com/science/article/abs/pii/S1424390325000900))

### 5.3 Diagnostic / screening reasons

There is **no population-level screening test** for pancreatic cancer. The reasons:

- **Low prevalence + invasive tests** = bad math. The standard screening modalities — endoscopic ultrasound (EUS) and MRI/MRCP — cost too much and have too many false positives to deploy to the general population. With a lifetime risk of 1.7%, you would do millions of unnecessary EUS procedures for every cancer caught.
- **CA 19-9, the standard blood biomarker**, has sensitivity 79–81% and specificity 82–90% in symptomatic patients, but its **positive predictive value as a screening test in asymptomatic people is 0.5–0.9%** — meaning more than 99% of "positive" screens would be false alarms. It is also unusable in 5–10% of the population who lack the Lewis blood-group antigen needed to express it, and it is falsely elevated in many benign conditions (cholangitis, biliary obstruction, diabetes). ([CA 19-9 review, PMC 3244191](https://pmc.ncbi.nlm.nih.gov/articles/PMC3244191/))
- **High-risk surveillance does exist** — the international **CAPS Consortium** recommends annual MRI/MRCP and EUS for people with strong family history, certain hereditary syndromes (Peutz-Jeghers, Lynch, BRCA2 carriers with affected relative, ATM, PALB2, CDKN2A) — but these eligibility criteria cover **only about 10–15% of patients who eventually develop pancreatic cancer**. The other 85% wouldn't qualify for surveillance under any current guideline. ([CAPS Consortium 2020](https://pubmed.ncbi.nlm.nih.gov/31672839/), [AGA Clinical Practice Update](https://www.gastrojournal.org/article/S0016-5085(20)30657-0/fulltext))

This is the fundamental gap: **the people who develop pancreatic cancer are mostly not the people we know to watch.**

---

## 6. New-onset diabetes as a biomarker and risk window

This is one of the most actionable findings in pancreatic cancer epidemiology of the last decade, and it's underexploited.

**The fact:** Approximately **1% of adults over 50 who develop new-onset diabetes (NOD) will be diagnosed with pancreatic cancer within 3 years.** That is roughly **6–8 times the baseline rate** for that age group. The biology: PDAC frequently causes diabetes (often called type 3c, or "pancreatogenic" diabetes) **before** it causes any other symptoms — the tumor disrupts insulin secretion, sometimes via paraneoplastic factors, often a year or more before the patient feels anything wrong. ([END-PAC model, Sharma et al. Gastroenterology 2018](https://www.gastrojournal.org/article/S0016-5085(18)34543-8/fulltext))

**The opportunity:** About **1.5 million Americans over 50 develop diabetes each year.** If we could identify the ~15,000 of them whose diabetes is a PDAC paraneoplastic syndrome and image them, we could catch a meaningful fraction of pancreatic cancers in the localized stage where 5-year survival is 44%.

**The END-PAC model** (Enriching New-Onset Diabetes for Pancreatic Cancer) stratifies NOD patients using three variables — change in weight, change in blood glucose, and age at diabetes onset. Patients with an END-PAC score ≥3 have a **3-year PDAC incidence of 3.6%** — high enough to justify imaging surveillance. Patients with score 1–2 are intermediate and would benefit from a sensitive blood biomarker (which doesn't yet exist) to triage further. ([END-PAC model, PMC 6120785](https://pmc.ncbi.nlm.nih.gov/articles/PMC6120785/), [Frontiers review 2025](https://www.frontiersin.org/journals/gastroenterology/articles/10.3389/fgstr.2025.1645459/full))

**What's missing to make this routine:**

1. A clinical workflow that flags NOD patients to a risk-stratification model automatically (an EHR integration problem, not a science problem).
2. A second-tier blood biomarker more specific than CA 19-9 for the intermediate group — an open research frontier.
3. Validated imaging protocols (likely MRI/MRCP) for the high-risk group, with cost reimbursement.

The "NOD window" is currently the **single most promising population-scale early-detection lever** in pancreatic cancer. It is screen-able, it has biological grounding, and it identifies the right people at roughly the right time.

---

## 7. Time-to-diagnosis: what we know

Studies reach different numbers depending on what interval they measure and where (different healthcare systems handle referrals differently). A rough composite:

| Interval | Typical median |
|---|---|
| First symptom → first healthcare visit (patient interval) | **21 days** (range 1–270) |
| First healthcare visit → diagnosis (diagnostic interval) | **39 days** (UK SYMPTOM study); **32 days** in some US series |
| Symptom onset → biopsy | **3.7 months** in some retrospective US series |
| Symptom onset → first oncologic consult | **3.9 months** |
| Diagnosis → treatment initiation | ~14–30 days; longer during COVID |

The UK [SYMPTOM Pancreatic Study](https://www.thelancet.com/journals/langas/article/PIIS2468-1253(16)30079-6/fulltext) (Lancet Gastroenterol Hepatol 2016) reported a total diagnostic interval median of about **60 days** from first symptom presentation, with significant tail (some patients wait > 6 months). Longer intervals correlated with vaguer symptoms (back pain, weight loss) versus jaundice (which prompted urgent imaging).

Even when symptoms do prompt evaluation, the diagnostic process is slow: **abdominal ultrasound** is often the first test ordered for vague abdominal symptoms, but ultrasound has poor sensitivity for pancreatic masses (especially in obese patients). The diagnostic gold standard, **EUS with fine-needle aspiration**, requires referral to a tertiary center and a procedure room. Many patients bounce between primary care, GI, and imaging before someone orders the right scan.

### COVID-19 impact

The pandemic worsened the time-to-diagnosis problem. During 2020:

- Stage III/IV pancreatic cancer presentations rose **14.7%** compared to 2019.
- Time from presentation to pathological diagnosis lengthened by **~14 days**.
- Median time from diagnosis to surgery extended from 112 to 140 days for COVID-tested patients.
- Many patients delayed seeking care for vague abdominal symptoms entirely.

The consequences are still propagating through 2024–2026 survival data. ([COVID PDAC cohort study, PMC 11181164](https://pmc.ncbi.nlm.nih.gov/articles/PMC11181164/))

---

## 8. Geographic and socioeconomic variation

### Within the US

Pancreatic cancer mortality is highest in a band running across the Deep South, parts of Appalachia, and into the upper Midwest. Mississippi, Louisiana, Kentucky, and West Virginia consistently rank in the highest-mortality quintile, while Utah, Colorado, and parts of the Mountain West rank lowest.

| Pattern | Finding |
|---|---|
| Urban vs. rural | Patients in completely rural areas are significantly **less likely** to be diagnosed at localized stage; **none** in some studies were diagnosed locally. They have higher mortality after adjustment. |
| Deep South cluster | Louisiana/Mississippi corridor has an identified geographic cluster of elevated incidence, partly driven by Black population concentration but persistent after adjustment. |
| Appalachia | Higher diabetes, obesity, smoking, and reduced specialty care all contribute. |
| Socioeconomic | Low-SES and rural patients have significantly elevated risk of death compared to affluent and urban patients. |

([Rural-urban PDAC stage, PubMed 32710689](https://pubmed.ncbi.nlm.nih.gov/32710689/), [Georgia county-wide analysis, PMC 4708903](https://pmc.ncbi.nlm.nih.gov/articles/PMC4708903/))

### Globally

The 5-year survival gap between high- and low-income countries is large, but not as large as for many cancers — because **no country has good outcomes**. Even Japan and the Nordic countries, with strong cancer infrastructure, report 5-year survival in the 10–15% range. This makes pancreatic cancer different from, say, breast cancer (90%+ in US/Western Europe, 30–50% in sub-Saharan Africa); for pancreatic cancer, the ceiling is low everywhere.

---

## 9. Early-onset pancreatic cancer (under 50)

A growing concern: PDAC incidence is rising faster in younger people than older people, mirroring the early-onset colorectal cancer trend that has reshaped CRC screening guidelines.

| Age group | Average annual % change (incidence) |
|---|---|
| Ages 45–49 | +0.77% |
| Ages 25–29 | **+4.34%** |
| Women 15–34 | **+6.45%** |
| Men 15–34 | +2.97% |
| Women <55 (all) | +2.36% |
| Men <55 (all) | +0.62% |

The acceleration is most striking in young women. The causes are unclear — possibilities include obesity epidemic onset, environmental exposures, alcohol consumption patterns, microbiome changes, and shifts in risk-factor distribution. Genetic syndromes account for some but not all early-onset cases. ([Lancet Gastroenterol Hepatol 2023](https://www.thelancet.com/journals/langas/article/PIIS2468-1253(23)00039-0/fulltext), [npj Precision Oncology 2025](https://www.nature.com/articles/s41698-025-01167-2))

**Counterintuitive bright spot:** despite rising early-onset incidence, age-standardized mortality from early-onset PDAC has **declined modestly** (0.75 → 0.65 per 100,000, a 13% drop from 1990 to 2021). Younger patients tolerate aggressive multi-agent chemotherapy (FOLFIRINOX) better, are more likely to be resection candidates, and have better baseline health.

Still, the trend is going the wrong direction in counts, and early-onset PDAC is often more aggressive biologically (more BRCA2, more PALB2 mutations).

---

## 10. Economic burden

### United States

- **Total direct US healthcare cost for pancreatic cancer (2020):** approximately **$29.8 billion**. ([Treatment Costs review, PMC 10047484](https://pmc.ncbi.nlm.nih.gov/articles/PMC10047484/))
- **Per-patient cost (metastatic, monthly):** $17,513 (gemcitabine alone) to **$27,889 (FOLFIRINOX)**. ([Economic burden of metastatic PDAC, PubMed 32967794](https://pubmed.ncbi.nlm.nih.gov/32967794/))
- **Per-patient lifetime treatment cost:** typically $150,000–$300,000, dominated by chemotherapy and hospitalizations in the final months.

### European/comparative data (proxy for productivity loss not separately tracked in US)

- Direct cost per patient: ~€20,000–40,000.
- **Indirect cost (lost productivity) per working-age patient: ~€154,000–328,000.**
- Indirect costs are **roughly 4–17x larger than direct costs** because patients lose years of earning, and caregivers lose work hours.

([European treatment cost review, PMC 10047484](https://pmc.ncbi.nlm.nih.gov/articles/PMC10047484/))

### The hidden burden

Pancreatic cancer's economic damage isn't well-captured by healthcare-cost numbers because:

1. **Short survival** truncates the treatment-cost meter — patients die before chronic-care costs accumulate.
2. **Caregiver burden** is severe but rarely measured.
3. **Productivity loss** is enormous because median diagnosis at 71 still includes many working/active people, and early-onset cases lose entire careers.
4. **End-of-life cost concentration** — pancreatic cancer's care costs cluster heavily in the last 6 months of life.

Total US societal burden, including productivity loss and caregiver costs, is plausibly **$50–80 billion per year**.

---

## 11. Comparison to other cancers: why has progress been so slow?

| Cancer | 1975 5-yr survival | 2025 5-yr survival | Absolute gain |
|---|---|---|---|
| Prostate | 69% | ~97% | +28 |
| Thyroid | 92% | ~98% | +6 |
| Breast (female) | 75% | ~92% | +17 |
| Melanoma | 82% | ~94% | +12 |
| Colorectal | 50% | ~65% | +15 |
| Cervical | 69% | ~67% | -2 (mostly already screened-down) |
| Lung | 12% | ~26% | +14 |
| **Pancreatic** | **~1%** | **13.7%** | **+13** |
| Liver | 3% | ~22% | +19 |

In *absolute* terms pancreatic cancer's gain is comparable to lung's. In *relative* terms it has improved more than 10x. But the starting point was so low — and the ceiling so close — that the patient experience has barely changed.

**Why so slow?**

1. **No effective screening.** Breast cancer benefited from mammography; cervical from Pap smears; colorectal from colonoscopy; prostate from PSA. Pancreatic has nothing comparable. Without screening, you can't catch early disease at scale, and almost all the survival improvement in those other cancers came from stage migration.

2. **Late presentation is intrinsic.** Even with perfect referral pathways, the tumor is silent until late by virtue of anatomy.

3. **Stromal barrier.** PDAC tumors generate a dense, fibrotic, hypovascular tumor microenvironment ("desmoplasia") that physically and chemically blocks drug delivery. About **80% of a PDAC tumor by volume is non-cancerous stroma** — collagen, immune-suppressive cells, and stiff matrix. Most chemotherapies barely reach the cancer cells. ([Pancreas journal 2025](https://journals.lww.com/pancreasjournal/fulltext/2025/07000/factors_driving_pancreatic_cancer_survival_rates.5.aspx))

4. **KRAS is the driver in ~90% of cases** — and KRAS was historically considered "undruggable." Only in the last few years (sotorasib, adagrasib, divarasib) have direct KRAS inhibitors emerged, and most target the G12C mutation that's rare in PDAC (only ~2% of cases). The dominant pancreatic KRAS mutations are G12D and G12V; G12D inhibitors are in early trials but not yet standard. ([KRAS in PDAC, PMC 12352898](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12352898/))

5. **Immunotherapy has largely failed.** Checkpoint inhibitors (pembrolizumab, nivolumab) that revolutionized melanoma and lung cancer have minimal effect in PDAC because the tumor microenvironment is profoundly immunosuppressive and PDAC has low neoantigen burden (few mutations to recognize). Only the ~1% of PDAC tumors with mismatch-repair deficiency respond well to immunotherapy.

6. **Tumor heterogeneity and rapid metastasis.** Even small PDAC tumors metastasize early — micrometastases are often present at diagnosis even when imaging looks localized.

7. **Funding and trial enrollment lag.** Pancreatic cancer receives less NCI funding per death than most major cancers, partly because the patient pool turns over quickly (few long-term survivors → fewer advocates).

---

## 12. What this means for a volunteer-compute project `[A]`

This section flags insights specifically relevant to designing PancScan.

### Big picture `[A]`

`[A]` **Pancreatic cancer is the highest-leverage cancer for any new approach that improves early detection or expands the druggable target space.** Survival gains in this disease will come from (1) catching it earlier in many more people, or (2) getting drugs through the stromal barrier and against KRAS variants we currently can't touch. Either is amenable to compute-driven research.

### Specific compute-can-help opportunities `[A]`

`[A]` **1. Early-detection biomarker discovery.** The NOD-to-PDAC window is a defined-population early-detection problem with a real prior (1% baseline). What's missing is a sensitive, specific biomarker (proteomic, metabolomic, methylation, miRNA, cfDNA) to enrich the intermediate-risk NOD population. Molecular dynamics simulations and structure-based scoring can help characterize candidate biomarker proteins; large-scale machine learning on existing proteomic datasets is a near-perfect distributed-compute task. *Volunteer compute fits because: embarrassingly parallel, no patient data leaves the central servers, only models and structures are distributed.*

`[A]` **2. KRAS-G12D and G12V drug discovery.** KRAS-G12C inhibitors hit only ~2% of PDAC. The dominant variants (G12D ~40%, G12V ~30%) are still essentially undrugged. Computational virtual screening at scale — docking billions of compounds, conformer enumeration, MD/FEP for binding-affinity refinement — is the highest-throughput approach. This is the **canonical** BOINC-compatible workflow: every workunit is a docking job. Folding@home, OpenPandemics, and Rosetta@home have all proven the model works at hit-discovery scale.

`[A]` **3. Tumor microenvironment / stromal target modeling.** PDAC desmoplasia is itself a target — break down the stroma and chemo works better. Targets include FAP, CXCR4, LOXL2, hyaluronan synthases, and various immune-modulatory pathways. Structure-based screening against these proteins is compute-friendly and underexplored.

### Where compute *won't* help much `[A]`

`[A]` Honest disclosure: compute is a *force multiplier on existing assays*, not a substitute for wet-lab biology. Volunteer compute can:
- generate hit lists for screening,
- predict structural conformations,
- run molecular dynamics on putative targets,
- explore protein-protein interfaces,
- train and score ML models on public datasets.

It cannot do animal trials, biomarker validation in patient cohorts, or clinical decision-making. The PancScan project's theory of impact should be: **feed a small number of validated hits per year to academic and biotech wet labs that would not otherwise have screened those compounds.** Even 1–2 such hits per year is a real contribution.

### Why this disease specifically `[A]`

`[A]` Several reasons pancreatic cancer is the right target for an open volunteer-compute effort:

- **Funding gap.** It is under-funded relative to its mortality. Volunteer compute is genuinely additive, not redundant with rich industry programs.
- **Open data exists.** TCGA-PAAD, ICGC PACA-AU/CA, PanCuRx, CPTAC PDAC proteomics, the HPA — all freely available.
- **No screening test = early detection is wide-open scientific territory.** Unlike breast cancer, the field has not yet picked the low-hanging fruit.
- **KRAS is having a moment.** The last 3 years have seen the first real progress on KRAS in 40 years. Compute can contribute meaningfully to expanding the chemical-space coverage of allele-specific inhibitors.
- **Personal scale matters.** Each contributing volunteer's machine is meaningfully helping a problem where every workunit increases the odds of a hit.

---

## 13. Sources

### Primary required sources

- [SEER Cancer Stat Facts: Pancreatic Cancer](https://seer.cancer.gov/statfacts/html/pancreas.html) — NCI SEER Program, accessed May 2026. Authoritative US statistics.
- [The Silent Risks: What Causes Pancreatic Cancer to Go Undetected](https://capitalhealthcancer.org/the-silent-risks-what-causes-pancreatic-cancer-to-go-undetected/) — Capital Health Cancer Center.

### Global incidence and projections

- [Bray F. et al. Global cancer statistics 2022: GLOBOCAN estimates. CA: A Cancer Journal for Clinicians, 2024.](https://acsjournals.onlinelibrary.wiley.com/doi/10.3322/caac.21834)
- [Global, regional and national burden of pancreatic cancer 2019–2021, projection to 2044. Frontiers in Oncology, 2024.](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2024.1521788/full)
- [Global burden of pancreatic cancer 1990–2021, projection to 2050. BMC Cancer, 2025.](https://link.springer.com/article/10.1186/s12885-025-13597-z)
- [Rahib L. et al. Projecting Cancer Incidence and Deaths to 2030. Cancer Research, 2014.](https://aacrjournals.org/cancerres/article/74/11/2913/592763)
- [PanCAN: Rankings of Most Common and Deadly Cancer Types Will Shift Over Next Two Decades.](https://pancan.org/press-releases/rankings-of-most-common-and-deadly-cancer-types-will-shift-over-next-two-decades/)
- [Unraveling the Burden of Pancreatic Cancer in the 21st Century. Cancers / MDPI, 2025.](https://www.mdpi.com/2072-6694/17/10/1607)
- [Global surge in pancreatic cancer cases. JOGH, 2026.](https://jogh.org/2026/jogh-16-04032)

### Survival and stage trends

- [Pancreatic Cancer Five-Year Survival Rate Increases to 13%. PanCAN, 2025.](https://pancan.org/news/pancreatic-cancer-five-year-survival-rate-increases-to-13/)
- [Factors Driving Pancreatic Cancer Survival Rates. Pancreas, July 2025.](https://journals.lww.com/pancreasjournal/fulltext/2025/07000/factors_driving_pancreatic_cancer_survival_rates.5.aspx)
- [Actual 5-year survivors of PDAC, Scientific Reports, 2020.](https://www.nature.com/articles/s41598-020-73525-y)
- [Recent estimates and predictions of 5-year survival, period analysis 2022.](https://pmc.ncbi.nlm.nih.gov/articles/PMC9773388/)

### Racial, ethnic, and geographic disparities

- [Racial disparities in treatment for pancreatic cancer. PMC, 2025.](https://pmc.ncbi.nlm.nih.gov/articles/PMC11824320/)
- [Ethnic/Racial Disparities in Pancreatic Cancer Mortality across the US. Cureus / PMC, 2024.](https://pmc.ncbi.nlm.nih.gov/articles/PMC11821361/)
- [Disparities in PDAC among Asian-Pacific Islander and AIAN populations. JCO 2023 abstract.](https://ascopubs.org/doi/abs/10.1200/JCO.2023.41.16_suppl.e16275)
- [Differences in pancreatic cancer incidence across Asian subpopulations in California. Pancreas, 2019.](https://pmc.ncbi.nlm.nih.gov/articles/PMC6629494/)
- [Rural-Urban Disparities in PDAC Stage of Diagnosis. PubMed, 2020.](https://pubmed.ncbi.nlm.nih.gov/32710689/)
- [Racial disparities of PDAC in Georgia, county-wide 2000–2011.](https://pmc.ncbi.nlm.nih.gov/articles/PMC4708903/)
- [AJMC: Disparities Drive Shifting Pancreatic Cancer Survival Trends.](https://www.ajmc.com/view/disparities-drive-shifting-pancreatic-cancer-survival-trends)

### Symptoms, time-to-diagnosis, COVID impact

- [SYMPTOM Pancreatic Study (Lancet Gastroenterol Hepatol, 2016).](https://www.thelancet.com/journals/langas/article/PIIS2468-1253(16)30079-6/fulltext)
- [PDAC symptom trajectories from Danish registry / EHR. medRxiv, 2023.](https://www.medrxiv.org/content/10.1101/2023.02.13.23285861)
- [Identifying signs and symptoms of pancreatic cancer using EHR NLP. ScienceDirect, 2025.](https://www.sciencedirect.com/science/article/abs/pii/S1424390325000900)
- [Impact of COVID-19 on Diagnosis and Treatment of PDAC. PMC, 2024.](https://pmc.ncbi.nlm.nih.gov/articles/PMC11181164/)
- [PDAC Care in the Era of COVID-19: Collateral Damage. PMC, 2022.](https://pmc.ncbi.nlm.nih.gov/articles/PMC9547483/)

### New-onset diabetes and risk stratification

- [Sharma A. et al. Model to Determine Risk of Pancreatic Cancer in Patients with New-Onset Diabetes (END-PAC). Gastroenterology, 2018.](https://www.gastrojournal.org/article/S0016-5085(18)34543-8/fulltext)
- [Risk of PDAC in glycemically defined NOD: Prospective Cohort. Gastroenterology, 2025.](https://www.gastrojournal.org/article/S0016-5085(25)05730-0/fulltext)
- [Frontiers: NOD as an emerging risk group for early detection of PDAC, 2025.](https://www.frontiersin.org/journals/gastroenterology/articles/10.3389/fgstr.2025.1645459/full)
- [Risk Factors for PDAC in NOD: Systematic Review and Meta-Analysis. PMC, 2022.](https://pmc.ncbi.nlm.nih.gov/articles/PMC9563634/)

### Early-onset PDAC

- [Cause for concern: rising incidence of early-onset pancreatic cancer. Lancet Gastroenterol Hepatol, 2023.](https://www.thelancet.com/journals/langas/article/PIIS2468-1253(23)00039-0/fulltext)
- [Growing burden of early-onset PDAC without increasing risk. npj Precision Oncology, 2025.](https://www.nature.com/articles/s41698-025-01167-2)
- [Current and Future Global Burden of Early-Onset PDAC. JCO Global Oncology, 2025.](https://ascopubs.org/doi/10.1200/GO-25-00016)
- [ASCO Post: Early-Onset Cancers on the Rise, May 2025.](https://ascopost.com/news/may-2025/early-onset-breast-colorectal-endometrial-pancreatic-and-kidney-cancers-on-the-rise/)

### Economic burden

- [Treatment Costs and Social Burden of Pancreatic Cancer. Cancers/MDPI, 2023.](https://pmc.ncbi.nlm.nih.gov/articles/PMC10047484/)
- [Economic burden of metastatic pancreatic cancer. J Med Econ, 2020.](https://pubmed.ncbi.nlm.nih.gov/32967794/)
- [Productivity Loss for Early- vs. Late-Stage Cancer. PMC, 2022.](https://pmc.ncbi.nlm.nih.gov/articles/PMC9596506/)
- [Pancreatic cancer healthcare cost and productivity loss, register-based. PubMed, 2011.](https://pubmed.ncbi.nlm.nih.gov/21850604/)

### Biology, biomarkers, screening

- [CA 19-9 as a biomarker for pancreatic cancer: comprehensive review. PMC, 2012.](https://pmc.ncbi.nlm.nih.gov/articles/PMC3244191/)
- [The Clinical Utility of CA 19-9: Diagnostic and Prognostic Updates. PMC, 2015.](https://pmc.ncbi.nlm.nih.gov/articles/PMC4419808/)
- [KRAS, TP53, CDKN2A, SMAD4, BRCA1/2 Mutations in PDAC. PMC, 2017.](https://pmc.ncbi.nlm.nih.gov/articles/PMC5447952/)
- [KRAS: the Achilles' heel of pancreas cancer biology. PMC, 2025.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12352898/)
- [Significance of TP53, CDKN2A, SMAD4, KRAS in PDAC. PMC, 2024.](https://pmc.ncbi.nlm.nih.gov/articles/PMC11049225/)
- [CAPS Consortium updated recommendations. Gut, 2020.](https://pubmed.ncbi.nlm.nih.gov/31672839/)
- [AGA Clinical Practice Update on Pancreas Cancer Screening in High-Risk Individuals. Gastroenterology, 2020.](https://www.gastrojournal.org/article/S0016-5085(20)30657-0/fulltext)
- [Ashkenazi Jewish ancestry and PDAC risk. PanCAN.](https://pancan.org/news/ashkenazi-jewish-ancestry-and-pancreatic-cancer-risk/)
- [Family history, Ashkenazi Jewish ancestry, and PDAC risk. British Journal of Cancer, 2019.](https://www.nature.com/articles/s41416-019-0426-5)
- [Age-dependent association of risk factors with PDAC. Annals of Oncology, 2022.](https://www.annalsofoncology.org/article/S0923-7534(22)00672-X/fulltext)
- [American Cancer Society: Pancreatic Cancer Risk Factors.](https://www.cancer.org/cancer/types/pancreatic-cancer/causes-risks-prevention/risk-factors.html)

### Cross-cancer comparison

- [AACR Cancer Progress Report 2025.](https://cancerprogressreport.aacr.org/progress/cpr25-contents/cpr25-cancer-in-2025/)
- [City of Hope: Signs of Progress in Pancreatic Cancer Survival.](https://www.cityofhope.org/hope-matters-blog/why-pancreatic-cancer-survival-improved)
- [Charted: Cancer survival rates reach record high. Advisory Board, January 2026.](https://www.advisory.com/daily-briefing/2026/01/21/cancer-survival)

---

*End of document. Next document in series: see 01_disease.md for biology and clinical treatment, 02_targets.md for the druggable-target landscape, 03_boinc.md for the compute architecture, and 04_proposal.md for the project's concrete plan.*
