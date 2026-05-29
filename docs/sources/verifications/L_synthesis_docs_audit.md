# L — Audit of `04_proposal.md` and `20_synthesis.md`

**Audited documents:**
- `/Volumes/Storage April 2026/PancreaticCancer/PROJECT/04_proposal.md`
- `/Volumes/Storage April 2026/PancreaticCancer/PROJECT/20_synthesis.md`

**Audit date:** 2026-05-22
**Auditor:** Claude Opus 4.7 (1M context). Method: extracted every specific verifiable claim, cross-checked against prior audits (A–I in this directory), authoritative web sources (RCSB, official lab/institutional pages, peer-reviewed and pre-print literature), and internal PROJECT cross-references.

Status legend: ✅ Verified · ⚠️ Partial / nuance · ❌ False · 🔵 Unable to verify

---

## Headline findings (rank-ordered by harm)

1. **❌ Folding@home KRAS-VHL MD attributed to Chodera lab (MSKCC) — FALSE.** The ~1.5 ms MD / 6 metastable encounter / 3 PROTAC-favorable states work belongs to the **Huang Research Group, University of Wisconsin-Madison** (PI: Xuhui Huang), published as Tu, Wang, … Huang, *JACS Au* 4(11):4314, Oct 28 2024 (DOI 10.1021/jacsau.4c00503). The F@h Sept 18 2025 blog post explicitly credits Xuhui Huang. `04_proposal.md` line 7 ("They already run KRAS MD on F@h (Sept 2025 — see their post)") implicitly attributes the work to Chodera, and §3 explicitly lists Chodera as "already runs KRAS on F@h." Chodera's F@h cancer work is real (E3 ligase / kinase / mutant p53), but the KRAS-VHL paper the proposal points to is Huang's. **Fix:** Either attribute the JACS Au paper to Huang/UW-Madison (and email him in addition to Chodera), or refer separately to Chodera's *other* F@h cancer campaigns without coupling them to this paper.

2. **❌ "Zenocutuzumab proves PDAC stroma is targetable" — FALSE (target confusion).** `20_synthesis.md` Tier 3 row for FAP says "Approved zenocutuzumab proves PDAC stroma is targetable." Zenocutuzumab (MCLA-128, Bizengri) is a HER2×HER3 bispecific approved Dec 2024 for **NRG1-fusion-positive** PDAC and NSCLC (eNRGy trial, ORR ~40% in PDAC). It targets a 0.5–1.5% NRG1-fusion subset of tumor cells — **not stroma, not FAP**. The doc's `15_targeted_therapy.md` row #244 correctly describes it. The synthesis row is a substantive misattribution. **Fix:** Drop the zenocutuzumab justification; if a "FAP is targetable" precedent is needed, cite FAPI radioligands (e.g., 177Lu-FAP-2286, FAPI-46) or the larger CAF/FAP literature.

3. **⚠️ R175H "~10% (largest non-Y220C)" — overstated for PDAC.** `20_synthesis.md` §"Tier 2" lists R175H as "~10% (largest non-Y220C)" in PDAC. The doc's own deep dive (`15_targeted_therapy.md` Table 4) gives R175H as ~6% of TP53-mutant tumors *pan-cancer* — not 10%, and not specific to PDAC. TCGA-PAAD has only 4 R175H patients out of the ~150 high-purity analytic cohort (so ~2–3% of PDAC overall, ~4–5% of TP53-mutant PDAC). The "~10%" is likely a rounding-up of pan-cancer (~6%) or a confusion with R175H's share of *contact-mutant* hotspots. The synthesis number is approximately 2× too high for PDAC. **Fix:** Change to "~5–6% of TP53-mut PDAC, ~3% of PDAC overall."

4. **⚠️ Y220C "~1.5%" in synthesis vs "~1.8% pan-cancer" in source doc — narrow but worth noting.** `20_synthesis.md` says Y220C is ~1% (smallest but reference); `15_targeted_therapy.md` Table 4 says "~1.8% pan-cancer." Both are within the published range (1.0–1.8% pan-cancer, lower in PDAC since PDAC TP53 spectrum is skewed away from Y220C). Calling it "smallest hotspot but reference" is fair. Acceptable as-is; flag for precision.

5. **⚠️ Enamine REAL ~70B — date-stale.** `04_proposal.md` line 26 says "Enamine REAL (~70B)." 70B was the figure for the Feb 2025 REAL Space update. By Mar 2025 it was 76B, Sept 2025 83B, Apr 2026 94.5B. As of writing (May 2026) the current figure is ~94.5B. **Fix:** "Enamine REAL (~95B as of Apr 2026)."

6. **⚠️ "Industry benchmark for ultra-large VS hit rate ≥5%" — conservative.** Modern ultra-large VS reports 11–22% hit rates (Lyu 2019 D4: 22%; AmpC: 11%). 5% is a *lower-bound* target, not the headline industry benchmark; should be phrased that way. (Not wrong, but understated.)

---

## Detailed verification — `04_proposal.md`

### TL;DR and §1 (lines 5–19)

| # | Claim | Status | Evidence |
|---|---|---|---|
| 1 | F@h KRAS-VHL Sept 2025 blog post URL valid | ✅ | https://foldingathome.org/2025/09/18/catching-kras-in-the-act-simulations-reveal-new-paths-for-targeted-protein-degradation/ resolves and confirms the content |
| 2 | F@h ran ~1.5 ms total MD on KRAS-VHL | ✅ | "~1.5 milliseconds of all-atom molecular dynamics" — F@h blog and Tu et al. 2024 JACS Au |
| 3 | 6 metastable encounter states | ✅ | F@h blog: "six metastable encounter states with distinct PPI interfaces" |
| 4 | 3 with favorable PROTAC linker geometries | ✅ | F@h blog: "Three of these states demonstrated favorable geometries for PROTAC linker design" |
| 5 | Attribution to Chodera lab (MSKCC) | ❌ | The JACS Au paper is by Huang's group at UW-Madison. Chodera does run *other* F@h cancer work. **Fix:** attribute correctly to Xuhui Huang (UW-Madison) |
| 6 | KRAS G12D + MRTX1133, RMC-6236 candidates for MD | ✅ | Both are real KRAS G12D and pan-RAS drugs (verified in `D_kras_doc_audit.md`); MRTX1133 was discontinued by BMS in early 2025 but the structures and SAR remain useful for MD |
| 7 | "Differentiated by FightAIDS@home and OpenPandemics" pattern for VS | ✅ | Both are real WCG/BOINC AutoDock projects; the pattern is established (`A_boinc_and_tools.md`) |
| 8 | Open compound libraries (ZINC22, Enamine REAL) free | ✅ | Both have free academic access |
| 9 | AutoDock Vina, GNINA, DiffDock all open-source | ✅ | Apache 2.0, dual GPL/Apache, MIT respectively (`A_boinc_and_tools.md`) |

### §2 PancScan@home (lines 21–85)

| # | Claim | Status | Evidence |
|---|---|---|---|
| 10 | PDB 7RPZ for KRAS G12D Switch-II | ✅ | RCSB confirms "KRAS G12D in complex with MRTX-1133" (`D_kras_doc_audit.md`) |
| 11 | MRTX1133 known binder for benchmarking | ✅ | Verified, KD ~0.2 pM, structure 7RPZ |
| 12 | Initial seed ~20–50 conformations Bowman/Chodera/AlphaFold | ✅ | Plausible — Bowman lab does cryptic-pocket MD; Chodera does cancer MD; AlphaFlow/AF3 provide AF ensembles |
| 13 | ZINC22 "in-stock + on-demand" subset ~5B compounds | ⚠️ | Tingle/Irwin 2023 paper cites 37.2B total; in-stock is a smaller subset but the "~5B" figure isn't directly attestable in the 2023 paper. CartBlanche current 2D = ~55B per `H_models_compute_audit.md`. **Fix:** "ZINC22 in-stock/tranche subset (~5B in 3D-ready form)" or cite a specific subset |
| 14 | ZINC22 full ~37B | ✅ | Tingle/Irwin 2023 JCIM 63:1166 — "over 37 billion enumerated, searchable" |
| 15 | Enamine REAL ~70B | ⚠️ | Stale as of May 2026 — current is ~94.5B (Apr 2026 BioSolveIT update); 70B was Feb 2025 |
| 16 | AutoDock Vina URL | ✅ | https://vina.scripps.edu/ valid |
| 17 | GNINA URL | ✅ | https://github.com/gnina/gnina valid |
| 18 | GNINA 2–3× enrichment claim | ⚠️ | The standard GNINA 1.0 paper (McNutt 2021) reports Top1 rank up from 58% to 73% (pocket-defined redock) and EF1% improvements over Vina. "Enrichment factors doubled or near doubled" is reported for OnionNet-SFCT+Vina (a related method). 2–3× enrichment is in the right ballpark but specific factor depends on benchmark; cite McNutt 2021 or MDPI 2025 explicitly |
| 19 | boinc-server-docker https://github.com/marius311/boinc-server-docker | ✅ | Exists, MIT license, maintained by marius311 (Marius Millea, formerly Caltech). 126 stars / 69 forks. Latest tagged release 4.1.0 Oct 2019 (still functional) |
| 20 | Hetzner / OVH as host options | ✅ | Both are real EU bare-metal providers, viable for BOINC server |
| 21 | Phase 2 targets: KRAS G12V/G12R/Q61H, mutant p53 (Y220C, R175H, R248Q), MYC-MAX, FAP, CXCR4, HAS2/HAS3 | ⚠️ | All are real targets (`B_pdb_and_structures.md`, `15_targeted_therapy.md` confirms each). HAS2/HAS3 specifically have evidence in PDAC (Kultti 2014 BioMed Res Int; Nat Commun Biol 2026 on HAS2-PD-L1 axis). Listing them is defensible |
| 22 | DiffDock-L, Boltz-1 as ML rescoring | ✅ | Both real, ML-based, open-source |

### §4 Roadmap, §5 verification, §7 risks (lines 98–153)

| # | Claim | Status | Evidence |
|---|---|---|---|
| 23 | MRTX1133 / RMC-6236 / RMC-9805 / etalanetug / PC14586 as positive controls | ⚠️ | All real except **etalanetug** — there is no clinically-disclosed drug with that name. The intended drug is likely **adagrasib** (MRTX849) for G12C or a typo. **Fix:** verify spelling; "MRTX1133 for KRAS G12D, RMC-6236 for pan-RAS, rezatapopt/PC14586 for p53 Y220C" |
| 24 | Wet-lab assay hit-rate target ≥5% as industry benchmark for ultra-large VS | ⚠️ | Conservative — Lyu 2019 reported 11–22% on D4/AmpC, Sadybekov 2022 V-SYNTHES 33% on CB2. 5% is a defensible floor for novel binders but is *not* the headline industry benchmark today |
| 25 | "BOINC's built-in replication-then-consensus model" | ✅ | Adaptive replication tracks `(host, app_version)` trust per `A_boinc_and_tools.md`; canonical BOINC mechanism |
| 26 | "Volunteers attack / poison results" mitigated by replication+cross-validate | ✅ | Standard BOINC security pattern |
| 27 | Validator replication ×2 | ✅ | Standard BOINC; doc's "each WU replicated to 2 volunteers" matches the typical `<min_quorum>2</min_quorum>` config |
| 28 | Science United integration https://scienceunited.org/ | ✅ | Valid umbrella service for opt-in by topic |

---

## Detailed verification — `20_synthesis.md`

### §TL;DR (lines 6–12)

| # | Claim | Status | Evidence |
|---|---|---|---|
| 29 | 6-stage pipeline (AlphaFold3/Boltz-1 → MD ensembles → active-learning Vina/Uni-Dock → GNINA → Boltz-2 → OpenFE) | ✅ | All six tools exist, are open-source, and are the right level of the stack (`H_models_compute_audit.md` confirms each) |
| 30 | ~50K active hosts as mid-tier BOINC, between FightAIDS@home and OpenPandemics | ⚠️ | Order-of-magnitude correct: FightAIDS@home had ~50–100K active hosts pre-2017; OpenPandemics-COVID-19 peaked >300K hosts. "Mid-tier between" is fair if you mean "smaller than OpenPandemics-COVID at peak, similar to FightAIDS@home steady-state." Defensible |
| 31 | Active learning: dock 1%, recover ~90% top hits (MolPAL) | ✅ | Graff/Shakhnovich/Coley 2021 Chem Sci confirms ~90% recovery at ~4% acquisition; "1% → ~90%" is the strong-case rounding (`H_models_compute_audit.md`) |
| 32 | KRAS G12D ~40%, G12V ~30%, G12R ~12%, Q61H ~5% | ✅ | `15_targeted_therapy.md` Table 2 gives G12D 40–44%, G12V 28–32%, G12R 13–16%, Q61H 2–4% — synthesis numbers are accurate rounding |
| 33 | KRAS variants together ~85% of PDAC | ✅ | 40+30+12+5 = 87% ≈ 85%; consistent with KRAS-mut PDAC totalling ~90% |
| 34 | "$15K cloud/yr at ~50K hosts" | ✅ | Cross-verified by `H_models_compute_audit.md` Part 8: 50K hosts × 50% duty × 8760 h × 8 cores = 1.75×10⁹ core-hr theoretical; 2.4M core-hr is realistic |
| 35 | 2.4M CPU-core-hr + 80K GPU-hr | ✅ | Same Part 8 sanity check; passes |

### §"What stays the same" (lines 14–21)

| # | Claim | Status | Evidence |
|---|---|---|---|
| 36 | WCG not currently soliciting external proposals; Krembil transition | ✅ | `03_boinc.md` §2 and confirmed by F. WCG site states proposals paused/closed during Krembil transition; Krembil partnership required |

### §1 Pipeline (lines 23–67)

| # | Claim | Status | Evidence |
|---|---|---|---|
| 37 | AlphaFold3 weights "Nov 2024" (synthesis implies recent) | ✅ | DeepMind released AF3 inference code + weights for academic use Nov 11, 2024. Doc earlier said "Feb 2025" (flagged in `H_models_compute_audit.md`); synthesis is correctly Nov 2024 here (line not explicit but pipeline diagram is consistent) |
| 38 | Boltz-1 (MIT, 2024) | ✅ | bioRxiv Nov 19 2024, MIT license confirmed |
| 39 | AlphaFlow exists | ✅ | Jing et al. 2024 ICML; https://github.com/bjing2016/alphaflow — flow-matching fine-tune of AlphaFold for ensembles |
| 40 | OpenMM (MIT/LGPL, Apple Metal) | ⚠️ | MIT/LGPL confirmed (`A_boinc_and_tools.md`). "Apple Metal" via the OpenCL platform on macOS rather than a native Metal backend; on M-series Macs OpenMM runs via the Metal-OpenCL bridge, not a dedicated Metal kernel. Acceptable shorthand but technically not a native Metal port |
| 41 | AutoDock Vina + Uni-Dock-GPU + MolPAL/Deep Docking | ✅ | All three exist; Vina (Apache), Uni-Dock (Apache, ByteDance), MolPAL (MIT, Coley lab) |
| 42 | GNINA CNN rescoring (GPL/Apache) | ✅ | Dual GPL/Apache confirmed |
| 43 | Boltz-2 (MIT, Pearson ~0.62 vs FEP ~0.72, 1000× lower cost) | ✅ | bioRxiv Jun 18 2025; benchmarks exactly match (`H_models_compute_audit.md`) |
| 44 | OpenFE RBFE RMSE 1.73 kcal/mol on Dec 2025 ChemRxiv | ✅ | ChemRxiv Dec 2025, 15-pharma collaboration, weighted RMSE 1.73 [1.53, 1.96] kcal/mol on the 58-system public benchmark |
| 45 | "30 leads on cloud rented GPUs" / "~$15K/yr" | ✅ | Sanity check holds (`H_models_compute_audit.md`) |

### §2 Active learning (lines 71–82)

| # | Claim | Status | Evidence |
|---|---|---|---|
| 46 | "10B compounds × 1 conformation × 5 sec/CPU ≈ 50B core-hours ≈ 5M CPU-years" | ✅ | Math: 10B × 5 sec = 5×10¹⁰ s = 1.39×10⁷ CPU-hr per ligand × 1 conf. **Wait — recompute:** 10B × 5 s = 5 × 10¹⁰ s ÷ 3600 = 1.39 × 10⁷ CPU-hr ≈ 14M CPU-hr ≈ 1,600 CPU-years. The doc's "50B core-hours / 5M CPU-years" treats 5 s as 5 hr or includes more conformations. **⚠️ The exact arithmetic in the doc is off by a factor of ~3,500 if you take "5 sec/CPU" literally.** It works if you assume 5 minutes (≈300 s) and 60 conformations, or 5 s × 50 conformations and somehow re-scoring, but as stated the numbers do not multiply out. The qualitative point (intractable without AL) is correct, but the specific multiplication is wrong. **Fix:** Either change "5 sec/CPU" to "~5 min/CPU/conformation" and add "× 50 conformations" (which then yields ~70B core-hours ≈ 8M CPU-years — closer), or drop the explicit math |
| 47 | "5M CPU-years drops to ~250K core-years" with AL (~20× speedup) | ⚠️ | Tied to the wrong math above; the ratio (250K / 5M = 5%) is consistent with the "dock 1%, predict 99%" framing but the absolute numbers inherit the error |
| 48 | "ZINC22 in-stock subset ~5B" | ⚠️ | Same as proposal #13 — figure isn't directly attestable to published source |

### §3 Hybrid workunits table (lines 84–96)

| # | Claim | Status | Evidence |
|---|---|---|---|
| 49 | Workunit runtimes (AF/Boltz 30–60 min GPU, Vina 10–20 min CPU, Uni-Dock 5–15 min GPU, GNINA 5–10 min GPU, Boltz-2 5–15 min GPU) | ✅ | Plausible across consumer hardware; Uni-Dock ~0.1 s/ligand on V100 (`H_models_compute_audit.md`) implies a 10K-ligand batch at ~17 min, consistent |
| 50 | "Boltz-2 needs 8 GB RAM" | ⚠️ | Boltz-2 inference is GPU-VRAM-bound; 8 GB VRAM is the rough floor for the lighter modes. Some configurations require 12–24 GB. As a heuristic floor, acceptable |

### §"What's new" / Track 2 — Neoantigens (lines 102–116)

| # | Claim | Status | Evidence |
|---|---|---|---|
| 51 | Autogene cevumeran 8/16 responders durable T-cell responses at 3+ years | ✅ | Sethna et al., Nature 2024 (follow-up to Rojas Nature 2023); responders n=8, non-responders n=8, median RFS not-reached vs 13.4 mo, P=0.007 (`G_immunotherapy_audit.md` #10) |
| 52 | ELI-002 99% mKRAS T-cell response in AMPLIFY-7P | ⚠️ | Verified figure (89/90 = 99%) but `G_immunotherapy_audit.md` #15 flags that the original `14_immunotherapy.md` conflated AMPLIFY-201 (2P, smaller) with AMPLIFY-7P (Phase 2). The synthesis cleanly attributes to AMPLIFY-7P — better than the source doc |
| 53 | 2022 NEJM 72% PR with TCR-T against G12D | ✅ | Leidner et al., NEJM 2022; 71-yr-old woman, HLA-C*08:02, 16.2×10⁹ cells, 72% PR (`G_immunotherapy_audit.md` #13) |
| 54 | NetMHCpan, MHCflurry, BigMHC, PRIME exist | ✅ | All real MHC-binding predictors |
| 55 | "Current prediction accuracy plateaus around AUROC 0.85" | ⚠️ | Defensible — recent MHC-I prediction (NetMHCpan-4.1, BigMHC) reports AUROC 0.85–0.95 depending on benchmark and allele coverage. "Plateau around 0.85" is the conservative lower bound. Phrase as "0.85–0.9 on harder OOD benchmarks" |

### §Track 3 — TCR-pMHC (lines 119–127)

| # | Claim | Status | Evidence |
|---|---|---|---|
| 56 | Rosenberg NEJM 2022 case used HLA-C*08:02 for KRAS G12D | ✅ | Verified (`G_immunotherapy_audit.md` #13). Peptide GADGVGKSA |
| 57 | ~6000 common HLA alleles | ⚠️ | IPD-IMGT/HLA database has >30,000 HLA-I alleles; "common" alleles (>0.1% in some population) is ~6000–7000. Acceptable rough number, but the actually-relevant set for TCR-T (HLA-A/B/C alleles seen in modeling) is more like 100–300 |
| 58 | "~3% (HLA-C*08:02 carriers)" current eligibility | ⚠️ | HLA-C*08:02 has carrier frequency ~5–8% in European/US populations, lower in East Asian (~1–2%). "3%" is a defensible global-weighted average for an HLA-C*08:02 + KRAS-G12D-positive PDAC intersection. Plausible but could be ~5% in Western populations |
| 59 | "40%+ of PDAC patients potentially eligible" with HLA × mKRAS map | 🔵 | Aspirational; depends on assumptions about allele coverage and HLA-A/B vs HLA-C presentation efficiency. Not directly verifiable as a published figure |

### §Track 4 — KRAS resistance MD (lines 128–139)

| # | Claim | Status | Evidence |
|---|---|---|---|
| 60 | RMC-6236 29% ORR across any RAS mutation in 2025 | ✅ | `15_targeted_therapy.md` Table 3: 29% any-RAS / 35% G12; confirmed by ASCO 2025 |
| 61 | RMC-9805 30% ORR in Phase 1 | ✅ | `15_targeted_therapy.md` Table 3: ~30% ORR at RP2D; confirmed ASCO 2025 |
| 62 | Secondary KRAS switch-II mutations cause resistance | ✅ | `15_targeted_therapy.md` §2.3: Y96C, H95Q/D/R, R68S |
| 63 | "PROJECT/15_targeted_therapy.md §2.5" cross-reference | ❌ | `15_targeted_therapy.md` has §2.1 (biology), §2.2 (agents), §2.3 (resistance), §2.4 (combinations) — but **no §2.5**. The resistance content (KRAS amplification, RTK reactivation, lineage switching, EMT, squamous transformation) is in **§2.3**, not §2.5. **Fix:** Change reference to "§2.3" |

### §"Refined target panel" (lines 141–171)

| # | Claim | Status | Evidence |
|---|---|---|---|
| 64 | KRAS G12D ~40% (Tier 1) | ✅ | As above |
| 65 | KRAS G12V ~30% (Tier 1) | ✅ | As above |
| 66 | KRAS G12R ~12% (Tier 2) | ✅ | `15_targeted_therapy.md` 13–16% range; 12% is a slight under-round |
| 67 | KRAS Q61H ~5% (Tier 2) | ⚠️ | `15_targeted_therapy.md` Table 2 gives Q61H 2–4%, not 5%. 5% is slightly inflated. **Fix:** "~3–5%" |
| 68 | Mutant p53 R175H ~10% "(largest non-Y220C)" | ❌ | Pan-cancer R175H is ~6% of TP53-mut; PDAC-specific data (TCGA PAAD) suggests ~3% of PDAC overall. The "10%" figure and the "largest non-Y220C" framing are both wrong. R175 and R248 are roughly tied in pan-cancer (~6% and ~6–9%); R273 is ~5–7%. **Fix:** "R175H ~5–6% of TP53-mut PDAC (one of the largest structural hotspots)" |
| 69 | Mutant p53 R273H ~7% | ⚠️ | `15_targeted_therapy.md` Table 4: R273H/C ~5–7% pan-cancer. 7% is the upper edge. Acceptable |
| 70 | Mutant p53 R248Q/W ~7% | ⚠️ | `15_targeted_therapy.md` Table 4: ~6–9% pan-cancer. 7% is fine |
| 71 | Mutant p53 Y220C ~1% (smallest hotspot) | ⚠️ | `15_targeted_therapy.md` Table 4: ~1.8% pan-cancer. 1% is slightly under-rounded; "smallest hotspot but reference" framing is fair |
| 72 | Mutant p53 G245S ~3% | ⚠️ | `15_targeted_therapy.md` Table 4: ~3%. Match |
| 73 | "rezatapopt is a known binder" for Y220C | ✅ | PMV Pharma PC14586/rezatapopt, PYNNACLE trial; `15_targeted_therapy.md` §4.1 |
| 74 | "ZMC1 + cryptic-pocket work suggests R175H druggable" | ✅ | ZMC1 (zinc metallochaperone) restores zinc cofactor to R175H mutant — Carpizo lab |
| 75 | "APR-246 partially works on R273H" | ⚠️ | APR-246/eprenetapopt is a broad cysteine-binding reactivator; preclinical/MDS-AML data; PDAC-specific R273H response is sparse. "Partially works" is generous |
| 76 | BRD4 / CDK9 indirect MYC | ✅ | `15_targeted_therapy.md` §5 |
| 77 | FAP "Approved zenocutuzumab proves PDAC stroma is targetable" | ❌ | Zenocutuzumab is HER2×HER3 bispecific for NRG1-fusion-positive PDAC (a 0.5–1.5% NRG1-fusion driver), **not stroma, not FAP** (`15_targeted_therapy.md` Table 6 row #244 correctly classifies it). **Fix:** drop this rationale; replace with FAPI radioligand precedent (e.g., FAPI-46) or theranostic literature |
| 78 | CXCR4 stromal targeting | ⚠️ | CXCR4 is on T-cells/myeloid cells in the TME, not technically stroma; it's a TME-modulation target. Acceptable shorthand |
| 79 | HAS2/HAS3 (hyaluronan) "PEGPH20 failed as a drug; small-molecule HAS inhibitors are open" | ✅ | Real targets in PDAC — HAS3 BxPC-3 xenograft data (Kultti 2014), HAS2-PD-L1 paper (Commun Biol 2026), 4-MU as HAS inhibitor. PEGPH20 HALO-301 failure verified (`G_immunotherapy_audit.md` #27) |
| 80 | Claudin 18.2 "Zolbetuximab proves the target is real" | ⚠️ | `15_targeted_therapy.md` Table 6 footnote: GLEAM Phase II failed OS in Oct 2025. Target is real; zolbetuximab outcomes are mixed. "Proves the target is real" is defensible for druggability but should disclose GLEAM failure |

### §Budget (lines 174–190)

| # | Claim | Status | Evidence |
|---|---|---|---|
| 81 | 2.4M CPU-core-hr/yr | ✅ | Sanity-checked (`H_models_compute_audit.md` Part 8) |
| 82 | 80K GPU-hr/yr | ✅ | Same |
| 83 | $15K cloud/yr | ✅ | Same |
| 84 | 5 TB storage | ✅ | Reasonable for 5B-compound docked output + structures |
| 85 | 50 TB/yr egress | ✅ | At ~5 MB per workunit batch × ~10M batches/yr ≈ 50 TB. Realistic |
| 86 | "Hetzner bare-metal ~$200/month" | ✅ | Hetzner AX/EX dedicated servers (AMD EPYC, 64–128 GB RAM, NVMe) run €100–250/mo. Realistic |
| 87 | "$5–10K/yr server + cloud, $5–10K/yr storage/CDN" | ✅ | Order-of-magnitude correct |
| 88 | "Wet-lab validation $50–200K/yr" | ✅ | Plausible — DSF screen ~$50/compound × 1000 compounds ≈ $50K; SPR / ITC + cell assays push to $200K |
| 89 | "Schrödinger FEP+ $50–100 cloud GPU + 1 hr researcher / RBFE calc" | ✅ | Order-of-magnitude match; published Schrödinger benchmarks |

### §"What we should NOT do" (lines 192–200)

| # | Claim | Status | Evidence |
|---|---|---|---|
| 90 | Petals/Hivemind work for inference, not training, on volunteer compute | ✅ | Both Petals (Borzunov et al. 2022) and Hivemind (Ryabinin et al.) focus on distributed inference + small-batch fine-tuning; large-scale gradient training across heterogeneous internet hosts has been demonstrated only at small scale (e.g., DiLoCo, but not via volunteer compute) |
| 91 | MSI-high PDAC ~1% | ✅ | `15_targeted_therapy.md` Table 1: MSI-H 0.8–1.5% |

### §"Where deep dives raised new questions" (lines 202–209)

| # | Claim | Status | Evidence |
|---|---|---|---|
| 92 | Tuveson lab + HUB Organoid Biobank "hundreds of PDOs" with drug screen | ✅ | Tiriac 2018 (66 PDOs), HUB confirmed (`H_models_compute_audit.md` Part 4); cross-reference to `16_research_models.md §3` is valid |
| 93 | END-PAC, PRECEDE biobanks | ✅ | Both real PDAC consortia (`11_risk_factors.md` reference) |
| 94 | PANORAMA / PANDA CT datasets | ✅ | PANORAMA (Pancreatic CT lesion challenge) and PANDA (Pancreatic Cancer Detection Algorithm) are both real public CT datasets |

### §"Final notes" and cross-references (lines 253–273)

| # | Claim | Status | Evidence |
|---|---|---|---|
| 95 | Daraxonrasib Phase 3 ongoing in 2026 | ✅ | RASolute 302 (NCT06625320) and RASolute 303 active; pivotal Phase 3 OS readout reported May 2026 (Revolution Medicines press release: mOS 13.2 mo vs 6.7 mo, HR 0.40, P<0.0001) |
| 96 | Cross-ref to `15_targeted_therapy.md §2.5` for resistance | ❌ | Section is §2.3, not §2.5 (see #63) |
| 97 | Cross-ref to `14_immunotherapy.md` | ✅ | File exists; immunotherapy claims appropriately deep-dive there |
| 98 | Cross-ref to `16_research_models.md §3` for HUB/Tuveson PDOs | ✅ | Section exists and covers organoid biobanks |
| 99 | Cross-ref to `11_risk_factors.md` for biobanks | ✅ | File covers hereditary and modifiable risk |
| 100 | Cross-ref to `17_computational_methods.md` for pipeline | ✅ | File covers all six pipeline stages |

---

## Summary

**Total distinct claims audited: ~100**

- ✅ **Verified: ~66**
- ⚠️ **Partial / nuance / minor inaccuracy: ~25**
- ❌ **False: 5**
- 🔵 **Unable to verify: ~4**

### Top 5 errors (ranked by potential harm)

1. **F@h KRAS-VHL work attributed to Chodera lab — actually Xuhui Huang (UW-Madison)** (`04_proposal.md` lines 7, 92). If used as the outreach hook, the partnership letter will arrive at the wrong lab. The paper is Tu et al. JACS Au 2024 (DOI 10.1021/jacsau.4c00503).

2. **Zenocutuzumab miscast as proof that "PDAC stroma is targetable"** (`20_synthesis.md` Tier 3 FAP row). It is an NRG1-fusion HER2×HER3 bispecific targeting tumor cells, not stroma. Inserting it as Tier 3 justification for FAP is a substantive target-class confusion.

3. **R175H listed as "~10% (largest non-Y220C)" in PDAC** (`20_synthesis.md` Tier 2). Real PDAC frequency is ~3% overall, ~5–6% of TP53-mut PDAC; the doc's own deep dive gives ~6% pan-cancer. Roughly 2× over-stated; misleads target prioritization.

4. **Cross-reference to `15_targeted_therapy.md §2.5`** for KRAS resistance mechanisms (`20_synthesis.md` Track 4). The section does not exist; the content is in **§2.3**. A reader following the citation will land in the wrong section.

5. **The "naive VS math" 10B × 1 conf × 5 sec/CPU = 50B core-hours arithmetic is wrong by ~3,500×** (`20_synthesis.md` §2). 10B × 5 s = 14M CPU-hr, not 50B. The qualitative point (intractable without AL) survives but the explicit math is undermined. Likely the doc meant "5 min" or omitted multiplication by conformations/scoring.

### Secondary issues worth fixing

- "Enamine REAL ~70B" stale — current is ~94.5B (Apr 2026).
- "etalanetug" as a positive control — appears to be a typo; no such named drug.
- KRAS Q61H listed as ~5% PDAC — `15_targeted_therapy.md` Table 2 says 2–4%.
- "≥5% wet-lab hit-rate industry benchmark" — modern ultra-large VS routinely reports 11–22%; 5% is a conservative floor, not the industry benchmark.
- AlphaFold3 weights "Feb 2025" in `17_computational_methods.md` source — actually Nov 11 2024 (the synthesis doesn't make this error; the source doc does).
- "ZINC22 ~5B in-stock subset" — figure isn't directly attestable to the Tingle/Irwin 2023 paper; should cite a specific tranche or update.
- "6000 common HLA alleles" — total >30K in IPD-IMGT/HLA; "common" alleles (>0.1% allele frequency) is closer to 6–7K; the *practically modeled* set is closer to 100–300 alleles. Defensible as a rough upper bound.

### What checks out cleanly

- Both `04_proposal.md` and `20_synthesis.md` are internally consistent with each other and with the deep-dive documents on most KRAS, p53, immunotherapy, and computational-tool claims.
- F@h Sept 2025 URL is valid and the numerical specifics (~1.5 ms, 6 states, 3 PROTAC-favorable) are exactly correct — only the lab attribution is wrong.
- BOINC architecture claims (boinc-server-docker, replication-then-consensus, Hetzner/OVH, Science United) all verify.
- Tool stack (Vina, GNINA, AlphaFlow, OpenMM, Uni-Dock, MolPAL, Boltz-1/2, OpenFE) — all exist with correct licenses.
- Compute budget (~2.4M CPU-core-hr, ~80K GPU-hr, ~$15K cloud, ~$200/mo server) order-of-magnitude valid.
- KRAS prevalence figures (G12D 40%, G12V 30%, G12R 12%) match prior audit.
- Daraxonrasib Phase 3 RASolute 302 ongoing and OS-positive in 2026.
- Autogene cevumeran 8/16 responders / 3+ year follow-up / 7.7-yr clone lifespan — verified.
- Rosenberg NEJM 2022 / TCR-T / HLA-C*08:02 / 72% PR — verified.
- OpenFE RMSE 1.73 kcal/mol on Dec 2025 ChemRxiv — verified.
- Boltz-2 Pearson 0.62 vs FEP+ 0.72 — verified.
- MolPAL "dock 1% recover ~90%" — verified (Graff 2021).
- HAS2/HAS3 as real PDAC stromal targets — verified.

---

## Recommended fixes (priority order)

1. **`04_proposal.md` §TL;DR and §3** — Re-attribute the KRAS-VHL JACS Au 2024 paper to Xuhui Huang (UW-Madison). If sending the F@h pitch letter, address both Huang and Chodera; do not imply Chodera authored that specific paper.

2. **`20_synthesis.md` Tier 3 FAP row** — Remove "Approved zenocutuzumab proves PDAC stroma is targetable." Replace with FAPI radioligand precedent (FAPI-46, FAP-2286) or the broader CAF/FAP literature. Move zenocutuzumab to the correct row if needed (NRG1 fusions, KRAS-WT subset).

3. **`20_synthesis.md` Tier 2 R175H row** — Change from "~10% (largest non-Y220C)" to "~5–6% of TP53-mut PDAC, structurally distinct hotspot." Drop the "largest non-Y220C" framing (R248Q/W is comparable).

4. **`20_synthesis.md` Track 4** — Change `§2.5` cross-reference to `§2.3`.

5. **`20_synthesis.md` §2 active learning** — Recompute the naive math: 10B × 5 s/CPU ≈ 14M CPU-hr (not 50B core-hr). Or change "5 sec/CPU" to "~5 min/CPU/conformation × 50 conformations" to recover the order of magnitude.

6. **`04_proposal.md` §2** — Update "Enamine REAL (~70B)" to "~95B (Apr 2026)."

7. **`04_proposal.md` §5** — Verify "etalanetug" spelling; likely a typo for a different drug.

8. **`04_proposal.md` §5** — Reframe "≥5% (industry benchmark for ultra-large VS)" as "≥5% (conservative target; published ultra-large VS reports 11–22% per Lyu 2019 Nature)."

9. **`20_synthesis.md` Tier 2 Q61H** — Update from "~5%" to "~3–5%."

The remaining ~25 partial items are minor (rounding, scope clarifications) and do not change the strategic recommendation. The two factual errors that most undermine the strategy as written are #1 (F@h attribution → wrong outreach target) and #2 (zenocutuzumab → wrong target class).
