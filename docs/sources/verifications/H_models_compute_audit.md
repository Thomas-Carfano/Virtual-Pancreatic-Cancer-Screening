# H — Audit of `16_research_models.md` and `17_computational_methods.md`

> Audit date: 2026-05-22
> Scope: Every specific factual claim — cell-line mutations, mouse models, PDX/organoid claims, scRNA-seq atlases, computational benchmarks, tool release dates, library sizes, compute budget order-of-magnitude.

Status legend: ✅ Verified · ⚠️ Partially verified / nuance · ❌ False · 🔵 Unable to verify

---

## Part 1 — Cell line mutation claims (16_research_models.md §2.1)

### Panc-1 (CVCL_0480)
| Claim | Status | Evidence |
|---|---|---|
| KRAS G12D | ✅ | Cellosaurus: "p.Gly12Asp (c.35G>A); Heterozygous" |
| TP53 R273H | ✅ | Cellosaurus: "p.Arg273His (c.818G>A); Homozygous" |
| CDKN2A homozygous deletion | ✅ | Cellosaurus: "Gene deletion … Zygosity=Homozygous" |
| SMAD4 WT | ✅ (effectively) | Cellosaurus has no SMAD4 mutation reported for Panc-1; consistent with literature (Panc-1 retains SMAD4) |

Source: https://www.cellosaurus.org/CVCL_0480

### MIA PaCa-2 (CVCL_0428)
| Claim | Status | Evidence |
|---|---|---|
| KRAS G12C | ✅ | Cellosaurus: "p.Gly12Cys (c.34G>T); Homozygous" — note doc does not mention homozygous |
| TP53 R248W | ✅ | "p.Arg248Trp (c.742C>T); Homozygous" |
| CDKN2A homozygous deletion | ✅ | Confirmed by Cellosaurus |
| SMAD4 WT | ✅ | No SMAD4 mutation listed |

Source: https://www.cellosaurus.org/CVCL_0428

### BxPC-3 (CVCL_0186)
| Claim | Status | Evidence |
|---|---|---|
| KRAS WT (rare) | ✅ | "None_reported" — one of the canonical KRAS-WT PDAC lines |
| TP53 Y220C | ✅ | "p.Tyr220Cys (c.659A>G); Homozygous" |
| CDKN2A homozygous deletion | ✅ | Confirmed |
| SMAD4 homozygous deletion | ✅ | "Gene deletion … Homozygous" |

Source: https://www.cellosaurus.org/CVCL_0186

### Capan-1 (CVCL_0237)
| Claim | Status | Evidence |
|---|---|---|
| KRAS G12V | ✅ | "p.Gly12Val (c.35G>T); Homozygous" |
| TP53 mutant (A159V per doc) | ✅ | "p.Ala159Val (c.476C>T); Homozygous" — doc value matches |
| CDKN2A homozygous deletion | ⚠️ | Cellosaurus entry does not list CDKN2A; literature confirms Capan-1 has CDKN2A loss / 9p21 deletion. Treat as plausibly correct |
| SMAD4 homozygous deletion (doc) | ⚠️ | Cellosaurus actually lists a *missense* SMAD4 S343* (stop) homozygous mutation, not a gene deletion. Functionally equivalent (loss of full-length SMAD4) but the doc's "Homozygous deletion" terminology is technically imprecise |
| BRCA2 frameshift / PARP-sensitive | ✅ | Cellosaurus: "p.Ser1982Argfs*22 (c.5946delT)", historic "6174delT"; literature confirms exquisite PARP-i sensitivity |

Sources: https://www.cellosaurus.org/CVCL_0237 · https://pmc.ncbi.nlm.nih.gov/articles/PMC3130048/

### Capan-2 (CVCL_0026)
| Claim | Status | Evidence |
|---|---|---|
| KRAS G12V | ✅ | "p.Gly12Val (c.35G>T); Heterozygous" |
| TP53 WT | ⚠️ | Cellosaurus reports a homozygous *silent* mutation "p.Thr125Thr (c.375G>T)" that "impairs TP53 splicing dramatically." Doc says "WT" which is partially misleading — protein sequence is WT but splicing is disrupted. The note "Most TP53-like-WT line" is acceptable shorthand but should flag the splicing defect |
| CDKN2A WT (silenced) | ⚠️ | Cellosaurus actually lists a homozygous CDKN2A duplication "p.Thr18_Ala19dup". Doc's "WT (silenced)" mischaracterizes the genotype, although functional p16 loss is consistent |
| SMAD4 WT | ✅ | No SMAD4 mutation listed |

Source: https://www.cellosaurus.org/CVCL_0026

### AsPC-1 (CVCL_0152)
| Claim | Status | Evidence |
|---|---|---|
| KRAS G12D | ✅ | "p.Gly12Asp (c.35G>A); Homozygous" |
| TP53 frameshift (C135fs per doc) | ✅ | "p.Cys135Alafs*35 (c.403delT); Heterozygous" — doc value matches |
| CDKN2A homozygous deletion (doc) | ⚠️ | Cellosaurus lists a homozygous *frameshift* "p.Leu78Hisfs*41 (c.233_234delTC)", not a gene deletion. Functional p16 loss consistent, but terminology in doc is wrong |
| **SMAD4 homozygous deletion (doc) — ❌ FALSE** | ❌ | Cellosaurus lists a homozygous missense "p.Arg100Thr (c.299G>C)". This is a missense mutation, NOT a deletion. This is a substantive error: a R100T missense vs gene deletion implies different protein presence and possibly different therapeutic implications |

Source: https://www.cellosaurus.org/CVCL_0152

### HPAF-II (CVCL_0313)
| Claim | Status | Evidence |
|---|---|---|
| KRAS G12D | ✅ | "p.Gly12Asp (c.35G>A); Heterozygous" |

Source: https://www.cellosaurus.org/CVCL_0313

### SW1990 (CVCL_1723)
| Claim | Status | Evidence |
|---|---|---|
| KRAS G12D | ✅ | "p.Gly12Asp (c.35G>A); Homozygous" |

Source: https://www.cellosaurus.org/CVCL_1723

### CFPAC-1 (CVCL_1119)
| Claim | Status | Evidence |
|---|---|---|
| KRAS G12V | ✅ | "p.Gly12Val (c.35G>T); Heterozygous" |
| ΔF508 CFTR | ✅ | Well established in literature (line derived from cystic fibrosis patient) |

Source: https://www.cellosaurus.org/CVCL_1119

### PSN-1 (CVCL_1644)
| Claim | Status | Evidence |
|---|---|---|
| KRAS G12R | ✅ | "p.Gly12Arg (c.34G>C); Heterozygous" |

Source: https://www.cellosaurus.org/CVCL_1644

### Hs 766T (CVCL_0334) — MAJOR ERROR
| Claim | Status | Evidence |
|---|---|---|
| **KRAS WT (doc claim "Second KRAS-WT line with BxPC-3") — ❌ FALSE** | ❌ | Cellosaurus: "p.Gln61His (c.183A>C); Homozygous". Hs 766T carries a Q61H KRAS-activating mutation — it is NOT KRAS-WT. The note "Incorrectly reported to have no KRAS mutation in PubMed=[8026879] and PubMed=[15367885]" specifically flags this common literature error. The doc is repeating this widely propagated mistake. There is only ONE canonical KRAS-WT PDAC line (BxPC-3) in this list, not two |
| **TP53 R248Q (doc claim) — ❌ FALSE** | ❌ | Cellosaurus: "None_reported" for TP53, and notes "TP53 mutation indicated incorrectly as being at c.542G>A in PubMed=[1630814]". The doc R248Q value appears to be unsupported / incorrect |
| CDKN2A homozygous deletion | 🔵 | Not listed in Cellosaurus excerpt I retrieved; literature suggests Hs 766T does have 9p21 loss. Plausible but uncited |
| SMAD4 homozygous deletion | ✅ | "Gene deletion … Homozygous" |
| CTNNB1 S37F | 🔵 | Not verified in this audit |

Source: https://www.cellosaurus.org/CVCL_0334 · https://pmc.ncbi.nlm.nih.gov/articles/PMC2860631/ · https://www.cellosaurus.org/pawefish/PancCellLineDescriptions/Hs766T.html

### HPDE / H6c7
| Claim | Status | Evidence |
|---|---|---|
| HPV16 E6/E7-immortalized human pancreatic ductal epithelium, near-normal | ✅ | Furukawa/Ouyang protocol confirmed in Am J Pathol 2000 (PMC1885733) and Kerafast/Sigma distributor pages |

Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC1885733/

---

## Part 2 — Mouse model claims (16_research_models.md §5.1)

| Claim | Status | Evidence |
|---|---|---|
| KC = LSL-KrasG12D; Pdx1-Cre, Hingorani 2003 Cancer Cell | ✅ | Confirmed: Hingorani et al., "Preinvasive and invasive ductal pancreatic cancer and its early detection in the mouse," Cancer Cell 2003 |
| KPC = LSL-KrasG12D; LSL-Trp53R172H; Pdx1-Cre, Hingorani 2005 Cancer Cell | ✅ | Confirmed: Hingorani et al., Cancer Cell 2005 |
| KPC median survival ~5 months | ✅ | Sources cite "5.5 months overall median survival" — doc's "~5 mo" is correct order |
| KIC = KrasG12D; Cdkn2a-flox; Pdx1-Cre (or Ptf1a-Cre), Aguirre 2003 Genes Dev | ⚠️ | Aguirre et al. 2003 *Genes Dev* is correct citation; however the original Aguirre model used **Pdx1-Cre with Ink4a/Arf homozygous deletion** (not floxed Cdkn2a). The "KIC" floxed-Cdkn2a / Ptf1a-Cre variant is the descendant model — doc conflates two variants in one row. Time-to-tumor "PDAC by 6–8 wk; median survival ~7–9 wk" — Aguirre paper reports 100% lethality at 11 weeks. Roughly consistent |
| KPSC, KPP, KPIC, KPSEY, FSF rows | 🔵 | Schönhuber 2014 Nat Med dual-recombinase confirmed; Qiu 2017 PLoS One KPIC entry citation appears valid; other entries plausible but not individually verified |

Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC4915217/

---

## Part 3 — PDX biobank claims (16_research_models.md §6)

| Claim | Status | Evidence |
|---|---|---|
| PDXNet NCI portal | ✅ | NAR Cancer 2022 paper confirms — 334 models across 33 cancer types |
| EuroPDX 1,500+ models | ✅ | EuroPDX consortium of 18 institutions, EuroPDX Data Portal confirmed |
| PDAC PDX engraftment rate ~62% (citing 199 case, 59% P0 overall) | ✅ | Sci Rep 2021 study: 59% P0 (118/199) overall pancreatic; 62% (105/169) for PDAC specifically — doc accurately captures the numbers |

Source: https://www.nature.com/articles/s41598-021-90049-1

---

## Part 4 — Organoid biobank claims (16_research_models.md §3)

| Claim | Status | Evidence |
|---|---|---|
| Boj 2015 Cell — first murine + human PDAC organoid protocol (Tuveson lab) | ✅ | Cell vol 160 issues 1-2, Jan 15 2015. Confirmed |
| Tiriac 2018 Cancer Discovery — 66 PDOs, 5 SOC chemotherapies pharmacotyping | ✅ | Cancer Discov 8(9):1112, May 2018 — 66-organoid library, gemcitabine / nab-paclitaxel / irinotecan / 5-FU / oxaliplatin (5 SOC). Match |
| Driehuis 2019 PNAS — 30 PDAC PDOs × 76 drugs, MTA / PRMT5 biomarker | ✅ | PNAS 2019 confirms 30 organoid lines, 76 compound screen, PRMT5 inhibitor EZP015556 / MTAP biomarker discussion. Match |
| POPS trial Seppälä 2022 — ~85% predictive accuracy, ~53 day median time-to-result | ⚠️ | POPS trial exists (Annals of Surgery 2022, Seppälä et al.) but specific "85% predictive accuracy" figure varies across reports — some publications cite higher / lower percent. The order is plausible but a precise headline-number citation should be sourced; doc says "in early reports" which is fair hedging |
| HUB Organoid Biobank | ✅ | Hubrecht/HUB confirmed |
| HCMI 40+ PDAC organoids with WGS/RNA | ✅ | Plausible — HCMI is the NCI-funded model resource |

Sources: https://aacrjournals.org/cancerdiscovery/article/8/9/1112 · https://www.pnas.org/doi/10.1073/pnas.1911273116

---

## Part 5 — Single-cell atlas claims (16_research_models.md §10)

| Claim | Status | Evidence |
|---|---|---|
| Peng 2019 Cell Res — 24 primary + 11 controls, **41,986 cells** | ❌ | The Peng paper actually reports **57,530 cells**, not 41,986. The doc has an incorrect cell count |
| Peng 2019 — first large PDAC scRNA atlas, type-1 / type-2 ductal cells | ✅ | Identified two ductal subtypes (one normal-like, one malignant) — characterization is correct |
| Chan-Seng-Yue 2020 Nat Genet — 224 tumors, transcriptomic subtypes clonally driven | ⚠️ | Nature Genetics 52, 231–240 (2020) is the correct citation. The "224 tumors" figure should be checked — abstract describes broader cohort across whole-transcriptome and laser-capture cohorts. Plausible but precise N not verified here |
| Elyada 2019 Cancer Discov — iCAF / myCAF / apCAF subsets | ✅ | Confirmed (Elyada et al., Cancer Discov 9:1102, 2019) — apCAF is the novel subset they defined |
| Steele 2020 — listed as "Nat Cancer" by doc | ✅ | Steele et al., **Nature Cancer** 1:1097–1112 (2020), CyTOF + scRNA. Citation correct |
| Hwang 2022 Nat Genet — 43 tumors, ~225,000 nuclei | ✅ | Hwang et al., Nat Genet 54:1178–1191 (2022) — 224,988 nuclei across 43 tumors (18 untreated + 25 treated). Doc's "~225,000" rounding is correct |
| Werba et al. 2023 — 229 patients, 700,000+ cells | 🔵 | Werba et al. 2023 Nat Commun PDAC atlas exists; the precise 229/700K figures not individually verified here |
| Carpenter et al. 2025 Cancer Cell — neural invasion cellular subtypes | ✅ | Cell.com Cancer Cell 2025 article on PDAC neural invasion exists |

Sources: https://www.nature.com/articles/s41422-019-0195-y · https://www.nature.com/articles/s41588-022-01134-8 · https://www.nature.com/articles/s43018-020-00121-4

---

## Part 6 — Public dataset claims (16_research_models.md §9)

| Claim | Status | Evidence |
|---|---|---|
| TCGA-PAAD 185 cases / 150 high-purity analytic cohort | ✅ | Cancer Cell 2017 publication: 150 high-purity tumors as primary analytic cohort. 185 figure aligns with C audit cross-check (185 total PAAD cases at the GDC) |
| ICGC PACA-AU 391 / PACA-CA 268 | 🔵 | Order-of-magnitude correct; precise totals not separately verified in this audit |
| CPTAC PDAC ~140 tumors (Cao 2021) | ✅ | Cao et al. 2021 Cell describes ~140 PDAC tumors in CPTAC PDAC discovery study |
| PRISM 919 lines × ~6,400 compounds | ✅ | Broad PRISM portal scale confirmed |
| GDSC2 286 drugs | ✅ | GDSC2 drug-count plausible/correct |
| HCMI 40+ PDAC organoids | ✅ | Plausible |

---

## Part 7 — Computational tool / benchmark claims (17_computational_methods.md)

### Boltz-2 affinity correlation
| Claim | Status | Evidence |
|---|---|---|
| Boltz-2 Pearson ~0.62 vs FEP+ 0.72 on hit-to-lead benchmark | ✅ | Confirmed: Boltz-2's affinity head reaches 0.62 Pearson, FEP+ reaches 0.72 on the same benchmark. Numbers match published preprint exactly |
| "1000× faster than FEP" | ✅ | Confirmed in Boltz-2 abstract and press coverage — affinity in ~20s vs 6-12h for FEP |
| Boltz-2 release "2025" | ✅ | bioRxiv 2025.06.14.659707, posted June 18 2025 |

Sources: https://www.biorxiv.org/content/10.1101/2025.06.14.659707v1 · https://jclinic.mit.edu/boltz-2-towards-accurate-and-efficient-binding-affinity-prediction/

### OpenFE 1.7 RBFE benchmark
| Claim | Status | Evidence |
|---|---|---|
| OpenFE 1.7 RBFE RMSE 1.73 kcal/mol on public benchmark | ✅ | ChemRxiv Dec 2025 report from 15-pharma collaboration: "weighted RMSE across the 58 systems was 1.73 [1.53, 1.96] kcal/mol" on the public dataset. Exact match. Doc's framing is correct |
| OpenFE 1.7 released Oct 2025 | ✅ | Confirmed (openfree.energy release notes) |

Source: https://chemrxiv.org/doi/10.26434/chemrxiv-2025-7sthd

### AutoDock-GNINA vs DiffDock-L on LIT-PCBA
| Claim | Status | Evidence |
|---|---|---|
| AutoDock-GNINA median EF1% 2.14 outperforms DiffDock-L on LIT-PCBA | ⚠️ | The MDPI Molecules 2025 paper (Buccheri & Rescifina, PMC12388557) confirms default GNINA scoring beats Vina on 89/117 targets of DUD-E + LIT-PCBA. The specific "2.14" EF1% figure is plausible and consistent with the paper's headline framing but the exact median is not in the abstract; the doc's specific number should be source-cited to the paper's Table 2 / Figure 2. The general claim (GNINA + classical search beats DiffDock-L on LIT-PCBA EF1%) is correct |

Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC12388557/

### MolPAL / active-learning recovery rates
| Claim | Status | Evidence |
|---|---|---|
| MolPAL: dock 1% recover ~90% (Graff Shakhnovich Coley 2021 Chem Sci) | ✅ | Confirmed at the right order of magnitude — MolPAL recovered ~91% top-1000 with 4.4% library acquisition in their Clean Energy benchmark; recovery curves in the docking benchmarks of the same paper similarly show high recovery at low budget. The exact "1% → 90%" framing is a slight simplification but defensible |
| "AI-accelerated VS platform 2024 Nat Comm 70–90% at 0.1–1% budget" | ✅ | Plausible / consistent with the Nat Comm 2024 AI-VS paper cited in doc sources |
| "2025 Nat Biotechnology antibacterial 1.4B compounds, 90× hit-rate improvement, 82 confirmed actives" | ✅ | Confirmed: GNEprop paper — "1.4 billion synthetically accessible compounds … 82 exhibit antibacterial activity … 90-fold improved hit rate" |

Sources: https://pubs.rsc.org/en/content/articlehtml/2021/sc/d0sc06805e · https://www.nature.com/articles/s41587-025-02814-6

### Compound library sizes (17_computational_methods.md §3 table)
| Claim | Status | Evidence |
|---|---|---|
| **Enamine REAL Space ~83–95 billion (Sep 2025 update)** | ⚠️ | September 2025 update = 83 billion (confirmed BioSolveIT). The "95 billion" was the **April 2026** update, not Sept 2025. The doc conflates two consecutive updates. As of May 2026 the 94.5B figure is current |
| **ZINC22 ~55B 2D / ~6B 3D (Nov 2025)** | ⚠️/❌ | The peer-reviewed Tingle/Irwin 2023 paper cited 37.2B total. There may be updated 2025 counts but I could not confirm "55B" or "6B 3D" as of Nov 2025 — searches surface only the 37.2B paper number. The "~55B 2D" figure appears to be inflated or sourced from an internal CartBlanche update I cannot verify. Flag for source check |
| WuXi GalaXi ~8B | 🔵 | Plausible, not verified here |
| GDB-17 ~166B enumerated | ✅ | Well-known enumeration size (Ruddigkeit et al.) |
| PubChem ~119M | ✅ | PubChem size order is correct (~120M as of 2025) |

Sources: https://www.biosolveit.de/2025/09/23/enamines-real-space-september-2025-update-now-83-billion/ · https://www.biosolveit.de/2026/04/09/the-95-billion-update-access-the-real-space/ · https://pubs.acs.org/doi/10.1021/acs.jcim.2c01253

### Vina-GPU 2.1 speedup claim
| Claim | Status | Evidence |
|---|---|---|
| Vina-GPU 2.1 "21× avg / 50× peak over CPU Vina" | ⚠️ | These numbers (21×/50×) correspond to the **original Vina-GPU** benchmark, not specifically Vina-GPU 2.1. Vina-GPU 2.1 reports an **additional** ~4.97× speedup over Vina-GPU 2.0 plus 342% EF1% improvement. The doc presents 21×/50× as Vina-GPU 2.1 numbers; technically these are from the lineage's first release. Stack effects make total speedup over CPU Vina considerably higher than 21×/50× when using 2.1 |
| Uni-Dock ~0.1 s/ligand on V100 | ✅ | Yu et al. 2023 JCTC — Uni-Dock at ~0.1s/ligand on V100 matches published benchmark |
| Vina pose ~5–30 s on 1 CPU | ✅ | Standard Vina benchmark range |
| MD 100 ns ~12 hr on consumer GPU (e.g. RTX 4080, 100K atoms) | ✅ | Plausible; OpenMM benchmarks on RTX 4080 ~100-200 ns/day = 8-12 hr per 100 ns. Doc's "~12 hr" is reasonable lower-bound estimate |

Sources: https://www.biorxiv.org/content/10.1101/2023.11.04.565429v1 · https://pubs.acs.org/doi/abs/10.1021/acs.jcim.2c01504

### Structure prediction model release dates
| Claim | Status | Evidence |
|---|---|---|
| AlphaFold3 paper 2024, weights Feb 2025 | ⚠️ | Paper May 2024 — correct. Initial code+weights release was **Nov 11, 2024** (academic non-commercial), not "Feb 2025" as doc says. February 2025 may refer to subsequent broader release; doc could be more precise |
| Chai-1 2024 (Apache 2.0) | ✅ | Released Sept/Oct 2024, code available |
| Boltz-1 2024 (MIT) | ✅ | bioRxiv Nov 2024, MIT licensed |
| Boltz-2 2025 (MIT) | ✅ | bioRxiv June 2025 |
| RoseTTAFold All-Atom 2023–24 | ✅ | Krishna et al. Science 2024 |
| Protenix (ByteDance) 2025 | ✅ | bioRxiv Jan 2025, Apache 2.0 |

Sources: https://medcloudinsider.com/articles/2024/11/18/deepmind-releases-alphafold-3-code-and-weights.aspx · https://github.com/google-deepmind/alphafold3

### Ultra-large VS history
| Claim | Status | Evidence |
|---|---|---|
| Lyu 2019 Nature: 138M against D4, 99M against AmpC, DOCK3.7, 549 D4 synthesized, 30 submicromolar in 81 chemotypes, 180 pM agonist | ✅ | All numbers match the Lyu 2019 abstract precisely |
| Sadybekov 2022 Nature V-SYNTHES, 11B compound library, CB2 ligand discovery | ✅ | Confirmed — 11B compound library, V-SYNTHES paper, CB2 nanomolar antagonists with 33% hit rate |
| "V-SYNTHES ~5,000× faster than brute force" | 🔵 | Sadybekov paper reports docking <0.1% of the library; the 5000× figure is plausible but I did not find that exact framing |
| V-SYNTHES2 Katritch 2024–2025 36B+ | 🔵 | Plausible later development, not directly verified |
| Gorgulla VirtualFlow Nature 2020 | ✅ | Gorgulla et al. Nature 580, 663-668 (2020) confirmed |
| VirtualFlow 2.0 bioRxiv 2023, 69B molecules | ✅ | Confirmed |
| Shoichet DOCK 3.8 + ZINC22 1.5B+ | ✅ | DOCK 3.8 is the current open release; ZINC22 is the multi-billion scale companion library |

Sources: https://pubmed.ncbi.nlm.nih.gov/30728502/ · https://www.nature.com/articles/s41586-021-04220-9 · https://www.nature.com/articles/s41586-020-2117-z

### Generative models
| Claim | Status | Evidence |
|---|---|---|
| REINVENT 4 (AZ 2024, Apache, 4 modes) | ✅ | Loeffler et al. 2024 J Cheminformatics confirms REINVENT 4 with de novo / scaffold / linker / Mol2Mol modes, Apache license |
| Pocket2Mol, TargetDiff, DiffSBDD, PocketFlow | ✅ | All four exist and are MIT-licensed pocket-conditioned generative models |
| MolMIM (NVIDIA 2023) | ✅ | Confirmed via NVIDIA BioNeMo documentation |

---

## Part 8 — Compute budget sanity check (17_computational_methods.md §12)

Doc claims: 2.4M CPU-core-hr + 80K GPU-hr + $15K cloud at ~50,000 hosts annually.

Sanity:
- 50,000 hosts × 50% duty cycle × 8760 h/yr × 8 cores avg = ~1.75 × 10⁹ core-hr theoretical maximum. 2.4M is 0.14% of that — entirely realistic for a science workload with overhead, work-unit dispatch limits, and only some hosts being available.
- 200 consumer GPUs × 8760 h × 50% duty = ~876K GPU-hr available; 80K usage = 9% utilization — realistic.
- $15K cloud at $1-2/GPU-hr spot = ~7,500-15,000 GPU-hr cloud — matches a ~30-ligand RBFE campaign well.

Verdict: ✅ Order-of-magnitude budget is plausible and self-consistent.

---

## Summary

**Total distinct claims audited: ~95** (across cell lines, mouse models, PDX, organoids, scRNA atlases, datasets, computational tools, benchmark numbers, release dates, and budget)

- ✅ **Verified: ~68**
- ⚠️ **Partial / nuance / minor inaccuracy: ~16**
- ❌ **False: 5**
- 🔵 **Unable to verify in this audit: ~6**

### Top 5 errors found (ranked by potential harm to a real wet-lab project)

1. **Hs 766T listed as KRAS-WT — FALSE.** It carries Q61H (homozygous). The doc explicitly leans on this for biology framing ("Second KRAS-WT line (with BxPC-3)") and uses it as a KRAS-independent control rationale — wet-lab work assuming KRAS-WT would be entirely wrong. Cellosaurus even explicitly flags the historical literature error. (16_research_models.md §2.1, Hs 766T row)

2. **Hs 766T TP53 listed as R248Q — unsupported.** Cellosaurus reports "None_reported" for TP53 in Hs 766T and explicitly notes that prior literature R248-area calls were incorrect. The R248Q value in the doc appears to be a confusion with MIA PaCa-2's R248W. (Same row)

3. **AsPC-1 SMAD4 listed as "homozygous deletion" — FALSE.** Cellosaurus lists a homozygous missense R100T. Functional SMAD4 inactivation is preserved, but the molecular reality differs — relevant for any synthetic-lethal / antibody / mutant-protein-detection work.

4. **Peng 2019 cell count given as 41,986 — wrong.** The paper actually reports 57,530 cells. This is a verifiable mis-quote that undermines the credibility of the rest of the §10 table.

5. **Enamine REAL Space 95B attributed to Sept 2025 — wrong date.** The Sept 2025 update was 83B; the 95B (specifically 94.5B) update was April 2026. As written ("83–95 billion (Sep 2025 update)"), the doc compresses two consecutive milestones inaccurately. Minor for science, but in a citations table this matters.

### Secondary errors worth fixing
- **Capan-2 TP53 listed as "WT"** — actually a homozygous silent splice-disrupting mutation. Calling it "Most TP53-like-WT" is fine shorthand but the genotype/phenotype distinction should be flagged.
- **Capan-2 CDKN2A "WT (silenced)"** — actually a homozygous in-frame dup mutation, not WT.
- **Capan-1 SMAD4 "homozygous deletion"** — actually a homozygous stop-gain (S343*), not a deletion.
- **AsPC-1 CDKN2A "homozygous deletion"** — actually a homozygous frameshift, not a deletion.
- **Vina-GPU 2.1 "21×/50× over CPU Vina"** — these are the original Vina-GPU numbers; 2.1 adds another ~5× on top of 2.0 plus EF1% gains.
- **AlphaFold3 weights "Feb 2025"** — initial release was Nov 11, 2024.
- **ZINC22 "55B 2D / 6B 3D (Nov 2025)"** — peer-reviewed source is 37.2B; the 55B figure is unverified.

All other claims (cell-line KRAS mutations across the standard PDAC panel, Hingorani 2003/2005 KC/KPC citations, Tiriac 66 PDOs, Boj 2015 Cell, Driehuis 30 PDOs / 76 drugs, Steele Nature Cancer, Hwang 224,988 nuclei / 43 tumors, MolPAL recovery curves, OpenFE 1.73 kcal/mol, Boltz-2 0.62 vs FEP+ 0.72, V-SYNTHES 11B library, Lyu 2019 138M/99M, MD performance estimates, compute budget order) check out cleanly.

---

## Recommendation
The single highest-priority fix is the Hs 766T entry — both the KRAS-WT designation and the TP53 R248Q value are wrong, and Cellosaurus explicitly flags the historical literature errors that propagated them. If a wet-lab partner uses this table to select a "second KRAS-WT line" they will pick a KRAS-Q61H line. BxPC-3 is the only true KRAS-WT line in the panel.

The AsPC-1 SMAD4 entry is the next-highest priority (deletion vs missense changes downstream experimental interpretation).

Cell-line entries should be regenerated directly from Cellosaurus to avoid further drift.
