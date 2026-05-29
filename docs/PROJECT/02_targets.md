# PDAC Drug Targets & Computational Frontiers (2026)

> Where the field is pushing, where it's stuck, and which problems a volunteer-compute project could meaningfully advance.

## 1. Top 5 PDAC drug targets in 2026

### A. KRAS G12D — ~40% of PDAC tumors
- **Best-in-class structurally:** MRTX1133 (non-covalent Switch-II pocket binder) — **clinical development discontinued by BMS in January 2025** due to highly variable / suboptimal PK; remains the canonical preclinical proof-of-concept and the best docking positive control.
- **Live clinical assets (G12D-selective and pan-RAS):** RMC-9805 (zoldonrasib, Revolution Medicines — Phase 1: ORR 30%, DCR 80%); RMC-6236 (daraxonrasib, pan-RAS tri-complex — Phase 3 RASolute 302/303 ongoing 2026); ASP3082 (Astellas); BPI-421286.
- **What's missing:** Resistance mechanisms are poorly mapped; combinations with SHP2, RAF, or MEK inhibitors barely explored at scale; switch-II pocket still susceptible to secondary mutations
- **Compute angle:** Ensemble virtual screening of 1B+ compounds against G12D + allosteric sites

### B. KRAS G12C — <2% of PDAC (but huge in NSCLC)
- **Approved:** Sotorasib (Lumakras), adagrasib (Krazati)
- **PDAC relevance:** Limited because G12C is rare; lessons transfer to G12D resistance mapping
- **Status:** Manageable tolerability (~16% grade 3–4 AEs)

### C. Pan-RAS / tri-complex inhibitors
- **Lead agents:** RMC-6236 (daraxonrasib), RMC-9805
- **Mechanism:** Form ternary complexes that block RAF interaction while KRAS is GTP-bound
- **Status (ASCO 2025):** RMC-9805 Phase 1 PDAC data — early efficacy signals
- **What's missing:** Broader variant coverage; optimal combo partners; predictive biomarkers

### D. Mutant p53 reactivation — >50% of PDAC has p53 mutations
- **Lead:** PC14586 (rezatapopt), selective for p53 Y220C, Phase 2
- **Competitor:** Eprenetapopt (APR-246), broader but less specific
- **Challenge:** Y220C is a minority of PDAC p53 mutations; need mutation-specific or broad-spectrum approaches
- **Compute angle:** Virtual screen against ensembles of mutant p53 conformations

### E. Stromal / immune microenvironment
- **Targets:** CXCR4 (BL-8040 + pembro + chemo COMBAT trial), FAP, FAK (defactinib), TAMs, TGF-β
- **What's missing:** Patient stratification (HA-high for PEGPH20, CXCL12-high for BL-8040); mechanistic clarity on which combos synergize

## 2. Top 3 "undruggable / cryptic-pocket" opportunities where compute is the bottleneck

| Tag | Opportunity | State of the art | Why volunteer compute helps |
|---|---|---|---|
| **[B1]** | Cryptic-pocket discovery in KRAS G12D via long all-atom MD | ~400 µs / state with co-solvent probes (2024–25); need 100× more across pan-RAS variants | Embarrassingly parallel replica-exchange MD; trajectory ensemble grows linearly with nodes |
| **[B2]** | MYC cryptic-pocket virtual screening | No direct MYC binder exists; intrinsically disordered, large flat surface | Screen 10B+ compounds (Enamine REAL) vs 100–1000 MD-derived MYC-MAX-MLXIP conformers |
| **[B3]** | Pan-KRAS allosteric pocket virtual screening | All approved drugs hit Switch-II; one allosteric site found; need broader screen | 70B+ Enamine REAL × 50 KRAS conformations = 3.5T poses; only volunteer-scale can do this |

## 3. Drug repurposing landscape

Available repurposing libraries:
- **ReFRAME** (Calibr/Scripps): 12,000 compounds with clinical history
- **Broad Drug Repurposing Hub:** 5,000+ compounds linked to literature
- **NCI / NIH historical screens** via PubChem and ChEMBL

Recent PDAC organoid screens have hit 1,800 FDA-approved drugs and revealed patient-specific vulnerabilities.

**[B4] Drug-drug synergy prediction.** 12,000 compounds = 72M pairs. Experimental screens cover ~1k–10k pairs/year per lab. Train a graph-neural-network surrogate on existing patient-derived organoid (PDO) data, then use volunteer compute to score 10M–100M *in silico* combinations and feed top hits back to wet labs.

## 4. Early detection / ML angle

PDAC ctDNA shedding is very low early; current stage-I sensitivity ~30–40%. Multi-omics + ML is the way forward.

Public data rich enough to train on:
- ctDNA + methylation (Galleri / GRAIL — limited public release, growing academic partnerships)
- Serum proteomics: 7–50 marker panels across >500 PDAC samples
- Serum miRNA-seq + automated ML — 80–90% sensitivity in some early-stage studies
- Microbiome (oral / gut dysbiosis signatures emerging 2024–26)

## 5. Public datasets suitable for volunteer compute

| Dataset | URL | Size | Use |
|---|---|---|---|
| **TCGA-PAAD** | https://portal.gdc.cancer.gov/ | 185 samples, multi-omics | Prognostic signatures, baseline ML |
| **ICGC PACA-CA/AU** | https://icgc.org | ~500 samples | Mutation hotspots, CNV, outcome |
| **LinkedOmics TCGA-PAAD** | https://www.linkedomics.org/data_download/TCGA-PAAD/ | Multi-omics tables | Protein-gene correlations |
| **cBioPortal TCGA-PAAD** | https://github.com/cBioPortal/datahub | Methylation + expression | Pathway analysis |
| **DepMap / CCLE pancreatic lines** | https://depmap.org/portal | ~50 lines | CRISPR dependencies, drug-response |
| **CPTAC Pancreatic** | https://proteomics.cancer.gov | Phospho + protein | Kinase-substrate, pathway |
| **ReFRAME library** | Calibr/Scripps portal | 12k compounds | Repurposing |
| **Broad Drug Repurposing Hub** | https://www.broadinstitute.org/drug-repurposing-hub | 5k+ compounds | Repurposing |
| **PubChem / ChEMBL PDAC screens** | https://pubchem.ncbi.nlm.nih.gov, https://www.ebi.ac.uk/chembl | Millions of assay results | HTS mining, SAR |
| **Enamine REAL (compound library)** | https://enamine.net/compound-collections/real-compounds | ~70B make-on-demand | Ultra-large VS |
| **ZINC22** | https://zinc.docking.org/ | ~37B purchasable | Ultra-large VS |

## 6. Compute bottlenecks tagged for BOINC-scale projects

| Tag | Bottleneck | Volunteer fit | Estimated speedup vs single lab |
|---|---|---|---|
| **[B1]** | Cryptic-pocket discovery via long MD on KRAS/RAS panel | Distribute replica-exchange microsecond trajectories | 100–1000× |
| **[B2]** | MYC cryptic-pocket VS (10B+ ligands) | Compound batching + GPU distribution | 50–500× |
| **[B3]** | Pan-KRAS allosteric VS (70B × 50 conformations) | Ligands × conformations partition naturally | 100–1000× |
| **[B4]** | Drug-synergy ML surrogate evaluation on 100M pairs | Distributed inference + active learning loop | 1000–10,000× |
| **[B5]** | Multi-omics feature-selection ensemble ML | Distributed grid search + nested CV | 100–1000× |
| **[B6]** | Time-series ctDNA MCMC subclonal deconvolution | Parallel MCMC chains | 50–500× |

## 7. Sources

- [Frontiers — KRAS inhibitor-directed therapies for pancreatic cancer](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2024.1402128/full)
- [PMC — KRAS Inhibition in PDAC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12842425/)
- [PMC — Broad-spectrum RAS inhibition in PDAC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12735763/)
- [PMC — Cryptic pockets via enhanced sampling along normal modes (KRAS G12D)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11558672/)
- [PMC — Decrypting cryptic pockets with physics + AI](https://pmc.ncbi.nlm.nih.gov/articles/PMC12959236/)
- [PMC — Targeting mutant p53 for cancer treatment](https://pmc.ncbi.nlm.nih.gov/articles/PMC9496879/)
- [Annals of Oncology — PYNNACLE Phase 2 (rezatapopt)](https://www.annalsofoncology.org/article/S0923-7534(24)03681-0/fulltext)
- [PMC — Drug repurposing opportunities in PDAC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8003696/)
- [Broad — Drug Repurposing Hub](https://www.broadinstitute.org/developing-diagnostics-and-treatments/drug-repurposing-hub)
- [PMC — Circulating cell-free tumor DNA for early detection](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7763954/)
- [Hunter Heidenreich — ZINC-22 database notes](https://hunterheidenreich.com/notes/chemistry/datasets/zinc-22/)
- [Nature Comms — AI-accelerated virtual screening platform (2024)](https://www.nature.com/articles/s41467-024-52061-7)
- [GDC Data Portal](https://portal.gdc.cancer.gov/)
- [LinkedOmics TCGA-PAAD](https://www.linkedomics.org/data_download/TCGA-PAAD/)
