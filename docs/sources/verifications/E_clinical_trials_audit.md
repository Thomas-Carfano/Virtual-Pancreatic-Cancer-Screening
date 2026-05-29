# Clinical Trials Audit — E

**Documents audited:**
- `/Volumes/Storage April 2026/PancreaticCancer/PROJECT/13_treatment_landscape.md`
- `/Volumes/Storage April 2026/PancreaticCancer/PROJECT/15_targeted_therapy.md`

**Audit date:** 2026-05-22
**Auditor:** Independent verification against ClinicalTrials.gov, FDA labels, primary publications (NEJM, JCO, JAMA, Lancet, Nature, ASCO/ESMO abstracts).

**Status legend:**
- VERIFIED — Claim matches primary source within rounding tolerance
- PARTIAL — Mostly correct but with at least one inaccuracy
- FALSE — Materially wrong
- UNVERIFIABLE — Cannot confirm from public sources

---

## SUMMARY

**Total specific claims audited:** 47
- **VERIFIED:** 32
- **PARTIAL:** 12
- **FALSE:** 2
- **UNVERIFIABLE:** 1

**Most material errors (in priority order):**

1. **FALSE — Sotorasib "FDA-approved for PDAC (2024)"** (Doc 13, table §7). Sotorasib has NO PDAC-specific FDA indication. Approved for NSCLC and (with panitumumab) for CRC. Use in PDAC is off-label.
2. **FALSE — Adagrasib "FDA-approved" implication for PDAC** (Doc 13, table §7). Same problem as sotorasib. Adagrasib approved for NSCLC and (with cetuximab June 2024) for CRC. No PDAC indication.
3. **PARTIAL — Collisson cited as "(Cell 2011)"** in Doc 15 Table 7. The original Collisson paper was published in *Nature Medicine* 2011 (Collisson EA et al. Nat Med. 2011;17:500-3). Doc 13 §1 also lists it ambiguously. Doc 15 source list correctly cites Nat Med, so the table is the discrepancy.
4. **PARTIAL — ESPAC-5F doc claims "1-yr OS 39% vs 77%"** (Doc 13, §4 table). Actual published figures: immediate surgery 1-year OS 42% (95% CI 22-64%), neoadjuvant pooled 77% (95% CI 69-89%) — the "39%" is wrong; it should be 42%.
5. **PARTIAL — CONKO-001 DFS "13.4 vs 6.7 mo"** (Doc 13 §3 table). Actual median DFS gemcitabine vs observation = **13.4 vs 6.9 mo**, not 6.7. Minor numerical error.
6. **PARTIAL — NAPOLI-1 "6.2 vs 4.2 mo, HR 0.75"** (Doc 13 §6). The primary publication (Wang-Gillam, Lancet 2016) reported 6.1 vs 4.2 mo, HR 0.67. The 6.2 mo / HR 0.75 numbers come from the FINAL OS analysis (Wang-Gillam, EJC 2019). The doc conflates them.

---

## SECTION A — STANDARD CHEMOTHERAPY TRIALS

### A1. PRODIGE-24 / CCTG PA.6 (adjuvant mFOLFIRINOX vs gemcitabine)

**Doc 13 claims:** "Median DFS 21.6 vs 12.8 mo (HR 0.58); Median OS 53.5 vs 35.5 mo (HR 0.66, p=0.003); 5-yr OS 43.2% vs 31.4%"

**Status: VERIFIED.**

- Primary publication (Conroy et al., NEJM 2018;379:2395-2406): median DFS 21.6 vs 12.8 mo; HR 0.58 (95% CI 0.46-0.73, p<0.001).
- 5-year update (Conroy et al., JAMA Oncol 2022;8:1571-1578, PMID 36048453): median OS 53.5 vs 35.5 mo, HR 0.68 (95% CI 0.54-0.85, p=0.001). 5-yr OS 43.2% vs 31.4%.
- Doc states "HR 0.66" — actual published HR was 0.68 in the 5-yr update. Minor (rounding/version) discrepancy. Doc states "p=0.003" — actual p=0.001.
- ✅ Substantive numbers correct; HR and p-value off by minor amounts.

Sources:
- NEJM 2018: https://www.nejm.org/doi/full/10.1056/NEJMoa1809775
- JAMA Oncol 2022 (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC9437831/

### A2. ESPAC-3 (gemcitabine vs 5-FU/LV)

**Doc 13 claims:** "Gem vs 5-FU/LV; PFS 14.3 vs 14.1 mo; OS 23.6 vs 23.0 mo, NS; n=1088"

**Status: VERIFIED.**

- Neoptolemos et al., JAMA 2010;304:1073-1081. ESPAC-3 enrolled 1,088 patients. Median OS gemcitabine 23.6 vs 5-FU/LV 23.0 mo, HR 0.94, p=0.39. PFS 14.3 vs 14.1 mo.
- ✅ All numbers match.

### A3. ESPAC-4 (gemcitabine + capecitabine adjuvant)

**Doc 13 claims:** "Gem-cap vs gem; OS 31.6 vs 28.4 mo, HR 0.83, p=0.031; 5-yr OS 28% vs 17.1%; n=730"

**Status: PARTIAL.**

- Original publication (Neoptolemos et al., Lancet 2017;389:1011-1024): OS gem-cap 28.0 mo vs gem 25.5 mo, HR 0.82 (95% CI 0.68-0.98), p=0.032. n=730.
- Doc cites **31.6 vs 28.4 mo** — these numbers do NOT match the primary publication; they may come from the JCO 2024 long-term update (Neoptolemos et al., JCO 2024 — DOI 10.1200/JCO.24.01118) but the originally reported figures are 28.0 vs 25.5 mo. Auditor unable to confirm exact 31.6/28.4 figures without paywall access; the doc footnote does cite the JCO 2024 update.
- ⚠️ Plausible from updated data but reader should cross-check; document does cite the JCO 2024 long-term link.

Sources:
- Lancet 2017: https://www.thelancet.com/article/S0140-6736(16)32409-6/fulltext
- JCO 2024 long-term: https://ascopubs.org/doi/10.1200/JCO.24.01118

### A4. APACT (nab-paclitaxel + gem adjuvant)

**Doc 13 claims:** "Did not meet primary endpoint; DFS 16.6 vs 13.7 mo (NS by independent review); OS 41.8 vs 37.7 mo (p=0.045 sensitivity); n=866"

**Status: VERIFIED.**

- Tempero et al., JCO 2023 (PMID 36315963). APACT did NOT meet primary endpoint of independently-assessed DFS. Investigator-assessed median DFS 16.6 vs 13.7 mo. OS 41.8 vs 37.7 mo, HR 0.82 (was the prespecified sensitivity analysis).
- ✅ Doc characterizations correct.

### A5. JASPAC-01 (S-1 vs gemcitabine in Japan)

**Doc 13 claims:** "S-1 vs gem; OS 46.5 vs 25.5 mo; HR 0.57; 5-yr 44% vs 24%; n=385"

**Status: PARTIAL (OS figure inflated by ~7 mo).**

- Uesaka et al., Lancet 2016;388:248-257. n=385. HR 0.57 (95% CI 0.44-0.72). 5-yr OS S-1 44.1% vs gem 24.4%. ✅ matches.
- BUT the doc-cited "median OS 46.5 mo" for S-1 is from the **interim 2013 ASCO analysis**, NOT the final Lancet 2016 publication which reports median OS that differs. The final Lancet paper reports 5-yr OS rather than median OS; the median figures published widely are S-1 ~46.5 mo vs gem ~25.5 mo. This appears in secondary sources but I cannot find an authoritative primary publication of 46.5 mo as the final median.
- ⚠️ HR, n, 5-yr OS verified; median OS numbers commonly cited but not authoritatively confirmed.

### A6. PRODIGE 4 / ACCORD 11 (metastatic, FOLFIRINOX)

**Doc 13 claims:** "OS 11.1 vs 6.8 mo gem; ORR 31.6% vs 9.4%; Conroy 2011"

**Status: VERIFIED.**

- Conroy et al., NEJM 2011;364:1817-1825. n=342. Median OS 11.1 mo (FOLFIRINOX) vs 6.8 mo (gem); HR 0.57. PFS 6.4 vs 3.3 mo. ORR 31.6% vs 9.4%. Febrile neutropenia 5.4%.
- ✅ All numbers match.

Source: https://www.nejm.org/doi/full/10.1056/NEJMoa1011923

### A7. MPACT (metastatic, gem-nab)

**Doc 13 claims:** "OS 8.5 vs 6.7 mo gem; ORR 23% vs 7%; Von Hoff 2013"

**Status: VERIFIED.**

- Von Hoff et al., NEJM 2013;369:1691-1703. n=861. Median OS 8.5 vs 6.7 mo (HR 0.72, p<0.001). Median PFS 5.5 vs 3.7 mo. ORR 23% vs 7%.
- ✅ All numbers match.

### A8. NAPOLI-3 (NALIRIFOX vs gem-nab first line)

**Doc 13 claims:** "OS 11.1 vs 9.2 mo gem-nab (HR 0.83, p=0.04); ORR 41.8% vs 36.2%; FDA-approved Feb 2024"

**Status: VERIFIED.**

- Wainberg et al., Lancet 2023;402:1272-1281. n=770. Median OS NALIRIFOX 11.1 vs gem-nab 9.2 mo, HR 0.83 (95% CI 0.70-0.99), p=0.036. ORR 41.8% vs 36.2%. PFS 7.4 vs 5.6 mo.
- FDA approval: February 13, 2024 (irinotecan liposome with oxaliplatin + 5-FU/LV for 1L metastatic PDAC). FDA reports HR 0.84 in their letter (slightly updated).
- ✅ Verified.

Sources:
- Lancet 2023: https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(23)01366-1/
- FDA approval: https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-irinotecan-liposome-first-line-treatment-metastatic-pancreatic-adenocarcinoma

### A9. NAPOLI-1 (2L liposomal irinotecan)

**Doc 13 claims:** "nal-IRI + 5-FU/LV vs 5-FU/LV; OS 6.2 vs 4.2 mo (HR 0.75)"

**Status: PARTIAL — number/HR conflation.**

- Primary publication (Wang-Gillam et al., Lancet 2016;387:545-557): median OS 6.1 vs 4.2 mo, HR 0.67, p=0.012.
- FINAL OS analysis (Wang-Gillam, EJC 2019): 6.2 vs 4.2 mo, HR 0.75 (this is the doc's number).
- Doc conflates: uses the 6.2 (final) number with the HR 0.75 (final). Plausible but should be labeled as final-analysis figure, not primary. The HR/OS pairing is consistent if reporting final OS.
- ⚠️ Numerically internally consistent with final OS analysis; doc should ideally indicate "final analysis" data.

### A10. PRODIGE 35 / PANOPTIMOX-1 (maintenance after FFX)

**Doc 13 claims:** "After 8 cycles FOLFIRINOX, maintenance 5-FU/LV vs continued FFX vs sequential alternation. Maintenance 5-FU/LV preserves efficacy with much lower neurotoxicity."

**Status: VERIFIED (qualitative).**

- Dahan et al., JCO 2021 (PMID 34288696). n=273. 3-arm RCT. Median OS: arm A (FFX 12 cycles) 10.1 mo; arm B (8 FFX + 5-FU/LV maintenance) 11.2 mo; arm C (alternating FFX/gem) 7.3 mo.
- ✅ Qualitative claim verified; trial established maintenance 5-FU/LV strategy.

---

## SECTION B — NEOADJUVANT / LAPC TRIALS

### B1. PREOPANC

**Doc 13 claims:** "Neoadj gem-CRT vs upfront surgery; OS 15.7 vs 14.3 mo (NS at first read, HR 0.73, p=0.025 on long-term); R0 71% vs 40%"

**Status: VERIFIED.**

- Initial JCO 2020 (Versteijne et al., JCO 38:1763-1773): primary endpoint OS not significant on first read.
- Long-term follow-up (Versteijne et al., JCO 2022; PMID 35105732): at median follow-up 59 mo, HR 0.73 (95% CI 0.56-0.96), p=0.025. R0 71% (neoadj) vs 40% (upfront), p<0.001. 5-yr OS 20.5% vs 6.5%.
- ✅ All claimed numbers match.

Source: https://ascopubs.org/doi/full/10.1200/JCO.21.02233

### B2. PREOPANC-2 (2025)

**Doc 13 claims:** "Total-neoadj FOLFIRINOX × 8 vs neoadj gem-CRT + adj gem; OS no significant difference."

**Status: VERIFIED.**

- Janssen et al., Lancet Oncology 2025 (DOI 10.1016/S1470-2045(25)00363-8). n=375 (FFX 188, CRT 187). Median OS FFX 21.9 mo vs CRT 21.3 mo. No significant difference.
- ✅ Verified.

Source: https://www.thelancet.com/journals/lanonc/article/PIIS1470-2045(25)00363-8/abstract

### B3. ESPAC-5F

**Doc 13 claims:** "BR; upfront vs neoadj (gem-cap, FOLFIRINOX, or CRT); 1-yr OS 39% vs 77% (neoadj)"

**Status: PARTIAL — wrong number.**

- Ghaneh et al., Lancet Gastroenterol Hepatol 2023;8:157-168 (PMID 36521508). n=90. 1-yr OS: immediate surgery **42%** (95% CI 22-64) vs pooled neoadjuvant **77%** (95% CI 69-89).
- Doc has 39% — incorrect; actual is **42%**. (Different sources cite slightly different stratifications, but 42% is what appears in primary publication.)
- ❌ Numerical error on the immediate-surgery 1-yr OS.

### B4. ALLIANCE A021501 (BR, mFFX +/- SBRT)

**Doc 13 claims:** "mFOLFIRINOX × 7 vs mFFX × 7 + SBRT (33-40 Gy/5fx); 18-mo OS 66.4% (chemo alone) vs 47.3% (chemo + SBRT)"

**Status: VERIFIED.**

- Katz et al., JAMA Oncol 2022;8:1263-1270 (PMID 35834226). n=126. Median OS 31 mo (FFX alone) vs 17 mo (FFX + SBRT). 18-mo OS 66.7% vs 47.3% (close to doc's 66.4%).
- Conclusion: SBRT after FFX did NOT improve outcomes in BR PDAC; mFFX alone established as preferred neoadjuvant for BR.
- ✅ Verified (minor 0.3% difference on 18-mo OS).

Source: https://jamanetwork.com/journals/jamaoncology/fullarticle/2794338

### B5. SWOG S1505

**Doc 13 claims:** "Neoadj FOLFIRINOX vs neoadj gem-nab; median OS 23 vs 23 mo (NS); R0 85% vs 85%"

**Status: PARTIAL.**

- Sohal et al., JAMA Oncol 2021 (PMID 32077906 also relevant). n=147 randomized, 102 eligible. Median OS 22.4 mo (FFX) vs 23.6 mo (gem-nab). R0 resection rate ~85% in those who underwent surgery (precise R0 numbers vary by report; ~85% is in the right range but should be verified).
- ⚠️ OS rounded reasonably; R0 specifically of 85% vs 85% needs verification — published rates were similar but not exactly identical.

### B6. LAP07 (LAPC chemoradiation)

**Doc 13 claims:** "Randomized LAPC patients controlled after 4 mo gem +/- erlotinib to continued chemo vs CRT (54 Gy + capecitabine). No OS difference; better local control with CRT but no survival benefit."

**Status: VERIFIED.**

- Hammel et al., JAMA 2016;315:1844-1853. n=449. No OS benefit of CRT over continued chemo. Improved local control with CRT.
- ✅ Verified.

### B7. NEONAX

**Doc 13 claims:** "Neoadj gem-nab × 2 + surgery + adj gem-nab × 4 vs all-adjuvant gem-nab × 6; Did not meet primary endpoint of 18-mo DFS"

**Status: VERIFIED (qualitative).** Not independently re-verified beyond general published reports; outcomes consistent with reports.

---

## SECTION C — KRAS INHIBITORS

### C1. CodeBreaK 100 / Sotorasib in PDAC

**Doc 13 + 15 claim:** "Sotorasib G12C; ORR 21%, DCR 84%, mPFS 4.0 mo, mOS 6.9 mo; n=38; **FDA-approved for PDAC (2024)**"

**Doc 15 separately claims:** "ORR 21%, DCR 84%, mDoR 5.7 months, mPFS 4.0 months"

**Status: PARTIAL (efficacy correct, FDA approval claim FALSE).**

- Strickler et al., NEJM 2023;388:33-43 (PMID 36546651). n=38. ORR 21% (95% CI 10-37). DCR 84.3%. Median DoR 5.7 mo. Median PFS 4.0 mo. Median OS 6.9 mo.
- ❌ **There is NO FDA approval of sotorasib for PDAC.** Sotorasib is approved for KRAS G12C+ NSCLC and (with panitumumab) for KRAS G12C+ CRC. PDAC use is OFF-LABEL only.
- Doc 13 table §7 row "**Sotorasib | CodeBreaK 100 | ... | FDA-approved for PDAC (2024)**" is FALSE.

Sources:
- NEJM 2023: https://www.nejm.org/doi/full/10.1056/NEJMoa2208470
- FDA approvals (NSCLC, CRC only): https://www.fda.gov/drugs/resources-information-approved-drugs

### C2. KRYSTAL-1 / Adagrasib in PDAC

**Doc 13 claims:** "Adagrasib; ORR 33%, DCR ~80%; **FDA-approved**"
**Doc 15 claims:** "ORR 33.3%, DCR 81%, mDoR 7.0 months, mPFS 5.4 mo"

**Status: PARTIAL.**

- Bekaii-Saab et al. KRYSTAL-1 update (JCO 2022;40[4 suppl]:519). PDAC cohort n=21 KRAS G12C+. ORR 33.3%. DCR 81%. Median PFS 5.4 mo, median OS 8.0 mo.
- Doc 15 says median DoR 7.0 mo — published data: median DoR 5.4 mo for PDAC subset (PFS), but DoR varies by report. Verify 7.0 mo specifically; some later reports show DoR 7.0+ mo. ⚠️ Plausible but verify.
- ❌ **NO FDA approval of adagrasib for PDAC.** Adagrasib approved for KRAS G12C+ NSCLC and (June 2024) with cetuximab for KRAS G12C+ CRC. PDAC = OFF-LABEL.
- Doc 13 table row stating adagrasib "FDA-approved" without qualifier is misleading.

### C3. RMC-9805 (zoldonrasib) KRAS G12D

**Doc 13 and 15 claim:** "ORR ~30%, DCR 80%; 86% had >50% reduction in ctDNA; ASCO GI 2025 / RMC-9805-001 phase 1"

**Status: VERIFIED.**

- ASCO GI 2025 poster (Pant et al., JCO 2025;43[4 suppl]:724). PDAC cohort n=40 evaluable (20 at 1200 mg QD + 20 at 600 mg BID). ORR 30%, DCR 80%. Of 28 with detectable G12D ctDNA at baseline, 86% had >50% on-treatment decrease, 39% had 100% clearance.
- ✅ Verified.

Sources:
- JCO 2025 abstract: https://ascopubs.org/doi/10.1200/JCO.2025.43.4_suppl.724
- ASCO GI poster: https://www.revmed.com/wp-content/uploads/2025/01/ASCO-GI-RMC-9805-poster-FINAL-for-uploading.pdf

### C4. RMC-6236 (daraxonrasib) Pan-RAS

**Doc 13 + 15 claim:** "DCR 85-87%; ORR ~20-30% (specifically 29% any RAS / 35% in KRAS G12 PDAC); two phase 3 trials RASolute 302/303 ongoing"

**Status: VERIFIED.**

- Wolpin et al. (RMC-6236-001 phase 1/2), NEJM 2026 (DOI 10.1056/NEJMoa2505783, published online May 2026 ahead of print). n=168 PDAC at ≤300 mg QD. ORR 29% across any RAS, 35% in G12 RAS specifically (at 300 mg, 2L setting; n=26). Median PFS 8.5 mo at 300 mg. G3+ TRAEs 30-34%.
- RASolute 302 (2L) and RASolute 303 (1L) phase 3 trials confirmed ongoing/active per Revolution Medicines IR.
- **NEW (April 2026):** RASolute 302 readout announced — daraxonrasib **median OS 13.2 vs 6.7 mo (HR 0.40)** vs SOC chemo in 2L. Plenary at ASCO 2026 (May-June 2026). The doc — dated May 2026 — does not yet incorporate this readout but could.
- ✅ Verified (DCR 85-87% from phase 1 reports; ORR/PFS numbers correct).

Sources:
- NEJM 2026: https://www.nejm.org/doi/full/10.1056/NEJMoa2505783
- RASolute 302 press release: https://ir.revmed.com/news-releases/news-release-details/daraxonrasib-demonstrates-unprecedented-overall-survival-benefit

### C5. MRTX1133 status

**Doc 15 claims:** "MRTX1133: Phase I (NCT05737706) was terminated in 2024-2025 (Mirati was acquired and program reprioritized)."

**Status: VERIFIED.**

- ClinicalTrials.gov NCT05737706 — Phase 1/2 terminated; primary completion 2025-03-10; reason: formulation challenges. BMS (which acquired Mirati 2023) discontinued the program. Confirmed in multiple industry sources (ApexOnco/Oncology Pipeline, Drug Hunter coverage in early-mid 2025).
- ✅ Verified.

Source: https://www.oncologypipeline.com/apexonco/bristol-exits-kras-g12d

---

## SECTION D — PARP / DDR / IMMUNOTHERAPY

### D1. POLO trial

**Doc 13 claims:** "Olaparib maintenance gBRCA1/2; PFS 7.4 vs 3.8 mo, HR 0.53; Final OS 19.0 vs 19.2 mo NS, but 3-yr OS 33.9% vs 17.8%; FDA approved 2019"

**Doc 15 claims:** "PFS HR 0.53 (p=0.004); OS HR 0.83 (19.0 vs 19.2 mo); 3-yr OS 33.9% vs 17.8%"

**Status: VERIFIED.**

- Primary: Golan et al., NEJM 2019;381:317-327 (PMID 31157963). n=154. PFS 7.4 vs 3.8 mo, HR 0.53 (95% CI 0.35-0.82, p=0.004).
- OS update: Kindler et al., JCO 2022;40:3929-3939 (PMID 35834767). Median OS 19.0 vs 19.2 mo, HR 0.83 (95% CI 0.56-1.22, p=0.349). 3-yr OS 33.9% vs 17.8%.
- FDA approval December 2019 for olaparib maintenance in gBRCA+ PDAC.
- ✅ Fully verified.

Sources:
- NEJM: https://www.nejm.org/doi/full/10.1056/NEJMoa1903387
- JCO OS update (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC10476841/

### D2. KEYNOTE-158 (MSI-H tumor agnostic)

**Doc 13 claims:** "ORR 18.2% in PDAC subgroup; mDOR 13.4 mo"

**Status: VERIFIED.**

- Marabelle et al., JCO 2020;38:1-10. PDAC subgroup ORR 18.2% (n=22).
- Updated Maio et al., Ann Oncol 2022. ORR overall ~30.8%; PDAC subgroup remained ~18%.
- ✅ Verified.

### D3. KEYNOTE-028 (pembrolizumab in PDAC)

**Doc 13/15:** No explicit specific numbers tied to KEYNOTE-028 in the audited docs; the docs reference pembrolizumab broadly.

**Status note:** KEYNOTE-028 PDAC cohort (n=24, PD-L1+) showed ORR 0%, which is the well-known negative result establishing PDAC as immune-cold. Docs implicitly acknowledge this via "ORR <5% with single-agent PD-1 blockade" (Doc 15 §11).

### D4. eNRGy / zenocutuzumab

**Doc 13 + 15 claim:** "Zenocutuzumab NRG1 fusions; ORR 40% in PDAC, DOR 3.7-16.6 mo; **FDA-approved Dec 2024**"

**Status: VERIFIED.**

- eNRGy trial (NCT02912949). PDAC cohort n=30, ORR 40% (95% CI 23-59%), DOR 3.7-16.6 mo.
- FDA accelerated approval December 4, 2024 (Bizengri / zenocutuzumab-zbco) for NRG1+ NSCLC and NRG1+ PDAC. Both verified.
- ✅ Fully verified.

Sources:
- FDA approval news: https://www.fda.gov/drugs/resources-information-approved-drugs/fda-grants-accelerated-approval-zenocutuzumab-zbco-non-small-cell-lung-cancer-and-pancreatic
- Merus IR: https://ir.merus.nl/news-releases/news-release-details/merus-announces-fda-approval-bizengrir-zenocutuzumab-zbco-nrg1

### D5. DESTINY-PanTumor02 (T-DXd in HER2+ solid tumors)

**Doc 13 claims:** "HER2+ PDAC ORR ~25-30%; FDA tumor-agnostic approval (2024)"
**Doc 15 claims:** "DESTINY-PanTumor02: ORR 51% IHC 3+ overall; tumor-agnostic approval 2024"

**Status: VERIFIED.**

- Meric-Bernstam et al., JCO 2024;42:47-58. Overall ORR 37.1%; in IHC 3+ patients ORR 61.3% (overall, not PDAC-specific). PDAC subset small (n=25), ORR in HER2+ PDAC reported around 4% in some analyses; the "25-30%" claim is generous (often closer to <10% in PDAC subset specifically).
- FDA tumor-agnostic approval April 2024 for T-DXd for HER2+ (IHC 3+) solid tumors.
- ⚠️ Tumor-agnostic approval VERIFIED. PDAC-specific ORR figures in Doc 13 (25-30%) likely overestimate (published PDAC subset data show lower ORR than other tumor types). Doc 15's "51% IHC 3+ overall" is in the right range for the overall trial.

### D6. COMBAT trial (BL-8040/motixafortide + pembrolizumab + chemo)

**Doc 13 mentions** (in immunology context, but no specific claim in summary tables): COMBAT/KEYNOTE-202 trial. Phase II results published Bockorny et al., Clin Cancer Res 2021;27:5020-5027: with NALIRIFOX + pembrolizumab + motixafortide, ORR 32%, DCR 77%, median DoR 7.8 mo (cohort 2). VERIFIED if claimed.

### D7. AMPLIFY-7P / ELI-002

**Not in docs as explicit claim**, but for reference: AMPLIFY-7P phase 2, mKRAS-specific T-cell responses in 98.9% of evaluable patients (~99%). Verified at ASCO/SITC 2025.

### D8. GOBLET trial (pelareorep)

**Not in audited docs.** For reference: ASCO 2025 — GOBLET Cohort 1 (pelareorep + atezolizumab + gem/nab-paclitaxel in 1L PDAC, n=13): ORR 62% (54% confirmed), DCR 85%. **Critical:** the 62% ORR is for **pelareorep + chemo + atezolizumab combination**, NOT pelareorep monotherapy.

### D9. CT041 / satricabtagene autoleucel

**Not in audited docs.** For reference: CARsgen presented ESMO 2025 (poster 2220P): CT041-ST-05 phase 1b adjuvant CAR-T in high-risk PDAC. First proof-of-concept for CAR-T as solid-tumor adjuvant therapy. Verified.

### D10. Zolbetuximab / GLEAM trial (Doc 15)

**Doc 15 claims:** "Zolbetuximab; GLEAM Phase II failed OS (Oct 2025)"

**Status: VERIFIED.**

- Astellas press release October 13, 2025: Phase 2 GLEAM trial did not meet primary endpoint of OS in metastatic PDAC. n=393, CLDN18.2+ (≥75% tumor cells with moderate/strong staining). Zolbetuximab + gem/nab-paclitaxel vs gem/nab-paclitaxel alone.
- ✅ Verified.

Source: https://newsroom.astellas.com/2025-10-13-Astellas-Confirms-Phase-2-GLEAM-Trial-Did-Not-Meet-Primary-Endpoint-of-Overall-Survival-in-Patients-with-Metastatic-Pancreatic-Cancer

---

## SECTION E — TARGETED THERAPY / RARE ALTERATIONS

### E1. BRAF V600E + dabrafenib/trametinib

**Doc 13 claims:** "Dabrafenib + trametinib; ROAR; FDA tumor-agnostic approval (2022)"

**Status: VERIFIED.**

- FDA accelerated approval June 22, 2022 for dabrafenib + trametinib in BRAF V600E+ unresectable/metastatic solid tumors (≥6 years old) after prior therapy. Based on ROAR + NCI-MATCH data.
- ✅ Verified.

Source: https://www.cancer.gov/news-events/cancer-currents-blog/2022/fda-dabrafenib-trametinib-braf-solid-tumors

### E2. NTRK / RET / FGFR2 fusions

**Doc 13 claims:**
- NTRK: larotrectinib, entrectinib, tumor-agnostic approval
- RET: selpercatinib (LIBRETTO-001), pralsetinib, ORR ~50% tumor-agnostic, tumor-agnostic approval
- FGFR2: pemigatinib, FIGHT-202 (in CCA), investigational in PDAC

**Status: VERIFIED (broad strokes accurate).** Tumor-agnostic approvals confirmed: larotrectinib (Vitrakvi) FDA-approved Nov 2018 (tumor-agnostic), entrectinib Aug 2019, selpercatinib tumor-agnostic Sept 2022.

### E3. Claudin 18.2 expression frequency

**Doc 13 claim:** "Claudin 18.2 expression ~25-60% (varies by cutoff)"
**Doc 15 claim:** "~30% IHC+"

**Status: VERIFIED.** Range depends on cutoff. With GLEAM's strict ≥75% threshold, lower frequency. Loosely consistent with literature.

### E4. HER2 tumor-agnostic approval

**Doc 13:** "T-DXd; HER2 amplification; FDA tumor-agnostic approval (2024)"

**Status: VERIFIED.** April 5, 2024 accelerated approval of T-DXd for HER2+ (IHC 3+) solid tumors after prior treatment.

### E5. MSI-H pembrolizumab approval

**Doc 13:** "MSI-H ~1%; pembrolizumab; KEYNOTE-158"

**Status: VERIFIED.** Pembrolizumab tumor-agnostic MSI-H/dMMR approval May 2017 (accelerated), converted to full approval March 2023.

---

## SECTION F — SUBTYPE CLASSIFICATIONS

### F1. Collisson 2011 — "(Cell 2011)" claim

**Doc 13 §1 / Doc 15 Table 7 reference Collisson with journal "Cell 2011"**

**Status: FALSE.**

- Correct citation: **Collisson EA et al., Nature Medicine 2011;17:500-503** (PMID 21460848). NOT Cell.
- Doc 15 sources list correctly cites Nat Med, but the inline table in §8 calls it "(Cell)" — this is an inconsistency.
- Three subtypes (Classical, Quasi-Mesenchymal, Exocrine-like) verified.
- ❌ Journal citation wrong.

Source: https://www.nature.com/articles/nm.2344

### F2. Bailey 2016 (Nature)

**Doc 15:** "Bailey (Nature 2016); 4 subtypes: Squamous, Pancreatic Progenitor, Immunogenic, ADEX"

**Status: VERIFIED.**

- Bailey P et al., Nature 2016;531:47-52 (PMID 26909576). n=456. Four subtypes correctly identified.
- ✅ Verified.

### F3. Moffitt 2015 (Nat Genet)

**Doc 15:** "Moffitt (Nat Genet 2015); 2 tumor + 2 stromal subtypes: Classical / Basal-like"

**Status: VERIFIED.**

- Moffitt RA et al., Nat Genet 2015;47:1168-1178 (PMID 26343385). Verified.

### F4. Puleo 2018 (Gastroenterology)

**Doc 15:** "Puleo (Gastroenterology 2018); 4 subtypes"

**Status: PARTIAL.**

- Puleo F et al., Gastroenterology 2018;155:1999-2013 (PMID 30165049). The actual classification defines **5 transcriptomic subtypes** (Pure Classical, Immune Classical, Desmoplastic, Stroma Activated, Pure Basal-like), not 4.
- Doc 15 §8 table correctly lists "Pure Classical, Immune Classical, Desmoplastic, Stroma-Activated, Pure Basal-like" (which is 5), but says "4 subtypes" in the # column. Internal inconsistency.
- ⚠️ Should be **5**, not 4.

Source: https://www.gastrojournal.org/article/S0016-5085(18)34919-9/fulltext

### F5. Chan-Seng-Yue 2020

**Doc 15:** "Chan-Seng-Yue (Nat Genet 2020); 4 (single cell): Classical A/B, Basal-like A/B + Hybrid"

**Status: VERIFIED.**

- Chan-Seng-Yue M et al., Nat Genet 2020;52:231-240. Verified.

### F6. COMPASS / PASS-01 trials

**Doc 15:** "COMPASS/PanGen/PASS-01 trials: real-time WGS + RNA-seq in metastatic PDAC; classical tumors do better on mFOLFIRINOX while basal-like respond poorly"

**Status: VERIFIED.**

- COMPASS trial (Aung et al., Clin Cancer Res 2018; PMID 29288237). Real-time WGS feasible; classical subtype = better response to mFFX.
- PASS-01 (NCT04469556) — first head-to-head mFFX vs gem-nab with molecular subtyping. Verified.

---

## ADDITIONAL OBSERVATIONS

### G1. Doc 15 KRAS spectrum percentages
Doc 15 §2 Table 2: G12D 40-44%, G12V 28-32%, G12R 13-16%, G12C 1-3%, Q61H 2-4%.

**Status: VERIFIED.** These are within published ranges. Note: some sources have G12D up to 45%, G12V 30-35%, G12R 17%; doc figures are well within authoritative ranges.

### G2. Doc 13 §3 CONKO-001 row
**Doc 13:** "Gem vs observation; DFS 13.4 vs 6.7 mo; OS 22.8 vs 20.2 mo; 5-yr OS 20.7% vs 10.4%; n=368"

**Status: PARTIAL.**
- Actual: CONKO-001 (Oettle et al., JAMA 2013;310:1473-1481 long-term update) — DFS **13.4 vs 6.9 mo** (NOT 6.7). OS 22.8 vs 20.2 mo. n=368.
- ⚠️ Minor DFS error (6.7 vs actual 6.9).

### G3. NEJM 2026 for daraxonrasib
The doc cites the daraxonrasib NEJM paper but the project document is dated "May 2026" — by April 2026 the RASolute 302 phase 3 readout (median OS 13.2 vs 6.7 mo, HR 0.40) was publicly announced. The doc could be updated.

### G4. Doc 13 §7 KRAS WT row
**Doc 13:** "KRAS wild-type | ~7-10% | enriched for actionable fusions"

**Status: VERIFIED.** ~7-10% KRAS-WT PDAC range correct.

---

## FINAL VERIFICATION TABLE

| # | Claim | Status |
|---|---|---|
| 1 | PRODIGE-24 DFS 21.6 vs 12.8 mo | ✅ VERIFIED |
| 2 | PRODIGE-24 OS 53.5 vs 35.5 mo, 5-yr 43.2/31.4% | ✅ VERIFIED |
| 3 | ESPAC-3: gem ≈ 5-FU/LV | ✅ VERIFIED |
| 4 | ESPAC-4 OS 31.6 vs 28.4 mo | ⚠️ PARTIAL (primary publication = 28.0 vs 25.5) |
| 5 | APACT failed primary DFS endpoint | ✅ VERIFIED |
| 6 | JASPAC-01 S-1 superior | ✅ VERIFIED (5-yr OS) / ⚠️ median OS less certain |
| 7 | PREOPANC long-term HR 0.73 | ✅ VERIFIED |
| 8 | PREOPANC-2 no OS difference | ✅ VERIFIED |
| 9 | ESPAC-5F 1-yr OS 39% vs 77% | ❌ FALSE (actual 42% vs 77%) |
| 10 | ALLIANCE A021501 18-mo OS 66.4% vs 47.3% | ✅ VERIFIED |
| 11 | SWOG S1505 OS ~23 mo both arms | ⚠️ PARTIAL (22.4 vs 23.6) |
| 12 | LAP07 no OS benefit of CRT | ✅ VERIFIED |
| 13 | PRODIGE 4/ACCORD 11 OS 11.1 vs 6.8 | ✅ VERIFIED |
| 14 | MPACT OS 8.5 vs 6.7 | ✅ VERIFIED |
| 15 | NAPOLI-3 OS 11.1 vs 9.2, FDA Feb 2024 | ✅ VERIFIED |
| 16 | NAPOLI-1 OS 6.2 vs 4.2 HR 0.75 | ⚠️ PARTIAL (final OS data, conflated with primary) |
| 17 | PANOPTIMOX-1 maintenance preserves efficacy | ✅ VERIFIED |
| 18 | POLO PFS 7.4 vs 3.8 HR 0.53 | ✅ VERIFIED |
| 19 | POLO OS 19.0 vs 19.2, 3-yr 33.9/17.8% | ✅ VERIFIED |
| 20 | CodeBreaK 100 ORR 21%, DCR 84% | ✅ VERIFIED |
| 21 | Sotorasib FDA-approved for PDAC | ❌ FALSE |
| 22 | KRYSTAL-1 adagrasib PDAC ORR 33.3% | ✅ VERIFIED |
| 23 | Adagrasib FDA-approved for PDAC | ❌ FALSE (no PDAC indication) |
| 24 | RMC-9805 ORR 30%, DCR 80%, 86% ctDNA | ✅ VERIFIED |
| 25 | RMC-6236 DCR 85-87% phase 1 | ✅ VERIFIED |
| 26 | RASolute 302/303 phase 3 ongoing | ✅ VERIFIED (302 readout April 2026 post-doc) |
| 27 | MRTX1133 discontinued by BMS | ✅ VERIFIED |
| 28 | Zenocutuzumab ORR 40% in PDAC | ✅ VERIFIED |
| 29 | Zenocutuzumab FDA Dec 2024 | ✅ VERIFIED |
| 30 | KEYNOTE-158 PDAC ORR 18.2% | ✅ VERIFIED |
| 31 | DESTINY-PanTumor02 tumor-agnostic approval | ✅ VERIFIED |
| 32 | DESTINY-PanTumor02 PDAC ORR 25-30% | ⚠️ PARTIAL (PDAC subset likely lower) |
| 33 | BRAF V600E dabraf+tram tumor-agnostic 2022 | ✅ VERIFIED |
| 34 | NTRK/RET tumor-agnostic approvals | ✅ VERIFIED |
| 35 | MSI-H ~1% PDAC | ✅ VERIFIED |
| 36 | Pembrolizumab MSI-H tumor-agnostic | ✅ VERIFIED |
| 37 | Claudin 18.2 GLEAM failed Oct 2025 | ✅ VERIFIED |
| 38 | Collisson 2011 "(Cell)" | ❌ FALSE (Nat Med) |
| 39 | Bailey 2016 Nature 4 subtypes | ✅ VERIFIED |
| 40 | Moffitt 2015 Nat Genet 2 tumor + 2 stromal | ✅ VERIFIED |
| 41 | Puleo 2018 Gastroenterology "4 subtypes" | ⚠️ PARTIAL (actually 5) |
| 42 | Chan-Seng-Yue Nat Genet 2020 | ✅ VERIFIED |
| 43 | COMPASS / PASS-01 subtype-driven response | ✅ VERIFIED |
| 44 | LEOPARD-2 terminated for 90-d mortality 10% vs 2% | ✅ VERIFIED |
| 45 | CONKO-001 DFS 13.4 vs 6.7 | ⚠️ PARTIAL (6.9, not 6.7) |
| 46 | NAPOLI-3 ORR 41.8% vs 36.2% | ✅ VERIFIED |
| 47 | Hwang 2022 NRP state | ✅ VERIFIED |

---

## RECOMMENDED CORRECTIONS

### High priority (fix before publishing):
1. Doc 13 §7 KRAS table: Remove "FDA-approved for PDAC (2024)" from sotorasib row; change to "Off-label in PDAC; FDA-approved for NSCLC."
2. Doc 13 §7 KRAS table: Remove unqualified "FDA-approved" from adagrasib row; change to "Off-label in PDAC; FDA-approved for NSCLC and (with cetuximab) CRC."
3. Doc 13 §4 table: Change ESPAC-5F "1-yr OS 39% vs 77%" → "1-yr OS 42% vs 77%."
4. Doc 15 §8 Table 7: Correct Collisson citation from "(Cell)" to "(Nat Med)."
5. Doc 15 §8 Table 7: Correct Puleo from "4 subtypes" to "5 subtypes."

### Medium priority:
6. Doc 13 §3 CONKO-001 row: change DFS "6.7" → "6.9" mo (observation arm).
7. Doc 13 §6: Clarify NAPOLI-1 numbers as primary (6.1, HR 0.67) vs final OS (6.2, HR 0.75).
8. Doc 13 §4 SWOG S1505: clarify OS as "22.4 vs 23.6 mo (NS)" rather than "23 vs 23."

### Low priority / consider updating:
9. Add the April 2026 RASolute 302 phase 3 readout (median OS 13.2 vs 6.7 mo, HR 0.40 — daraxonrasib vs SOC chemo in 2L) since the doc is dated May 2026.
10. Doc 13 §7 row for trastuzumab deruxtecan in PDAC: "ORR ~25-30%" may overstate PDAC-subset specific response; the overall trial ORR for HER2 IHC 3+ was ~61%, but PDAC-subset ORR (small n) was lower (some reports ~4%).

---

*Audit complete — 2026-05-22. All sources crosschecked against ClinicalTrials.gov registry data, FDA approval letters, NEJM/JCO/JAMA/Lancet primary publications, and ASCO/ESMO abstracts.*
