# Pancreatic Cancer Research Models — A Deep Reference

> File: `PROJECT/16_research_models.md`
> Audience: contributors to a self-funded, volunteer-computing project aimed at a cure for pancreatic ductal adenocarcinoma (PDAC).
> Companion file: `PROJECT/17_computational_methods.md`.

## 1. The Model Hierarchy — A One-Paragraph Framing

Pancreatic ductal adenocarcinoma (PDAC) is one of the most difficult cancers to model in the laboratory because the tumor is defined as much by its stromal/immune ecosystem as by its epithelial cells. Researchers therefore use a *stack* of complementary systems, climbing from simplest to most physiological: (1) **2D cell lines** for fast, cheap, mechanistic experiments; (2) **patient-derived organoids (PDOs)** for personalized drug screening that retains 3D architecture and patient-specific genetics; (3) **co-culture and organ-on-chip** systems that add cancer-associated fibroblasts (CAFs), stellate cells, endothelium and immune cells; (4) **xenografts** (CDX, PDX, orthotopic, humanized) for in vivo pharmacology in an immunodeficient or partly reconstituted host; (5) **genetically engineered mouse models (GEMMs)** like KPC for full immunocompetent tumor evolution; (6) **zebrafish larval xenografts** for fast, low-cost in vivo screening; (7) **in silico / computational models** that integrate genomics, transcriptomics, structural biology and pharmacology to triage hypotheses before any wet experiment. The Pancreatic Cancer Action Network (PanCAN) groups these into the three classical buckets — cell lines, xenografts, GEMMs — but modern PDAC research adds organoids, microphysiological systems and computational atlases on top. The compute angles for a distributed volunteer network sit largely in the in silico layer, but with concrete experimental anchors at every level.

---

## 2. 2D Cell Lines

2D pancreatic cancer cell lines remain the workhorse of mechanistic and high-throughput pharmacological PDAC research because they are immortal, cheap, easy to engineer, and supported by decades of profiling data (mutations, transcriptomes, drug responses, CRISPR fitness scores). The most-used lines are listed below with the four canonical PDAC drivers (KRAS, TP53, CDKN2A, SMAD4 — the "big four") and the key practical notes.

### 2.1 Cell-line reference table

| Line | Origin | KRAS | TP53 | CDKN2A | SMAD4 | Doubling | In-vivo tumorigenic? | Source | Notes |
|------|--------|------|------|--------|-------|----------|----------------------|--------|-------|
| **Panc-1** | Primary PDAC, 56F duct head, 1975 | G12D | R273H | Homozygous deletion | WT | ~52 h | Yes (nude SC) | ATCC CRL-1469 | Most-used PDAC line; mesenchymal-like; KRAS-dependent |
| **MIA PaCa-2** | Primary PDAC, 65M body/tail | G12C | R248W | Homozygous deletion | WT | ~40 h | Yes (nude SC) | ATCC CRL-1420 | Poorly differentiated; KRAS-G12C → benchtop sotorasib/adagrasib substrate |
| **BxPC-3** | Primary PDAC, 61F body | **WT** | Y220C | Homozygous deletion | Homozygous deletion | ~48–60 h | Yes (SCID/nude SC) | ATCC CRL-1687 | Rare *KRAS-WT* PDAC line; useful as KRAS-independent control |
| **Capan-1** | Liver metastasis, 40M | G12V | A159V | Homozygous deletion | Homozygous deletion | ~96 h | Yes | ATCC HTB-79 | BRCA2 frameshift — sensitive to PARP inhibitors; well-differentiated |
| **Capan-2** | Primary PDAC, 56M | G12V | WT | WT (silenced) | WT | ~96 h | Yes | ATCC HTB-80 | "Most TP53-like-WT" line; well-differentiated; elevated EGFR |
| **AsPC-1** | Ascites, 62F | G12D | C135fs/null | Frameshift (not deletion) | **R100T homozygous missense** (protein expressed but inactivated; NOT a deletion) | ~40 h | Yes | ATCC CRL-1682 | Metastatic-derived; FBXW7 R465C; aggressive in mice |
| **HPAF-II** | Ascites, 44M | G12D | P151S | In-frame deletion (exon2) | Homozygous deletion | ~30 h | Yes | ATCC CRL-1997 | Well-differentiated, forms tight epithelial clusters |
| **SW1990** | Spleen metastasis, 56M | G12D | WT | Homozygous deletion | Homozygous deletion | ~30 h | Yes (highly invasive) | ATCC CRL-2172 | Highly resistant to gemcitabine in monolayer (highest IC50) |
| **CFPAC-1** | Liver met from cystic-fibrosis patient | G12V | C242R | Methylated (WT seq, no protein) | Homozygous deletion | ~30 h | Yes | ATCC CRL-1918 | ΔF508 *CFTR* — unique CF background |
| **PSN-1** | Primary PDAC | G12R | M214R/del | Homozygous deletion | WT | ~36 h | Yes | DSMZ ACC-87 | Less common but in DepMap; G12R substrate |
| **Hs 766T** | Lymph-node met, 46M | **Q61H homozygous** (corrected per Cellosaurus — earlier literature WT call was incorrect) | None reported (R248Q claim unsupported in Cellosaurus) | Homozygous deletion | Homozygous deletion | ~50 h | Yes | ATCC HTB-134 | NOT a KRAS-WT line; KRAS Q61H is rare in PDAC (~1%) but real. CTNNB1 S37F; cellosaurus CVCL_0334 |
| **HPDE / H6c7** | Normal pancreatic duct, immortalized E6/E7 | WT | WT (E6/E7 inactivates) | WT | WT | ~36 h | No | Kerafast / Sigma SCC442 | Standard "normal" control; HPV16 E6/E7-immortalized; near-normal genotype/phenotype |

### 2.2 Why 2D matters (and where it lies)

The 11 cancerous lines above cover the canonical PDAC mutation space — KRAS-mutant (the 93% case; including a rare KRAS Q61H avatar in Hs 766T), KRAS-WT (BxPC-3 — the ONLY true KRAS-WT line in this panel as ~7% control), TP53-mutant vs WT (Capan-2, SW1990), SMAD4-null vs intact, and a BRCA2-frameshift / PARP-sensitive avatar (Capan-1). Most lines are deposited at ATCC and several also at DSMZ; all are profiled in CCLE and DepMap (mutations + RNA + dependency map). 2D limitations: loss of the desmoplastic stroma that defines PDAC, no immune contribution, monolayer geometry that distorts drug penetration, and selection for aggressive subclones that survive plastic. 2D drug IC50s correlate poorly with patient response — gemcitabine sensitivity in monolayer is famously over-optimistic compared to in vivo or PDO data — so 2D screens require validation in 3D or in vivo. They remain the only realistic substrate for genome-wide CRISPR dependency mapping at scale.

---

## 3. Patient-Derived Organoids (PDOs)

PDOs are 3D, self-renewing miniature tumors grown from patient biopsies or resections, embedded in basement-membrane extract (Matrigel/BME) with a defined growth-factor cocktail (Wnt3a, R-spondin, Noggin, EGF, FGF10, gastrin, A83-01, nicotinamide, Y-27632 — the "WRN+" recipe). They preserve the genetic and architectural features of the source tumor over many passages, can be expanded from sub-millimeter biopsies, and can be drug-screened on a clinically relevant timescale (~3–8 weeks from biopsy to result).

### 3.1 Pioneering work and current state

- **Boj et al., *Cell* 2015 (Tuveson lab, CSHL)** — first murine and human PDAC organoid protocol; recapitulates PanIN-to-invasive progression on transplantation.
- **Tiriac et al., *Cancer Discovery* 2018** — pharmacotyping of 66 patient PDOs against standard-of-care PDAC chemotherapy; defined organoid-derived response signatures correlating with patient outcome.
- **Driehuis et al., *PNAS* 2019 / *Cell* 2019** — Hubrecht / HUB Organoids biobank of 30 PDOs, 76-drug screen, plus CRISPR drug-gene interaction mapping; demonstrated reproducible drug sensitivity profiles and identified MTA as a biomarker for PRMT5-inhibitor response.
- **Seppälä et al., 2022 — POPS / PARIS feasibility trials** — prospective trials testing whether PDO pharmacotyping can predict patient response; multidrug AUC-based clustering reached ~85% predictive accuracy for clinical outcome in early reports. As of 2025, organoid-guided trials are running in the US, EU and Japan.
- **HUB Organoid Biobank (Utrecht)** — commercial/academic distribution of well-annotated PDOs across cancer types, including PDAC, with paired germline-tumor sequencing.

### 3.2 Drug screening — predictive accuracy

For standard PDAC agents (gemcitabine, 5-FU, oxaliplatin, irinotecan, paclitaxel) PDO pharmacotyping has shown sensitivity ~70–90% and specificity ~70–85% for predicting clinical response in feasibility cohorts. Predictive accuracy for targeted agents (PARPi in BRCA-mutant, MEKi, KRAS-G12D-i) is higher when the molecular biomarker is also present. The bottleneck is time-to-result (median ~53 days from biopsy in POPS), which is improving as biopsy-to-organoid pipelines and miniaturized screening (5–20 µL droplet assays, automated imaging) mature.

### 3.3 Biobanks and access

| Biobank | Host | Size | Access |
|---------|------|------|--------|
| Tuveson Lab Organoid Bank | CSHL | >100 PDAC PDOs | Collaborative + MTAs |
| HUB Organoids | Hubrecht / commercial | hundreds across tumor types | Commercial/academic licensing |
| MD Anderson PDAC Organoid Resource | UT MD Anderson | ~70 lines | Collaborative + internal trials |
| PRECISION-Panc | UK / Glasgow consortium | growing, paired clinical | UK academic access |
| HCMI (Human Cancer Models Initiative) | NCI + Sanger + Hubrecht + Broad | >40 PDAC organoids, with WGS/RNA | Public via ATCC |

### 3.4 Limitations

PDOs are still epithelial-only by default — they lack endogenous stroma and immune cells; "take rate" varies (~60–80% for resections, lower for fine-needle biopsies); BME (Matrigel) batch variability confounds reproducibility; and current culture media may select for ductal/classical subtype over basal-like clones present in the tumor. Many of these gaps are addressed by co-culture systems (see §4) and synthetic hydrogels replacing Matrigel.

---

## 4. Co-Culture and Immune-PDO Systems

Because the PDAC microenvironment (>80% of tumor volume is stroma) is so dominant, the past 5 years have seen rapid development of **multi-component organoid systems**:

- **PDO + CAF co-culture** — pancreatic stellate cells (PSCs) or patient-matched CAFs added in Matrigel induce CAF differentiation into the inflammatory (iCAF) and myofibroblastic (myCAF) subsets first defined by Öhlund et al. 2017. Co-culture drives gemcitabine resistance in PDOs, recapitulating in-patient stromal protection.
- **PDO + autologous T cells** — Dijkstra-style protocols where CD3+ T cells from peripheral blood (PBMCs) or tumor-infiltrating lymphocytes (TILs) are co-cultured with PDOs to expand tumor-reactive clones. Reactivity is measured by IFNγ release, CD137 upregulation, and organoid killing.
- **Air-liquid interface (ALI) organoids** — Kuo lab protocol: tumor fragments rather than dissociated cells retain endogenous TILs, myeloid cells and fibroblasts for several weeks; preserves the native TME for immunotherapy testing.
- **hiPSC-derived "full PDAC organoids" (FPCOs)** — induced PSCs + endothelial cells assembled with PDAC ductal cells to form vascularized constructs with heterogeneous CAFs and ECM proteins (STAR Protocols 2024).
- **Organoid-in-matrix platforms** — engineered Matrigel/collagen blends with tunable stiffness to study T-cell killing as a function of matrix density.

These systems are the bridge between PDOs and organ-on-chip (§7), and are the substrate where immunotherapy combinations for PDAC are now triaged.

---

## 5. GEMMs — Genetically Engineered Mouse Models

GEMMs are the gold standard for *immunocompetent, autochthonous* (tumors arising in situ) PDAC modeling. They are slow and expensive but capture stromal recruitment, immune exclusion, metastasis and clonal evolution in a single integrated system.

### 5.1 The canonical models

| Name | Genotype | Driver promoter | First described | Time to PDAC | Phenotype |
|------|----------|------------------|-----------------|---------------|-----------|
| **KC** | LSL-Kras<sup>G12D/+</sup>; Pdx1-Cre | Pdx1 (pancreas) | Hingorani 2003, *Cancer Cell* | Slow — PanIN by 8–10 wk, PDAC after >1 yr in fraction | PanIN1/2/3 progression; small fraction → invasive PDAC; good model for premalignancy |
| **KPC** | LSL-Kras<sup>G12D/+</sup>; LSL-Trp53<sup>R172H/+</sup>; Pdx1-Cre | Pdx1 | Hingorani 2005, *Cancer Cell* | Rapid — invasive PDAC by ~8–10 wk; median survival ~5 mo | Faithful human-like PDAC with desmoplastic stroma, metastasis, immune exclusion; most used model in immuno-oncology |
| **KPC**<sup>flox</sup> | Kras<sup>G12D</sup>; Trp53<sup>flox/flox</sup>; Cre | various | various | Even faster, more aggressive | Conditional p53 loss rather than dominant-negative |
| **KIC** | Kras<sup>G12D</sup>; Cdkn2a<sup>flox/flox</sup>; Pdx1-Cre (or Ptf1a-Cre) | Pdx1 / Ptf1a | Aguirre 2003, *Genes Dev* | Very fast — PDAC by 6–8 wk; median survival ~7–9 wk | Highly proliferative; high metastasis; useful for combo therapy timing |
| **KPP** | Kras<sup>G12D</sup>; p53<sup>flox/flox</sup>; Pdx1-Cre | Pdx1 | Bardeesy / various | ~6–8 wk | Aggressive, common alternative to KPC for chemoprevention |
| **KPIC** | Kras<sup>G12D</sup>; Trp53<sup>R172H/+</sup>; Ink4<sup>flox/+</sup>; Ptf1/p48-Cre | Ptf1a | Qiu 2017, *PLoS One* | Median survival ~89 d (vs 62 d KIC) | Locally invasive + metastatic; rich stroma; better for therapy trials than KIC |
| **KPSC** | Kras<sup>G12D</sup>; Trp53<sup>R172H/+</sup>; Smad4<sup>flox/flox</sup>; Pdx1-Cre | Pdx1 | Bardeesy 2006 / others | Variable | SMAD4 loss adds IPMN-like cystic features, accelerated metastasis |
| **KPSEY** | KPC + Smad4 conditional + extra modifiers (e.g. EGFR or YAP variants) | Pdx1 | Various | Variable | Used for stromal/immune signaling dissection |
| **KrasFSF; FSF-Trp53; FlpO** | Dual-recombinase | Multiple | Schönhuber 2014, *Nat Med* | Variable | Allows sequential genetic events — model resistance & evolution |

### 5.2 Histology vs human disease

KPC tumors faithfully recapitulate the *desmoplastic, immune-excluded, gemcitabine-resistant* phenotype of human PDAC. Whole-genome sequencing of KPC tumors shows clonal evolution similar to human PDAC, including chromosome instability. KIC tumors lack p53 mutations and show a more uniform histology — useful for studying CDKN2A-driven progression but less faithful to advanced human PDAC. KPC remains the dominant choice for immuno-oncology preclinical testing.

### 5.3 Workflow and practical notes

Most GEMM colonies are maintained on a mixed C57BL/6 background. Tumor monitoring uses palpation, ultrasound (high-frequency US-1), or contrast-enhanced µCT/MRI. Tumors can be derived as cell lines (e.g., the KPC-derived KPC4662, KCKO and KPC-Brca1<sup>−/−</sup> lines) for syngeneic transplantation back into immunocompetent C57BL/6 hosts — a powerful intermediate between GEMM and orthotopic xenograft.

---

## 6. Xenografts — CDX, PDX, Orthotopic, Humanized

### 6.1 CDX (Cell-Line-Derived Xenografts)

Established by injecting human PDAC lines (Panc-1, MIA PaCa-2, BxPC-3, AsPC-1, etc.) into immunodeficient mice — typically subcutaneous (flank) in athymic nude (T-cell deficient), SCID (T+B-cell deficient), or NSG (T+B+NK-deficient, IL2Rg<sup>null</sup>) hosts. Pros: rapid, cheap, monitorable by caliper. Cons: artificial site (no pancreas microenvironment), no immune system, line-specific bias.

### 6.2 PDX (Patient-Derived Xenografts)

Surgical or biopsy tissue is implanted into immunodeficient mice (most commonly NSG). PDXs retain patient histology and many genomic features over early passages, with engraftment rates of **~60% for PDAC** (one study reports 59% P0 engraftment across 199 pancreatic cancers, 62% for PDAC specifically). Consortia:

- **NCI PDXNet** (USA) — coordinated PDX development, data, and tools across multiple PDXDCs and PDTCs; the portal hosts pancreatic PDX models with paired -omics.
- **EuroPDX** (Europe) — >1,500 SC and orthotopic PDX models across >30 pathologies including PDAC; the EuroPDX Data Portal supports federated access.
- **Baylor / BCM PDX portal** — pancreatic PDXs with curated annotation.

PDX limitations: human stroma is replaced by murine stroma within 1–2 passages, immune system is absent, takes ~3–6 months per passage, and clonal selection during engraftment biases the represented tumor toward more aggressive subclones.

### 6.3 Orthotopic xenografts

Cells or PDX fragments are implanted into the *pancreas* of the recipient mouse. This restores the relevant microenvironment, allows realistic metastatic patterns (liver, peritoneum) and intra-pancreatic pressure dynamics. Higher engraftment/growth in NSG vs NOD/SCID. The technical price is surgical complexity, the need for IVIS imaging (luciferase-tagged lines) to monitor growth, and higher cost per mouse.

### 6.4 Humanized mice

To restore an immune compartment for testing immunotherapies:

| Model | Reconstitution | Strengths | Weaknesses |
|-------|----------------|-----------|------------|
| **NSG hu-PBMC** | Adult human PBMCs IV | Quick (4–6 wk); strong CD4/CD8 | Graft-versus-host disease (GvHD); short window (~6–8 wk); no myeloid lineage |
| **NSG hu-CD34** | CB or bone-marrow CD34<sup>+</sup> HSCs | Multi-lineage; longer window | Low myeloid; HLA-mismatched |
| **NSG-SGM3** | hCD34 with hIL3/GM-CSF/SCF transgenes | Better myeloid; higher cytokine response | Hyperactivation possible |
| **MISTRG** | hCD34 with hM-CSF/IL3/GM-CSF/TPO/SIRPα knock-ins on Rag2/Il2rg KO | Best myeloid (DCs, macrophages); good for PDAC TAM biology | Anaemia, short lifespan, license-restricted |
| **NOG-EXL / huNOG-EXL** | hCD34 with hIL3/GM-CSF transgenes | Myeloid + lymphoid balance | Cost and complexity |

For PDAC specifically — a myeloid-driven, TAM-rich tumor — **MISTRG and NSG-SGM3** are increasingly used to test myeloid-targeting therapies (CSF1R inhibitors, CD40 agonists), checkpoint inhibitors and cellular therapies.

---

## 7. Organ-on-Chip, Microfluidics, 3D Bioprinting

### 7.1 Pancreas-on-a-chip and PDAC-on-chip

Microfluidic devices (PDMS or thermoplastic) create perfused, multi-compartment cultures with controlled biochemical and biomechanical inputs. PDAC-relevant chips:

- **Multilayer PDAC-on-chip (Beer et al., Biomat Sci 2023)** — PDAC cells + pancreatic stellate cells in collagen I, separated by a nanofibrous membrane; allows control of stroma–epithelium crosstalk.
- **5-channel PDAC chip (Lab on a Chip 2024)** — supports 21-day culture under flow with biophysical-barrier readout for drug penetration.
- **Personalized PDAC chip with endothelial barrier** — patient PDO + endothelium + flow, with on-chip biomarker secretion sampling for precision medicine.
- **Tumor stroma-immune chip** — adds PBMCs to study T-cell penetration through desmoplastic stroma; consistently shows that stromal density limits T-cell cytotoxicity, and that targeted stromal modulation enhances gemcitabine efficacy.
- **Commercial platforms** — Emulate Organ-Chip (S-1, gut, liver chips adaptable to pancreas), TissUse HUMIMIC (multi-organ chip with pancreas islet modules), Mimetas OrganoPlate (96-well plate microfluidic).

### 7.2 3D bioprinting

Extrusion or DLP bioprinters deposit bioinks (gelatin-methacrylate/GelMA, collagen I, alginate, methylcellulose, decellularized pancreas ECM) loaded with PDAC cells, stellate cells, endothelial cells and/or immune cells in spatially defined patterns. 2024–2025 work has produced:

- Collagen–GelMA–alginate bioinks tuned to recapitulate the desmoplastic stiffness (>5 kPa) of human PDAC stroma.
- PANC-1 / plasma / alginate / methylcellulose bioink optimized for vascular-like channels.
- Patient-derived bioprinted PDAC constructs with heterogeneous CAFs for precision therapy testing.

Bioprinted constructs have shown reproducible paclitaxel resistance and high desmoplasia marker expression — making them attractive substrates for screening anti-stromal combinations.

### 7.3 Where this fits

Chip and print systems sit between PDOs and animals: they are reproducible, multi-cell, perfused, but still in vitro. Their physiological realism and assay diversity are improving fast, and they are increasingly used in late preclinical triage — particularly for stromal-modulating, anti-desmoplastic and immunotherapy combinations.

---

## 8. Zebrafish Models

### 8.1 Larval xenografts (zPDX, zCDX)

Cells (cell lines or freshly dissociated patient tissue) are microinjected into 2-day-post-fertilization (2 dpf) zebrafish embryos — typically into the yolk sac, perivitelline space or duct of Cuvier — and tumors grow for 4–7 days. Advantages: cheap (1 patient sample → 50–200 fish), fast (results within a week), transparent (live confocal imaging), low cell-number requirement (sufficient for biopsy-scale samples), and innate-immunocompetent (macrophages, neutrophils present). PANC-1, BxPC-3, AsPC-1 and CFPAC-1 each induce distinct innate immune phenotypes — primary-derived lines drive antitumoral macrophage activation while metastasis-derived lines polarize to pro-tumoral states. zPDX is being developed as a 1–2 week clinical avatar for drug triage in patients too sick for PDX timelines.

### 8.2 Genetic zebrafish PDAC

Transgenic zebrafish with ptf1a- or ela3l-driven Kras<sup>G12V</sup> develop pancreatic neoplasia; combinations with tp53 mutants give invasive carcinoma. Less faithful to human PDAC than KPC but supports rapid, large-N genetic screens.

---

## 9. In Silico Data Resources — Where Computation Meets the Disease

This is the layer where volunteer compute can most directly contribute. The table below lists the open or near-open public resources that anchor every modern PDAC computational project. Sizes and counts are as of mid-2025.

| Resource | Modality | Scope (PDAC-relevant) | Size | License | URL | What it enables |
|----------|----------|-----------------------|------|---------|-----|-----------------|
| **TCGA-PAAD** | WXS + RNA-seq + methylation + clinical | 185 PDAC primary tumors (integrative paper analyzed 150 high-purity) | ~1 TB raw | Open (controlled-access for raw) | [portal.gdc.cancer.gov](https://portal.gdc.cancer.gov/projects/TCGA-PAAD) | Mutation calls, subtypes, survival models, expression panels |
| **ICGC-PACA-AU** | WGS + RNA + clinical | 391 Australian PDAC (Biankin/Waddell) | ~5 TB | DACO-controlled | [dcc.icgc.org](https://dcc.icgc.org/projects/PACA-AU) | Whole-genome SVs; basal/classical subtyping (Bailey 2016) |
| **ICGC-PACA-CA** | WGS + RNA + clinical | 268 Canadian PDAC (Notta) | ~3 TB | DACO-controlled | [dcc.icgc.org](https://dcc.icgc.org/projects/PACA-CA) | Mitotic genome evolution; chromothripsis spectrum |
| **PCAWG** | Uniform WGS reanalysis | ~2,800 cancers incl. 200+ PDAC | ~700 TB | Controlled | [dcc.icgc.org/pcawg](https://dcc.icgc.org/pcawg) | Unified SV catalog, mutational signatures, driver discovery |
| **CPTAC PDAC** | Proteomics + phosphoproteomics + WES + RNA | 140 PDAC tumors (Cao 2021) | ~5 TB | Open | [proteomics.cancer.gov](https://proteomics.cancer.gov/programs/cptac) | Phospho-driver mapping; proteogenomic subtypes |
| **DepMap / CCLE** | Mutation, RNA, proteomics, dependency CRISPR, drug | 20+ PDAC cell lines, all canonical | ~2 TB | CC-BY | [depmap.org](https://depmap.org) | Cancer dependencies; biomarker discovery; selective lethalities |
| **Sanger Project Score** | Genome-wide CRISPR knockout fitness | 50+ PDAC lines | ~500 GB | CC-BY | [depmap.sanger.ac.uk](https://depmap.sanger.ac.uk) | Fitness-target prioritization for PDAC |
| **GDSC1 + GDSC2** | Cell line × drug response (IC50/AUC) | ~1000 lines incl. 40+ pancreatic; 286 drugs in GDSC2 | <100 GB | CC-BY-NC | [cancerrxgene.org](https://www.cancerrxgene.org) | Genotype → drug response models |
| **PRISM (Broad)** | Barcoded multiplexed drug screen | 919 lines × ~6,400 compounds | ~50 GB | CC-BY | [depmap.org/portal/prism](https://depmap.org/portal/prism) | Repurposing screens; off-target signature discovery |
| **CTRPv2** | Sensitivity to small-molecule probes | 860 lines × 481 compounds | ~10 GB | CC-BY | [portals.broadinstitute.org/ctrp](https://portals.broadinstitute.org/ctrp/) | Probe-pathway mapping |
| **HMS LINCS** | Drug response, kinome profiling | Cell-line + biochemical; some PDAC | ~50 GB | CC-BY | [lincs.hms.harvard.edu](https://lincs.hms.harvard.edu) | Kinase-inhibitor selectivity; signature matching |
| **ChEMBL 35** | Drug-target bioactivity DB | >2.5M compounds incl. PDAC-protein bioassays | ~30 GB | CC-BY-SA | [ebi.ac.uk/chembl](https://www.ebi.ac.uk/chembl) | Target-ligand triage; QSAR |
| **HCMI** | Paired -omics + organoid/PDX models | 40+ PDAC PDOs with WES/WGS/RNA | open | NCI DACO | [ocg.cancer.gov/programs/HCMI](https://ocg.cancer.gov/programs/HCMI) | PDO-anchored modeling |
| **PDXNet portal** | PDX -omics + drug | hundreds of PDX models incl. PDAC | varies | Open + controlled | [portal.pdxnetwork.org](https://portal.pdxnetwork.org) | PDX dataset discovery + workflows |
| **EuroPDX Data Portal** | PDX -omics + treatment | 1,500+ PDX, PDAC subset | varies | Federated | [dataportal.europdx.eu](https://dataportal.europdx.eu) | EU PDX cohort assembly |
| **cBioPortal PAAD studies** | Curated TCGA/ICGC/QCMG/UTSW | 1,000+ PDAC tumors aggregated | <50 GB | Open | [cbioportal.org](https://www.cbioportal.org) | Cohort comparison, biomarker exploration |
| **Cellosaurus** | Cell-line metadata + STR | All PDAC lines | <1 GB | CC-BY | [cellosaurus.org](https://www.cellosaurus.org) | Provenance, contamination flags |
| **PDB** | 3D protein structures | KRAS (incl. G12D/V/C), p53, MYC, SMAD4, MEK1/2, BRCA2 fragments — hundreds of entries | <100 GB total | CC0 | [rcsb.org](https://www.rcsb.org) | Docking, MD, structure-based design |
| **AlphaFold DB** | Predicted structures | All human + mouse PDAC proteins | ~10 TB | CC-BY | [alphafold.ebi.ac.uk](https://alphafold.ebi.ac.uk) | Models for proteins lacking PDB entries |
| **Enamine REAL / ZINC22** | Make-on-demand chemical space | ~50B compounds (REAL); 5B "in stock" (ZINC22) | catalog only | varies | [enamine.net](https://enamine.net/library-synthesis/real-compounds), [zinc.docking.org](https://cartblanche22.docking.org) | Virtual screening at scale |
| **PROGENy / decoupleR** | Pathway responsive gene weights | 14 cancer-relevant pathways | <100 MB | GPL/MIT | [saezlab.github.io/decoupleR](https://saezlab.github.io/decoupleR/) | Pathway-activity inference from bulk/scRNA |
| **MSigDB / Hallmark** | Gene-set collections | ~50 hallmark; thousands of curated | <1 GB | Free academic | [gsea-msigdb.org](https://www.gsea-msigdb.org) | GSEA, pathway enrichment |

---

## 10. Single-Cell PDAC Atlases

Single-cell genomics has redefined PDAC heterogeneity in the last six years. Key reference datasets:

| Study | Year | Platform | N samples | Cells | Key contribution |
|-------|------|----------|-----------|-------|------------------|
| **Peng et al.** *Cell Res* | 2019 | 10x scRNA-seq | 24 primary + 11 controls | 57,530 | First large PDAC scRNA atlas; ductal-type clusters; type-1 vs type-2 ductal cells |
| **Chan-Seng-Yue et al.** *Nat Genet* | 2020 | snRNA + DNA | 224 tumors | — | Showed transcriptomic subtypes are clonally driven; combined "classical / basal" continuum from single-cell |
| **Elyada et al.** *Cancer Discov* | 2019 | scRNA-seq | KPC + human | — | Defined iCAF / myCAF / apCAF subsets — a cornerstone of PDAC stromal biology |
| **Steele et al.** *Nat Cancer* | 2020 | CyTOF + scRNA | Tumor + blood | — | Multi-modal map of PDAC immune landscape — TAM-dominant, T-cell-excluded |
| **Hwang et al.** *Nat Genet* | 2022 | snRNA + Visium | 43 PDAC, neoadjuvant treated | ~225,000 | First combined snRNA + spatial PDAC atlas; treatment-resistant programs identified |
| **Krieger et al.** *Nat Comm* | 2021 | scRNA-seq | — | — | Mapping cellular and molecular landscape of patient-derived models |
| **CXCL10+ CAF Atlas (Croft et al., Clin Cancer Res 2025)** | 2025 | scRNA + multiplex | — | — | Linked CXCL10<sup>+</sup> fibroblasts to basal subtype tumor cells, prognostic implications |
| **PDAC scRNA atlas (Werba et al. / others)** | 2023+ | Integrated | 229 patients | 700,000+ | Unified PDAC atlas integrating spatial transcriptomics; extends subtyping framework |
| **Carpenter et al. *Cancer Cell* 2025** | 2025 | snRNA + ST | Multi-cohort | — | Cellular subtypes involved in neural invasion |

These atlases provide reference signatures (classical/basal tumor subtypes; iCAF/myCAF/apCAF stromal subsets; immune phenotypes) that anchor any new scRNA experiment in PDAC and are the substrate for cell-deconvolution of bulk RNA-seq, ligand-receptor analysis (CellChat, NicheNet) and trajectory inference.

---

## 11. Drug-Response Prediction Datasets

The core machine-learning substrate for *in silico* drug-response prediction in PDAC:

| Dataset | Scope | Endpoint | PDAC coverage | Best uses |
|---------|-------|----------|----------------|-----------|
| **GDSC1 + GDSC2** | ~1000 cell lines × 350+ drugs | IC50, AUC | ~40 pancreatic lines; standard PDAC chemo included | Genotype–drug models; benchmarking |
| **CCLE drug v2** | 500+ lines × 24 drugs | IC50 | Standard pancreatic lines | Multi-omic biomarker discovery |
| **CTRPv2** | 860 lines × 481 small molecules | AUC, EC50 | Pancreatic subset | Probe-pathway annotation |
| **PRISM Repurposing** | 919 lines × ~6,400 drugs | log2-fold viability | All major PDAC lines | Drug-repurposing screens |
| **DepMap CRISPR (Achilles)** | 1,100+ lines × 18k genes | Dependency score | All major PDAC lines | Genetic-vulnerability discovery |
| **Sanger Project Score** | 300+ lines | CRISPR fitness | 50+ PDAC | Independent dependency replication |
| **NCI-60** | 60 cancer lines | IC50 | Limited PDAC, includes BxPC-3 et al. | Legacy, well-validated |
| **Driehuis 2019 PDO panel** | 30 PDAC PDOs × 76 agents | AUC | All PDAC | Organoid-anchored drug response |
| **Tiriac 2018 PDAC PDO panel** | 66 PDAC PDOs × 5 SOC + targeted | AUC | All PDAC | Pharmacotype signatures |
| **HMS LINCS Kinomescan / KINOMEscan + viability** | 100s of drugs × dozens of lines | Kinase binding + viability | Some PDAC | Selectivity profiling |
| **PharmacoDB 2.0** | Aggregator over GDSC/CTRP/CCLE/PRISM | Harmonized | All PDAC | Cross-dataset modeling |

Combined, these resources support: (i) **classical regression** of drug response from -omics; (ii) **deep learning** (DRP-DL, DeepDR, DrugCell) trained on cell lines and tested on PDOs and TCGA; (iii) **biomarker discovery** (KRAS-G12D inhibitor response predictors, PARP-inhibitor in BRCA-deficient lines); and (iv) **drug repurposing** by signature matching (CMap, L1000 in LINCS).

---

## 12. Where Compute Could Help — `[A]` Items

Below are the angles where a self-funded volunteer-computing project (BOINC-style or web-worker grid) can produce *original*, *useful* output for PDAC research. Each is tagged with the model layer it most depends on.

- **[A] KRAS-G12D / G12V / G12R / Q61H pocket virtual screen.** Dock the Enamine REAL (50B) or a curated 1–10B subset against the PDB structures of inactive-state KRAS-G12D (e.g., 7RPZ, the MRTX1133 co-crystal), G12V, G12R, Q61H, and the recently published switch-II pocket states. Re-score top 0.01% with MM-GBSA or FEP+. Output: ranked novel non-covalent G12D/G12V binder candidates. Anchor: 2D KRAS-mutant lines for follow-up validation.
- **[A] Synthetic-lethal screen prediction on KRAS-mutant PDAC.** Train graph-NN or matrix-factorization models on DepMap CRISPR + GDSC2 + PRISM restricted to PDAC lines + KRAS-mutant non-PDAC lines (to expand sample size). Predict gene-pairs whose joint knockdown is selectively lethal in KRAS-G12D backgrounds. Output: ranked SL pairs, with experimental priors. Anchor: 2D lines and PDOs for short-list validation.
- **[A] Pan-PDO drug-response prediction.** Train a multi-modal deep-learning model (RNA + mutation + methylation → AUC) on GDSC2 + CTRP + Driehuis/Tiriac PDO data, predict on TCGA-PAAD + ICGC-PACA + spatial-tx atlases. Output: per-tumor drug rankings, ready for downstream wet-lab triage.
- **[A] Subtype-conditioned drug repurposing.** Use PRISM + classical/basal subtype labels (Bailey 2016, Moffitt 2015, Collisson 2011) to find compounds with subtype-selective activity. Output: drug shortlist per subtype.
- **[A] Stroma–epithelium ligand-receptor inference at scale.** Run CellChat / NicheNet / liana-py across all public PDAC scRNA atlases unified (Peng, Hwang, Steele, Werba, etc.) for stable iCAF/myCAF/apCAF–tumor signaling edges. Output: high-confidence stromal therapy-target signaling axes.
- **[A] AlphaFold–docking pipeline for the PDAC interactome.** Predict structures of underexplored PDAC drivers (e.g., RNF43, GNAS, ARID1A, KDM6A, ATM, MLH1 — frequent in subsets of PDAC) using AlphaFold 3 / Boltz / RoseTTAFold-AllAtom; identify druggable pockets with fpocket / DoGSiteScorer; virtual-screen Enamine REAL against ranked pockets. Output: druggable-pocket atlas + initial ligand candidates.
- **[A] Mutational-signature deconvolution across the global PDAC WGS pool.** Re-analyze ICGC-PACA-AU + PACA-CA + PCAWG PDAC with up-to-date COSMIC SBS / DBS / ID signatures and identify HRD, MMR, BER and clock-like signatures per sample. Output: HRD/MMR positivity per case → PARP-i & ICI eligibility map.
- **[A] Molecular dynamics of mutant-KRAS conformational ensembles.** Run µs-scale MD on KRAS-G12D/G12V/G12R/Q61H, both GDP- and GTP-bound, with and without lead compounds. Volunteer-compute friendly via Folding@home-style protocol. Output: free-energy landscapes informing drug-design hypotheses.
- **[A] Mechanistic mathematical modeling of PDAC tumor + metastasis.** Calibrate Tasmania-style hybrid ABM/PDE models against KPC growth curves and patient longitudinal CT volumetry; explore therapy-scheduling alternatives. Output: dose-schedule recommendations for preclinical groups.
- **[A] CRISPR fitness biomarker discovery.** Cross-link Project Score + Achilles dependency scores with multi-omic features in PDAC lines to identify biomarkers predicting essentiality (e.g., MTAP-deletion → PRMT5 dependency in PDAC). Output: ranked biomarker–target pairs.
- **[A] Multi-task transfer-learning from organoid to patient.** Use organoid pharmacotyping (Tiriac, Driehuis, POPS) as target labels and CCLE/GDSC features as source data; predict patient-level drug response on TCGA-PAAD + CPTAC. Output: in silico organoid-equivalent predictions for any PDAC bulk-RNA sample.
- **[A] Chemical-space sampling around clinical PDAC leads.** Generative chemistry (REINVENT, equivariant diffusion) around MRTX1133, RMC-6236, AMG-510 scaffolds for selectivity vs. wild-type KRAS. Output: docking-validated novel-analog libraries.
- **[A] Image-based phenotype prediction.** Train CNN/ViT on H&E from TCGA-PAAD + CPTAC to predict subtype, KRAS allele and HRD status — democratizes molecular subtyping for centers without sequencing. Output: open model weights.
- **[A] Drug-combination synergy prediction on PDAC organoids.** Train DeepSynergy/MatchMaker on existing GDSC2 + DREAM combos restricted to or weighted toward PDAC contexts; predict synergistic pairs across PDAC PDO panels. Output: ranked combination shortlist (e.g., MEKi + autophagy-i, KRAS-G12D-i + ATR-i).

---

## 13. Sources

- [PanCAN — Pancreatic Cancer Models overview](https://pancan.org/research/strategic-research-program/learn/pancreatic-cancer-models/)
- [Deer et al. — Phenotype and Genotype of Pancreatic Cancer Cell Lines (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2860631/)
- [Gradiz et al. — MIA PaCa-2 and PANC-1, Sci Rep 2016](https://www.nature.com/articles/srep21648)
- [ATCC Pancreatic Cancer Cell Panel (TCP-1026)](https://www.atcc.org/products/tcp-1026)
- [Cellosaurus — Hs 766T (CVCL_0334)](https://www.cellosaurus.org/CVCL_0334)
- [Sigma — HPDE6c7 datasheet](https://www.sigmaaldrich.com/US/en/product/mm/scc442)
- [Boj et al., Cell 2015 — Organoid Models of PDAC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4847151/)
- [Driehuis et al., PNAS 2019 — PDOs recapitulate disease and allow personalized drug screening](https://www.pnas.org/doi/10.1073/pnas.1911273116)
- [Driehuis et al., Cell 2019 — Drug screening and genome editing in PDAC organoids](https://pmc.ncbi.nlm.nih.gov/articles/PMC7612395/)
- [Seppälä et al., 2021 — POPS feasibility trial](https://pmc.ncbi.nlm.nih.gov/articles/PMC8196829/)
- [Organoid-based precision medicine in pancreatic cancer, UEG Journal 2025](https://onlinelibrary.wiley.com/doi/full/10.1002/ueg2.12701)
- [Tuveson Lab page, Cold Spring Harbor](https://www.cshl.edu/research/faculty-staff/david-tuveson/)
- [CSHL — Organoid profiling personalizes treatments](https://www.cshl.edu/organoid-profiling-personalizes-treatments-for-pancreatic-cancer/)
- [Lee et al., Curr Protoc Pharmacol 2016 — GEMMs of PDAC, the KPC model](https://pmc.ncbi.nlm.nih.gov/articles/PMC4915217/)
- [Hingorani et al., Cancer Cell 2003 / 2005 (KC, KPC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4915217/)
- [Qiu et al., PLoS One 2017 — KPIC (Kras; Trp53; Ink4flox; p48-Cre)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5419507/)
- [Smad4 deficiency study, 2021](https://pubmed.ncbi.nlm.nih.gov/33483239/)
- [Patient-derived xenograft models in cancer therapy, Sig Transduct Target Ther 2023](https://www.nature.com/articles/s41392-023-01419-2)
- [EuroPDX](https://www.europdx.eu/) and [EuroPDX Data Portal](https://dataportal.europdx.eu/data/about/objectives/)
- [PDXNet portal, NAR Cancer 2022](https://academic.oup.com/narcancer/article/4/2/zcac014/6572305)
- [PDOX models for PDAC, In Vivo 2022](https://iv.iiarjournals.org/content/36/3/1114)
- [Establishment and characterization of PDX for PDAC, 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10741928/)
- [Humanized mice for cancer immunotherapy, Front Oncol 2021](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2021.784947/full)
- [PBMC-humanized NSG-SGM3 mouse model, AACR 2019](https://aacrjournals.org/cancerres/article/79/13_Supplement/3902/635763/Abstract-3902-Increased-sensitivity-for-detecting)
- [Next-generation PBMC humanized mice, 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC8344070/)
- [Comprehensive analysis of humanized mouse models, bioRxiv 2025](https://www.biorxiv.org/content/10.1101/2025.09.04.674233v1.full)
- [PDAC-on-chip for stromal–cancer crosstalk, Biomat Sci 2023](https://pubs.rsc.org/en/content/articlehtml/2023/bm/d2bm00881e)
- [Personalized PDAC chip with endothelial barrier, 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11460472/)
- [Biophysical-barrier PDAC chip, Lab Chip 2024](https://pubs.rsc.org/en/content/articlehtml/2024/lc/d3lc00660c)
- [PDAC-on-a-chip immune distribution, 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10185841/)
- [3D bioprinted PDAC, Biomacromolecules 2025](https://pubs.acs.org/doi/10.1021/acs.biomac.5c00450)
- [Patient-derived 3D-bioprinted PDAC models, ScienceDirect 2025](https://www.sciencedirect.com/science/article/pii/S0169409X25001553)
- [PANC-1/plasma/alginate/methylcellulose bioink](https://pmc.ncbi.nlm.nih.gov/articles/PMC10421301/)
- [Zebrafish xenograft model for PDAC innate immunity, 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9224329/)
- [Patient-derived zebrafish xenograft of PDAC, JoVE 2019](https://www.jove.com/t/59507/patient-derived-heterogeneous-xenograft-model-pancreatic-cancer-using)
- [TCGA-PAAD — Integrated Genomic Characterization, 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC5964983/)
- [cBioPortal PAAD TCGA GDC 2025](https://www.cbioportal.org/study/summary?id=paad_tcga_gdc)
- [Pan-cancer analysis of whole genomes (PCAWG), Nature 2020](https://www.nature.com/articles/s41586-020-1969-6)
- [Project Score documentation, Sanger](https://depmap.sanger.ac.uk/documentation/project-score/)
- [Broad–Sanger Unified Pan-Cancer CRISPR Screens](https://depmap.org/broad-sanger/)
- [Project Score database, NAR 2021](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7778984/)
- [PharmacoDB 2.0, NAR 2022](https://academic.oup.com/nar/article/50/D1/D1348/6438034)
- [Learning and actioning general principles of cancer cell drug sensitivity, Nat Comm 2025](https://www.nature.com/articles/s41467-025-56827-5)
- [Peng et al. — single-cell PDAC atlas, Cell Res 2019](https://www.nature.com/articles/s41422-019-0195-y)
- [Hwang et al. — snRNA + spatial PDAC atlas, Nat Genet 2022](https://www.nature.com/articles/s41588-022-01134-8)
- [Refining the molecular framework for PDAC with single-cell and spatial technologies](https://ncbi.nlm.nih.gov/pmc/articles/PMC8282742)
- [Human PDAC single-cell atlas — CXCL10+ fibroblasts and basal subtype, Clin Cancer Res 2025](https://aacrjournals.org/clincancerres/article/31/4/756/751743)
- [Single-cell and spatial atlas of pancreatic cancer immunophenotypes, bioRxiv 2025](https://www.biorxiv.org/content/10.1101/2025.02.08.637283v1.full)
- [Spatially resolved multi-omics single-cell analyses in PDAC, Gastroenterology 2023](https://www.gastrojournal.org/article/S0016-5085(23)00810-7/fulltext)
- [Spatial transcriptomics and PDAC neural invasion, Cancer Cell 2025](https://www.cell.com/cancer-cell/fulltext/S1535-6108(25)00270-3)
- [PROGENy / decoupleR documentation](https://saezlab.github.io/decoupleR/articles/pw_bk.html)
- [PROGENy R/Python package](https://saezlab.github.io/progeny/)
- [PDAC organoid-fibroblast co-culture chemoresistance, 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9588250/)
- [Pancreatic cancer organoid in matrix — T-cell killing, Sci Rep 2024](https://www.nature.com/articles/s41598-024-60107-5)
- [Heterogeneous TME PDAC organoid protocol, STAR Protocols 2024](https://www.cell.com/star-protocols/fulltext/S2666-1667(24)00704-4)
- [Organoid co-culture for TME, Cancer Innovation 2024](https://onlinelibrary.wiley.com/doi/10.1002/cai2.101)
- [MRTX1133 small molecule targeting KRAS-G12D, 2023/2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC10922474/)
- [Mutant KRAS inhibitors for pancreatic cancer, 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11399826/)
- [Targeting KRAS G12D inhibitors, Thoracic Cancer 2025](https://onlinelibrary.wiley.com/doi/10.1111/1759-7714.70203)
- [Pancreatic Cancer Organoids: Modeling Disease and Guiding Therapy, Cancers 2025](https://www.mdpi.com/2072-6694/17/23/3850)
- [Large-scale organoid-based drug repurposing platform, Cell Genomics 2022](https://www.cell.com/cell-genomics/fulltext/S2666-979X(22)00017-9)
- [Organoid models predict chemotherapy response, 2024](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12768194/)
- [Immortal human pancreatic duct epithelial cell lines, Am J Pathol 2000](https://pmc.ncbi.nlm.nih.gov/articles/PMC1885733/)
- [Kerafast H6c7 line](https://www.kerafast.com/productgroup/531/human-pancreatic-duct-epithelial-cell-line-h6c7)
- [Spatial Biology and Organoid Technologies Reveal Therapy-Resistant CSC in PDAC, 2025](https://www.biorxiv.org/content/10.1101/2025.05.22.655586.full.pdf)
- [Multidrug resistance gene screening in PDAC](https://cancerci.biomedcentral.com/articles/10.1186/s12935-022-02785-7)
- [Bioengineering 3D PDAC Models with Fibrotic Stroma](https://www.mdpi.com/2072-666X/16/10/1140)
- [Comprehensive molecular analysis of 26 newly established PDAC cell lines, 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11837577/)

---

*This document is part of the open project repository at `/Volumes/Storage April 2026/PancreaticCancer/PROJECT/`. Companion files: `02_targets.md` (PDAC targets), `03_boinc.md` (volunteer-compute plan), `17_computational_methods.md` (algorithms behind the `[A]` items). All references are open-access where possible; controlled-access genomic datasets require dbGaP/EGA application.*
