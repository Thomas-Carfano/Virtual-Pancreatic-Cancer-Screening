# 14. Immunotherapy and Cellular Therapy for Pancreatic Cancer

*A deep-research review for the volunteer-computing pancreatic-cancer project. Plain-language where possible, with mechanism-level detail where it matters. Items tagged `[A]` mark places where distributed compute could meaningfully move the needle.*

---

## 1. Why PDAC is "Immune-Cold" — A Mechanism Deep Dive

Across solid tumors, immunotherapy has rewritten the playbook for melanoma, lung, kidney, bladder, and a growing list of others. Pancreatic ductal adenocarcinoma (PDAC) is the conspicuous holdout. Single-agent checkpoint inhibitors produce response rates of essentially zero outside a microsatellite-instability-high (MSI-H) subset that represents about 1% of patients. Why? PDAC is the textbook example of an **immune-cold tumor**, and the reasons are layered.

**1.1 Low tumor mutational burden (TMB).** Neoantigens — the mutant peptides displayed on cancer-cell surfaces that immune cells learn to recognize — are the substrate of T-cell-based immunity. Melanoma carries ~10–100 mutations per megabase (Mb). PDAC carries roughly **2–3 mutations/Mb**, an order of magnitude lower. Fewer mutations means fewer neoantigens, means fewer T-cell clones with potentially useful specificity. In practice the dominant driver mutation, **KRAS** (almost always G12D, G12V, G12R, or G12C), is shared by 90%+ of PDACs but is a poor MHC binder for most HLA alleles, so it often escapes natural presentation.

**1.2 Dense fibrotic stroma.** PDAC tumors are famously desmoplastic — up to 80–90% of tumor volume is non-cancer cells and matrix. Cancer-associated fibroblasts (CAFs), activated pancreatic stellate cells, hyaluronic acid, and collagen form a physical and biochemical barrier. Interstitial fluid pressure climbs to levels that collapse blood vessels and prevent T-cell extravasation. T cells that do enter are often trapped at the stromal periphery and never reach tumor nests.

**1.3 Regulatory T cell (Treg) and MDSC dominance.** Tregs (CD4+ FoxP3+) actively suppress effector T cells. PDAC tumors are enriched in Tregs at every stage, including pre-invasive PanINs. Myeloid-derived suppressor cells (MDSCs) — monocytic and granulocytic — pour out of bone marrow under chemokine signals from the tumor (CCL2, CCL5, CXCL1/2, CXCL5, GM-CSF) and suppress T cells via arginase, iNOS, ROS, and PD-L1. The KRAS oncogene itself drives GM-CSF secretion, recruiting MDSCs directly.

**1.4 M2 macrophage skewing.** Tumor-associated macrophages (TAMs) in PDAC are polarized toward the M2 / wound-healing phenotype, secreting IL-10, TGF-β, and arginase. They suppress T cells, drive fibrosis, and promote angiogenesis. CCR2+ monocytes recruited from the bone marrow are a major source.

**1.5 CD8+ T-cell exclusion and exhaustion.** Even when CD8+ T cells make it in, they are sparse, often peri-tumoral rather than intra-tumoral, and exhausted — high expression of PD-1, TIM-3, LAG-3, and TIGIT, low IFN-γ, low granzyme. Activated stellate cells release **CXCL12**, which sequesters CD8+ T cells away from tumor nests. Blocking CXCR4 (the CXCL12 receptor) with plerixafor in early trials transiently restored T-cell infiltration.

**1.6 Defective antigen presentation.** PDAC cells frequently downregulate MHC class I via autophagy-mediated degradation of MHC-I — a mechanism described by the Yamamoto/Pylayeva-Gupta and Perera labs. Loss of heterozygosity at the HLA locus is also documented. The end result is that even neoantigens that exist aren't shown to T cells.

**1.7 Wnt/β-catenin and immune exclusion.** Tumor-cell-intrinsic activation of WNT/β-catenin signaling correlates with absence of T cells in melanoma and is now implicated in PDAC. β-catenin suppresses CCL4 production, which would otherwise recruit BATF3+ dendritic cells — the DCs that cross-present tumor antigens to CD8+ T cells. No BATF3 DCs, no priming.

**1.8 Metabolic hostility.** The PDAC TME is hypoxic, acidic, and depleted of arginine, tryptophan, and glucose. T cells, which depend on glycolysis for effector function, starve. Adenosine accumulates (via CD39/CD73), suppressing T-cell function through A2A receptors.

The bottom line: PDAC is not merely cold — it is **actively immunosuppressive on at least seven independent axes**. Any therapy that addresses only one of them will fail.

---

## 2. The PDAC Immune Microenvironment — A Cell-by-Cell Map

| Cell type | Role in PDAC | Frequency | Key markers / signals |
|---|---|---|---|
| Tumor cells (ductal epithelial origin) | KRAS-driven; secrete GM-CSF, CXCL1, CCL2 | Variable, often <30% of tumor mass | CK19, KRT19, low MHC-I |
| Cancer-associated fibroblasts (CAFs) | Build stroma; secrete IL-6, CXCL12, TGF-β | Dominant non-immune compartment | α-SMA, FAP, PDPN |
| Pancreatic stellate cells | Activated CAFs; deposit hyaluronan, collagen | Major fibrosis driver | Vimentin, desmin, GFAP |
| Tumor-associated macrophages (TAMs) | M2-polarized; T-cell suppression | 15–50% of immune infiltrate | CD68+ CD163+ CD206+ |
| MDSCs (monocytic and granulocytic) | Arginase, iNOS, ROS suppression | 10–30% of infiltrate | CD11b+ Gr-1+ (mouse); CD14+/CD15+ HLA-DR-low (human) |
| Regulatory T cells (Tregs) | CTLA-4, IL-10, TGF-β secretion | 10–30% of CD4+ | CD4+ FoxP3+ CD25+ |
| Conventional CD4+ T cells | Mostly Th2-skewed | Low | CD4+ FoxP3- |
| CD8+ T cells | Often excluded; exhausted when present | 1–5% of TME | PD-1+ TIM-3+ LAG-3+ |
| BATF3+ cDC1 dendritic cells | Cross-present tumor antigen | Very rare | CD141+ (human); CD103+/CD8α+ (mouse) |
| NK cells | Reduced cytotoxicity | Sparse | NKG2D, NKp46 |
| B cells / tertiary lymphoid structures | When present, correlate with better survival | Variable | CD19, CD20; some PDACs form TLS |

Tertiary lymphoid structures (TLS) — organized aggregates resembling lymph node germinal centers within tumors — are emerging as a positive prognostic feature. Long-term PDAC survivors disproportionately show TLS. Inducing TLS is now a therapeutic goal.

---

## 3. Checkpoint Inhibitors — What's Failed and Why

The PDAC checkpoint inhibitor story is one of repeated, expensive negatives interrupted by a single narrow approval.

**3.1 Anti-PD-1/PD-L1 monotherapy.**
- **KEYNOTE-028** (pembrolizumab in PD-L1+ tumors): 24 PDAC patients, **0% objective response rate**.
- **KEYNOTE-158** (pembrolizumab in MSI-H solid tumors): 22 PDAC patients with MSI-H, **ORR 18.2%**. This is the basis for the FDA tissue-agnostic approval — but MSI-H comprises ~1% of PDAC.
- **Dostarlimab** is similarly approved for dMMR PDAC.

**3.2 Anti-CTLA-4 monotherapy.** Ipilimumab as a single agent in PDAC: no objective responses in phase II.

**3.3 Combination ipi+nivo.** Multiple trials including dual checkpoint blockade in PDAC have shown minimal activity (<5% ORR), in stark contrast to melanoma or RCC.

**3.4 Chemo + checkpoint.** Adding anti-PD-1 to FOLFIRINOX or gemcitabine/nab-paclitaxel did not improve overall survival in randomized trials. The CheckMate-9KD and similar studies were negative.

**3.5 CCR2 + chemo.** PF-04136309 plus FOLFIRINOX showed early promise in a phase Ib (Wainberg et al.) — TAM reduction, encouraging response rate. The phase II program was discontinued for toxicity / efficacy reasons. The biology — depleting recruited monocytes — remains attractive and is being revisited with newer agents.

The mechanistic reason for the failures: checkpoint blockade releases brakes on T cells that already exist. In PDAC, the T cells are absent, excluded, or never primed in the first place. There are no brakes to release. **You can't take the foot off a brake on a car that has no engine.**

---

## 4. Therapeutic Vaccines — Summary Table

| Vaccine | Target / format | Trial | Status (2025/26) |
|---|---|---|---|
| Autogene cevumeran (BNT122) | Personalized neoantigen mRNA | Phase 1 MSKCC (resected PDAC); Phase 2 ongoing | **Active — most promising vaccine in field; 3-year follow-up positive** |
| ELI-002 7P (Elicio) | KRAS amphiphile (G12D/V/R/A/C/S, G13D) + CpG | AMPLIFY-7P (Phase 1/2) | **Active — 99% T-cell response rate; Phase 2 readout Q4 2025** |
| Algenpantucel-L | Allogeneic whole-cell, α-gal modified | IMPRESS Phase 3 (resected) | **Failed 2016; program terminated** |
| GVAX Pancreas | Allogeneic GM-CSF-secreting tumor cells | Combined with CRS-207, ipilimumab, nivolumab | **Multiple combinations evaluated; ECLIPSE Phase IIb did not beat chemo** |
| CRS-207 | Listeria monocytogenes expressing mesothelin | With GVAX | **Discontinued as monotherapy approach** |
| KRAS peptide vaccines | Mutant KRAS long peptides + adjuvant | Multiple Phase I (NCI, Hopkins) | **Active; durable T-cell responses observed** |
| GV1001 | Telomerase (hTERT) peptide | Phase 3 TeloVac | **Failed 2014** |
| MUC1 vaccines | Mucin-1 (PankoMab, ONT-10, others) | Multiple Phase I/II | **Generally weak responses, ongoing variants** |
| Allogeneic DC vaccines | Tumor lysate–pulsed DCs | Various | **Heterogeneous; investigational** |
| ELI-007 / next-gen amphiphile | mKRAS + additional drivers | Preclinical | **Discovery / IND-enabling** |

The pattern is clear: **off-the-shelf, single-target vaccines have failed; personalized neoantigen and KRAS-targeted approaches with potent adjuvants are now showing real signals.**

---

## 5. Personalized Neoantigen Vaccines — Autogene Cevumeran in Depth

This is the most exciting story in PDAC immunotherapy in the past five years.

**The trial.** Vinod Balachandran's group at Memorial Sloan Kettering Cancer Center, in collaboration with BioNTech and Genentech, ran a Phase 1 trial in 16 patients with resected PDAC. After surgery, each patient's tumor was sequenced. Up to 20 personalized neoantigens were chosen using a machine-learning prediction pipeline ranking peptides by predicted MHC binding, expression, and clonality. mRNAs encoding these neoantigens were manufactured in lipid nanoparticles (the BioNTech platform that produced their COVID vaccine). Patients received:
1. Atezolizumab (anti-PD-L1).
2. Autogene cevumeran (8 priming doses + boosts).
3. Modified FOLFIRINOX adjuvant chemotherapy.

**Results (Nature 2023; updates 2024-2025).**
- 8 of 16 patients mounted vigorous, polyclonal, **de novo** neoantigen-specific T-cell responses (responders). These T cells were not present pre-vaccination — they were newly generated.
- In responders, median recurrence-free survival was not reached at 18 months. In non-responders, it was ~13 months.
- Three-year follow-up presented in 2024–2025: vaccine-induced T cells persisted up to 3 years in responders. Responder patients had substantially longer recurrence-free survival.
- Single-cell TCR sequencing tracked individual T-cell clones — some expanded >10,000-fold.
- One responder developed a liver lesion that regressed concurrent with infiltration of vaccine-induced T cells, demonstrating in-human tumor recognition.

**Why it's important.** PDAC has low TMB — but each tumor still carries ~10–50 high-quality neoantigens if you look. The trial proved that even in a "cold" tumor, you can induce a strong, durable, tumor-specific T-cell response *if* you (a) pick the right antigens, (b) deliver them in mRNA/LNP with TLR-stimulating adjuvant biology, and (c) combine with checkpoint blockade.

**The randomized Phase 2** is ongoing. Topline data are expected to determine whether autogene cevumeran becomes the first effective vaccine for PDAC.

**Bottleneck: neoantigen prediction.** Current pipelines (NetMHCpan, MHCflurry, BigMHC, etc.) miss many true neoantigens and yield many false positives. The bottleneck is largely computational. **[A]**

---

## 6. KRAS Vaccines — ELI-002 and Others

KRAS is the holy grail of PDAC antigens: present in ~90% of tumors, clonal, truncal, and shared across patients with the same mutation. The challenge has always been that mutant KRAS peptides bind most HLA alleles poorly.

**ELI-002 (Elicio Therapeutics).** ELI-002 uses an "amphiphile" platform: a hydrophilic peptide antigen linked to a lipid tail that binds albumin and traffics to lymph nodes, dramatically improving cross-presentation. The 7-peptide version (**ELI-002 7P**) covers G12D, G12V, G12R, G12A, G12C, G12S, and G13D — the seven most common KRAS mutations, covering ~90% of PDAC. The vaccine is coupled with **ELI-004**, an amphiphile-modified CpG oligonucleotide adjuvant (TLR9 agonist).

**AMPLIFY-201 (Phase 1) and AMPLIFY-7P (Phase 1/2).**
- 99% of evaluable patients (89/90) developed mKRAS-specific T-cell responses with a mean **145-fold increase** over baseline.
- 85% showed combined CD4+ and CD8+ responses.
- 86% of target antigens elicited responses.
- Patients are minimal-residual-disease-positive post-resection or post-adjuvant chemo (CA19-9 elevated or ctDNA positive).
- Updated Nature Medicine 2024 paper showed correlation between T-cell response magnitude and recurrence-free survival.
- Independent Data Monitoring Committee in 2025 recommended Phase 2 continue unchanged; event-driven DFS readout anticipated Q4 2025.

**Other KRAS efforts.**
- The NCI Surgery Branch and Johns Hopkins have run KRAS long-peptide vaccines for years with adjuvants such as poly-ICLC; multiple Phase I trials reported durable T-cell responses with hints of clinical benefit.
- Targovax's TG01 (KRAS peptide mix) showed positive Phase I/II signals but the program has had mixed development.
- A growing list of biotechs are working on KRAS mRNA, dendritic-cell, and viral-vector vaccines.

---

## 7. CAR-T Cell Therapy in PDAC

CAR-T transformed B-cell malignancies but has struggled in solid tumors generally and PDAC specifically. The reasons mirror the immune-cold story: trafficking, persistence, target heterogeneity, and the immunosuppressive TME. Still, every major solid-tumor target has been (or will be) tried in PDAC.

### Major PDAC CAR-T constructs

| Target | Construct / sponsor | Trial | Status | Key finding |
|---|---|---|---|---|
| **Mesothelin** | Multiple (Penn, MSK, others) | Phase I IV and intratumoral | Tolerable but limited efficacy; best outcome usually stable disease | Antigen loss, exhaustion, TME suppression all observed |
| **Mesothelin + oncolytic virus** | Preclinical / early clinical | OncHSV boosts MSLN expression | Active research | Combination strategy to overcome heterogeneity |
| **Claudin 18.2** | Satricabtagene autoleucel (CT041, CARsgen) | CT041-ST-05 (PDAC adjuvant) Phase 1b; CT041-ST-01 (gastric) Phase 2 positive | World's first proof-of-concept for adjuvant CAR-T in solid tumors. 5/6 PDAC patients had significant CA19-9 decreases at ESMO 2025 | Most promising solid-tumor CAR-T data to date |
| **CEA** | CARTHA, Adaptimmune | Multiple Phase I | Tolerable; modest activity; ongoing | CEA is widely expressed including normal colon |
| **HER2** | Various | Phase I | Limited activity; toxicity concerns | HER2 is variable in PDAC |
| **EGFR** | Various | Phase I | Limited activity | EGFR widely expressed normally |
| **MUC1** | Various | Phase I | Limited | Heterogeneous, glycosylation-dependent |
| **PSCA** | Several | Phase I | Investigational | Prostate-stem-cell antigen expressed in PDAC |
| **FAP** (stromal) | CRI-supported program | Preclinical/early clinical | Targets stroma rather than tumor | Conceptually interesting; toxicity concerns in mouse |
| **TAG-72** | Several | Phase I | Investigational | Glycoprotein |
| **Multi-antigen / logic-gated** | Synthetic biology programs | Preclinical | Active research area | AND/OR gates to mitigate antigen heterogeneity |

**Key insight: claudin 18.2 is the breakout target.** CLDN18.2 is a tight-junction protein normally expressed only in differentiated gastric mucosa. It's aberrantly accessible on the cell surface in PDAC and gastric tumors. CT041 has now demonstrated:
- Significant PFS improvement in gastric/GEJ cancer (Phase 2 in The Lancet, 2025).
- First-ever positive adjuvant CAR-T signal in solid tumors (PDAC, ESMO 2025).

**Mesothelin CAR-T resistance dissection.** Recent Cell Reports Medicine work has dissected the molecular and clinical reasons mesothelin CAR-T fails in PDAC: antigen heterogeneity, soluble mesothelin sink, T-cell exhaustion driven by chronic antigen exposure, and TME suppression. Solutions being explored: armored CARs (IL-15, IL-18 secretion), CRISPR-edited CARs (PD-1 knockout, TGF-β receptor decoy), and CAR-NK / CAR-NKT alternatives.

---

## 8. TCR-T Therapy and the Landmark KRAS G12D NEJM Case

TCR-T differs from CAR-T in a crucial way: a CAR recognizes surface proteins as antibodies do; a TCR recognizes peptide-MHC complexes. That means TCR-T can target *intracellular* proteins, including driver oncogenes — which is exactly what KRAS is.

**The landmark case (Leidner, Rosenberg et al., NEJM June 2022).** Providence Cancer Institute, with Steve Rosenberg's NCI Surgery Branch lab. A 71-year-old woman with progressive metastatic PDAC bearing KRAS G12D and HLA-C*08:02 received a single infusion of **16.2 × 10⁹ autologous T cells engineered to express two HLA-C*08:02–restricted TCRs targeting the KRAS G12D 9-mer peptide GADGVGKSA**. The TCRs had been originally cloned from a long-surviving colorectal-cancer patient. Results:
- **72% partial response** by RECIST 1.1 at 6 months — visceral lung metastases regressed.
- Engineered T cells comprised >2% of all peripheral-blood T cells at 6 months — durable engraftment.
- Response ongoing at the time of publication.

This was the first clear demonstration that a TCR-engineered cell could attack a mutated oncogene in a solid tumor and produce a major objective response in metastatic PDAC. It electrified the field.

**Subsequent developments.**
- The same group has been treating additional patients across multiple HLA / KRAS-mutation combinations.
- Several biotech companies (Affini-T, T-knife, IMA-401, Tmunity, others) are developing off-the-shelf TCR-T against various KRAS mutations and HLA alleles.
- The principal bottleneck: **TCR discovery is HLA-restricted**, so each HLA + KRAS mutation combination needs its own TCR. There are perhaps 30 clinically-relevant HLA × KRAS pairs. Building this library is now a major industry effort.
- KRAS G12V TCRs have been clinically tested and show activity in some patients.
- **Mesothelin TCR-T** (FH-TCR-T-MSLN, NCT04809766) is in trial for metastatic PDAC, an alternative MHC-restricted approach.

**Why this matters for the field.** A single highly potent TCR for the most-shared oncogenic mutation in PDAC, in a patient on no other therapy, produced a real response. This is a proof of biology: PDAC *is* targetable by adoptive cell therapy *if* the target is right and the cells are functional.

---

## 9. TIL Therapy

Tumor-infiltrating lymphocyte therapy expands lymphocytes harvested from a patient's tumor ex vivo and reinfuses them after lymphodepletion. **Lifileucel (Amtagvi, Iovance)** received FDA accelerated approval in February 2024 for advanced melanoma after checkpoint failure (ORR 31.5–35%). The natural question: does it work in PDAC?

**The challenge.** PDAC tumors have so few TILs that harvesting enough is technically difficult. Even when expanded, the dominant TIL specificities may be against viral or irrelevant antigens, not tumor neoantigens. The PDAC TME also induces severe exhaustion, meaning expanded cells may be functionally weak.

**Adaptations under investigation.**
- **Neoantigen-selected TIL** — expanding only the subset of TILs reactive to predicted tumor neoantigens, pioneered at NCI. Several patients with cholangiocarcinoma and other GI cancers have had striking responses; PDAC application is ongoing.
- **TIL + checkpoint** — Iovance and others are testing combinations.
- **Engineered TIL** — adding cytokine support genes (IL-12, IL-15), PD-1 knockout, or other engineering to enhance persistence and function.
- **TIL from non-tumor tissue** — for example, sentinel lymph node TIL where tumor TIL is sparse.

To date no PDAC-specific TIL therapy is approved; this remains an early-stage approach.

---

## 10. Bispecific Antibodies and ADCs

### Bispecific T-cell engagers (BiTEs)

BiTEs link CD3 on T cells to a tumor surface antigen, forcing local T-cell activation regardless of TCR specificity. Off-the-shelf, simpler to manufacture than cell therapy.

| Bispecific | Target | Stage | Notes |
|---|---|---|---|
| **ASP2138** (Astellas) | CLDN18.2 × CD3 | Phase 1/1b in PDAC and gastric (NCT05365581) | One of few CD3 bispecifics actively trialing in PDAC |
| **MUC16 × CD3** | MUC16 (CA-125) × CD3 | Phase I (ovarian, PDAC) | Multiple programs |
| **HER2 × CD3** | HER2 × CD3 | Phase I across HER2+ tumors | PDAC subset variable |
| **B7-H3 × CD3** | B7-H3 × CD3 | Early Phase I | B7-H3 is widely expressed in PDAC |
| **Mesothelin × CD3** | MSLN × CD3 | Phase I | Soluble mesothelin sink remains an issue |
| **Claudin 6 × CD3** | CLDN6 × CD3 | Phase I (multiple solids) | Embryonic antigen |

### Antibody-drug conjugates (ADCs)

ADCs deliver cytotoxic payloads (auristatins, maytansinoids, topoisomerase inhibitors, etc.) to antigen-positive cells. Notable PDAC-relevant programs:

| ADC | Target / payload | PDAC stage | Notes |
|---|---|---|---|
| **Trastuzumab deruxtecan (T-DXd / Enhertu)** | HER2 / DXd (topo-I inhibitor) | Tissue-agnostic FDA approval (HER2 IHC 3+) covers PDAC on paper, **but DESTINY-PanTumor02 PDAC cohort was closed for futility (0 ORR in first 15 patients, 25 enrolled total)** | Strong across other solids; clinical reality in PDAC has been null so far |
| **Anetumab ravtansine** | Mesothelin / DM4 | Phase II in MSLN+ PDAC; modest activity | Bystander effect helps with antigen heterogeneity |
| **Mirvetuximab soravtansine** | Folate-receptor α / DM4 | Approved in ovarian; PDAC investigational | FR-α expressed in subset of PDAC |
| **DS-7300 / ifinatamab deruxtecan** | B7-H3 / DXd | Phase I/II across tumors including PDAC | B7-H3 broadly expressed in PDAC |
| **Datopotamab deruxtecan / Dato-DXd** | TROP2 / DXd | Phase I/II in multiple solids; PDAC subset | TROP2 highly expressed in >50% of PDAC |
| **PT886 (spevatamig, Phanes)** | Claudin 18.2 × CD47 **bispecific** (NOT an ADC — no cytotoxic payload) | FDA Fast Track for CLDN18.2+ metastatic PDAC | Misclassified in this row historically; mechanism is dual-engagement of CLDN18.2-expressing tumor cells and CD47 phagocytosis-checkpoint blockade |
| **Upifitamab rilsodotin** | NaPi2B / SC209 (auristatin) | Mostly ovarian; PDAC exploratory | Sodium-phosphate transporter |

The ADC field is exploding. Even when the payload itself is the main effector (the antibody acting as a homing device), good targeting + potent payload can produce activity that pure immune mechanisms cannot.

---

## 11. Oncolytic Viruses

Oncolytic viruses (OVs) selectively replicate in cancer cells, causing immunogenic cell death that releases tumor antigens and pro-inflammatory danger signals — in effect, an in-situ vaccine that may turn cold tumors hot.

| Virus | Platform | PDAC trials | Status |
|---|---|---|---|
| **T-VEC (talimogene laherparepvec)** | HSV-1 expressing GM-CSF | Approved in melanoma; investigational in PDAC | Intratumoral injection challenging in PDAC |
| **Pelareorep (Reolysin)** | Wild-type reovirus | GOBLET Phase I/II + chemo + atezolizumab | **GOBLET Cohort 1: 62% ORR in n=13 evaluable first-line metastatic PDAC patients (later updates: 69% ORR). Phase 3 trial design aligned with FDA in 2025; trial launch H1 2026 (NOT yet "Phase 3 cleared" / not yet enrolling at audit time).** |
| **VCN-01** | Modified adenovirus expressing PH20 hyaluronidase | Phase I + gem/nab-pac | Designed to digest PDAC stroma; promising signals |
| **Pexa-Vec (JX-594)** | Vaccinia expressing GM-CSF | Various tumors; PDAC adjunct | Mixed results across indications |
| **CG0070, ONCR-177, others** | Various | Multiple oncology programs | PDAC exploratory |

**Pelareorep is the breakout — with caveats.** Reovirus IV-infused with chemo and checkpoint produced ORR roughly **3× historical benchmark** in GOBLET Cohort 1 (n=13 evaluable, first-line metastatic PDAC). The mechanism is multi-modal: direct oncolysis where the virus replicates, plus systemic Type-I interferon induction, plus T-cell priming. **FDA aligned on Phase 3 trial design with Oncolytics in 2025; the Phase 3 trial launch is H1 2026** — calling it "Phase 3 cleared" overstated the regulatory status at audit time. Small evaluable-N (n=13) means the headline ORR has wide confidence intervals. **Promising but unconfirmed at the scale needed for a regulatory or clinical decision.**

---

## 12. Combination Immunotherapy Strategies

Given that PDAC's immune-cold state is multi-axis, the field has converged on **combinations** as the only realistic path. The major strategies:

**12.1 Chemo + checkpoint + vaccine.** Chemo (especially FOLFIRINOX) causes immunogenic cell death, releasing neoantigens; vaccine focuses the immune system; checkpoint blockade prevents exhaustion. This is the autogene cevumeran approach.

**12.2 Chemo + CAR-T.** Lymphodepleting chemo enables CAR-T engraftment; subsequent chemo may reduce tumor burden and antigen heterogeneity. CT041 + chemo combinations are emerging.

**12.3 Stromal disruption + immunotherapy.** Strategies:
- **Hyaluronidase (PEGPH20)** — depletes hyaluronan to drop interstitial pressure. Phase III HALO-301 in PDAC failed; toxicity also problematic. Now being revisited with selective patient enrichment.
- **FAK inhibitors (defactinib)** — reprogram stroma to permit T-cell infiltration; tested with pembrolizumab and gemcitabine; phase II ongoing.
- **FAP-targeted CAR-T or BiTE** — deplete CAFs.
- **CXCR4 inhibition (plerixafor, motixafortide)** — relieves CXCL12 sequestration of T cells; combined with checkpoint in pilot trials.

**12.4 Radiation + immunotherapy.** Stereotactic body radiation therapy (SBRT) plus checkpoint and/or vaccine: aimed at inducing the **abscopal effect** where local irradiation provokes systemic immunity. Multiple Phase I/II trials at MD Anderson, Hopkins, Penn. Signals are modest but real; the optimal dose and fractionation remain undefined.

**12.5 CD40 agonists.** APX005M (sotigalimab), selicrelumab, and others activate antigen-presenting cells, especially DCs, driving systemic priming. In the PRINCE / OPTIMIZE-1 trials at Penn (Vonderheide), CD40 agonist + chemo + checkpoint produced encouraging early signals — though randomized data have been mixed.

**12.6 Treg depletion.**
- **Anti-CCR8** — CCR8 is highly enriched on tumor-infiltrating Tregs and absent on peripheral Tregs, enabling selective depletion. Multiple programs (BMS, Pfizer, others) in Phase I.
- **Low-dose anti-CD25 (anti-IL2Rα)** — depletes Tregs while sparing effector cells. New constructs avoid effector-cell suppression.
- **Anti-CTLA-4 (low dose, intratumoral, or Fc-engineered)** — leveraging CTLA-4's Treg expression for ADCC-based Treg depletion rather than checkpoint blockade per se.

**12.7 Macrophage reprogramming.**
- **CSF1R inhibitors** (cabiralizumab, pexidartinib) — deplete TAMs.
- **CD40 agonists** — repolarize M2 to M1.
- **CCR2/5 inhibitors** — block monocyte recruitment.

**12.8 Microbiome modulation.** Long-term PDAC survivors carry distinct gut and intratumoral microbiota. Stool transplant and selected bacterial cocktails (e.g., Saccharopolyspora, Pseudoxanthomonas) are in early clinical study to enhance immunotherapy response.

---

## 13. Why Combinations Might Finally Crack PDAC's Immune Cold

The narrative arc of the last decade in PDAC immunotherapy can be summarized:

1. **Single-agent monoclonal checkpoint blockade failed** — because there was no T-cell engine to release.
2. **Single-target vaccines failed** — because off-the-shelf antigens like MUC1, telomerase, and tumor-cell lysates produced weak, narrow responses.
3. **Single-target CAR-T struggled** — because of antigen heterogeneity, exclusion, and exhaustion.

What is finally working — or showing real signal — has three properties:
- **Builds the T cells from scratch** (personalized neoantigen mRNA, KRAS amphiphile, TCR-T) rather than assuming they exist.
- **Combines T-cell generation with TME disruption** (chemo, CD40, radiation, OV, stromal agents).
- **Sustains the response with checkpoint blockade** rather than relying on checkpoint alone.

The autogene cevumeran result is paradigm-shifting because it proves that PDAC can be made immunogenic. The KRAS G12D TCR-T case proves that a well-engineered cell can attack PDAC. Pelareorep proves that oncolytic immune priming works in PDAC. ELI-002 proves that targeting KRAS with the right adjuvant can break tolerance.

Each of these individually produces a survival benefit measured in months, not years. But these are largely Phase 1/2 monotherapies in patient subsets. The combinations — **mRNA neoantigen vaccine + KRAS amphiphile + OV + checkpoint + chemo** in a rationally designed staircase — have not been tested. They are likely where the eventual wins will be.

This is also where the field's main remaining barriers are computational: predicting neoantigens, designing optimal HLA-presenting TCRs, modeling combination kinetics, choosing which combinations to test among an exponentially large search space.

---

## 14. Where Compute Could Help — `[A]` Items

PDAC immunotherapy is gated as much by computational and modeling problems as by laboratory ones. A volunteer-computing project can move several of these.

**[A1] Personalized neoantigen prediction.** Current pipelines (NetMHCpan-4.1, MHCflurry-2.0, BigMHC, NetCleave, NetChop) miss real neoantigens and call too many false positives. Better tools that combine MHC binding, TAP transport, proteasome cleavage, TCR-affinity prediction, and clonality scoring would directly improve vaccines like autogene cevumeran. **Distributed compute**: run large MHC ligandome retraining campaigns with new immunopeptidomics datasets; ensemble multiple predictors per patient; full MD of peptide-MHC complexes for top candidates.

**[A2] KRAS-mutation peptide-MHC binding atlas.** A complete atlas across all common HLA alleles × all KRAS mutation peptides × all post-translational variants × all length variants would tell us which HLA × mutation pairs are tractable for vaccines and TCR-T. This is computationally tractable today but no one has done it at scale with full molecular dynamics validation. **Distributed compute**: GROMACS / AMBER MD of every relevant pMHC complex; ML training data for next-gen predictors.

**[A3] TCR-pMHC affinity and specificity prediction.** Engineering the next KRAS G12D TCR — or thousands of them for the full HLA × KRAS combinatorial space — requires being able to model TCR-pMHC interactions in silico. Current tools (TCRdock, TCRen, ImmuneBuilder/ABodyBuilder) are improving but limited. **Distributed compute**: massive TCR-pMHC docking and MD refinement; cross-reactivity screening to avoid on-target/off-tumor toxicity.

**[A4] Combination simulation.** With ~50 modalities (vaccines, OVs, ADCs, CAR-Ts, checkpoints, stromal agents, radiation schedules, chemo regimens), the combination space is >10⁶ even ignoring dose and sequence. Quantitative systems pharmacology (QSP) and agent-based TME models — calibrated to single-cell and spatial transcriptomic data from real PDAC trials — could prioritize the top 20–50 combinations to test clinically. **Distributed compute**: parameter-sweep ABMs of TME dynamics under combinations; Bayesian model averaging over plausible mechanisms.

**[A5] HLA loss / antigen escape modeling.** PDAC frequently loses HLA. Predicting which patients will escape vaccines and which residual HLAs can still present neoantigens would change patient selection. **Distributed compute**: pan-cancer HLA-LOH-aware neoantigen pipelines.

**[A6] Stromal MD and drug discovery.** The PDAC stroma is rich with structured hyaluronan, FAP, and other targets. MD simulations of hyaluronidase-substrate complexes, of FAP-inhibitor binding, of CXCR4 antagonist docking would accelerate next-gen stromal agents. **Distributed compute**: Folding@home-style MD on stromal protein targets.

**[A7] Oncolytic-virus host-range engineering.** Designing tumor-selective viral capsids and immune-evasive but tumor-replicative viruses requires evolutionary and structural modeling. **Distributed compute**: directed-evolution screens in silico for capsid variants.

**[A8] Single-cell + spatial transcriptomics integration.** Existing PDAC datasets (Peng et al. Nature 2019, Steele Nature Cancer 2020, Hwang Nature Genetics 2022, Lin Nature 2024) have thousands of patient samples but are not jointly modeled. A community-scale federated analysis with consistent gene programs, immune deconvolution, and clinical annotation linkage would yield biomarkers for who responds. **Distributed compute**: large-scale dimensionality reduction, transfer learning across atlases.

**[A9] T-cell repertoire mining.** Mining bulk and single-cell TCR datasets for cross-reactive, KRAS-specific, mesothelin-specific, or neoantigen-specific TCRs — and predicting their HLA restriction — would dramatically accelerate adoptive cell therapy. **Distributed compute**: large-scale TCR similarity graphs (GLIPH, TCRMatch extensions); GNN-based TCR-pMHC prediction at population scale.

**[A10] Patient-similarity / N-of-1 trial design.** Given small PDAC trial numbers, computational matching of patients to optimal regimens via causal-inference and synthetic-control methods could squeeze more signal per trial. **Distributed compute**: massive bootstrap and matching procedures.

**Top three (highest leverage):**
1. **[A1] Personalized neoantigen prediction** — direct, immediate impact on autogene-cevumeran-style vaccines.
2. **[A3] TCR-pMHC modeling for KRAS** — enables off-the-shelf KRAS TCR-T at population scale.
3. **[A4] Combination simulation** — chooses which trials to run among an intractable search space.

---

## 15. Sources

- [Stanford Pancreatic Cancer Research](https://med.stanford.edu/cancer/about/news/pancreatic.html) — Stanford Cancer Institute (Longaker, Delitto)
- [Cancer Research Institute — Pancreatic Cancer Immunotherapy](https://www.cancerresearch.org/immunotherapy-by-cancer-type/pancreatic-cancer)
- [CRI Anna-Maria Kellen Clinical Accelerator](https://www.cancerresearch.org/clinical-accelerator)
- [CRI Pancreatic Cancer Blog — How Immunotherapy Targets Pancreatic Cancer](https://www.cancerresearch.org/blog/breaking-barriers-how-immunotherapy-targets-pancreatic-cancer)
- [CRI Pancreatic Cancer "Silent Killer" — taking on PDAC](https://www.cancerresearch.org/blog/how-cri-is-taking-on-pancreatic-cancer-the-silent-killer)
- [Engleman Lab, Stanford Medicine](https://med.stanford.edu/englemanlab.html)
- [Rojas et al., Nature 2023 — Personalized RNA neoantigen vaccines (autogene cevumeran)](https://www.nature.com/articles/s41586-023-06063-y)
- [MSKCC press release — Phase 1 update, durable response](https://www.mskcc.org/news-releases/new-phase-1-data-from-mskcc-shows-investigational-cancer-vaccine-may-elicit-lasting-immune-response-in-patients-with-pancreatic)
- [BioNTech 3-year follow-up data — autogene cevumeran](https://investors.biontech.de/news-releases/news-release-details/three-year-phase-1-follow-data-mrna-based-individualized)
- [MSKCC follow-up article on pancreatic cancer mRNA vaccine](https://www.mskcc.org/news/can-mrna-vaccines-fight-pancreatic-cancer-msk-clinical-researchers-are-trying-find-out)
- [Elicio — ELI-002 7P 99% T-cell response data](https://elicio.com/press_releases/elicio-therapeutics-reports-eli-002-7p-achieved-robust-mkras-specific-t-cell-responses-in-99-of-evaluable-patients-in-ongoing-phase-2-amplify-7p-trial/)
- [Elicio — Nature Medicine AMPLIFY-201 follow-up](https://elicio.com/press_releases/elicio-therapeutics-announces-publication-of-eli-002-updated-amplify-201-phase-1-follow-up-data-in-nature-medicine-for-minimal-residual-disease-mrd-positive-adjuvant-stage-patient/)
- [Elicio AMPLIFY-7P IDMC positive recommendation](https://elicio.com/press_releases/elicio-therapeutics-announces-positive-recommendation-by-idmc-to-continue-eli-002-7p-randomized-phase-2-study-in-pancreatic-cancer-without-modifications-to-final-analysis/)
- [AMPLIFY-7P clinical trial JCO abstract](https://ascopubs.org/doi/10.1200/JCO.2024.42.16_suppl.2636)
- [Leidner et al., NEJM 2022 — TCR gene therapy KRAS G12D in pancreatic cancer](https://www.nejm.org/doi/10.1056/NEJMoa2119662)
- [Tran et al., NEJM 2016 — T-cell transfer therapy targeting mutant KRAS](https://www.nejm.org/doi/full/10.1056/NEJMoa1609279)
- [Wang et al., therapeutic high-affinity TCR for KRAS G12D neoantigen](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9464187/)
- [Satricabtagene autoleucel ESMO 2025 PDAC adjuvant results](https://www.prnewswire.com/news-releases/carsgen-presents-preliminary-results-on-satri-cel-for-adjuvant-therapy-of-pancreatic-cancer-at-esmo-congress-2025-302587311.html)
- [Satri-cel Phase 2 gastric/GEJ — The Lancet 2025](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(25)00860-8/abstract)
- [CT041 (satricabtagene autoleucel) trial NCT04581473](https://clinicaltrials.gov/study/NCT04581473)
- [Clinical and molecular dissection of CAR-T resistance in pancreatic cancer — Cell Reports Medicine 2025](https://www.cell.com/cell-reports-medicine/fulltext/S2666-3791(25)00374-X)
- [Mesothelin CAR-T + oncolytic HSV boosting](https://pubmed.ncbi.nlm.nih.gov/40366419/)
- [Allogeneic CAR-NKT cells targeting mesothelin in PDAC — PNAS 2025](https://www.pnas.org/doi/10.1073/pnas.2517786122)
- [Mesothelin TCR-T trial NCT04809766](https://clinicaltrials.gov/study/NCT04809766)
- [Mesothelin-targeted CAR-T neoadjuvant feasibility trial](https://clinicaltrials.gov/study/NCT06054308)
- [Frontiers in Immunology 2023 — PDAC immunosuppressive features in TME](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2023.1258538/full)
- [Frontiers in Immunology 2025 — PDAC immunosuppressive TME mechanisms](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2025.1582305/full)
- [Frontiers in Immunology 2024 — PDAC TME as therapeutic target](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2024.1287459/full)
- [The TIM in PDAC — neither hot nor cold review](https://pmc.ncbi.nlm.nih.gov/articles/PMC9454892/)
- [Evaluation of Cy/GVAX + CRS-207 ± nivolumab (Clin Cancer Res 2020)](https://dx.doi.org/10.1158/1078-0432.CCR-19-3978)
- [ECLIPSE study — GVAX + CRS-207 vs chemo Phase IIb](https://pubmed.ncbi.nlm.nih.gov/31126960/)
- [Algenpantucel-L IMPRESS Phase 3 failure (AJMC)](https://www.ajmc.com/view/newlinks-pancreatic-cancer-vaccine-fails-to-improve-survival-in-phase-3)
- [Pelareorep GOBLET pancreatic cancer data 2025 — Oncolytics](https://www.ainvest.com/news/oncolytics-biotech-pelareorep-breakthrough-pancreatic-cancer-buy-signal-investors-2505/)
- [Oncolytic virus therapy 2025 review](https://www.labiotech.eu/in-depth/oncolytic-virus-therapy-cancer-2025/)
- [Pelareorep + pembrolizumab + chemo Phase Ib (Clin Cancer Res 2020)](https://clincancerres.aacrjournals.org/content/26/1/71)
- [Pancreatic OV clinical trial landscape 2025 review](https://pmc.ncbi.nlm.nih.gov/articles/PMC12430829/)
- [Lifileucel (Amtagvi) FDA approval editorial](https://pmc.ncbi.nlm.nih.gov/articles/PMC11071689/)
- [Advancing immunotherapy in PDAC — emerging adoptive cell therapies 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11853216/)
- [Astellas GLEAM trial zolbetuximab PDAC negative readout](https://newsroom.astellas.com/2025-10-13-Astellas-Confirms-Phase-2-GLEAM-Trial-Did-Not-Meet-Primary-Endpoint-of-Overall-Survival-in-Patients-with-Metastatic-Pancreatic-Cancer)
- [PT886 FDA Fast Track CLDN18.2+ PDAC (OncLive)](https://www.onclive.com/view/fda-grants-fast-track-status-to-pt886-for-metastatic-claudin-18-2-pancreatic-adenocarcinoma)
- [Claudin 18.2 expression concordance in PDAC — bioRxiv 2025](https://www.biorxiv.org/content/10.1101/2025.04.11.648482.full.pdf)
- [CLDN18.2-targeted therapy in GI cancers review (MDPI 2025)](https://www.mdpi.com/2072-6694/17/23/3764)
- [Anetumab ravtansine Phase II in mesothelin-expressing PDAC (NCT03023722)](https://ichgcp.net/clinical-trials-registry/NCT03023722)
- [TROP2-directed nanobody-drug conjugate in PDAC (J Nanobiotech 2023)](https://jnanobiotechnology.biomedcentral.com/articles/10.1186/s12951-023-02183-9)
- [B7-H3 in pancreatic cancer review (World J Gastroenterol 2024)](https://www.wjgnet.com/1007-9327/full/v30/i31/3654.htm)
- [CCR2 + FOLFIRINOX Phase Ib PDAC (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5407285/)
- [Targeting CCR2+ macrophages after IRE in PDAC (Science Advances 2025)](https://www.science.org/doi/10.1126/sciadv.adw2937)
- [Pembrolizumab high-TMB PDAC case series](https://pmc.ncbi.nlm.nih.gov/articles/PMC9119368/)
- [Stromal reprogramming by FAK inhibition + radiation + checkpoint (Cancer Discovery 2022)](https://aacrjournals.org/cancerdiscovery/article-abstract/12/12/2774/711197/Stromal-Reprogramming-by-FAK-Inhibition-Overcomes)
- [Anti-CTLA-4 + radiation abscopal effect in PDAC model](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9101709/)
- [Irreversible electroporation reverses checkpoint resistance in PDAC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6385305/)
- [Personalized medicine in PDAC — mRNA vaccines review (PMC 2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11879674/)
- [Oncology Times — Personalized mRNA in PDAC 2025](https://journals.lww.com/oncology-times/fulltext/2025/08000/revolutionizing_pancreatic_cancer_with.1.aspx)
- [Reprogramming immunosuppressive niches with neoantigen mRNA + nanocarrier (PMC 2025)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12874651/)
- [Adoptive cell therapy for cancer — combination strategies and biomarkers (Frontiers 2025)](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2025.1603792/full)
- [Engineered immune cell therapies for solid tumors (Frontiers Pharmacol 2025)](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2025.1614325/full)
- [Targeting OAS3 reverses M2 infiltration and restores anti-tumor immunity in PDAC (medRxiv 2024 — Engleman group context)](https://www.medrxiv.org/content/10.1101/2024.08.07.24311609.full.pdf)
- [SUMOylation and CD155/TIGIT immunomodulation in PDAC (bioRxiv 2025)](https://www.biorxiv.org/content/10.1101/2025.02.06.636475.full.pdf)
- [JCI Insight — More T-cell receptors to the RAScue in cancer](https://www.jci.org/articles/view/184782)
- [KRAS G12D targeted therapies in PDAC review (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9749787/)
- [Cancer Network — ELI-002 7P CancerNetwork coverage](https://www.cancernetwork.com/view/eli-002-7p-elicits-robust-t-cell-responses-in-kras-pancreatic-cancer)
- [Honcology — Personalized vaccine development in PDAC](https://honcology.com/blog/advances-in-personalized-vaccine-development-for-pancreatic-cancer)
