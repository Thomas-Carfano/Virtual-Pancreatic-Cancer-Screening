# Pancreatic Cancer Treatment Landscape (2026)

A practitioner-grade survey of how pancreatic ductal adenocarcinoma (PDAC) is treated today — what the trials actually showed, what the standards of care are right now, and where the next wave of progress is coming from. Written for the volunteer-compute project so that compute-relevant opportunities can be identified explicitly. PDAC is the dominant histology (>90% of pancreatic cancers); this document is about PDAC unless otherwise noted.

Compute-relevant items are tagged `[A]` and consolidated in section 11.

---

## 1. Treatment decision tree by stage

Pancreatic cancer is staged anatomically (resectability) and biologically (systemic vs. local). The first and most consequential decision after diagnosis is whether the primary tumor can be removed with negative margins (R0). Roughly 15–20% of patients present with clearly resectable disease, another 20–30% with borderline resectable or locally advanced (LAPC) disease where vascular involvement is the limiting factor, and 50–60% with overt metastases. The decision tree below reflects 2026 consensus across NCCN, ESMO, ASCO, and the Dutch Pancreatic Cancer Group. Note that *upfront surgery* — historically the default for resectable disease — is being progressively displaced by *neoadjuvant therapy first* even for resectable tumors, because of high R1 (margin-positive) rates and the very high early-recurrence rate after upfront resection.

```
                       Diagnosis (histology + staging CT/MRI + CA 19-9 + EUS)
                                          |
                  +-----------------------+-----------------------+
                  |                                               |
              Localized                                       Metastatic
                  |                                               |
       Vascular relationship                              Performance status?
              on CTA                                              |
                  |                              +-----------------+--------+
   +---------+----+----+-----+                   ECOG 0-1                ECOG 2+
   |         |        |     |                       |                       |
 Resect.  Borderl.  LAPC  Vasc.                   1L:                   1L: gem
          (BR)       (no  unfit                NALIRIFOX                or supportive
            |        rsx)                      / FOLFIRINOX                 |
            |          |                       / gem-nab                    |
            |          |                          |                         |
            |          |                       Maint?: 5-FU/LV,             |
            |          |                       gem; olaparib if BRCA        |
            |          |                          |                         |
            v          v                          v                         v
   Neoadj FOLFIRINOX  Induction FOLFIRINOX     2L: NAPOLI (nal-IRI/         Hospice / palliative
   x 6-8 cycles       x 4-6 mo +/- SBRT        5-FU/LV) after gem;          chemo (capecitabine)
            |        +/- conversion surgery    gem-nab after FFX
            v                |
   Restage CT + CA19-9       v
            |              R0? -> adjuvant
   Operable?-> Surgery
   R0 -> adjuvant mFOLFIRINOX
   (or gem-cap if unfit) x 6 mo
            |
   Surveillance
   (CT q3mo x 2y, then q6mo)
```

Throughout the tree, *molecular profiling* (germline + somatic NGS, MSI, KRAS variant, BRCA, NRG1, BRAF, HER2, NTRK, RET, claudin-18.2) is recommended at diagnosis for advanced disease and at recurrence — it changes management in roughly 10–15% of patients today, and that share is growing with the KRAS G12D and pan-RAS agents.

---

## 2. Surgical management

Surgery is the only curative-intent therapy for PDAC. Roughly 20% of patients are operable at diagnosis; in modern series the operative mortality at high-volume centers is 1–3% and 90-day mortality is 5–6%. Five-year survival after R0 resection plus adjuvant chemotherapy is 25–35% — better than the 10-year average for the disease as a whole (~13%) but still poor by oncologic standards because the majority recur with distant disease.

### Procedure types

| Procedure | Indication | 30-day mortality (high-volume) | Major morbidity | Notes |
|---|---|---|---|---|
| Pancreaticoduodenectomy (Whipple) | Head, uncinate, distal CBD, ampullary | 1–3% | 30–50% | Most common PDAC operation; defines volume threshold |
| Pylorus-preserving PD (PPPD) | Same indications | Similar | Similar | Slightly faster gastric emptying recovery; oncologically equivalent |
| Distal pancreatectomy +/- splenectomy | Body/tail | 1–2% | 25–40% | Splenectomy usually included for malignancy |
| Total pancreatectomy | Multifocal IPMN, diffuse tumor, salvage | 3–5% | 50%+ | Causes brittle diabetes + complete exocrine insufficiency; reserved for clear indications |
| Distal pancreatectomy with celiac axis resection (modified Appleby / DP-CAR) | Body tumors involving celiac axis | 4–7% | up to 100% | Liver perfusion via SMA -> GDA collateral; preop coil embolization sometimes used |
| Vascular resection (PV/SMV) | Borderline resectable | similar to standard | slightly higher | Routine at high-volume centers; PV/SMV resection does not worsen oncologic outcomes if R0 achieved |
| Arterial resection (CHA, SMA) | Selected LAPC after response to neoadjuvant | 5–10% | 50–70% | Higher mortality; very selective |

### Open vs. minimally invasive

**LEOPARD** (Dutch Pancreatic Cancer Group, multicenter RCT, 102 patients) showed that minimally invasive distal pancreatectomy (MIDP — laparoscopic or robotic) shortened time to functional recovery vs. open distal pancreatectomy in an enhanced-recovery setting. Long-term follow-up showed better quality of life persisting 2 years post-op. **LAPOP** (single-center RCT) corroborated the shorter hospital stay finding for laparoscopic distal pancreatectomy.

For pancreaticoduodenectomy (Whipple), the picture is more nuanced. **LEOPARD-2** (the analogous trial for laparoscopic PD) was terminated early due to a safety signal — 90-day mortality of 10% in the laparoscopic arm vs. 2% in the open arm. The conclusion was that laparoscopic PD is not safe outside expert hands. Robotic PD, by contrast, has shown comparable mortality to open in high-volume programs, with lower blood loss and shorter LOS; 30-day mortality of ~2.8% and 90-day mortality of ~5.7% have been reported in large series. The learning curve is steep — meaningful improvement in outcomes appears after ~60 cases per surgeon.

### Volume-outcome relationship

This is one of the most robust findings in all of surgical oncology. **Centers performing <5 pancreatectomies/year have 90-day mortality 3–5x that of centers doing >20/year.** Mechanisms include better OR teams, ICU systems for managing post-op fistula and hemorrhage, and ready interventional radiology. The American College of Surgeons and others recommend regionalization for pancreatic resection.

### Quality metrics

- **R0 resection rate:** target ≥80% at high-volume centers; influenced by margin definition (1mm circumferential rule from CAP/Royal College of Pathologists raises R1 rates substantially)
- **Lymph node yield:** ≥15 nodes is the ISGPS-endorsed minimum for adequate staging after PD
- **Postoperative pancreatic fistula (POPF):** graded by ISGPS 2016 update
  - *Biochemical leak (BL, formerly grade A):* elevated drain amylase >3x serum, no clinical consequence
  - *Grade B:* requires prolonged drainage (>21 days), pharmacologic treatment (somatostatin analogs, antibiotics), percutaneous drainage, or endoscopic/angiographic intervention. Affects 10–20% of PDs.
  - *Grade C:* requires reoperation, causes organ failure, ICU admission, or death. Affects 1–3%.
- **Delayed gastric emptying (DGE):** present in 15–30% post-PD
- **Post-pancreatectomy hemorrhage (PPH):** sentinel-bleed pattern from eroded GDA stump after POPF is the classic life-threatening complication

### Survival after R0 resection

| Stage (AJCC 8th) | Median OS, R0 + modern adjuvant | 5-yr OS |
|---|---|---|
| IA (T1, N0) | ~50 mo | 35–45% |
| IB (T2, N0) | ~40 mo | 25–35% |
| IIA (T3, N0) | ~30 mo | 20–25% |
| IIB (any T, N1) | ~24 mo | 15–20% |
| III (N2 or T4) | ~18 mo | 8–12% |

---

## 3. Adjuvant therapy

Adjuvant chemotherapy after R0/R1 resection is the standard of care; without it, even after curative-intent surgery, median OS is ~17–20 months. The modern standard for fit patients is six months of mFOLFIRINOX. Less fit patients receive six months of gemcitabine + capecitabine; S-1 is the standard in Japan.

| Trial | N | Regimen vs. comparator | Median DFS | Median OS | 5-yr OS | Status |
|---|---|---|---|---|---|---|
| **CONKO-001** (2007) | 368 | Gem vs. observation | 13.4 vs 6.7 mo | 22.8 vs 20.2 mo | 20.7 vs 10.4% | Established gem as standard |
| **ESPAC-3** (2010) | 1088 | Gem vs. 5-FU/LV | 14.3 vs 14.1 mo | 23.6 vs 23.0 mo | NS | Gem and 5-FU equivalent; gem better tolerated |
| **ESPAC-4** (2017; long-term 2024) | 730 | Gem-cap vs. gem | NR | **31.6 vs 28.4 mo** (HR 0.83, p=0.031) | 28.0% vs 17.1% | Gem-cap became EU standard |
| **JASPAC-01** (2016) | 385 | S-1 vs. gem (Japan) | NR | 46.5 vs 25.5 mo (HR 0.57) | 44 vs 24% | S-1 is Japanese standard; pharmacogenomics may limit Western use |
| **PRODIGE-24 / CCTG PA.6** (2018; 5-yr 2022) | 493 | mFOLFIRINOX vs. gem | **21.6 vs 12.8 mo** (HR 0.58) | **53.5 vs 35.5 mo** (HR 0.66, p=0.003) | **43.2% vs 31.4%** | mFFX is new standard for fit patients |
| **APACT** (2023) | 866 | Gem-nab vs. gem | 16.6 vs 13.7 mo (NS by independent review) | 41.8 vs 37.7 mo (p=0.045 on sensitivity analysis) | NR | Did not change practice |

**Current standard (2026):**
- Fit (ECOG 0–1, no clinically significant comorbidity, recovered surgical course): **mFOLFIRINOX × 12 cycles (6 months)** — adopted globally based on PRODIGE-24.
- Less fit / older: **Gemcitabine + capecitabine × 6 cycles** (ESPAC-4).
- Japan: **S-1**.
- Timing: start within 12 weeks of surgery; longer delays erode benefit.
- About 40% of patients fail to receive their planned adjuvant regimen because of post-op complications or rapid recurrence — one of the central arguments for neoadjuvant first.

---

## 4. Neoadjuvant therapy

The rationale for neoadjuvant treatment: (1) PDAC is a systemic disease at diagnosis even when imaging looks localized — micrometastases drive recurrence; (2) tumor biology can be tested before committing to surgery (patients who progress on chemo are spared a non-curative operation); (3) R0 rates rise; (4) ~100% of patients receive systemic therapy, vs. ~60% in adjuvant pathways. The trade-off is that some patients with potentially resectable disease become unresectable due to progression on chemo — but in modern series this is offset by the gain in patients with occult metastatic disease who would have failed an upfront operation.

| Trial | Population | Design | Result | Verdict |
|---|---|---|---|---|
| **PREOPANC** (2020) | Resectable + BR | Neoadj gem-CRT vs. upfront surgery | OS 15.7 vs 14.3 mo (NS at first read, **HR 0.73, p=0.025 on long-term**); R0 71% vs 40% | Established neoadjuvant > upfront for BR |
| **PREOPANC-2** (2025) | Resectable + BR | Total-neoadj FOLFIRINOX × 8 vs. neoadj gem-CRT + adjuvant gem | OS no significant difference between arms | Both options remain reasonable; FFX favored by many for systemic efficacy |
| **ESPAC-5F** (2022) | BR | Upfront surgery vs. neoadj (gem-cap, FOLFIRINOX, or CRT) | 1-yr OS 39% vs 77% (neoadj) | Strong support for neoadjuvant in BR |
| **ALLIANCE A021501** (2021) | BR | mFOLFIRINOX × 7 vs. mFFX × 7 + SBRT (33–40 Gy/5fx) | 18-mo OS 66.4% (chemo alone) vs 47.3% (chemo + SBRT) | mFFX alone established as the standard for BR; SBRT after chemo did not help |
| **NEONAX** (2023) | Resectable | Neoadj gem-nab × 2 + surgery + adj gem-nab × 4 vs. all-adjuvant gem-nab × 6 | Did not meet primary endpoint of 18-mo DFS | No clear winner |
| **SWOG S1505** (2020) | Resectable | Neoadj FOLFIRINOX vs. neoadj gem-nab | Median OS 23 vs 23 mo (NS); R0 85% vs 85% | Both regimens equally effective as neoadj |

**Current trend (2026):**
- **Borderline resectable:** neoadjuvant FOLFIRINOX (× 6–8 cycles) is the standard; restaging at 3 months; surgery if no progression. SBRT is *not* added based on A021501.
- **Resectable:** Practice is moving toward neoadjuvant in many centers, especially for high-risk features (CA 19-9 >500 U/mL, large primary, suspicious nodes, weight loss). PREOPANC-2 supports either modern approach; FOLFIRINOX preferred for systemic coverage.
- **Total neoadjuvant therapy (TNT)** — all chemo before surgery, no adjuvant — is increasingly common. Approximately 30–40% of patients have a complete or near-complete pathologic response on TNT, a strong prognostic marker.

---

## 5. Locally advanced PDAC (LAPC) management

LAPC means the tumor encases or invades major arteries (SMA, celiac axis) such that R0 resection is not feasible at presentation. Roughly 30% of patients are LAPC at diagnosis. The historic median OS was 9–12 months; with modern induction chemo, it is 18–24 months, and ~20–30% convert to surgical resectability after response.

**Standard approach:**

1. **Induction chemotherapy** — FOLFIRINOX (preferred if performance status allows) or gemcitabine + nab-paclitaxel for ≥4 months.
2. **Restaging** at 3–4 months: CT pancreatic protocol + CA 19-9. If no progression, continue induction; if response, reassess for surgical conversion.
3. **Conversion surgery:** in modern series, 20–40% of LAPC patients become resectable after induction. R0 rates after response are 60–80%; median OS for converted patients reaches 30–40 months.
4. **For non-responders or those who decline surgery:** continue chemotherapy until progression or intolerance, or consider consolidative radiation.

### The chemoradiation debate

**LAP07** (2016, JAMA) randomized LAPC patients controlled after 4 months of induction gemcitabine +/- erlotinib to either continued chemo or chemoradiotherapy (54 Gy + capecitabine). No OS difference; better local control with CRT but no survival benefit. This dampened enthusiasm for CRT in LAPC.

However, dose-escalated SBRT and MR-guided SBRT have revived interest:

- **MSK / Alliance / AAPM SBRT cohorts** show 1-yr local control of 70–80% with 33–40 Gy in 5 fx, with low toxicity.
- **MASTERPLAN** (AGITG, Australasia, randomized phase II): 2:1 mFOLFIRINOX vs. mFOLFIRINOX + SBRT 40 Gy/5 fx; primary endpoint 12-mo locoregional control. Results presented in 2024–2025 are encouraging for the SBRT arm but await mature OS.
- **MASTERPLAN-2** is ongoing.
- **CONKO-007** (German cooperative group): induction chemo +/- consolidative CRT; recent reports suggest the role of CRT in LAPC remains uncertain.

**Bottom line:** systemic therapy is the foundation; radiation is a local-control adjunct best delivered as MR-guided SBRT at experienced centers, particularly when surgical conversion is not achievable. `[A]` Adaptive radiation planning is a strong compute angle.

---

## 6. Metastatic disease — line-by-line

### First line

| Regimen | Pivotal trial | Median OS | ORR | Notes |
|---|---|---|---|---|
| **FOLFIRINOX** (5-FU, LV, irinotecan, oxaliplatin) | PRODIGE 4 / ACCORD 11 (Conroy 2011) | 11.1 mo vs 6.8 mo gem | 31.6% vs 9.4% | Standard for fit ECOG 0–1 |
| **Gemcitabine + nab-paclitaxel (gem-nab)** | MPACT (Von Hoff 2013) | 8.5 mo vs 6.7 mo gem | 23% vs 7% | Standard for less-fit patients |
| **NALIRIFOX** (liposomal irinotecan, oxaliplatin, 5-FU, LV) | NAPOLI-3 (Wainberg 2023) | **11.1 mo vs 9.2 mo gem-nab** (HR 0.83, p=0.04) | 41.8% vs 36.2% | FDA-approved Feb 2024; new standard quadruplet |
| **Gemcitabine monotherapy** | Burris 1997 (vs. 5-FU) | 5.6 mo | 5% | Reserved for ECOG 2 |

NALIRIFOX is the first regimen to beat gem-nab in a phase 3 head-to-head and has emerged as a standard 1L option alongside FOLFIRINOX. There is no head-to-head between NALIRIFOX and FOLFIRINOX, but the regimens are likely similar in efficacy; choice depends on toxicity profile, infusion logistics, and prior experience.

### Maintenance after 1L response

- **PRODIGE 35 (PANOPTIMOX-1):** after 8 cycles of FOLFIRINOX, randomized maintenance with 5-FU/LV vs. continued FOLFIRINOX vs. sequential alternation. Maintenance 5-FU/LV preserves efficacy with much lower neurotoxicity.
- **POLO** (NEJM 2019): in germline BRCA1/2-mutant patients (~5–7% of PDAC) responding to ≥16 weeks of platinum-based 1L, **olaparib maintenance** doubled PFS (7.4 vs 3.8 mo, HR 0.53). Final OS analysis: median OS 19.0 vs 19.2 mo (NS), but 3-yr OS 33.9% vs 17.8% — a striking long-tail benefit. POLO led to the first targeted therapy approval in PDAC.

### Second line

After **gemcitabine-based** 1L:
- **NAPOLI-1** (Lancet 2016): nal-IRI + 5-FU/LV vs 5-FU/LV. Median OS 6.2 vs 4.2 mo (HR 0.75). Only level-1 evidence for 2L after gem failure.

After **FOLFIRINOX** 1L:
- **Gem-nab** or gem monotherapy is standard 2L based on retrospective data and consensus. No phase 3 head-to-head specifically in the 2L setting.

### Third line and beyond

No standard of care. Options include capecitabine, single-agent gem if not previously used, NTRK/RET/BRAF/HER2/MSI-targeted therapy if mutation present, clinical trial enrollment (strongly preferred), or best supportive care.

**Pan-RAS inhibitor (RMC-6236 / daraxonrasib)** — phase 1 disease control rates of 85–87% in previously treated RAS-mutant PDAC, ORR ~20–30%; phase 3 RASolute 302 (vs SOC chemo in 2L) and RASolute 303 (1L registrational) ongoing. This will likely be the next major change in the metastatic algorithm.

---

## 7. Targeted therapy

Molecular profiling has finally arrived in PDAC. Approximately 25–30% of patients have a "potentially actionable" alteration, and 10–15% have an alteration with evidence of clinical benefit. KRAS-targeted therapy is the imminent revolution; in 2026, 90%+ of PDAC patients carry a KRAS mutation, and for the first time most of them are druggable.

| Alteration | Frequency in PDAC | Drug | Trial | Response (in PDAC) | Status |
|---|---|---|---|---|---|
| **KRAS G12D** | ~40% | RMC-9805 (zoldonrasib) | RMC-9805-001 phase 1 | ORR 30%, DCR 80%; 86% of pts had >50% reduction in ctDNA | Investigational, breakthrough designation expected |
| **KRAS G12V** | ~32% | RMC-6236 (daraxonrasib, pan-RAS) | RMC-6236-001 / RASolute 302/303 | DCR 85–87%; ORR ~20–30% | Phase 3 ongoing |
| **KRAS G12R** | ~16% | RMC-6236 (pan-RAS); G12R-selective in development | Various phase 1 | Data emerging | Investigational |
| **KRAS G12C** | ~1–2% | Sotorasib | CodeBreaK 100 | ORR 21.1%, DCR 84.3%, mPFS 4.0 mo, mOS 6.9 mo | FDA-approved for PDAC (2024) |
| **KRAS G12C** | ~1–2% | Adagrasib | KRYSTAL-1 | ORR 33%, DCR ~80% | FDA-approved |
| **KRAS wild-type** | ~7–10% | Standard chemo + others | — | — | Enriched for actionable fusions |
| **BRCA1/2 germline** | 5–7% | Olaparib (maintenance after platinum) | POLO | PFS 7.4 vs 3.8 mo; 3-yr OS 33.9 vs 17.8% | FDA-approved (2019) |
| **BRCA1/2 somatic, PALB2** | 1–2% | Olaparib, rucaparib | RUCAPANC, off-label | Responses documented | Off-label / NCCN-listed |
| **NRG1 fusions** | 0.5–1% | Zenocutuzumab | eNRGy phase 2 | ORR 40% in PDAC; DOR 3.7–16.6 mo | FDA-approved Dec 2024 |
| **NTRK fusions** | <0.5% | Larotrectinib, entrectinib | NAVIGATE, STARTRK-2 | ORR 75–80% (tumor-agnostic) | FDA-approved (tumor-agnostic) |
| **MSI-H / dMMR** | ~1% | Pembrolizumab | KEYNOTE-158 | ORR 18.2% in PDAC subgroup; mDOR 13.4 mo | FDA-approved (tumor-agnostic) |
| **BRAF V600E** | ~1% | Dabrafenib + trametinib | ROAR; case series | Responses documented | FDA tumor-agnostic approval (2022) |
| **HER2 amplification / overexpression** | 2–3% | Trastuzumab deruxtecan (T-DXd) | DESTINY-PanTumor02 | ORR ~25–30% in HER2+ PDAC | FDA tumor-agnostic approval (2024) |
| **Claudin 18.2 expression** | ~25–60% (varies by cutoff) | Zolbetuximab | Phase 2 in PDAC ongoing | TBD | Investigational in PDAC; approved in gastric |
| **RET fusions** | <0.5% | Selpercatinib, pralsetinib | LIBRETTO-001 | ORR ~50% (tumor-agnostic) | FDA-approved (tumor-agnostic) |
| **ALK fusions** | <0.5% | Alectinib, lorlatinib | Case reports | Variable | Off-label |
| **FGFR2 fusions** | <1% | Pemigatinib, futibatinib | FIGHT-202 (in CCA) | Off-label in PDAC | Investigational |

KRAS G12D is the single largest unmet need — it accounts for 40% of PDAC, and the first selective inhibitors (RMC-9805, MRTX1133, HRS-4642) are showing meaningful activity. Combined with the pan-RAS inhibitor RMC-6236 and emerging G12V-selective agents, KRAS-targeted therapy will likely be applicable to ~80% of PDAC patients within 3–5 years.

---

## 8. Radiation modalities

Radiation therapy plays adjunctive roles in PDAC: local control in unresectable disease, neoadjuvant downstaging in select cases (still debated), palliation of pain and bleeding, and SBRT to oligometastatic recurrence.

| Modality | Typical dose | Use | Pros | Cons |
|---|---|---|---|---|
| **3D conformal RT** | 50.4 Gy / 28 fx with concurrent capecitabine | Historic CRT (mostly obsolete) | Simple | Large planning volumes, GI toxicity |
| **IMRT/IGRT** | 50.4–54 Gy / 28 fx | Current "standard" CRT when used | Sharper dose drop-off | Still 5–6 weeks |
| **SBRT (CT-based)** | 33–40 Gy / 5 fx | LAPC induction-followed boost; oligomets | Short course; high BED | Motion management critical; GI dose constraints tight |
| **MR-guided SBRT (MR-LINAC: Elekta Unity, ViewRay MRIdian)** | 50 Gy / 5 fx (BED10 ~100 Gy) | LAPC, BR; emerging standard at expert centers | Real-time soft tissue imaging; daily online adaptive planning; allows dose escalation | Expensive; long session times (45–75 min); limited centers |
| **Proton therapy** | 50.4 Gy(RBE) / 28 fx, or hypofractionated | Reduces dose to bowel, kidneys, marrow | Sharper Bragg peak; spares OARs | Range uncertainty in changing anatomy; few PDAC RCTs; high cost |
| **Carbon-ion therapy** | 55.2 Gy(RBE) / 12 fx | Investigational; mostly Japan/Germany | Higher RBE; better hypoxic-cell kill | Very limited availability; expensive |
| **Intraoperative RT (IORT)** | 10–20 Gy single fraction | Boost during open surgery for selected unresectable | Direct application | Few centers; mixed evidence |

The **MR-LINAC** is the most significant radiation advance for PDAC in a decade. Daily online adaptive planning lets the physicist re-plan to that day's anatomy in 30–45 minutes while the patient remains on the couch, accounting for stomach/duodenum filling, gas, and pancreatic motion. The MOMENTUM cohort reports 1-year OS of 67% in LAPC treated with Elekta Unity 5-fraction SBRT to ~50 Gy. `[A]` Daily replanning is heavily compute-bottlenecked.

---

## 9. Supportive / disease-modifying care

These are not "supportive" in the sense of comfort-only; several genuinely extend life or quality-adjusted life expectancy.

**Pancreatic enzyme replacement therapy (PERT):** Exocrine pancreatic insufficiency affects ≥80% of PDAC patients (from tumor obstruction, surgery, or both). Untreated EPI causes steatorrhea, weight loss, fat-soluble vitamin deficiency, and accelerated cachexia. A retrospective study from a single high-volume institution showed PERT was associated with significantly improved overall survival in advanced PDAC; another series showed less weight loss with PERT (−1.5 vs −2.5 kg) and improved quality of life. PERT is grossly underprescribed; the standard starting dose is 25,000–50,000 units of lipase with meals and half that with snacks, titrated to symptoms and stool quality.

**Cachexia management:** Cancer cachexia accounts for ≥20% of PDAC deaths. **Anamorelin** (a ghrelin-receptor agonist) is approved in Japan for advanced GI cancer cachexia; it improves lean body mass, appetite, and grip strength but has not shown OS benefit. Multimodal cachexia programs (nutrition, resistance exercise, anti-inflammatories) are emerging; the **MENAC trial** evaluated such a program with modest results.

**Pain management — celiac plexus block / EUS-CPN:** Pancreatic pain is the worst symptomatic burden in PDAC. **EUS-guided celiac plexus neurolysis** provides pain relief in ~60–80% of patients, reduces opioid requirements, and improves QoL. Early intervention (at diagnosis, not as salvage) appears superior. Central injection is safest. Complications (hypotension, diarrhea, rare paraplegia from anterior spinal artery injury) are uncommon.

**Biliary obstruction:** Painless jaundice is a presenting feature in ~70% of pancreatic-head tumors. **Self-expanding metal stents (SEMS)** placed via ERCP are standard for both palliation and pre-operative decompression when surgery is delayed >2 weeks. Plastic stents are reserved for short-interval expected surgery. Endoscopic ultrasound-guided choledochoduodenostomy (EUS-CDS) is an emerging alternative when ERCP fails.

**Gastric outlet obstruction (GOO):** Affects 15–25% of advanced PDAC patients. Options:
- **Endoscopic duodenal stenting** (covered SEMS): faster recovery, shorter hospital stay, good for limited life expectancy.
- **Surgical gastrojejunostomy** (open or laparoscopic): durable, better for patients with longer expected survival.
- **EUS-guided gastrojejunostomy** with a lumen-apposing metal stent (LAMS) is a newer hybrid option with promising outcomes.

**Venous thromboembolism prophylaxis:** PDAC is one of the most thrombogenic cancers — VTE risk is ~20% over the disease course. Outpatient primary prophylaxis with apixaban or rivaroxaban (per the AVERT and CASSINI trials) is increasingly common, especially during initial chemotherapy.

**Nutrition:** Pre-operative protein-calorie malnutrition is a major morbidity driver. Pre-habilitation programs (exercise + nutrition + smoking cessation × 4 weeks pre-op) improve recovery; major institutions are integrating them into the BR/resectable pathway.

---

## 10. Treatment-related morbidity

| Modality | Common toxicities | Severe toxicities (Grade ≥3) | Long-term sequelae |
|---|---|---|---|
| **Whipple / distal pancreatectomy** | POPF (10–20% grade B+), DGE (15–30%), wound infection | Grade C POPF, PPH from GDA, anastomotic dehiscence | Diabetes (10–20% new-onset after PD; >90% after total panc), exocrine insufficiency, weight loss |
| **mFOLFIRINOX** | Fatigue, diarrhea, nausea, neutropenia (chronic), neuropathy (cumulative) | Febrile neutropenia, severe diarrhea, neuropathy | Persistent peripheral neuropathy |
| **NALIRIFOX** | Similar to FOLFIRINOX; diarrhea more prominent | Diarrhea, neutropenia | Similar |
| **Gemcitabine + nab-paclitaxel** | Cytopenias, neuropathy, fatigue, alopecia | Neuropathy, neutropenia | Neuropathy |
| **Capecitabine** | Hand-foot syndrome, diarrhea | HFS, severe diarrhea | — |
| **SBRT** | Fatigue, nausea | Duodenal/bowel ulceration, GI bleed (~5–10%) | Strictures (rare) |
| **MR-LINAC SBRT** | Lower toxicity than non-adaptive SBRT — fatigue, nausea | <5% grade ≥3 GI toxicity | — |
| **Olaparib** | Fatigue, anemia, nausea | Anemia, MDS/AML (rare, <2%) | Secondary hematologic malignancy risk |
| **KRAS/RAS inhibitors** | Rash (~90%), diarrhea, nausea | Rash, hepatitis | Long-term unknown |
| **Pembrolizumab** | Fatigue, rash, endocrinopathy | Pneumonitis, colitis, hepatitis, hypophysitis | Permanent endocrinopathies (~10%) |
| **Zenocutuzumab** | Diarrhea, infusion reactions, asthenia | Cardiac dysfunction (rare; HER2-related) | — |

---

## 11. Where compute could help — `[A]` items

Treatment is where most patients spend most of their post-diagnosis lives. Concrete compute angles, ranked by tractability and impact:

1. **`[A]` KRAS variant-specific small-molecule discovery.** The KRAS G12D / G12V / G12R / Q61H pockets are now understood structurally. Volunteer compute can dock or do free-energy perturbation against curated KRAS conformations (active GTP-bound state, switch I/II open) to triage chemical libraries before wet-lab. RMC-6236 and MRTX1133 demonstrate that the problem is tractable; the variant-specific chemistry is wide open. Highest-impact target.

2. **`[A]` Adaptive radiation replanning for MR-LINAC.** Each session requires re-segmentation (deformable image registration, dose accumulation across fractions, organ-at-risk constraint solving) under time pressure. AI-segmentation models for the pancreas, duodenum, stomach, and bowel are improving but compute-hungry. A distributed training set or inference farm could meaningfully speed up adaptive workflows.

3. **`[A]` Patient-specific drug response prediction.** Multi-omic profiling (RNA, DNA, methylation, proteomics) is generating per-patient datasets that today don't drive treatment decisions. Volunteer compute could run patient-derived organoid simulations or graph-based drug-response models on a curated cohort to test predictive accuracy.

4. **`[A]` Resistance-mutation prediction for KRAS inhibitors.** Sotorasib and adagrasib resistance arises via Y96D, R68S, secondary RAS mutations, MAPK reactivation, and amplifications. Predicting resistance-mutant binding energies before they emerge clinically helps inform sequencing of agents and combination design.

5. **`[A]` Surgical-decision modeling.** Resectability assessment from imaging is observer-dependent. Volunteer-compute training of CT-segmentation models (vessel involvement, parenchymal extent) could improve regional decision-making at low-volume centers — useful in low-resource settings where high-volume referral isn't feasible.

6. **`[A]` Trial-eligibility matching at scale.** Mapping a patient's clinical + molecular features to all open trials (NCI MATCH, basket trials, KRAS-G12D trials) is currently manual. A federated compute service could solve this at population scale.

7. **`[A]` Cachexia / metabolic modeling.** Whole-body metabolic models (e.g., Recon3D, tissue-specific GEMs) are large enough that running personalized simulations to predict cachexia trajectory and response to anamorelin / nutritional intervention is compute-intensive but feasible.

8. **`[A]` Radiomics + circulating biomarkers for early recurrence detection.** Combining serial imaging features with ctDNA (KRAS variant-specific assays) to predict recurrence months earlier than standard surveillance — training and inference benefit from distributed compute.

---

## 12. Sources

**Surgery:**
- [LEOPARD trial: minimally invasive vs open distal pancreatectomy](https://pmc.ncbi.nlm.nih.gov/articles/PMC5385082/)
- [LEOPARD long-term QoL outcomes (BJS 2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9997774/)
- [LAPOP trial protocol](https://link.springer.com/article/10.1186/s13063-019-3460-y)
- [Robotic vs laparoscopic PD propensity match (2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11078803/)
- [ISGPS POPF 2016 update](https://www.surgjournal.com/article/S0039-6060(16)30757-7/fulltext)
- [Grade B POPF subclassification (2022)](https://www.sciencedirect.com/science/article/abs/pii/S0039606021008886)
- [Modified Appleby procedure / DP-CAR (AJR)](https://www.ajronline.org/doi/10.2214/AJR.18.20887)
- [DP-CAR outcomes series](https://pmc.ncbi.nlm.nih.gov/articles/PMC8041923/)
- [Pancreaticoduodenectomy StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK560747/)

**Adjuvant chemotherapy:**
- [PRODIGE-24 primary publication (NEJM 2018)](https://www.nejm.org/doi/full/10.1056/NEJMoa1809775)
- [PRODIGE-24 5-year outcomes (JAMA Oncol 2022)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9437831/)
- [ESPAC-4 primary publication (Lancet 2017)](https://www.thelancet.com/article/S0140-6736(16)32409-6/fulltext)
- [ESPAC-4 long-term outcomes (JCO 2024)](https://ascopubs.org/doi/10.1200/JCO.24.01118)
- [Long-term OS gem-cap vs gem (ASCO Post 2024)](https://ascopost.com/news/december-2024/long-term-overall-survival-with-adjuvant-gemcitabine-capecitabine-vs-gemcitabine-in-pancreatic-adenocarcinoma/)

**Neoadjuvant:**
- [PREOPANC-2 trial (Lancet Oncology 2025)](https://www.thelancet.com/journals/lanonc/article/PIIS1470-2045(25)00363-8/abstract)
- [ALLIANCE A021501 (JCO 2021)](https://ascopubs.org/doi/10.1200/JCO.2021.39.3_suppl.377)
- [A021501 RT QA analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC11329353/)
- [ALLIANCE A021501 ASCO Post](https://ascopost.com/issues/july-10-2021/modified-folfirinox-established-as-preferred-neoadjuvant-treatment-of-borderline-resectable-pancreatic-cancer/)

**Locally advanced:**
- [LAP07 trial (JAMA 2016)](https://jamanetwork.com/journals/jama/fullarticle/2518265)
- [MASTERPLAN protocol (BMC Cancer 2021)](https://link.springer.com/article/10.1186/s12885-021-08666-y)
- [Histo-molecular response after FOLFIRINOX+SBRT (BJC 2025)](https://www.nature.com/articles/s41416-025-03274-0)
- [CONKO-007 lessons learned](https://pmc.ncbi.nlm.nih.gov/articles/PMC12972021/)

**Metastatic:**
- [NAPOLI-3 primary publication (Lancet 2023)](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(23)01366-1/fulltext)
- [NAPOLI-3 updated OS (JCO 2024)](https://ascopubs.org/doi/10.1200/JCO.2024.42.16_suppl.4136)
- [NAPOLI-3 final OS / long-term survivors (JCO 2025)](https://ascopubs.org/doi/10.1200/JCO.2025.43.17_suppl.LBA4175)
- [NAPOLI-3 first-line news (ASCO Post)](https://ascopost.com/news/september-2023/first-line-nalirifox-vs-nab-paclitaxelgemcitabine-in-metastatic-pancreatic-cancer-napoli-3/)
- [NAPOLI-1 long-term survivors](https://www.ejcancer.com/article/S0959-8049(18)31553-3/fulltext)
- [POLO trial OS results (JCO 2022)](https://ascopubs.org/doi/abs/10.1200/JCO.21.01604)
- [POLO trial primary publication (NEJM)](https://www.nejm.org/doi/full/10.1056/NEJMoa1903387)

**Targeted therapy:**
- [Sotorasib in KRAS G12C PDAC (NEJM 2022)](https://www.nejm.org/doi/full/10.1056/NEJMoa2208470)
- [KRAS inhibition review (PMC 2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12842425/)
- [RMC-9805 phase 1 PDAC (JCO 2025)](https://ascopubs.org/doi/10.1200/JCO.2025.43.4_suppl.724)
- [RMC-9805 OncLive coverage](https://www.onclive.com/view/rmc-9805-triggers-tumor-regressions-in-kras-g12d-mutant-pancreatic-cancer)
- [RMC-6236 phase 1 PDAC (JCO 2025)](https://ascopubs.org/doi/10.1200/JCO.2025.43.4_suppl.722)
- [RASolute 302 trial in progress](https://ascopubs.org/doi/10.1200/JCO.2025.43.16_suppl.TPS4230)
- [Daraxonrasib in RAS+ PDAC (OncLive)](https://www.onclive.com/view/daraxonrasib-demonstrates-efficacy-potential-to-inhibit-major-ras-on-variants-in-ras-pdac)
- [Pan-RAS PDAC review](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12735763/)
- [Pembrolizumab MSI-H KEYNOTE-158 (JCO)](https://ascopubs.org/doi/10.1200/JCO.19.02105)
- [KEYNOTE-158 update (Annals of Oncology 2022)](https://www.annalsofoncology.org/article/S0923-7534(22)01720-3/fulltext)
- [Zenocutuzumab NRG1+ FDA approval (MSK)](https://www.mskcc.org/news/fda-approves-zenocutuzumab-for-pancreatic-and-lung-cancers-with-nrg1-fusions)
- [eNRGy trial (ASCO Post 2025)](https://ascopost.com/news/february-2025/enrgy-trial-zenocutuzumab-for-nrg1-gene-fusion-positive-solid-tumors/)
- [Claudin 18.2 / HER2 in pancreatic cancer (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9907975/)
- [Claudin 18.2 emerging targets review](https://www.sciencedirect.com/science/article/pii/S0304383524007572)

**Radiation:**
- [Elekta Unity for pancreatic cancer (Elekta)](https://www.elekta.com/products/radiation-therapy/unity/pancreas/)
- [Adaptive MRI-guided pancreatic SBRT (Frontiers Oncol 2024)](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2024.1441227/full)
- [MR-LINAC dosimetric comparison Unity vs MRIdian](https://pmc.ncbi.nlm.nih.gov/articles/PMC12384352/)
- [Definitive RT for LAPC review (2025)](https://www.sciencedirect.com/science/article/abs/pii/S1053429625000578)

**Supportive care:**
- [PERT improves OS in advanced PDAC (Oncologist 2025)](https://academic.oup.com/oncolo/article/30/4/oyaf014/8113510)
- [PERT in pancreatic cancer review](https://pmc.ncbi.nlm.nih.gov/articles/PMC7073203/)
- [Anamorelin weight loss in PDAC cachexia](https://pmc.ncbi.nlm.nih.gov/articles/PMC10372274/)
- [EUS-CPN meta-analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC8221153/)
- [Celiac plexus neurolysis review (2025)](https://www.tandfonline.com/doi/full/10.1080/17581869.2025.2555163)

---

*Document version 1.0 — May 2026. Maintained as part of the public Pancreatic Cancer Volunteer Compute Project. Corrections welcome.*
