# Full Audit Synthesis — All Verifications, All Material Errors

> **Status: Internal audit map only. Not publication-ready. Not pipeline-ready for PDB-dependent workflows until the p53 PDB column is manifest-validated.**
>
> This is the canonical verification record across our project corpus. It combines `PROJECT/23_external_research_verification.md` (external reports, audits A–C), `PROJECT/24_internal_doc_audit.md` (first internal pass, audits D–I), the extended audit pass (J–M), and the final spot-check pass (audit N). Acted on by external review `sources/external_research/Search3-audit-of-25.md` (Search3 audit, 2026-05-22 — flagged structural problems with this document; this version addresses the P0 items).

## Status legend

The reviewer correctly pointed out that "Fixed or flagged" was too binary. We now use:

| Status | Meaning | Allowed reuse |
|---|---|---|
| `Fixed in source` | The source document was edited; corrected text is recorded. | Internal + external after citation check. |
| `Flagged in source` | A visible warning sits in the source document, but underlying erroneous content may remain in tables / lists / passages. | Internal use only. **No pipeline use.** |
| `Logged only` | Issue known but not yet visible in the affected source document. | **Do not cite or reuse until fixed or flagged.** |
| `Needs re-verification` | The claim depends on volatile or high-risk facts (FDA approvals, software versions, dataset sizes, corporate status). | No external use until rechecked. |
| `Quarantined` | Known-bad or high-risk structured data has been removed from normal workflow paths. | No reuse except for audit/debugging. |
| `Resolved` | Fixed, source-linked, reviewed, and regression-protected. | Reuse allowed per confidence class. |

---

## Headline numbers

**~760 distinct factual claims audited across ~10,000 lines of source content** spanning 9 deep-dive docs + 5 synthesis/technical docs + 2 external research reports.

| Audit | Scope | Claims | Verified | Partial | False | Unverifiable |
|---|---|---|---|---|---|---|
| A | BOINC + tools + licenses (external reports) | 22 | 20 | 1 | 1 | 0 |
| B | PDB + structures + KRAS biology (external reports) | 15 | 9 | 5 | 1 | 0 |
| C | Datasets + benchmarks + LIT-PCBA (external reports) | 18 | 14 | 2 | 1 | 1 |
| D | `30_kras_structural_biology.md` | 63 | 56 | 4 | 3 | 0 |
| E | `13_treatment_landscape.md` + `15_targeted_therapy.md` | 47 | 32 | 12 | 2–3 | 1 |
| F | `10_epidemiology.md` + `11_risk_factors.md` | ~75 | ~58 | ~13 | 0 | 1 |
| G | `14_immunotherapy.md` | ~29 | ~20 | ~6 | 3 | 0 |
| H | `16_research_models.md` + `17_computational_methods.md` | ~95 | ~68 | ~16 | 5 | ~6 |
| I | `12_diagnosis_staging.md` | ~90 | ~72 | ~12 | 3 | ~3 |
| J | `01_disease.md` + `02_targets.md` + `03_boinc.md` | ~85 | ~44 | ~27 | 8 | ~6 |
| K | `31_mutant_p53_structural_biology.md` (thorough) | 69 | 45 | 10 | 13 | 1 |
| L | `04_proposal.md` + `20_synthesis.md` | ~100 | ~66 | ~25 | 5 | ~4 |
| M | `21_local_test_plan.md` + `22_boinc_technical_spec.md` | 52 | 28 | 12 | 5 | 5 |
| N | Final spot-check + agent-suggested PDB-ID verification | ~25 | ~15 | ~4 | ~5 (incl. catches of my own prior over-corrections) | 1 |
| **Totals** | | **~785** | **~547 (70%)** | **~149 (19%)** | **~55 (7%)** | **~29 (4%)** |

Approximate counts (rows marked `~`) reflect the difficulty of cleanly counting independent claims in narrative text. Exact integers should be regarded as approximate to ±5.

**Material false-claim rate ≈ 7%.** The thorough sweep of `31_mutant_p53_structural_biology.md` (audit K) alone surfaced 13 wrong PDB IDs — a structural-biology hallucination pattern that the first pass had only partially caught.

---

## Tracked issues — what's still open

The reviewer's central critique: many items were "Logged" without owner, location, or closure criterion. Every issue below is now tracked.

### Quarantined — known-bad structured data, do not reuse

| ID | Issue | Source | Closure criterion |
|---|---|---|---|
| Q-01 | **PDB column in `31_mutant_p53_structural_biology.md` Sections 6 + 14** contains 13 misidentified PDB IDs (e.g., 4LO8 = botulinum neurotoxin; 7XZS = Ricin; 7Z1V = PARP15; 6FF9 = R280K apo; 5LAW, 4ZYC, 4HG7, 5VK0, 1RV1, 2J1X, 4IBT, 4MZR, 4LO9 all flagged in header but still appear in tables) | `PROJECT/31_mutant_p53_structural_biology.md` | Replace each row's PDB ID with `UNVERIFIED_PDB_ID` placeholder OR validate via `sources/verifications/structure_manifest.csv` with RCSB lookup capturing title, ligand, mutation, construct, resolution, assembly, validation date. |
| Q-02 | **8A32 referenced 10× as "rezatapopt anchor"** — actually contains ligand KVA (Joerger/SGC Y220C stabilizer), not rezatapopt. Header warning added; pipeline-readiness section says use 9BR4 instead. | `PROJECT/31_mutant_p53_structural_biology.md` | All in-table mentions of 8A32 as "rezatapopt + Y220C" replaced with KVA-as-ligand wording; verified 9BR4 used for rezatapopt self-docking. |
| Q-03 | **No verified KRAS G12D apo PDB ID exists** in our manifest. 8AZV (claimed in 21 as G12D apo) is actually KRAS + BI-2865 inhibitor complex. 4DSO has GSP/GTP-analog + benzamidine bound. 7T47 is holo MRTX-1133. 8AZY is G12D + BI-2865. Stripping ligands from holo crystals leaves cavity-conditioned receptors, NOT true apo. | `PROJECT/21_local_test_plan.md` | A G12D apo source must be selected via structure-selection SOP (most likely MD-derived apo conformers, not a holo crystal with ligand removed) before any Tier-1 docking work that requires an apo target. |

### Flagged in source — visible warning exists, may need follow-up edit

| ID | Issue | Source | Action |
|---|---|---|---|
| F-01 | PEGPH20 HALO-301 Phase 3 failed 2019 / Halozyme oncology discontinued — but `01_disease.md` §6 still implies PEGPH20 "early combination trials show improved survival" | `PROJECT/01_disease.md` §6 | Audit J flagged; need to rewrite the stromal-remodeling paragraph |
| F-02 | TP53 frequency in PDAC table | `PROJECT/01_disease.md` (already corrected to "~65–75% modern consensus") | Done; double-check no other doc still has the wrong range |
| F-03 | Cross-reference `15_targeted_therapy.md §2.5` → §2.3 | `PROJECT/20_synthesis.md` Track 4 | Header-corrected; lazy fix because section numbers may shift |
| F-04 | Wassman 2013 misattribution to Y220C cavity dynamics | `PROJECT/31_mutant_p53_structural_biology.md` §6a | Body text needs replacement beyond the header warning |

### Logged only — known issue not yet visible in source

| ID | Issue | Source | Severity |
|---|---|---|---|
| L-01 | ESPAC-5F 1-yr OS "39% vs 77%" should be 42% vs 77% (Ghaneh Lancet Gastro Hep 2023) | `PROJECT/13_treatment_landscape.md` | Minor numeric drift |
| L-02 | Familial PC SIRs (Klein 2004 outdated; JNCI 2022 update gives 3.46/5.44/10.78 — currently shows Klein 2004 "6.4×/32×") | `PROJECT/11_risk_factors.md` | Material — overstates risk |
| L-03 | GLOBOCAN 2022 PDAC counts off by ~400 (510,566/467,005 vs Bray 2024 510,992/467,409) | `PROJECT/10_epidemiology.md` | Minor numeric drift |
| L-04 | SEER M/F mortality 12.8/10.0 should be 12.9/9.9 | `PROJECT/10_epidemiology.md` | Minor numeric drift |
| L-05 | Early-onset women trend lacks NET-overdiagnosis caveat | `PROJECT/10_epidemiology.md` | Material — affects interpretation |
| L-06 | ELI-002 2P (AMPLIFY-201) vs 7P (AMPLIFY-7P) data conflated | `PROJECT/14_immunotherapy.md` | Material — trials are different |
| L-07 | "86% of target antigens" likely typo for 88% | `PROJECT/14_immunotherapy.md` | Minor numeric drift |
| L-08 | Capan-2/Capan-1/AsPC-1 CDKN2A specifics (silent splice vs duplication vs frameshift vs deletion) | `PROJECT/16_research_models.md` | Minor mechanism precision |
| L-09 | ZINC22 size: peer-reviewed source (Tingle 2023) says 37.2B 2D / 4.5B 3D; doc claims 55B | `PROJECT/17_computational_methods.md` | Material — affects budget math |
| L-10 | Vina-GPU 2.1 speedup attribution (numbers are from Vina-GPU 1.0) | `PROJECT/17_computational_methods.md` | Minor citation drift |
| L-11 | KRAS G12V frequency 29% vs 32.5% in PDAC | `PROJECT/12_diagnosis_staging.md` | Minor numeric drift |
| L-12 | Prodromal depression "up to ~50%" overstated (10–20% prodromal; higher includes post-diagnosis) | `PROJECT/12_diagnosis_staging.md` | Material — narrative implication |
| L-13 | VTE 20–30% applies to metastatic PDAC; all-comer 1-yr cumulative is ~7.4% | `PROJECT/12_diagnosis_staging.md` | Material — overstates risk |
| L-14 | Post-ERCP pancreatitis rate (3–5% is low end; current meta-analyses 4.6–6.5%) | `PROJECT/12_diagnosis_staging.md` | Minor numeric drift |
| L-15 | Staging laparoscopy yield 5–14% understated; Hashimoto meta gives 20% (14–38%) | `PROJECT/12_diagnosis_staging.md` | Material — operative decisions |
| L-16 | Enamine REAL stale at "70B" — Apr 2026 is ~94.5B | `PROJECT/02_targets.md` + others | Material — budget math affected |
| L-17 | Stromal volume "50–80%" should be "80–90% by canonical sources" | `PROJECT/01_disease.md` §4 | Material — central narrative number |
| L-18 | GPUGrid "2,000+ publications" likely overstated ~10× | `PROJECT/03_boinc.md` | Minor citation drift |

### Resolved — fixed in source

Applied across audits A–N and propagated into source docs. Full list deferred to per-audit files; key categories: PDB ID misidentifications (7JWU, 7T47, 8A32→KVA, etc.); FDA-approval indication scope (sotorasib + adagrasib NSCLC/CRC only); F@h lab attribution (Huang/UW-Madison, not Chodera/MSKCC; primary paper Qiu et al. *JACS Au* 2024); PMV "now Pfizer" fabrication retracted; "Placek" → Placido (Nature Medicine 2023); divarasib still investigational not FDA-approved; cell line corrections (Hs 766T KRAS Q61H not WT; AsPC-1 SMAD4 R100T missense not deletion; Peng 2019 cell count 57,530 not 41,986); AlphaFold3 weights Nov 2024 not Feb 2025; OpenMM has no Apple Metal backend (use OpenCL or third-party plugin); brew install --cask miniforge syntax fix; OpenFE Apple Silicon (installs natively on osx-arm64; FEP backend CUDA-only); fpocket = MIT (final-pass verification confirmed; an interim audit had incorrectly flagged it as GPL-3 and the synthesis briefly carried that error); MRTX1133 termination (registry: formulation challenges; secondary: PK); US PDAC incidence 67,530 / 3rd leading (not 64,000 / 4th); naive VS arithmetic corrected to ~14M core-hours; R175H frequency ~3% PDAC not ~10%; zenocutuzumab is NRG1-fusion HER2×HER3 bispecific not stromal/FAP.

### Needs re-verification — volatile claims with short half-life

Per reviewer P1-08, these should be re-checked before any external publication:

| Claim type | Re-verification source | Suggested interval |
|---|---|---|
| FDA approvals (sotorasib, adagrasib, zenocutuzumab, NALIRIFOX, olaparib, divarasib, etc.) | drugs@fda + FDA oncology approval announcements | Before publication; every 6 months otherwise |
| Clinical trial status (RASolute, AMPLIFY-7P, PYNNACLE, GOBLET, DESTINY-PanTumor, etc.) | ClinicalTrials.gov + recent ASCO/ESMO/AACR proceedings | Before publication; every 3 months otherwise |
| Software versions + capabilities (OpenMM, OpenFE, Vina, GNINA, Boltz, AlphaFold3) | Project GitHub releases + docs | Before installation; every 3–6 months otherwise |
| Compound library sizes (ZINC22, Enamine REAL) | Project websites + recent publications | Before commitment; every 3 months otherwise |
| Corporate status (PMV, BMS-Mirati, Revolution Medicines, etc.) | Company IR pages + SEC filings + NASDAQ/NYSE listings | Before any acquisition/sponsorship claim |
| BOINC Central admission process | Direct inquiry to BOINC Central staff | Before submission |

---

## Lower-risk claims after audit (verified 2026-05-22)

> Renamed from "safe to cite" per reviewer P0-09. These survived multiple audits and are lower-risk for citation than unaudited content — but for any external-facing publication, **re-verify against primary source within 30 days of the publication date**.

### KRAS biology + drugs
| Claim | Primary source | Verified |
|---|---|---|
| KRAS mutated in 93% of PDAC (TCGA-PAAD, 140/150 cases) | Cancer Genome Atlas Research Network, *Cancer Cell* 2017 | A,B,C,J |
| KRAS G12D in PDAC ~40% (range 35–45% across cohorts) | TCGA-PAAD + multiple cohort reviews | B,J |
| PDB 7RPZ = KRAS G12D + MRTX1133 + GDP, 1.30 Å | RCSB | B,D,N |
| PDB 6OIM = KRAS G12C + sotorasib, covalent | RCSB | B |
| PDB 6UT0 = KRAS G12C + adagrasib, covalent | RCSB | B |
| PDB 9PZY = KRAS G12C + divarasib | RCSB | D,N |
| PDB 9DMM = KRAS G12C + divarasib (Shokat lab UCSF deposition) | RCSB + N audit | N |
| MRTX1133 KD ~0.2 pM, IC50 <2 nM, 700× selectivity over WT | Wang et al. *J Med Chem* 2022 65(4):3123–3133 | C,D |
| MRTX1133 in vivo: 8/11 PDAC PDX models ≥30% regression | Hallin et al. *Nature Medicine* 2022 | B |
| MRTX1133 NCT05737706 terminated before Phase 2 — registry reason "formulation challenges"; secondary reporting cites variable/suboptimal PK | ClinicalTrials.gov NCT05737706 + FierceBiotech 2025 | B,J,N |
| Sotorasib FDA: NSCLC (May 2021) + CRC + panitumumab (Jan 2025) — **NOT PDAC** | FDA drug label | E |
| Adagrasib FDA: NSCLC (Dec 2022) + CRC + cetuximab (Jun 2024) — **NOT PDAC** | FDA drug label | E |
| Divarasib remains investigational (Phase 3 head-to-head vs sotorasib/adagrasib ongoing) | ClinicalTrials.gov | D,N |

### Treatment + trials
| Claim | Primary source | Verified |
|---|---|---|
| PRODIGE-24 mFOLFIRINOX adjuvant: DFS 21 vs 13 mo; 5-yr OS 43% vs 31% | Conroy et al. NEJM 2018 + JCO 2022 long-term | E |
| NAPOLI-3 NALIRIFOX 1L: 11.1 vs 9.2 mo OS; FDA Feb 2024 | Wainberg 2023 + FDA label | E |
| POLO olaparib for BRCA-mutated maintenance: PFS 7.4 vs 3.8 mo; FDA 2019 | Golan NEJM 2019 + FDA label | E |
| PREOPANC-2 (2025): TNT FOLFIRINOX vs neoadj gem-CRT — no OS difference | Janssen Lancet Gastro Hep 2025 | E |
| KEYNOTE-158 pembrolizumab MSI-high PDAC: 18.2% ORR | Marabelle JCO 2019 + PDAC subgroup analyses | E,G |
| **Zenocutuzumab-zbco received FDA accelerated approval Dec 4 2024** for advanced/unresectable/metastatic **NRG1 fusion-positive NSCLC OR pancreatic adenocarcinoma after prior systemic therapy**; **May 8 2026 added cholangiocarcinoma** after prior systemic therapy | FDA approval pages (Dec 2024 + May 2026) | E,N |
| GLEAM Phase 2 zolbetuximab failed OS in PDAC (Oct 2025) | Sponsor announcement + ESMO 2025 | E |

### Datasets
| Claim | Primary source | Verified |
|---|---|---|
| TCGA-PAAD: 185 cases / 12,853 files | GDC API | C |
| RCSB PDB 2025 archive: 1,583 GB / 246,905 structures | RCSB stats page | C |
| TCIA Pancreas-CT: 82 abdominal CT scans + manual segmentations | TCIA collection page | C |
| TCIA CPTAC-PDA: 155.24 GB total, 168 subjects | TCIA collection page | C |
| AlphaFold DB: >200M structures | EBI AlphaFold DB | C |
| DUD-E: 102 targets, 22,886 ligands, 50 property-matched decoys each | Mysinger *J Med Chem* 2012 | C |
| PDC (CPTAC etc.): ~29 TB managed (NOT 70 TB) | ICF client story | C |
| AACR Project GENIE BPC PANC v1.0: 1,109 PDAC patients | AACR + cBioPortal | C |

### Computational tools
| Claim | Primary source | Verified |
|---|---|---|
| Boltz-2 affinity Pearson ~0.62 vs FEP+ ~0.72 at 1000× lower cost | Boltz-2 preprint 2025 | H,N |
| OpenFE 1.7 RBFE RMSE 1.73 kcal/mol public benchmark | OpenFE ChemRxiv Dec 2025 | H |
| MolPAL active learning ~1% dock → ~90% top-hit recovery | Graff *Chemical Science* 2021 | H |
| Lyu 2019: 138M D4 + 99M AmpC docking | Lyu *Nature* 2019 | H |
| KPC mouse median survival ~5 months | Hingorani *Cancer Cell* 2005 + subsequent | H |
| PDAC PDX engraftment ~62% | NCI PDXNet + EuroPDX | H |
| AlphaFold3 weights released **November 2024** (non-commercial) | DeepMind release notes | H,N |
| AutoDock Vina = Apache 2.0 | github.com/ccsb-scripps/AutoDock-Vina LICENSE | A |
| AutoDock-GPU = GPL-2.0 + LGPL-2.1 | github.com/ccsb-scripps/AutoDock-GPU LICENSE files | A |
| GNINA = dual GPL/Apache (GPL via OpenBabel) | github.com/gnina/gnina README | A |
| P2Rank = MIT (Java 17+) | github.com/rdk/p2rank | A |
| **fpocket = MIT** (verified at https://raw.githubusercontent.com/Discngine/fpocket/master/LICENSE; an intermediate audit incorrectly flagged it as GPL-3 and a subsequent verification confirmed MIT) | Discngine/fpocket LICENSE | A,M,N |
| OpenMM = MIT + LGPL; no native Apple Metal backend | github.com/openmm/openmm + docs | M,N |
| ChEMBL = CC BY-SA 3.0 | ChEMBL interface docs | C |

### Cell lines (after audit corrections)
| Line | KRAS | Notes |
|---|---|---|
| Panc-1 | G12D | R273H |
| MIA PaCa-2 | G12C | R248W |
| BxPC-3 | **WT — the only true KRAS-WT line in the canonical panel** | Y220C |
| Capan-1 | G12V | BRCA2-deficient |
| AsPC-1 | G12D | **SMAD4 R100T missense (not deletion)** |
| Hs 766T | **Q61H homozygous** (NOT KRAS-WT — historical literature error) | per Cellosaurus CVCL_0334 |

### Vaccines + cellular therapy
| Claim | Primary source | Verified |
|---|---|---|
| Autogene cevumeran 8/16 responders + ~7.7-yr T-cell lifespan | Rojas *Nature* 2023, MSKCC 3-yr update 2025, NCT04161755 | G |
| Leidner *NEJM* 2022: mutant KRAS G12D TCR-T, 72% PR, HLA-C\*08:02 | NEJM 2022 | G |
| PT886 (spevatamig) = CLDN18.2 × CD47 bispecific (NOT an ADC; no payload) | Phanes Therapeutics + FDA Fast Track release | G |
| DESTINY-PanTumor02 PDAC cohort closed for futility (0/15 ORR) — even though tumor-agnostic T-DXd approval technically applies | ESMO 2023 + AstraZeneca update | G |
| Pelareorep Phase 3: FDA aligned on design 2025; launch H1 2026 (NOT yet enrolling); 62% ORR was n=13 evaluable in GOBLET Cohort 1 | Oncolytics Biotech IR 2025 + GOBLET ASCO 2025 | G |

### Epidemiology
| Claim | Primary source | Verified |
|---|---|---|
| US PDAC ~67,530 new cases / **3rd leading cancer death** (ACS 2026) | ACS *Cancer Facts & Figures 2026* | J |
| Rahib 2014: PC projected #2 cancer killer by 2030 | Rahib *Cancer Research* 2014 | C,F |
| 5-yr survival ~13% all stages (NCI SEER) | SEER statfacts/html/pancreas.html | F |
| NOD ≥50 → ~1% PDAC within 3 years (8× baseline) | END-PAC + multiple cohorts | F |
| Smoking PAF ~20–25%; obesity PAF ~17–28% (PDAC) | Multiple meta-analyses | F |
| USPSTF "D" against general-population PDAC screening | USPSTF current recommendation | F |
| Kyoto 2024 IPMN guidelines: cyst growth ≥2.5 mm/yr + NOD as worrisome features | Kyoto IPMN 2024 update | I |
| NCCN universal germline testing for ALL PDAC since 2019 | NCCN PDAC guidelines current version | F,I |
| CA 19-9 PPV 0.5–0.9% as a screening test | Standard literature | I |
| CancerSEEK: 72% stage I–III sensitivity at >99% specificity | Cohen *Science* 2018 | I |

### BOINC platform
| Claim | Primary source | Verified |
|---|---|---|
| BOINC Central exists; supports Docker apps + AutoDock as of March 2026 | https://boinc.berkeley.edu/central/ | A |
| 1.9 GB VirtualBox cookbook example | BOINC wiki "Deploy Linux apps using VirtualBox" | A |
| Code-signing key on offline machine = BOINC standard | BOINC Security wiki | A |
| Adaptive replication tracks (host, app_version) | Anderson 2019 + AdaptiveReplication wiki | A |
| Hundreds of jobs/sec dispatch single server | Anderson 2019 + server-perf paper | A |
| BOINC supports docker_wrapper, vboxwrapper, native, BOINC wrapper, WSL wrapper | github.com/BOINC/boinc wiki | A |
| Rosetta@home active since 2005; recently deploying RosettaVS | Baker Lab + Rosetta@home blog | A |
| **Docking@Home retired May 2014** (do not list as "existing") | University of Delaware project news | A |
| WCG/OpenPandemics motivated AutoDock-GPU v1.4–v1.5 features | WCG article + AutoDock-GPU release notes | A |
| GPUGRID active but in transition since April 2025 server migration | GPUGRID status page | A |
| LIT-PCBA 2025 audit (arXiv:2507.21404 — Huang/Knight/Naprienko, SieveStack) | arXiv | C |

---

## Lessons learned

From the first internal pass we knew:
1. **PDB IDs are highly error-prone** — verify before commissioning agents.
2. **FDA-approval claims are time-sensitive** — require explicit indication callout, not "approved" alone.
3. **Cell line mutation status is error-prone** — Cellosaurus is authoritative.
4. **Numerical specificity ≠ accuracy** — claims like "62% ORR" or "23.31 GB" should be sanity-checked.
5. **Trial-name + acronym claims are usually reliable; trial *outcomes* sometimes wrong.**

The extended audit (J–M + N) added:
6. **Lab-attribution claims for collaborative work are error-prone.** F@h KRAS work was attributed to Chodera/MSKCC instead of Huang/UW-Madison.
7. **Corporate acquisition / IPO / regulatory claims are highly error-prone.** "PMV (now Pfizer)" was wholesale fabricated.
8. **Platform / hardware compatibility claims** default to over-optimism. "OpenMM has Apple Metal backend" — does not exist. Verify against project documentation.
9. **License claims** drift across forks and versions; verify each at the project's LICENSE file in its repository. An intermediate audit can be wrong (we briefly carried fpocket = GPL-3 in this synthesis based on one audit before the final pass corrected it back to MIT).
10. **Unit errors in compute math** survive review. Always do a back-of-envelope sanity check on big numbers.
11. **(NEW from Search3 review)** **The synthesis document itself can drift.** Inconsistent claim counts (~620 vs ~760), confidence ratings that don't account for unresolved items, and "logged" treated as equivalent to "fixed" all need explicit guardrails.

---

## Confidence ratings — split into narrative and pipeline-readiness

Per reviewer P0-04, a document can be narratively correct (safe to read, cite in background) yet pipeline-unsafe (do not feed values into docking scripts, MD setups, or external claims). These are now separate.

| Doc | Narrative confidence | Pipeline-readiness | Notes |
|---|---|---|---|
| `01_disease.md` | Medium-High | Background only | TP53 freq table + PEGPH20 paragraph (F-01) outstanding |
| `02_targets.md` | High | Background only | ZINC22 + Enamine REAL sizes stale (L-16, L-09) |
| `03_boinc.md` | High | OK for partnership planning | F@h Huang attribution corrected; GPUGRID pubs count overstated |
| `04_proposal.md` | High | OK | All known errors fixed |
| `10_epidemiology.md` | High | Background only | L-03/04/05 logged |
| `11_risk_factors.md` | High | Background only | L-02 logged (familial SIRs overstated) |
| `12_diagnosis_staging.md` | High | Background only | L-11–L-15 logged |
| `13_treatment_landscape.md` | High | OK | sotorasib/adagrasib FDA scope fixed |
| `14_immunotherapy.md` | Medium-High | Background only | L-06 (ELI-002 trial conflation) outstanding |
| `15_targeted_therapy.md` | High | Background only | Collisson/Puleo fixes applied |
| `16_research_models.md` | Medium-High | OK with caveats | Major cell-line errors fixed; minor allele specifics (L-08) outstanding |
| `17_computational_methods.md` | High | OK with caveats | AlphaFold3 date fixed; L-09 + L-10 outstanding |
| `20_synthesis.md` | High | OK | Huang attribution + zenocutuzumab + R175H + VS math fixed |
| `21_local_test_plan.md` | High | **BLOCKED on PDB selection** | Q-03 (no verified G12D apo) must be resolved before Tier-1 docking |
| `22_boinc_technical_spec.md` | High | OK | fpocket license corrected to MIT |
| `30_kras_structural_biology.md` | High | OK with caveats | All verified PDB IDs (7RPZ, 6GJ7, 6OIM, 6UT0, 9PZY, 9DMM) are correct; PDB ID inventory recommended before mass-loading |
| `31_mutant_p53_structural_biology.md` | Medium | **BLOCKED on PDB column validation (Q-01)** | 13 wrong PDB IDs flagged in header but still appear in tables; PDB column must be quarantined before pipeline use |

---

## Publication gate

Per reviewer P0-10, no external-facing claim may ship unless it meets these criteria:

1. **Primary-source URL recorded** — the URL where the claim can be re-verified (FDA approval page, RCSB structure page, GitHub LICENSE, ClinicalTrials.gov, etc.).
2. **`verified_as_of` date recorded** — when the claim was last checked against the primary source.
3. **Claim owner recorded** — person responsible if the claim becomes stale.
4. **Re-verification interval** — for volatile claim categories (FDA, trial status, software versions, library sizes, corporate status), max age before re-check.

Special rules for high-risk claim categories:

| Claim category | Re-verification window before external use |
|---|---|
| PDB IDs / structure manifests | 30 days |
| FDA approvals + indications | 30 days |
| Clinical trial status + results | 90 days |
| Software versions + capabilities | 90 days |
| Tool licenses | Verify at each release; lock to a specific commit if bundling |
| Compound-library sizes | 90 days |
| Corporate status (acquisitions, IPOs) | 30 days; verify against IR page + SEC filing |
| Cell-line mutation status | Once per project; cite Cellosaurus version |
| Lab attributions / institutional affiliations | Verify against the cited paper's author affiliations |

---

## Regression-prevention files

Per reviewer P2-07, three new files in `sources/verifications/` to prevent the same errors from recurring:

- **`known_bad_claims.md`** — denylist of facts we've already proven wrong, with the correct value and source. Future content generation should check against this list before publishing.
- **`must_verify_claim_types.md`** — checklist of claim categories that require primary-source verification before publication, with example queries.
- **`structure_manifest.csv`** — SOP table for any PDB ID used in a workflow. Columns: PDB ID, RCSB title, mutation, nucleotide state, ligand identity, ligand role, organism, construct/residue range, resolution/method, biological assembly, validation date, reviewer, allowed use.

---

## Bottom line

Identified material false claims have been **fixed, flagged in affected documents, or logged for follow-up**. Items marked "Logged only" remain unresolved until the affected source file is edited or carries a visible warning. The corpus is dramatically more trustworthy than before the audit pass — but **agent-generated content still requires human verification before any external-facing use**, and **the p53 PDB column + the missing G12D apo target are operational blockers** that must be closed before Tier-1 docking work begins.

For any future doc citing a specific PDB ID, FDA approval, corporate acquisition, cell line mutation, drug clinical status, lab attribution, license, or platform compatibility claim: **verify against the primary source within the re-verification window above, before publication.**

---

## Document history

| Date | Change |
|---|---|
| 2026-05-22 (initial) | Audits A–C (external reports) + D–I (first internal pass) consolidated |
| 2026-05-22 (extended) | Audits J–M added; ~50 material errors corrected |
| 2026-05-22 (final spot-check) | Audit N: caught two of my own previous over-corrections (fpocket; OpenFE) |
| 2026-05-22 (external review) | Search3 external review identified P0 structural problems; this revision addresses headline count, logged-vs-resolved distinction, publication gate, confidence split, p53 PDB quarantine, G12D apo quarantine, fpocket/OpenFE corrections, and adds the regression-prevention file pointers |
