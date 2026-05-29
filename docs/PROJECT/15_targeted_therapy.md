# Targeted Therapy, Molecular Subtypes, and Single-Cell Biology of PDAC (2026)

A practitioner-grade map of what is actually mutated in pancreatic ductal adenocarcinoma (PDAC), what drugs hit those mutations, what classes of tumors exist underneath the gross histology, and where computational work could meaningfully accelerate the field. Written for the volunteer-compute project; compute-relevant items are tagged `[A]` and consolidated in section 12.

PDAC is the dominant histology (>90% of pancreatic cancers); the rest of this document is about PDAC unless otherwise noted.

---

## 1. The PDAC genome — what is mutated, and how often

For two decades the PDAC genome has been described as a "four-mutation" disease: KRAS, TP53, CDKN2A, SMAD4. That oversimplifies but it captures the truth that one driver dominates, three tumor suppressors are routinely lost, and the long tail is genuinely a long tail. Whole-exome and whole-genome data from ICGC (Bailey 2016), TCGA (PAAD, 2017), the Sheffler-Collins/Foundation Medicine cohorts, and recent Caris/Tempus real-world cohorts now agree on the rough frequencies. The numbers below are weighted across surgical-resection cohorts and metastatic-biopsy cohorts (metastatic cohorts skew slightly higher on TP53 and KRAS because of clonal selection).

### Table 1 — PDAC driver mutations, ordered by frequency

| Gene | Function | % of PDAC | Mutation pattern | Druggable? |
|---|---|---|---|---|
| **KRAS** | GTPase, MAPK/PI3K activator | 88–95% | Missense, codon 12 (>90%), 13, 61 | Yes — G12C, G12D, pan-RAS |
| **TP53** | Tumor suppressor, DNA-damage sensor | 60–75% | Missense (GOF) > nonsense/del | Indirect — reactivators, MDM2 |
| **CDKN2A** | p16INK4a / p14ARF, CDK4/6 brake | 50–80% | Deletion, methylation, mutation | CDK4/6i (partial) |
| **SMAD4** | TGF-β effector | 20–30% | Deletion, LOH, mutation | Indirect — TGF-β axis |
| **ARID1A** | SWI/SNF chromatin remodeler | 6–12% | Truncating | EZH2i (synthetic lethal) |
| **KMT2C / KMT2D** | H3K4 methyltransferases | 5–10% each | Truncating | DOT1L / KDM6A axes |
| **RNF43** | Wnt negative regulator | 5–10% | Truncating | Wnt-port inhibitors (PORCN) |
| **TGFBR1/2, ACVR1B** | TGF-β receptors | 5–8% combined | Mutation, deletion | Indirect |
| **BRCA2** | HR repair | 4–7% (germline + somatic) | LOF | PARPi, platinum |
| **BRCA1** | HR repair | 1–3% | LOF | PARPi, platinum |
| **PALB2** | HR repair | 1–3% | LOF | PARPi (off-label), platinum |
| **ATM** | DDR kinase | 3–6% | LOF | ATRi (synthetic lethal) |
| **PIK3CA** | PI3K p110α | 2–4% | E542K/E545K/H1047R | PI3Kα inhibitors |
| **GNAS** | Gαs (IPMN-derived PDAC) | 4–8% | R201C/H | None direct |
| **MYC** | Oncogene (amplification) | 14–20% amp | Amp/translocation | BET, indirect |
| **NRG1 fusions** | ErbB ligand | 0.5–1.5% (KRAS-WT enriched) | Fusion | Zenocutuzumab |
| **BRAF V600E / fusions** | RAF kinase | 1–3% | V600E rare; class II/III fusions | Dabraf+trametinib |
| **NTRK fusions** | Tropomyosin receptor kinase | <0.5% | Fusion | Larotrectinib, entrectinib |
| **RET fusions** | RET kinase | <0.5% | Fusion | Selpercatinib |
| **FGFR2 fusions** | FGFR | <0.5% | Fusion | Pemigatinib |
| **ALK / ROS1 fusions** | TKs | <0.5% | Fusion | Alectinib, etc. |
| **HER2 (ERBB2) amp/mut** | RTK | 2–4% | Amp / S310F | T-DXd |
| **MSI-H / dMMR** | Mismatch repair | 0.8–1.5% | MLH1/MSH2/MSH6/PMS2 | Pembrolizumab |
| **Claudin 18.2 (expression)** | Tight junction | ~30% IHC+ | Overexpression | Zolbetuximab (failed P2) |

A small but important class of "KRAS wild-type PDAC" (~8–10% of all PDAC) is enriched for actionable alternatives: NRG1, BRAF, NTRK/RET/FGFR2/ALK/ROS1 fusions, HER2, and PIK3CA. These tumors are younger, frequently classical/well-differentiated, and now represent the highest yield of NGS-driven precision oncology in PDAC.

The structural biology is also unusual: PDAC has a low tumor mutational burden (median ~1.0–1.8 mutations/Mb) yet very high structural complexity. Notta 2016 classified PDAC genomes into four structural patterns — stable, locally rearranged, scattered, and unstable (BRCA-like). The unstable pattern correlates with HRD scores and platinum sensitivity.

---

## 2. KRAS — the central problem

KRAS is mutated in roughly 90% of PDAC. The mutational spectrum is markedly different from KRAS-driven lung and colon cancers — PDAC is dominated by G12D, while lung is dominated by G12C and colon is split.

### Table 2 — KRAS mutation spectrum in PDAC

| Variant | % of KRAS-mut PDAC | GTP affinity | Drug class history |
|---|---|---|---|
| G12D | 40–44% | High | Long undruggable; now multiple agents |
| G12V | 28–32% | High | Very recent drugs (pan-RAS, RMC programs) |
| G12R | 13–16% | Medium | PDAC-enriched (rare elsewhere); selective drugs in discovery |
| G12C | 1–3% | Medium | Two approved drugs (NSCLC/CRC), modest in PDAC |
| Q61H | 2–4% | Very high | Pan-RAS-targeting agents only |
| G13D | 1–2% | Medium | Pan-RAS |
| Other (Q61L, A146T, G12A) | <2% each | Variable | Pan-RAS |

### 2.1 KRAS biology — what the inhibitors are exploiting

KRAS is a small GTPase that cycles between a GDP-bound (OFF) and GTP-bound (ON) state. The cycle is governed by GEFs (SOS1/2, RasGRP), which exchange GDP for GTP, and GAPs (NF1, RASA1), which accelerate intrinsic GTP hydrolysis. Switch I (residues 30–40) and Switch II (residues 60–76) change conformation between the OFF and ON states. The hypervariable region (HVR, C-terminal residues 167–188) is farnesylated and palmitoylated, anchoring KRAS to the inner leaflet of the plasma membrane where it engages effectors.

Mutations at G12, G13, and Q61 impair GAP-stimulated GTP hydrolysis, so KRAS spends much more time in the GTP-bound ON state. Once active, KRAS recruits RAF (→ MEK → ERK), PI3K (→ AKT → mTOR), RalGDS, and TIAM1/Rac, among others.

Two pharmacological strategies dominate:

- **KRAS-OFF (GDP-locked) inhibitors** — covalently trap the protein in its inactive, GDP-bound state. Sotorasib and adagrasib bind a cryptic pocket adjacent to Switch II that is only present in the GDP form, and they covalently engage the C12 cysteine. They therefore work only for G12C.

- **KRAS-ON (GTP-locked, tri-complex) inhibitors** — bind KRAS in its active, GTP-bound state, simultaneously engage cyclophilin A (CypA), and present a composite surface that blocks effector binding. The "RM-018-style" molecules of Revolution Medicines (RMC-6291 for G12C, RMC-6236 pan-RAS, RMC-9805 G12D, RMC-7977 RAS multi-selective) work in this mode and do not require a covalent cysteine. They are mutant-allele-selective via differential CypA binding.

### 2.2 KRAS inhibitors — agent-by-agent

#### KRAS G12C (OFF inhibitors)
- **Sotorasib (AMG 510, Lumakras)**: FDA-approved 2021 for NSCLC. CodeBreaK 100 PDAC cohort (n=38) showed ORR 21%, DCR 84%, mDoR 5.7 months, mPFS 4.0 months. Manageable safety. Activity in PDAC is real but durations are short.
- **Adagrasib (MRTX849, Krazati)**: KRYSTAL-1 PDAC cohort (n=21) reported ORR 33.3%, DCR 81%, mDoR 7.0 months. Slightly better than sotorasib in PDAC numerically.
- **Divarasib (GDC-6036)**: highest single-agent ORR in G12C tumors in early-phase work; PDAC numbers small but encouraging.
- **Olomorasib (LY3537982)**: lower-dose, deeper inhibition profile; PDAC subset reports forthcoming.

#### KRAS G12D
- **MRTX1133**: noncovalent KRAS G12D inhibitor, the first proof of concept. Phase I (NCT05737706) was terminated in 2024–2025 (Mirati was acquired and program reprioritized). Strong preclinical activity in PDAC PDX panels, single-agent responses in genetically engineered mouse models.
- **RMC-9805**: oral KRAS G12D(ON) tri-complex inhibitor. Phase I/Ib (NCT06040541) — ORR ~30% in heavily pretreated G12D-PDAC at recommended phase 2 dose presented at ASCO 2025. Combination cohorts with RMC-6236 are open.
- **ASP3082**: KRAS G12D-selective heterobifunctional degrader (Astellas). Phase I (NCT05382559) — disease control in early data; the first clinical-stage KRAS PROTAC.
- **BPI-421286**: BeiGene-partnered G12D inhibitor in early Phase I.
- **HRS-4642**: Hengrui G12D inhibitor with reported phase I activity in Chinese PDAC patients.

#### Pan-RAS / multi-selective (ON inhibitors)
- **RMC-6236 (daraxonrasib)**: RAS(ON) multi-selective tri-complex inhibitor; targets G12D, G12V, G12R, G12X, G13X, Q61X (all "G12X" variants share a common active-site geometry). Phase I in metastatic PDAC: ORR 29% across any RAS mutation, 35% in KRAS G12 PDAC, ctDNA clearance signal early. Grade ≥3 TRAEs ~34%, no discontinuations. The phase III **RASolute 302** is randomizing 2L PDAC vs chemotherapy; **RASolute 303** is randomizing 1L PDAC. Daraxonrasib is the lead candidate to become the first mainstream KRAS therapy for the bulk of PDAC.
- **RMC-7977**: a related pan-RAS(ON) molecule with broader effector blockade; preclinical only so far in PDAC.

#### Degraders / molecular glues
- **ASP3082**: see above.
- **BI-2865 / BI-2493**: pan-KRAS degraders (Boehringer Ingelheim) — preclinical, strong on-target activity in KRAS-amplified models.
- **RMC-035**: KRAS-targeted molecular glue (Revolution); preclinical.

### 2.3 KRAS resistance — what acquires when daraxonrasib or G12C drugs fail

Mechanisms documented in PDAC patients on adagrasib/sotorasib and in mouse models on MRTX1133 / RMC-6236:

- **Secondary KRAS mutations** in the switch-II pocket (Y96C, H95Q/D/R, R68S) preventing drug binding.
- **KRAS amplification** of the mutant allele, raising signaling above drug capacity.
- **Bypass via RTK reactivation** — EGFR, HER2, FGFR, MET, IGF1R, AXL re-engage MAPK/PI3K.
- **Downstream activating mutations** — PIK3CA (E545K/H1047R), BRAF V600E, MEK1/2 activating mutations, PTEN loss.
- **EMT / lineage switching** — classical → basal-like → mesenchymal transitions are observed in PDX models after MRTX1133 treatment, with epigenetic reprogramming, glutaminolysis dependence, and Wnt/AXL upregulation. Notably, in some KPC and PDX models, mesenchymal/basal cells are *more* sensitive to KRAS inhibition than classical cells, suggesting a state-dependent response.
- **Squamous transformation** in a subset of PDAC under prolonged KRAS pressure — a parallel to neuroendocrine transformation in EGFRi-treated NSCLC.

### 2.4 Combination strategies (rationale and current trials)

| Target axis | Rationale | Drugs combined with KRASi | Trial / status |
|---|---|---|---|
| SHP2 (PTPN11) | Blocks RTK→RAS feedback after KRAS inhibition; downstream of every RTK | TNO155, RMC-4630, BBP-398, JAB-3068 | Multiple Ph I/II with KRASi |
| SOS1 | Blocks GDP→GTP loading; depletes mutant KRAS-GTP pool | BI-1701963, MRTX0902 | Ph I, combos planned |
| ERK1/2 | Cuts the proximal downstream node that bypass mutations re-engage | ulixertinib, LY3214996 | Ph I |
| MEK | Same as ERK, more clinical maturity | trametinib, binimetinib | Numerous Ph I/II |
| PI3Kα | Blocks parallel pathway, especially in PIK3CA-mutant subset | alpelisib, inavolisib | Ph I |
| EGFR / HER2 | Reduces RTK feedback | cetuximab, T-DXd | Investigator-initiated |
| CDK4/6 | Cell-cycle re-entry block; addresses CDKN2A loss | palbociclib, ribociclib | Ph I/II |
| Autophagy | KRAS-driven cells are autophagy-addicted | hydroxychloroquine | Several PDAC trials |
| Anti-PD-1 / PD-L1 | KRAS inhibition reshapes the TME (less suppressive) | pembrolizumab, atezolizumab | RMC-6236 combo arms |

The mechanistic logic is that any single-node MAPK inhibitor is rapidly bypassed; vertical pathway suppression (KRAS + SHP2, or KRAS + SOS1, or KRAS + ERK) is more durable preclinically. Trials are still maturing on whether durability translates clinically.

---

## 3. KRAS clinical landscape — at a glance

### Table 3 — KRAS-directed drug landscape in PDAC

| Drug | Class | Mutation | Trial / cohort | n | ORR | mDoR / mPFS | Status (2026) |
|---|---|---|---|---|---|---|---|
| Sotorasib | G12C-OFF cov. | G12C | CodeBreaK 100 PDAC | 38 | 21% | 5.7 mo / 4.0 mo | Approved NSCLC; PDAC off-label |
| Adagrasib | G12C-OFF cov. | G12C | KRYSTAL-1 PDAC | 21 | 33.3% | 7.0 mo / 5.4 mo | Approved NSCLC; PDAC accepted use |
| Divarasib | G12C-OFF cov. | G12C | GDC-6036 PDAC | small | ~36% (small n) | NR | Phase II |
| Olomorasib | G12C-OFF cov. | G12C | LIBRETTO-432 / -411 PDAC arms | early | preliminary | NR | Phase I/II |
| MRTX1133 | G12D non-cov. | G12D | NCT05737706 | discontinued | preliminary | NR | Terminated 2024–2025 |
| RMC-9805 | G12D-ON tri-complex | G12D | NCT06040541 | ~70 PDAC at update | ~30% | maturing | Phase I/Ib, RP2D set |
| ASP3082 | G12D PROTAC | G12D | NCT05382559 | small | early | NR | Phase I escalation |
| BPI-421286 | G12D inhibitor | G12D | Ph I | small | early | NR | Phase I |
| RMC-6236 (daraxonrasib) | Pan-RAS-ON tri-complex | G12X / Q61X | RMC-6236-001 PDAC | 127 in pivotal update | 29% any RAS / 35% G12 | mPFS 8.5 mo (300mg) | Phase III (RASolute 302/303) |
| RMC-6291 | G12C-ON tri-complex | G12C | Ph I | small | early | NR | Phase I |
| BI-2865 / BI-2493 | Pan-KRAS degrader | broad | Preclinical | n/a | n/a | n/a | IND-enabling |
| RMC-035 | KRAS molecular glue | broad | Preclinical | n/a | n/a | n/a | Preclinical |
| TNO155 | SHP2 inhibitor | with KRASi | Multiple | — | combo only | — | Phase I/II |
| RMC-4630 | SHP2 inhibitor | with KRASi | Multiple | — | combo only | — | Phase I/II |
| BBP-398 | SHP2 inhibitor | with KRASi | combo with adagrasib | — | early | — | Phase I |
| BI-1701963 | SOS1 inhibitor | with KRASi or single | Ph I (BI-3406 series) | 23% SD over 18 mo | — | — | Phase I |
| MRTX0902 | SOS1 inhibitor | with adagrasib | Ph I | small | early | — | Phase I |
| Ulixertinib | ERK1/2 inhibitor | with palbociclib | NCT03454035 | small | n/a | n/a | Phase I |

Source data: ASCO GI 2025, ASCO Annual 2025, AACR 2025, NEJM (Hong/Rosen 2025 daraxonrasib PDAC), CodeBreaK 100 PDAC publication.

---

## 4. Mutant p53 — reactivation rather than restoration

TP53 is mutated in 60–75% of PDAC. About 70% of TP53 mutations are missense, producing a stable mutant protein that often gains new oncogenic functions (gain-of-function, GOF) — driving invasion, chemoresistance, and stromal remodeling. The hotspots cluster in the DNA-binding domain.

### Table 4 — TP53 hotspot mutations relevant to PDAC

| Mutation | Class | Mechanism | Frequency (pan-cancer) | Specific drugs |
|---|---|---|---|---|
| R175H | Structural | Protein misfolding | ~6% of TP53 mut | APR-246 (broad), ZMC1 (zinc chaperone) |
| R248Q / R248W | Contact | Loses DNA contact | ~6–9% | APR-246, broad reactivators |
| R273H / R273C | Contact | Loses DNA contact | ~5–7% | APR-246 |
| R282W | Structural | Destabilizes DBD | ~3% | APR-246 |
| G245S | Structural | DBD instability | ~3% | APR-246 |
| Y220C | Structural | Pocket-creating mutation | ~1.8% pan-cancer | PC14586/rezatapopt (highly selective) |
| Splice / nonsense | LOF | No protein | ~25% of TP53 mut | MDM2i not useful (no WT p53 left) |

### 4.1 Reactivators
- **Rezatapopt (PC14586, PMV Pharmaceuticals)**: small molecule that occupies the surface pocket created by the Y220C mutation, thermodynamically stabilizing the protein. Phase II PYNNACLE (NCT04585750) in TP53 Y220C solid tumors; PDAC subset is small (Y220C is ~1% of pan-cancer TP53 muts, lower in PDAC). Preliminary monotherapy responses reported in 2024–2025.
- **Eprenetapopt (APR-246)**: cysteine-binding small molecule, methylene quinuclidinone (MQ); works by alkylating cysteines including C277 to refold mutant p53. Tested in MDS/AML with azacitidine; PDAC preclinical signals; clinical PDAC data sparse.
- **ZMC1 / COTI-2**: zinc-binding chelators that restore the zinc cofactor for R175H. Preclinical.
- **Arsenic trioxide (ATO)**: was repurposed because it stabilizes specific p53 structural mutants by binding cysteines in the DBD; PDAC translational interest but no positive PDAC trial.

### 4.2 Mutant p53 degraders / MDM2 axis
For *wild-type* TP53 tumors only (which in PDAC is the minority 25–40% of patients without TP53 mutation), MDM2 inhibition can stabilize and activate p53:
- **Idasanutlin (RG7388)** — MDM2 inhibitor; PDAC trials have not reported responses.
- **KRT-232 / navtemadlin (Kartos)** — MDM2 inhibitor; PDAC not a lead indication.
- **AMG-232 / KRT-232** — same molecule.

A different strategy is to *degrade* mutant p53 itself — mutant p53 GOF requires its stability. HSP90 inhibitors (ganetespib) and HDAC inhibitors destabilize mutant p53 via the HSP90/HSP70 chaperone axis; clinical activity in PDAC has been disappointing.

The realistic 2026 picture is that mutant p53 is still a *very* hard target. The Y220C work is the strongest proof of concept; structurally selective drugs for R175H, R248Q, and R273H are open opportunities. Computational structure prediction is one of the few ways to find pocket-creating mutants — see section 12.

---

## 5. MYC — indirect approaches

MYC is amplified or overexpressed in 14–20% of PDAC, with much higher functional MYC activity (transcriptional signatures) across most tumors because of KRAS-driven MAPK output. MYC has been considered a paradigm of an undruggable transcription factor because it lacks a deep ligand-binding pocket, it dimerizes with MAX, and its half-life is short. Approaches:

- **BET bromodomain inhibitors** — BRD4, BRD2, BRD3 bind acetylated lysines on the MYC enhancer (super-enhancer) and on the MYC promoter; BET inhibitors reduce MYC transcription. Agents: MK-8628 (OTX015/birabresib), mivebresib (ABBV-075), molibresib (GSK525762), pelabresib (CPI-0610), CPI-0610. Single-agent activity in PDAC is modest; combinations (with MEK, CDK9, KRAS) are the focus.
- **CDK9 inhibitors** — CDK9 phosphorylates RNA Pol II ser-2, supporting MYC and other short-half-life oncoprotein transcription. AZD4573, KB-0742, fadraciclib (CYC065). Preclinical PDAC signals.
- **MNK1/2 inhibitors** — MNK1/2 phosphorylates eIF4E, governing MYC mRNA translation. Tomivosertib (eFT508). Clinical work mostly in lymphoma/CRC.
- **MEK + BET** or **MEK + CDK4/6** combinations — preclinical synergies because MAPK and CDK4/6 both raise MYC.
- **OMOMYC (OMO-103, Peptomyc)** — a direct-binding mini-protein that competes with c-MYC for MAX dimerization. Successfully completed Phase I — first MYC-targeted therapy to do so. Currently in a Phase Ib first-line + chemotherapy trial in metastatic PDAC, and a window-of-opportunity trial with OHSU Knight Cancer Institute began enrolling in 2025. Preclinical synergy with PARP inhibitors. This is the most distinctive direct-MYC approach in the clinic.
- **TGF-β / MYC dual regulation** — SMAD4-loss tumors upregulate MYC; the TGF-β axis acts as a brake on classical MYC programs early, then becomes prometastatic later — combined TGF-β + MYC modulation is an open computational and translational question.

---

## 6. DNA damage response (DDR) / "BRCAness"

### 6.1 PARP inhibition

The POLO trial (Golan et al., NEJM 2019, OS update JCO 2022) established maintenance olaparib for germline BRCA1/2-mutated metastatic PDAC after at least 16 weeks on platinum chemotherapy without progression. PFS HR 0.53 (p=0.004); OS was not statistically improved (HR 0.83, 19.0 vs 19.2 months) but the tail of the curve separated — estimated 3-year OS 33.9% vs 17.8%. The drug is now standard, but the population is small: only ~4–7% of PDAC has a germline BRCA1/2 alteration. Somatic BRCA mutations and PALB2 mutations expand the eligible population to ~8–10%, and some practitioners use olaparib off-label there.

### Table 5 — PARP inhibitors in PDAC

| Drug | Trial | Population | n | Result | Status |
|---|---|---|---|---|---|
| Olaparib (Lynparza) | POLO | gBRCA-mut, post-platinum | 154 | mPFS 7.4 vs 3.8 mo (HR 0.53); OS NS | FDA-approved 2019 (maintenance) |
| Rucaparib | RUCAPANC; Reiss 2021 | BRCA/PALB2, maintenance | 46 | mPFS 13.1 mo; ORR 41.7% | Off-label use |
| Niraparib | Niraparib+PD-L1 (NIRA-PD1) | platinum-treated | 80 | mPFS modest | Investigator-initiated |
| Talazoparib | TALAPRO Pan-Tumor | BRCA-mut | small | activity signal | Phase II |

### 6.2 Beyond PARP — ATR, WEE1, CHK1, POLθ

PDAC has constitutive replication stress because of KRAS-driven proliferation, MYC overexpression, and frequent TP53 loss. Targeting replication-stress nodes is synthetic lethal with this background.

- **ATR inhibitors**: berzosertib (M6620), ceralasertib (AZD6738), elimusertib (BAY-1895344), camonsertib (RP-3500). PDAC monotherapy activity is modest; combinations with gemcitabine or PARPi look more promising in HRD or ATM-mutated tumors.
- **CHK1/2 inhibitors**: prexasertib (LY2606368); preclinical PDAC activity, clinical pace slow.
- **WEE1 inhibitors**: adavosertib (AZD1775). Phase I with gemcitabine + radiation in LAPC showed feasibility and response signal especially in TP53-mutant tumors (21% vs 12% in wild-type). Newer WEE1 inhibitors (Debio-0123, ZN-c3/azenosertib) under study.
- **POLQ (POLθ) inhibitors**: ART4215, novobiocin. POLθ becomes essential in HR-deficient cells (mediates microhomology-mediated end-joining); synthetic lethality with BRCA1/2 loss makes them attractive for the same population as PARPi, with potential efficacy in PARPi-resistant disease.
- **USP1 inhibitors**: KSQ-4279, RP-3500-combo target translesion synthesis; PDAC-relevant in BRCA-mut tumors.

### 6.3 Synthetic lethality screens

PDAC-specific CRISPR and shRNA screens (DepMap, Sanger; Bryant Lab, Der Lab, Ying Lab) have identified recurrent dependencies: glutaminase (GLS1), MNK1/2, ULK1 (autophagy), GOT1 (aspartate aminotransferase), SLC7A11 (cystine import), and FASN. The "KRAS allostere" of metabolic dependencies in PDAC remains a major area for compute-enabled discovery.

---

## 7. Other targetable alterations

KRAS-wild-type PDAC (~8–10%) is enriched for actionable fusions and HER2 alterations. NGS testing of every metastatic PDAC patient is now standard of care to find these.

### Table 6 — Non-KRAS targetable alterations

| Target | Frequency in PDAC | Drug(s) | Trial / setting | Status |
|---|---|---|---|---|
| **NRG1 fusions** | 0.5–1.5% (KRAS-WT enriched) | Zenocutuzumab (MCLA-128) | eNRGy: ORR 40% in PDAC | FDA-approved Dec 2024 |
| **NTRK fusions** | <0.5% | Larotrectinib, entrectinib | Pan-tumor; PDAC subset small | Tumor-agnostic approval |
| **RET fusions** | <0.5% | Selpercatinib (LIBRETTO-001), pralsetinib | Pan-tumor | Tumor-agnostic approval |
| **BRAF V600E** | <1% (mostly KRAS-WT) | Dabrafenib + trametinib | ROAR; pan-tumor approval | Approved |
| **BRAF class II/III (non-V600)** | 2–3% | MEK + RAF dimer inhibitors (tovorafenib, plixorafenib) | Phase II | Investigational |
| **FGFR2 fusions** | <0.5% | Pemigatinib, futibatinib | FIGHT-202 (cholangio), PDAC subset rare | Pan-tumor signal |
| **ALK fusions** | <0.5% | Alectinib, lorlatinib | Case reports | Off-label |
| **ROS1 fusions** | <0.5% | Crizotinib, repotrectinib | Case reports | Off-label |
| **HER2 (ERBB2) amp / IHC 3+** | 2–4% | Trastuzumab deruxtecan (T-DXd) | DESTINY-PanTumor02: ORR 51% IHC 3+ overall | Tumor-agnostic approval 2024 |
| **HER2 mutations (S310F, V842I)** | 1% | T-DXd, neratinib | Phase II | Investigational |
| **MSI-H / dMMR** | 0.8–1.5% | Pembrolizumab | KEYNOTE-158: ORR ~18–34% in PDAC subset | Tumor-agnostic approval |
| **TMB-high (≥10 mut/Mb)** | <1% in PDAC | Pembrolizumab | KEYNOTE-158 | Tumor-agnostic approval |
| **PIK3CA mutations** | 2–4% | Alpelisib, inavolisib | Phase I/II in combos | Investigational |
| **Claudin 18.2 (IHC+)** | ~30% | Zolbetuximab | **GLEAM Phase II failed OS (Oct 2025)** | Setback |
| **CLDN18.2 (CAR-T, ADCs)** | ~30% expressing | CT041, AB011, IMC-F106C | Phase I/II | Active |
| **DLL3** | 5–10% subset (squamous/neuroendocrine) | Tarlatamab (BiTE), rovalpituzumab | Phase I | Exploratory |
| **B7-H3** | broadly expressed | Various ADCs | Phase I | Exploratory |
| **Mesothelin** | 80–90% (high in PDAC) | CAR-T (e.g., MCY-M11), ADCs, anetumab ravtansine | Multiple Ph I/II | Investigational |
| **TROP2** | 40–60% | Sacituzumab govitecan, datopotamab deruxtecan | Pan-tumor activity, PDAC tested | Investigational |
| **PRMT5 (MTAP-co-deletion)** | 25–30% (CDKN2A-co-del) | MRTX1719, AMG-193, AZ-PRMT5 | Phase I/II, PDAC-enriched cohorts | Investigational (high interest) |

The PRMT5 line deserves emphasis: ~50% of PDAC has CDKN2A deletion, and ~25–30% have *MTAP* co-deletion (MTAP sits next to CDKN2A on chromosome 9p21). MTAP loss generates methylthioadenosine accumulation, which sensitizes cells to PRMT5 inhibition. The new generation of "MTA-cooperative" PRMT5 inhibitors (MRTX1719, AMG-193) selectively target MTAP-null tumors. PDAC is one of the most enriched indications.

---

## 8. Molecular subtypes — Collisson, Bailey, Moffitt, Puleo, and what comes next

Bulk-transcriptome classification of PDAC has converged on a primary axis: **classical** (well-differentiated, GATA6-high, epithelial) vs **basal-like** (poorly differentiated, squamous-program, mesenchymal-shifted, worse prognosis).

### Table 7 — Major bulk-transcriptome PDAC classifiers

| Classifier | Year | # of subtypes | Subtype labels | Key markers | Treatment relevance |
|---|---|---|---|---|---|
| **Collisson** (Cell) | 2011 | 3 | Classical, Quasi-Mesenchymal, Exocrine-like | GATA6, KRT19; ZEB1, vim; CELA1 | First framework; QM = worst |
| **Bailey** (Nature) | 2016 | 4 | Squamous, Pancreatic Progenitor, Immunogenic, ADEX | TP63, ΔNp63, KRT5; PDX1; CD8+ infiltrate; aberrant differentiation | Squamous = worst; ADEX often contamination |
| **Moffitt** (Nat Genet) | 2015 | 2 (tumor) + 2 (stromal) | Classical / Basal-like; Normal / Activated stroma | KRT5/6, S100A2; KRT19, GATA6 | Drives the most clinically used model |
| **Puleo** (Gastroenterology) | 2018 | 4 | Pure Classical, Immune Classical, Desmoplastic, Stroma-Activated, Pure Basal-like | Combinatorial | Adds immune/stromal axes |
| **PurIST** (Rashid 2020) | 2020 | 2 (refined Moffitt) | Classical / Basal-like | 8-gene classifier (FAM3D, KRT6A, S100A2, etc.) | Clinically actionable; orderable test |
| **Chan-Seng-Yue** (Nat Genet) | 2020 | 4 (single cell) | Classical A/B, Basal-like A/B + Hybrid | Subtype-graded GATA6, KRT5 | Recognized hybrid/co-existing states |
| **CCC (consensus, 2025)** | 2025 | 2 (consensus) | Classical / Basal-like | Cross-classifier consensus | Practical unification |

Across classifiers, basal-like tumors (QM in Collisson, squamous in Bailey, Moffitt-basal, Puleo-pure-basal) align as the worst prognostic group with mPFS and mOS roughly half of classical tumors.

### 8.1 Clinical relevance

- **COMPASS / PanGen / PASS-01 trials**: showed that real-time whole-genome and RNA-seq profiling is feasible in metastatic PDAC and that classical tumors do better on mFOLFIRINOX while basal-like tumors respond poorly to all available chemotherapy. The PASS-01 trial is randomizing patients by molecular profile.
- **GATA6 IHC**: serves as a clinical surrogate for classical subtype. GATA6-low / KRT81-high tumors are basal-like.
- **Patient-derived organoids** can be subtyped and have been shown to predict drug response.
- **PurIST** is a single-sample classifier that returns Classical or Basal-like and is the most widely adopted clinical tool.

### 8.2 Lineage plasticity

Critically, classical and basal-like are not fixed states. Chan-Seng-Yue's single-cell work showed that nearly every tumor contains cells from both populations and a hybrid intermediate. Therapy (chemotherapy or KRAS inhibition) shifts the balance toward basal-like in many cases, the way that EGFR-mutant NSCLC undergoes squamous transformation. Lineage tracing in KPC mice with KRAS inhibition shows reversible plasticity. This is the central conceptual update from 2020 onward: subtype is a state, not a destiny.

---

## 9. Single-cell and spatial transcriptomics

### 9.1 The major PDAC single-cell atlases

| Study | Year | Sample | Cells | Key contribution |
|---|---|---|---|---|
| Peng et al., Cell Res | 2019 | 24 PDAC + 11 normal | 57,530 | First PDAC scRNA atlas; identified type-1 vs type-2 (malignant) ductal cells |
| Elyada et al., Cancer Discov | 2019 | Mouse + human PDAC | ~3,000 each | Defined myCAF, iCAF, and discovered apCAF |
| Steele et al., Nat Cancer | 2020 | 16 human PDAC | ~25,000 | Mapped neutrophils, macrophage diversity |
| Lin et al., Nat Commun | 2020 | 24 PDAC | 57,418 | Validated subtypes at single-cell level |
| Chan-Seng-Yue et al., Nat Genet | 2020 | 314 (bulk) + scRNA validation | — | Subtypes co-existing within tumors |
| Hwang et al., Nat Genet | 2022 | snRNA + ST in PDAC + neoadjuvant | 156,792 | Treatment-induced state reprogramming, neural-like progenitor (NRP) state |
| Williams et al., Cancer Cell | 2023 | 200+ patients | >700K | Pan-PDAC integrated atlas |
| Cui Zhou et al., Nat Genet | 2022 | 56 PDAC | >124,000 | Spatial neighborhoods, classical vs basal niches |
| Carpenter et al., Cancer Cell / Hwang lab | 2024–2025 | autopsy + ST | dozens of patients | Lineage states across primary and metastasis |
| Single-cell Atlas + CXCL10+ CAF (CCR 2025) | 2025 | integrated | — | Association of CXCL10+ fibroblasts with basal subtype |

The Hwang 2022 paper deserves special mention: it identified a "**neural-like progenitor**" (NRP) malignant state that emerges under chemotherapy/radiation pressure, characterized by axon-guidance and neural-development genes. This is the cleanest single-cell evidence that PDAC cells phenotypically transit through distinct identities under treatment.

### 9.2 Tumor cell states from single-cell data

Across atlases, recurring PDAC malignant cell states are:

- **Classical (CLA)** — GATA6+, HNF1A+, HNF4A+, KRT19+, mucin-producing
- **Basal-like (BSL)** — KRT5/6+, S100A2+, TP63 (sometimes), ANXA1+, SOX2+
- **Squamous** — TP63, ΔNp63, full keratinization
- **Mesenchymal / EMT** — VIM+, ZEB1, SNAI1/2
- **Neural-like progenitor (NRP)** — SOX2, neural progenitor markers (e.g., DCX, STMN2), axon-guidance genes
- **MYC-high** — proliferation signature, MYC-target genes
- **Stress-response / IFN-induced** — ISG15+, MX1+; emerges after CPI or chemo

In any given tumor, multiple states co-exist; bulk subtypes reflect the dominant state.

### 9.3 Spatial transcriptomics

Visium (10x), Stereo-seq (BGI), GeoMx DSP, MERFISH/Xenium (10x), and CosMx (NanoString) are all being applied to PDAC. Findings:

- **Classical and basal-like cells form spatially distinct niches** within the same tumor, with sharp boundaries on the ~100-μm scale.
- **myCAF surround tumor glands**, iCAF are at the periphery.
- **CD8+ T cells localize to tertiary lymphoid structures**, far from tumor glands.
- **Neural invasion** carries distinct gene signatures and is enriched in basal-like and NRP states.
- **Liver and lung metastases** retain primary-tumor classification but have higher mesenchymal content.

---

## 10. CAF heterogeneity — myCAF, iCAF, apCAF, and beyond

PDAC's defining histology is its desmoplastic stroma — typically 70–90% of tumor mass is non-tumor cells. Most are CAFs (cancer-associated fibroblasts). The Tuveson lab's seminal organoid + scRNA-seq work (Öhlund 2017; Elyada 2019) defined three major subtypes.

### Table 8 — PDAC CAF subtypes

| Subtype | Markers | Spatial location | Function | Origin (current model) |
|---|---|---|---|---|
| **myCAF** (myofibroblastic) | αSMA-high, IL-6-low, COL1A1, TAGLN, ACTA2 | Adjacent to tumor cells | Contractile, deposits ECM (collagen), supports tumor architecture | Activated pancreatic stellate cells (PSC) via TGF-β |
| **iCAF** (inflammatory) | αSMA-low, IL-6-high, LIF, CXCL1/2, HAS1, PDPN, PDGFRα | Distal to tumor | Secretes IL-6, LIF, CXCL family; drives JAK-STAT in tumor; immunosuppressive | PSC activated by tumor-derived IL-1α via NF-κB |
| **apCAF** (antigen-presenting) | MHC-II+, CD74+, low αSMA | Variable | Express MHC-II without classical co-stim; modulate T-cell tolerance; may convert into Treg-inducers | Mesothelial origin (recently reassigned, 2022–2023) |
| **CXCL10+ CAF** (newly defined, 2024–2025) | CXCL10, CXCL9, IFN-responsive | Near T-cell infiltrate | Associated with basal-like tumor cells; may attract effector T cells but in suppressive context | Likely subset of iCAF |
| **Cycling CAF** | MKI67+, TOP2A+ | Variable | Expanding population | Any of above |
| **Meflin+ CAF (rCAF)** | Meflin/ISLR+ | Variable | "Tumor-restraining" — opposite of myCAF | Subset of stellate cells |

The myCAF/iCAF balance is dynamic and pharmacologically modifiable: TGF-β favors myCAF; IL-1/NF-κB favors iCAF. Clinical attempts to "remove the stroma" (hedgehog inhibitors, hyaluronidase PEGPH20) have failed and in some cases worsened outcomes — depleting myCAFs accelerated tumor invasion in mouse models. Modern thinking is to *reprogram* rather than remove: vitamin D analog calcipotriol shifts iCAF → quiescent; FAK inhibitors modulate the immunosuppressive iCAF program.

---

## 11. Immune subset map

PDAC is notoriously "immune cold" with low CD8 infiltration, dense myeloid suppression, and minimal response to single-agent PD-1 blockade (ORR <5%). The single-cell immune atlas (Wang 2022 MCP, Steele 2020, Hwang 2022) maps the following:

### Table 9 — Immune subsets in PDAC

| Compartment | Subsets | Relevance |
|---|---|---|
| **CD8 T cells** | Naive, effector-memory, terminally exhausted (TOX+/PD-1-hi/TIM-3+), tissue-resident memory (TRM) | Low frequency; exhausted phenotype dominates |
| **CD4 T cells** | Th1, Th2, Th17, Treg (FOXP3+), Tfh | Treg-rich; CD4 Th1 sparse |
| **B cells** | Naive, memory, plasma; in TLS | TLS associated with better prognosis |
| **Macrophages** | M1-like (IFNG-responsive), M2-like (TAM, CD163+, MRC1+), SPP1+, FOLR2+, lipid-associated (LAM) | TAMs (M2-like) dominate; SPP1+ TAMs associated with poor outcome |
| **Monocytes** | Classical (CD14+CD16-), intermediate, non-classical | Recruit via CCL2/CCR2 axis |
| **Neutrophils / MDSC** | Classical, mature, immunosuppressive (MDSC-like; LOX-1+) | Major contributor to T-cell exclusion; high N:L ratio is prognostic |
| **Dendritic cells** | cDC1 (XCR1, CLEC9A), cDC2 (CD1c), pDC (CLEC4C), mature/CCR7+ DCs | cDC1 sparse — key bottleneck for CD8 priming |
| **Mast cells** | Tryptase+, chymase+ | Pro-tumorigenic in PDAC |
| **NK cells** | CD56-bright, CD56-dim; ILC1/2/3 | Functional NK rare in PDAC TME |

Recurrent observation: PD-1+CD8+ T cells stratify PDAC into immune-hot vs immune-cold tumors, with PD-1+CD8+ tumors having the best prognosis. The combination of PD-1+ and CD8 has been used to define three immune subtypes (S1–S3), with S1 = best.

The dominant immunosuppressive feature is a **myeloid-rich, T-cell-poor** TME with massive collagen ECM acting as a physical and chemical barrier. Therapeutic implications:
- CCR2/CCR5 inhibitors (BMS-813160, plozalizumab) to disrupt monocyte recruitment
- CSF1R inhibitors (cabiralizumab, pexidartinib) to deplete TAMs
- CXCR4 inhibitors (motixafortide, plerixafor) to disrupt CXCL12-CXCR4 (myCAF-driven exclusion)
- TIGIT, LAG-3, TIM-3 checkpoint targeting (still investigational in PDAC)
- IL-2v / NKTR-358 / mRNA neoantigen vaccines (autogene cevumeran etc.) to generate de novo T-cell responses

---

## 12. Where compute could help — [A] items

This section consolidates the compute-relevant opportunities across all of the above. Tagging convention: `[A]` = clear computational angle suitable for a volunteer-compute platform.

### 12.1 Structure & drug design

- `[A]` **KRAS mutant-allele structural ensemble simulation.** Daraxonrasib and RMC-9805 work by stabilizing tri-complexes whose interfaces are dependent on the specific RAS mutation. The induced-fit landscape of G12D, G12V, G12R, Q61H is incompletely mapped. Long-timescale MD simulations (μs to ms) of mutant KRAS-CypA-inhibitor complexes could explain mutation-selective binding and predict G12X drugs that do not yet exist (e.g., a clean G12R inhibitor for the ~15% of PDAC KRAS-mutants that are G12R).
- `[A]` **KRAS resistance mutations forecasting.** Build a structural model of every possible single-residue mutation in the switch-II pocket and the CypA interface, predict drug-binding ΔG, rank likely resistance mutations *a priori* before they appear clinically. The Y96C, H95Q, R68S clinical data give ground-truth.
- `[A]` **Pocket discovery on mutant p53 hotspots.** Rezatapopt exploits a pocket only present in Y220C. Apply pocket-prediction and cryptic-pocket-finding methods (P2Rank, fpocket, deep-learning models, MD with enhanced sampling) to R175H, R248Q, R273H, R282W, G245S — identify if any have druggable cryptic pockets analogous to Y220C.
- `[A]` **Hot-spot–specific virtual screening for p53 reactivators.** For each promising pocket, run ultra-large library docking (Enamine REAL, ZINC22, ~10⁹ compounds) on volunteer compute, with rescoring via MM/PBSA and short MD.
- `[A]` **PROTAC/molecular-glue ternary-complex modeling.** ASP3082 forms KRAS–E3 ternary complexes; the cooperativity is geometry-dependent. Simulating the conformational space of E3-PROTAC-KRAS complexes informs linker design.
- `[A]` **OMOMYC-MAX-DNA ternary dynamics.** Direct MYC inhibitors are scarce. Modeling OMOMYC binding to MYC and the perturbation of MAX dimerization and E-box DNA engagement could feed a next-gen rational design.

### 12.2 Genome / multi-omics

- `[A]` **Pan-PDAC mutation imputation and subtype prediction.** Build a federated machine-learning model that predicts molecular subtype (PurIST), GATA6 expression, and key vulnerabilities (HRD score, MTAP loss, MSI) from clinical features + limited NGS panels — extending precision medicine to the >80% of PDAC patients globally who do not get full RNA/WGS.
- `[A]` **HRD calling refinement** specifically for PDAC, which has a different mutational signature mix than breast/ovarian (more SBS1/5, less APOBEC). Compute-driven Bayesian HRD calls would improve PARPi selection.
- `[A]` **Splice-aware fusion calling from low-input cfDNA** for NRG1, NTRK, RET, FGFR2, BRAF fusions — currently missed by most cfDNA panels. A community compute project could optimize new bioinformatic pipelines using public test data.

### 12.3 Single-cell / spatial

- `[A]` **Cross-atlas integration of all published PDAC scRNA-seq** (Peng, Elyada, Steele, Lin, Chan-Seng-Yue, Hwang, Cui Zhou, Williams, others — 1M+ cells). Batch correction (Harmony, scVI), cell-type label transfer, and a *canonical PDAC reference atlas* would be a public good.
- `[A]` **Cell-state transition modeling.** Use RNA velocity (scVelo), dynamo, CellRank, or deep-learning trajectory models to map classical ↔ basal ↔ NRP transitions and identify the regulators (transcription factors, chromatin remodelers) that gate them. Predict drug perturbations that lock the favorable state.
- `[A]` **Spatial niche discovery.** Across Visium / Stereo-seq / Xenium datasets, identify recurrent spatial niches (e.g., classical+myCAF, basal+iCAF, TLS niches) and their prognostic associations.
- `[A]` **CAF reprogramming target discovery.** From integrated scRNA + perturbation atlases (Perturb-seq), identify single TFs or surface receptors whose perturbation flips iCAF → quiescent or myCAF → reverting CAFs.

### 12.4 TME and immunology

- `[A]` **PDAC immune-evasion network model.** Build a digital-twin agent-based model of PDAC TME (tumor cells, CAFs, TAMs, MDSCs, T cells) calibrated on single-cell + spatial data; simulate therapy combinations *in silico* before trial design.
- `[A]` **Neoantigen prioritization.** PDAC has low TMB but KRAS-derived neopeptides (G12D, G12V) are recurrent shared antigens with HLA-presentation predictions still imperfect. Compute-intensive MHC-I and MHC-II affinity + immunogenicity modeling (NetMHCpan, MHCflurry, BigMHC, deep learning ensembles) on the entire HLA repertoire is an ideal volunteer-compute task.
- `[A]` **TCR repertoire mining.** Public PDAC TCR-seq + matched single-cell data can train models that predict tumor-reactive TCRs for adoptive transfer.

### 12.5 Trials and clinical reasoning

- `[A]` **Federated outcome prediction.** Real-world data on KRASi response, daraxonrasib durability, and resistance can be pooled across sites with federated learning to predict who benefits and for how long.
- `[A]` **Synthetic-lethal screen aggregation.** DepMap + project SCORE + literature mining → predict the next high-yield combinations for PDAC by integrating CRISPR essentiality scores with PDAC-specific subtype profiles.

### 12.6 What is NOT a great compute fit
For honesty: drug formulation, GMP manufacturing, regulatory navigation, surgical decision-making, and patient-recruitment logistics are not where volunteer compute helps. The compute leverage is at structure prediction, large-scale virtual screening, multi-omics integration, model-based trial simulation, and TCR/MHC modeling.

---

## 13. Sources

### KRAS

- [NEJM 2023 — Sotorasib in KRAS p.G12C–Mutated Advanced Pancreatic Cancer (CodeBreaK 100 PDAC cohort)](https://www.nejm.org/doi/full/10.1056/NEJMoa2208470)
- [Adagrasib (MRTX849) in KRYSTAL-1 PDAC cohort](https://pmc.ncbi.nlm.nih.gov/articles/PMC10852394/)
- [NEJM 2025 — Daraxonrasib in Previously Treated Advanced RAS-Mutated Pancreatic Cancer](https://www.nejm.org/doi/full/10.1056/NEJMoa2505783)
- [Pan-RAS inhibitor shows early, deep molecular responses in PDAC (ASCO 2025 daily news)](https://dailynews.ascopubs.org/do/pan-ras-inhibitor-shows-early-deep-molecular-responses-pdac)
- [Revolution Medicines news on RASolute 303 first-line PDAC](https://ir.revmed.com/news-releases/news-release-details/revolution-medicines-shares-new-clinical-results-supporting/)
- [JCO 2025 — RMC-6236 ctDNA analysis in PDAC](https://ascopubs.org/doi/10.1200/JCO.2025.43.4_suppl.722)
- [Mechanisms of Resistance to Oncogenic KRAS Inhibition in Pancreatic Cancer — Cancer Discovery 2024](https://aacrjournals.org/cancerdiscovery/article/14/11/2135/749207/Mechanisms-of-Resistance-to-Oncogenic-KRAS)
- [Mechanisms of Resistance to KRAS Inhibitors — Cancer Science 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11875783/)
- [Recent anti-KRAS G12D therapies review 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11853620/)
- [SHP2 and SOS1 targets — review on KRAS combo strategies](https://blog.crownbio.com/shp2-and-sos1-targets)
- [Drugging the 'undruggable' KRAS: breakthroughs in PDAC — 2025](https://www.cancerbiomed.org/content/22/7/762)
- [MRTX1133 review and clinical perspective](https://aacrjournals.org/clincancerres/article/30/4/655/734212/A-Small-Molecule-with-Big-Impact-MRTX1133-Targets)

### TP53 and mutant p53 reactivation

- [Rezatapopt (PC14586) discovery — ACS MedChem Lett 2024](https://pubs.acs.org/doi/10.1021/acsmedchemlett.4c00379)
- [Rezatapopt restoration of Y220C-mutant p53 — Cancer Discovery 2025](https://aacrjournals.org/cancerdiscovery/article/15/6/1159/762587/Restoration-of-the-Tumor-Suppressor-Function-of)
- [Rezatapopt JMC review 2025](https://pubs.acs.org/doi/10.1021/acs.jmedchem.5c00670)

### MYC

- [Omomyc Phase I — first MYC-targeted therapy in clinic](https://www.peptomyc.com/omomyc-as-the-first-myc-targeted-theraphy-to-succesfully-complete-a-phase-i-clinical-trial/)
- [Peptomyc — OMOMYC PDAC window-of-opportunity trial with OHSU](https://www.peptomyc.com/peptomyc-announces-research-ind-approval-for-innovative-window-of-opportunity-trial-in-collaboration-with-ohsu-knight-cancer-institute-portland-oregon-usa-in-pdac-patients/)

### DDR / PARP / synthetic lethality

- [POLO trial — olaparib maintenance in gBRCA PDAC (NEJM 2019)](https://www.nejm.org/doi/full/10.1056/NEJMoa1903387)
- [POLO OS update — JCO 2022 / PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10476841/)
- [POLO erratum 2024](https://pubmed.ncbi.nlm.nih.gov/38687918/)
- [WEE1 (adavosertib) in LAPC — phase I with gemcitabine + RT](https://pubmed.ncbi.nlm.nih.gov/31398082/)
- [WEE1 inhibition review 2025](https://www.sciencedirect.com/science/article/pii/S1040842825000988)

### Other targets and approvals

- [FDA approval — Zenocutuzumab in NRG1+ NSCLC and PDAC (Dec 2024)](https://www.onclive.com/view/fda-grants-accelerated-approval-to-zenocutuzumab-for-nrg1-nsclc-and-pancreatic-adenocarcinoma)
- [eNRGy trial — continued zenocutuzumab beyond progression (ASCO GI 2026)](https://www.prnewswire.com/news-releases/continued-zenocutuzumab-treatment-beyond-progression-shows-benefit-in-patients-with-nrg1-pancreatic-cancer-and-cholangiocarcinoma-new-results-from-the-enrgy-trial-presented-at-asco-gi-302656811.html)
- [DESTINY-PanTumor02 — trastuzumab deruxtecan in HER2-expressing solid tumors (JCO 2024)](https://ascopubs.org/doi/10.1200/JCO.23.02005)
- [Astellas — GLEAM Phase II zolbetuximab in PDAC missed OS endpoint (Oct 2025)](https://newsroom.astellas.com/2025-10-13-Astellas-Confirms-Phase-2-GLEAM-Trial-Did-Not-Meet-Primary-Endpoint-of-Overall-Survival-in-Patients-with-Metastatic-Pancreatic-Cancer)
- [Claudin 18.2 expression in PDAC — biomarker assessment](https://pmc.ncbi.nlm.nih.gov/articles/PMC11979426/)
- [Palbociclib in CDKN2A-altered pancreatic/biliary — TAPUR](https://ascopubs.org/doi/full/10.1200/PO.19.00124)
- [CDK4/6 + ERK combination therapies for KRAS-mutant PDAC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9812941/)

### Genomic landscape

- [Integrated Genomic Characterization of PDAC — TCGA PAAD (Cancer Cell 2017)](https://www.cell.com/cancer-cell/fulltext/S1535-6108(17)30299-4)
- [Bailey et al — Genomic analyses identify molecular subtypes of pancreatic cancer (Nature 2016)](https://www.nature.com/articles/nature16965)
- [Comprehensive Molecular Profiling of Metastatic PDAC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11815932/)
- [Genomic landscape of KRAS WT PDAC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10315669/)

### Molecular subtypes

- [Collisson et al — Subtypes of pancreatic ductal adenocarcinoma (Nat Med 2011)](https://www.nature.com/articles/nm.2344)
- [Moffitt et al — Virtual microdissection identifies distinct PDAC subtypes (Nat Genet 2015)](https://www.nature.com/articles/ng.3398)
- [Puleo et al — Stratification of PDAC (Gastroenterology 2018)](https://www.gastrojournal.org/article/S0016-5085(18)34746-7/fulltext)
- [Chan-Seng-Yue et al — Transcription phenotypes of PDAC (Nat Genet 2020)](https://www.nature.com/articles/s41588-019-0566-9)
- [PurIST — pdacR open source two-subtype model (Comms Bio 2023)](https://www.nature.com/articles/s42003-023-04461-6)
- [Consensus molecular classifier for PDAC (Genome Medicine 2025)](https://link.springer.com/article/10.1186/s13073-025-01568-9)
- [COMPASS trial overview](https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2021.743908/full)
- [Mechanisms of PDAC subtype heterogeneity (Trends in Cancer 2022)](https://www.cell.com/trends/cancer/abstract/S2405-8033(22)00188-1)

### Single cell and spatial

- [Peng et al — single-cell RNA-seq of PDAC (Cell Research 2019)](https://www.nature.com/articles/s41422-019-0195-y)
- [Elyada et al — discovery of apCAFs (Cancer Discovery 2019)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6727976/)
- [Hwang et al — single-nucleus + spatial PDAC under neoadjuvant therapy (Nat Genet 2022)](https://www.nature.com/articles/s41588-022-01134-8)
- [Spatial transcriptomics in PDAC — review 2024](https://pubmed.ncbi.nlm.nih.gov/38942220/)
- [Spatial mapping of transcriptomic plasticity in metastatic PDAC](https://pubmed.ncbi.nlm.nih.gov/40269162/)
- [Integrated single-cell and spatial — neural invasion in PDAC (Cancer Cell 2025)](https://www.cell.com/cancer-cell/fulltext/S1535-6108(25)00270-3)
- [Pancreatic cancer single-cell atlas — CXCL10+ fibroblasts (CCR 2025)](https://aacrjournals.org/clincancerres/article/31/4/756/751743/Human-Pancreatic-Cancer-Single-Cell-Atlas-Reveals)

### CAFs

- [PDAC CAFs heterogeneity — Cell Death & Disease 2022](https://www.nature.com/articles/s41419-022-05351-1)
- [Fibroblast heterogeneity in PDAC TME — Cancer Discovery 2020](https://aacrjournals.org/cancerdiscovery/article/10/5/648/2554/Fibroblast-Heterogeneity-in-the-Pancreatic-Tumor)
- [CAF heterogeneity update — 2021/2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC8706283/)
- [Transcriptome landscape of CAFs in human PDAC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12120754/)

### Immune subsets

- [Single-cell atlas of tumor-infiltrating immune cells in PDAC (MCP 2022)](https://www.mcponline.org/article/S1535-9476(22)00066-4/fulltext)
- [Single-cell sequencing of TIL trajectory in PDAC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9547957/)
- [Distinct immune cell infiltration patterns in PDAC (Nat Commun 2024)](https://www.nature.com/articles/s41467-024-55424-2)
- [Mechanisms of T-cell exhaustion in pancreatic cancer (Cancers 2020)](https://www.mdpi.com/2072-6694/12/8/2274)

### General reviews

- [KRAS inhibition in PDAC (PMC 2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12842425/)
- [Treatment of KRAS-mutated PDAC (MDPI Cancers 2025)](https://www.mdpi.com/2072-6694/17/15/2453)
- [Recent advances and challenges in advanced PDAC trials (Cancers 2025)](https://www.mdpi.com/2072-6694/17/8/1319)
- [Targeted therapies in pancreatic cancer — precision medicine review](https://pmc.ncbi.nlm.nih.gov/articles/PMC11505516/)
- [Lustgarten — KRAS drug development in PDAC](https://lustgarten.org/from-undruggable-to-unstoppable-the-state-of-kras-drug-development-in-pancreatic-cancer/)

---

*Document last updated: May 2026. Word count target met. Compute-relevant items are tagged `[A]` in section 12. This document is a living artifact — subtype consensus, KRAS resistance taxonomy, and the immune atlas are all maturing fast.*
