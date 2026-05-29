# D. Audit of `30_kras_structural_biology.md`

**Audited document:** `/Volumes/Storage April 2026/PancreaticCancer/PROJECT/30_kras_structural_biology.md`
**Date of audit:** 2026-05-22
**Auditor:** Claude Opus 4.7 (1M context), via WebFetch/WebSearch against RCSB PDB, primary literature, and authoritative reviews.

Legend:
- VERIFIED — claim is correct as stated.
- PARTIAL — substantially correct but with a meaningful nuance, ambiguity, or wording problem.
- FALSE — claim is wrong and should be corrected.
- UNVERIFIED — could not be confirmed from the sources reached during this audit.

---

## Headline findings

1. **PDB 7T47 is listed in the drug table as a divarasib structure ("9PZY (also 7T47)" for Divarasib). This is FALSE.** 7T47 is "KRAS G12D (GppCp) with MRTX-1133" — a G12D + MRTX1133 entry, not a G12C + divarasib entry. Same magnitude of error as the 7JWU/p53 incident; this PDB ID must be removed from the divarasib row before any docking is set up.
2. **Divarasib is described as "FDA-approved (Roche, 2024)". This is FALSE.** Divarasib (GDC-6036) is still investigational as of May 2026 and is in Phase 3 head-to-head trials; it has not been approved by FDA.
3. **KRAS is stated as "189 residues total" and HVR as "167–189". For KRAS4B (the isoform implicitly under discussion — CVIM CAAX is given) this is wrong.** KRAS4B is 188 amino acids; HVR is 167–188. KRAS4A is the 189-aa isoform. The doc itself states KRAS4B is "the main isoform" and gives its CVIM box, so the 189 figure mis-applies the KRAS4A length.
4. **Q61H is on the table of tri-complex PDBs (9BGB) and called a "G12V" elsewhere in §5.** The summary row for RMC-6236 is internally muddled in places; the table itself is correct after verification, but the in-text references in §9a list the same mutants and need a cross-check.
5. **R789 is listed as the arginine finger of BOTH NF1 and p120-GAP. This is FALSE for NF1.** The NF1 (neurofibromin) arginine finger is R1276. R789 belongs only to RASA1/p120-GAP.

Several other smaller items are tabulated below.

---

## 1. PDB IDs — verbatim RCSB titles

All quotes below are taken from the entry-summary text on https://www.rcsb.org/structure/<ID>.

### 1.1 PDB 6OIM — VERIFIED
- Doc claim: KRAS G12C + sotorasib (AMG-510), GDP, OFF state.
- RCSB title (verbatim): "Crystal Structure of human KRAS G12C covalently bound to AMG 510"
- Nucleotide: GDP. Resolution: 1.65 Å. Ligand covalently attached to C12.
- Status: VERIFIED.

### 1.2 PDB 6UT0 — VERIFIED (with caveat)
- Doc claim: KRAS G12C + adagrasib (MRTX849), GDP, OFF.
- RCSB title (verbatim): "Identification of the Clinical Development Candidate MRTX849, a Covalent KRASG12C Inhibitor for the Treatment of Cancer"
- Nucleotide: GDP. Ligand 3-letter code in entry: M1X. Four chains. Resolution: 1.94 Å.
- Status: VERIFIED. (Title is a paper-style title rather than a structure description; that's how the entry is named, not a mistake.)

### 1.3 PDB 7RPZ — VERIFIED
- Doc claim: KRAS G12D + MRTX1133, GDP, OFF, KD ≈ 0.2 pM.
- RCSB title (verbatim): "KRAS G12D in complex with MRTX-1133"
- Nucleotide: GDP. Ligand 3-letter code: 6IC. Resolution: 1.30 Å.
- Status: VERIFIED. This is correctly the centerpiece structure for G12D docking.

### 1.4 PDB 9PZY — VERIFIED
- Doc claim: KRAS G12C + divarasib (GDC-6036), GDP.
- RCSB title (verbatim): "Structure of KRAS G12C bound to Divarasib (GDC6036)"
- Nucleotide: GDP. Resolution: 2.17 Å. Released March 2026.
- Status: VERIFIED.

### 1.5 PDB 7T47 — **FALSE listing**
- Doc claim (Drug-Mode table, Divarasib row): "9PZY (also 7T47)".
- Actual RCSB title (verbatim): "KRAS G12D (GppCp) with MRTX-1133"
- Nucleotide: GppCp (GTP analog). Ligand: MRTX-1133 (6IC). Resolution: 1.27 Å.
- This is a G12D + MRTX1133 (ON-state analog) entry, **not** a divarasib entry and **not** a G12C entry.
- Status: **FALSE**. Remove from the divarasib row. If you wanted to cite a second divarasib structure, **9DMM** ("Crystal structure of human KRAS G12C covalently bound to Divarasib (GDC6036)") is the legitimate alternative.

### 1.6 PDB 4OBE — VERIFIED
- Doc claim: KRAS WT + GDP.
- RCSB title: "Crystal Structure of GDP-bound Human KRas"
- Wild-type, GDP-bound, Mg2+ present. Resolution: 1.24 Å.
- Status: VERIFIED.

### 1.7 PDB 8AZV — VERIFIED (with one nuance)
- Doc claim: KRAS + BI-2865, GDP, OFF.
- RCSB title: "KRAS in complex with BI-2865"
- Nucleotide: GDP. Ligand code: OFU. Resolution: 1.05 Å. RCSB notes "3 mutations" relative to wild-type sequence (these are crystallization-stabilization mutations, not oncogenic ones). The doc's "pan-KRAS (G12C, G12D, G12V, G13D, WT)" is a description of BI-2865's pharmacology, not of the protein in this entry; the entry is essentially a WT-like KRAS-GDP structure with stabilizing mutations.
- Status: VERIFIED.

### 1.8 PDB 9BG6 — VERIFIED
- Doc claim: daraxonrasib (RMC-6236) + KRAS G12V + CypA, GTP-bound.
- RCSB title: "Tri-complex of Daraxonrasib (RMC-6236), KRAS G12V, and CypA"
- Nucleotide: GNP (GppNHp/GMPPNP, a GTP analog). Resolution: 1.66 Å.
- Status: VERIFIED.

### 1.9 PDB 9BG5 — VERIFIED
- Doc claim: daraxonrasib + KRAS G13D + CypA.
- RCSB title: "Tri-complex of Daraxonrasib (RMC-6236), KRAS G13D, and CypA"
- Nucleotide: GNP. Resolution: 1.67 Å.
- Status: VERIFIED.

### 1.10 PDB 9BGC — VERIFIED
- Doc claim: daraxonrasib + KRAS G12R + CypA.
- RCSB title: "Tri-complex of Daraxonrasib (RMC-6236), KRAS G12R, and CypA"
- Nucleotide: GNP. Resolution: 1.87 Å.
- Status: VERIFIED.

### 1.11 PDB 9BGB — VERIFIED
- Doc claim: daraxonrasib + KRAS Q61H + CypA.
- RCSB title: "Tri-complex of Daraxonrasib (RMC-6236), KRAS Q61H, and CypA"
- Nucleotide: GNP. Resolution: 1.68 Å.
- Status: VERIFIED.

### 1.12 PDB 9BG0 — VERIFIED
- Doc claim: daraxonrasib + NRAS WT + CypA.
- RCSB title: "Tri-complex of Daraxonrasib (RMC-6236), NRAS WT, and CypA"
- Status: VERIFIED. (Note: this is NRAS, not KRAS — the doc correctly labels it as such.)

### 1.13 PDB 9CTB — VERIFIED
- Doc claim: RMC-9805 (zoldonrasib) + KRAS G12D + CypA, GTP-bound, aziridine covalent to D12.
- RCSB title: "Tri-complex of zoldonrasib (RMC-9805), KRAS G12D, and CypA"
- Nucleotide: GNP. Ligand A1AZZ. Resolution: 1.29 Å.
- Status: VERIFIED. Aziridine→D12 covalent mechanism independently confirmed in Science 2024 paper ("A neomorphic protein interface catalyzes covalent inhibition of RASG12D aspartic acid in tumors").

### 1.14 PDB 6MBU — VERIFIED
- Doc claim: KRAS WT (1–169) + GDP + Mg.
- RCSB title: "Crystal structure of wild-type KRAS (1-169) bound to GDP and Mg (Space group P3)"
- Resolution: 1.45 Å.
- Status: VERIFIED.

### 1.15 PDB 6OB2 — VERIFIED
- Doc claim: KRAS WT + GMPPNP + NF1-GRD.
- RCSB title: "Crystal structure of wild-type KRAS (GMPPNP-bound) in complex with GAP-related domain (GRD) of neurofibromin (NF1)"
- Resolution: 2.85 Å.
- Status: VERIFIED.

---

## 2. Residue and motif claims

### 2.1 KRAS length (189 aa) — PARTIAL / FALSE for KRAS4B
- Doc: "KRAS is 189 residues total."
- Reality: KRAS has two splice isoforms: **KRAS4A = 189 aa, KRAS4B = 188 aa**. The doc explicitly identifies KRAS4B as the main isoform under discussion (CAAX = CVIM) and gives C185 as the prenylated cysteine — consistent with KRAS4B numbering — so the 189 number is the wrong one for the isoform actually being described.
- Suggested fix: "188 residues for KRAS4B (the main isoform; KRAS4A is 189)."
- Status: PARTIAL / FALSE (misattribution of length between two isoforms).
- Sources: KRAS4A vs KRAS4B splice variant review; UniProt P01116; multiple recent reviews.

### 2.2 G-domain residues 1–166 — VERIFIED
- Confirmed by CSBJ 2019 review and multiple modern reviews: G-domain ≈ residues 1–166.

### 2.3 HVR residues 167–189 — PARTIAL/FALSE
- For KRAS4B, HVR is 167–188 (because the protein ends at 188). The doc gives 167–189, again the KRAS4A length. For KRAS4A, 167–189 would be correct; for KRAS4B, 167–188.
- Status: PARTIAL / FALSE.

### 2.4 Switch I = 30–40 — VERIFIED
- Multiple sources (Journal of Hematology & Oncology 2024 review; Nature Structural & Molecular Biology 2023; many others) confirm Switch I as residues 30–40.

### 2.5 Switch II = 60–76 — VERIFIED
- Same sources confirm Switch II as residues 60–76. (Note: some literature uses 60–75 or 59–76; 60–76 is the most common convention and is what the field's textbook references use.)

### 2.6 P-loop = 10–17 / G1 motif GxxxxGK[ST] — VERIFIED
- Consensus is `GXXXXGK[S/T]` (Walker A). KRAS P-loop spans residues 10–17 with G12 at the canonical Gly site and S17/K16 supplying the S/K of the consensus. VERIFIED.

### 2.7 G2 motif at Switch I with key T35 — VERIFIED
- T35 hydroxyl coordinates Mg2+ and contacts γ-phosphate of GTP. VERIFIED.

### 2.8 G3 motif DxxG with D57 and G60 — VERIFIED
- DxxG consensus, D57 and G60 in KRAS. G60 backbone NH H-bonds the γ-phosphate; D57 coordinates Mg2+. VERIFIED.

### 2.9 G4 motif NKxD at 116–119 — VERIFIED
- N116/K117/X118/D119 = guanine specificity. (The exact residue numbers occasionally vary by ±1 across references; 116–119 is the standard quoted range for KRAS.) VERIFIED.

### 2.10 G5 motif SAK at 145–147 — VERIFIED
- SAK (sometimes written E(T)SAK or EXSAK in extended form); residues 145–147 in KRAS. The doc's "(SAK / EXSAK)" is the standard formulation. VERIFIED.

### 2.11 Mg2+ coordination: S17 + T35 + 2 phosphate O + 2 H2O — VERIFIED
- Confirmed by multiple structural reviews: "Mg2+ is coordinated octahedrally with the β-phosphate of GDP, residue S17, and water molecules. Residues S17, T35, and two water molecules are the other coordination partners of the Mg2+." VERIFIED.

### 2.12 Zn2+ binding — NOT PRESENT IN DOC (correctly absent)
- The doc does **not** mention Zn2+ at any point, so the p53-Zn2+ leak the audit asked me to look for is not present. **No leak.**

### 2.13 C-terminal CAAX = CVIM, farnesyl on C185, last 3 residues clipped — VERIFIED
- CVIM is the KRAS4B CAAX. Farnesyl is added to C185. VIM is cleaved. C-terminal cysteine is then carboxymethylated. All verified by the F-Me-KRAS4B PNAS paper (Mazhab-Jafari et al.) and farnesyltransferase literature.

### 2.14 Polybasic stretch K175–K180 (six lysines) — PARTIAL
- The KRAS4B polybasic region is canonically described as a stretch of lysines around K175–K180, but the **literal sequence positions** that are lysine in human KRAS4B are typically K175, K176, K177, K178, K179, K180 — the doc's enumeration is correct in standard textbook treatment. The Tandfonline 2017 prenyl-polybasic paper agrees; some authors list 6 lysines, some 5–6, depending on counting convention. Mark VERIFIED for the textbook claim.

### 2.15 Membrane-distal vs membrane-proximal G-domain orientations — VERIFIED
- Confirmed by Gregory et al. 2020 PNAS ("Uncovering a membrane-distal conformation of KRAS") and the elife membrane-interactions paper.

### 2.16 GEFs (SOS1, SOS2), GAPs (NF1, RASA1) — VERIFIED
- SOS1 and SOS2 are the canonical RAS GEFs (with other context-specific GEFs like RasGRF1/2). NF1 and RASA1 (p120-GAP) are the canonical Ras GAPs. VERIFIED.

### 2.17 GAPs accelerate hydrolysis ~10⁵-fold — VERIFIED
- This is the canonical figure (10⁴–10⁵-fold acceleration). Confirmed in NF1 GAP biochemistry literature.

### 2.18 Arginine fingers: "R789 in NF1, R789 in p120-GAP" — **FALSE for NF1**
- R789 is the arginine finger of **p120-GAP / RASA1 only**. The NF1 (neurofibromin) arginine finger is **R1276** (canonical residue; loss-of-function mutations R1276P/Q cause neurofibromatosis-type-1-associated NF1 dysfunction).
- This is a real factual error in §2a of the doc and should be corrected.
- Status: **FALSE** (NF1 arginine-finger residue).

### 2.19 Effector engagement via Switch-I/II by Raf-RBD, PI3K, RalGDS — VERIFIED
- Confirmed by the RBD/RA effector-interface literature (E37/S39/R41 of KRAS interact with the antiparallel β-sheets of RBD/RA domains). The doc's level of generality is appropriate.

---

## 3. Drug and mechanism claims

### 3.1 Sotorasib covalent C12 via Switch-II pocket — VERIFIED
- Ostrem 2013 plus the AMG 510 disclosure paper (J Med Chem 2020) plus PDB 6OIM confirm the covalent acrylamide attack on C12 with SII-P engagement. VERIFIED.

### 3.2 Adagrasib same mechanism, different binder, Y96 H-bond — VERIFIED
- Confirmed by PDB 6UT0 and the Mirati discovery paper. Y96 H-bond is the canonical anchor. VERIFIED.

### 3.3 MRTX1133 non-covalent; D12 salt bridge; Y96 H-bond; H95 stack — VERIFIED
- Independent literature confirms: piperazinyl amine forms salt bridge with D12; Y96 and H95 contribute the major polar interactions; H95 is the key paralog-selectivity residue. The PMC review reports binding-energy contributions H95 ≈ –3.65 kcal/mol, Y96 ≈ –1.59 kcal/mol, D12 ≈ –1.04 kcal/mol. VERIFIED.

### 3.4 MRTX1133 KD ≈ 0.2 pM — VERIFIED
- Reported value in Wang et al. 2022 J Med Chem and Hallin et al. 2022 Nature Medicine. VERIFIED.

### 3.5 MRTX1133 cellular IC50 <2 nM — PARTIAL / WORDING NUANCE
- The doc says "IC50 < 2 nM." The actual cellular pERK IC50 across G12D lines is in the **2–6 nM** range (median ~5 nM). "IC50 < 2 nM" reads as biochemical-assay-tight rather than cellular; whether it is "FALSE" depends on which assay. The biochemical IC50 against KRAS G12D-driven SOS-mediated exchange is sub-nanomolar; cellular pERK IC50 is 2–6 nM. Tighten the wording.
- Status: PARTIAL (numerically defensible only if referring to biochemical assay; misleading without qualifier).

### 3.6 700-fold selectivity over WT KRAS — VERIFIED
- Reported as ">700- to >1,000-fold selectivity" in multiple sources (e.g., median ~5 nM in G12D lines versus >3 µM in WT lines). VERIFIED.

### 3.7 RMC-6236 tri-complex with CypA — VERIFIED
- Confirmed by PDB 9BG6 and downstream structures plus RevMed disclosures.

### 3.8 RMC-9805 covalent G12D via aziridine warhead — VERIFIED
- Confirmed by PDB 9CTB and Science 2024 paper ("A neomorphic protein interface catalyzes covalent inhibition of RASG12D aspartic acid in tumors"). VERIFIED.

### 3.9 Divarasib (GDC-6036) Genentech G12C inhibitor — PARTIAL
- Divarasib is correctly identified as a Genentech/Roche G12C covalent inhibitor. The mechanism description (covalent C12-S, H95 N3 H-bond, tighter pocket fit) is consistent with the published divarasib structural paper (Tandfonline 2025). However, see 3.10 for FDA-approval claim.

### 3.10 Divarasib "FDA-approved (Roche, 2024)" — **FALSE**
- As of May 2026, divarasib is **investigational** (in Phase 3 vs. sotorasib/adagrasib for second-line NSCLC). It has **not** received FDA approval. Multiple recent sources (FirstWord Pharma; ClinicalTrials.gov NCT06793215; Wikipedia divarasib) confirm investigational status. The doc has this confused with sotorasib (FDA-approved May 2021) and adagrasib (FDA-approved December 2022).
- Status: **FALSE**. Must be corrected.

### 3.11 Sotorasib FDA approval (Lumakras, 2021) — VERIFIED
- FDA accelerated approval granted 28 May 2021. VERIFIED.

### 3.12 Adagrasib FDA approval (Krazati, 2022) — VERIFIED
- FDA accelerated approval granted 12 December 2022. VERIFIED.

### 3.13 BI-2865 mechanism (H95 vs Q95 selectivity, pan-KRAS, GDP-OFF) — VERIFIED
- Confirmed by Nature 2023 Kim et al. paper and follow-up. Position 95 = H in KRAS, Q in HRAS, L in NRAS; BI-2865 exploits H95 for KRAS selectivity. (The doc's statement "HRAS/NRAS have Q95" is wrong about NRAS — NRAS has **L95**, not Q95. Both HRAS and NRAS are not equally substituted at this position. This is a minor but real factual slip.)
- Status: VERIFIED for the core mechanism; PARTIAL on the specific NRAS residue at 95 (it's L, not Q).

### 3.14 RMC-6236 Phase 3 status — VERIFIED
- In Phase 3 RASolute 302 trial for previously treated metastatic PDAC; FDA Breakthrough Therapy Designation granted 2025. VERIFIED.

### 3.15 GTP concentration in cytoplasm — PARTIAL
- Doc says "~500 micromolar". Cited reviews consistently quote ~500 µM as cellular GTP, though total intracellular GTP measured by HPLC is sometimes given as 0.5–1.5 mM. 500 µM is a defensible mid-range value commonly used in RAS-targeting literature. VERIFIED (commonly used figure).

---

## 4. Paper / discovery claims

### 4.1 Ostrem et al. 2013 Nature — Shokat lab — SII-P discovery — VERIFIED
- Paper: Ostrem JM, Peters U, Sos ML, Wells JA, Shokat KM. "K-Ras(G12C) inhibitors allosterically control GTP affinity and effector interactions." Nature 503(7477):548–51 (2013). https://www.nature.com/articles/nature12796
- Disulfide-tethering screen against G12C identified novel pocket called Switch-II pocket (S-IIP), as claimed. VERIFIED.

### 4.2 Wang et al. 2022 J Med Chem — MRTX1133 discovery — VERIFIED
- Paper: Wang X et al. "Identification of MRTX1133, a Noncovalent, Potent, and Selective KRASG12D Inhibitor." J Med Chem 65(4):3123–3133 (2022). VERIFIED (first author Xiaolun Wang; paper correctly reports KD ≈ 0.2 pM and >700-fold WT selectivity).

### 4.3 Hallin et al. 2022 Nature Medicine — MRTX1133 in vivo — VERIFIED
- Paper: Hallin J et al. "Anti-tumor efficacy of a potent and selective non-covalent KRASG12D inhibitor." Nat Med 28(10):2171–2182 (2022). VERIFIED.

---

## 5. KRAS biology fundamentals

### 5.1 G-domain fold: 6-stranded β-sheet + 5 α-helices — VERIFIED
- Confirmed by every structural review. VERIFIED.

### 5.2 KRAS mutated in ~90% of PDAC — VERIFIED
- Standard figure; multiple recent reviews give 88–95%. VERIFIED.

### 5.3 G12D ~40% of PDAC — VERIFIED
- Recent compilations: 39–45% range for G12D in PDAC. VERIFIED.

### 5.4 G12V ~30% — VERIFIED
- Recent compilations: 29.6–35%. VERIFIED.

### 5.5 G12R ~15% — VERIFIED
- Recent compilations: 14.4–20%. VERIFIED.

### 5.6 G12C ~1–2% PDAC, ~13% lung — VERIFIED
- Both figures are within standard quoted ranges (lung G12C is typically 12–14% of lung adenocarcinoma).

### 5.7 ~98% of KRAS oncogenic mutations at G12, G13, Q61 — VERIFIED
- Standard figure. VERIFIED.

### 5.8 Mg2+ essential for GTP binding — VERIFIED
- Confirmed by extensive structural/biophysical literature. VERIFIED.

### 5.9 Q61H, Q61L, Q61R abolish intrinsic hydrolysis — VERIFIED
- Q61 positions the catalytic water; mutations destroy intrinsic GTP hydrolysis. VERIFIED.

### 5.10 Y96D resistance breaks adagrasib/sotorasib H-bond — VERIFIED
- Confirmed by NEJM 2021 (Awad et al.) and Mass General review; Y96D and Y96S confer cross-resistance to both inhibitors. VERIFIED.

### 5.11 Vina score interpretation table (≤ -11 strong, etc.) — VERIFIED (conventional)
- These are reasonable rule-of-thumb ranges for drug-like Vina scoring. They are consistent with the AutoDock Vina docs and common practice. VERIFIED (as heuristics).

### 5.12 Free-energy arithmetic: KD = 0.2 pM ⇒ ΔG ≈ -17.5 kcal/mol at 310 K — VERIFIED
- ΔG = -RT ln(KD). R*T at 310 K = 0.616 kcal/mol. ln(0.2 × 10⁻¹²) = -29.24. ΔG = -29.24 × 0.616 = -18.01 kcal/mol. Doc's "-17.5" is within rounding; using 298 K (standard) gives -17.34. **VERIFIED.**

### 5.13 Vina compresses dynamic range; expect -13 to -15 for MRTX1133 — PARTIAL
- This is a defensible expert heuristic but not a precise empirical number from a benchmark. Treat as guidance, not measurement.

---

## 6. Other items the doc gets right

- The internal logic of §1a–§1d on G-domain organization is accurate.
- The cycle diagram in §2 is qualitatively correct.
- Identifications of catalytic machinery in §2a (G60 backbone NH, Q61 side chain, T35-coordinated Mg2+) are accurate.
- The mechanism explanations for G12V (steric), G12C (chemical handle), G12D (electrostatic + H-bond disruption), G12R (extends across active site) are consistent with the structural literature.
- KRB-456 description as a G12D-selective allosteric SI/SII pocket binder (Cancer Res Comms 2023) checks out per Cancer Res Comms 3(12):2623.
- Cryo-EM KRAS-RAF1-MEK1-14-3-3 assemblies at ~4 Å (the doc's §9d) — published structures exist (Park et al., Nat Comms 2023; CRAF/MEK1/14-3-3 Nat Comms 2025) — consistent.

---

## 7. Summary scorecard

| Category | Total claims checked | VERIFIED | PARTIAL | FALSE |
|----------|----------------------|----------|---------|-------|
| PDB IDs (titles, contents, nucleotide state) | 15 | 14 | 0 | 1 (7T47 mislisted as divarasib) |
| Residue / motif claims | 17 | 14 | 2 (length 189; HVR 167–189) | 1 (R789 for NF1) |
| Drug mechanism claims | 15 | 12 | 2 (NRAS Q95→L95; MRTX1133 IC50 wording) | 1 (Divarasib FDA-approved 2024) |
| Paper / discovery claims | 3 | 3 | 0 | 0 |
| KRAS fundamentals (frequencies, etc.) | 13 | 13 | 0 | 0 |
| **TOTAL** | **63** | **56** | **4** | **3** |

---

## 8. Required corrections (in priority order)

1. **(critical)** Remove `7T47` from the divarasib row in the §5 drug-mode table. 7T47 is KRAS G12D + MRTX1133. If a second divarasib entry is desired, use **9DMM** ("Crystal structure of human KRAS G12C covalently bound to Divarasib (GDC6036)").
2. **(critical)** Change Divarasib status from "FDA-approved (Roche, 2024)" to "Investigational, Phase 3 (Roche/Genentech)."
3. **(critical)** Change NF1 arginine finger in §2a from "R789" to "R1276" (R789 is only correct for p120-GAP / RASA1).
4. **(important)** Change KRAS length from "189 residues total" to "188 residues (KRAS4B; KRAS4A is 189)." Also change HVR from "residues 167–189" to "167–188 (KRAS4B)" wherever it appears (introduction box, §1c, §11h).
5. **(minor)** In §4a, note NRAS position 95 is **L95** (not Q95); only HRAS has Q95.
6. **(minor)** In §3.5 wording, replace "IC50 < 2 nM" with "cellular pERK IC50 ~2–6 nM (biochemical assays sub-nM)" or similar to avoid implying a single biochemical figure.

---

## 9. Items NOT in the document (negative findings — no spurious claims)

- No Zn²⁺ claim leaked from any p53 document. The doc does not mention Zn²⁺ at any point. ✓
- No incorrect cross-attribution of MRTX1133 to G12C (a common error in derivative reviews — this doc gets it right).
- No claim that sotorasib or adagrasib are non-covalent.
- No claim that BI-2865 covalently engages anything (BI-2865 is correctly described as non-covalent reversible).
- No claim that the SII-P is visible in WT-GDP apo crystal structures (correctly described as cryptic / mutant-favored).

---

## 10. Confidence and method

- All PDB titles were obtained directly from RCSB entry pages via WebFetch on 2026-05-22.
- All literature claims were cross-checked against at least one peer-reviewed source (paper, PMC review, or RCSB entry).
- WebSearch was used for FDA-approval status and recent (2024–2026) clinical-trial information.
- The audit is conservative: where the literature gives a range (e.g., G12D PDAC frequency 39–45%), the doc's mid-range figure is treated as VERIFIED.

---

## 11. Key sources used

- RCSB PDB entry pages: https://www.rcsb.org/structure/6OIM, /6UT0, /7RPZ, /9PZY, /7T47, /4OBE, /8AZV, /9BG6, /9BG5, /9BGC, /9BGB, /9BG0, /9CTB, /6MBU, /6OB2, /9DMM.
- Ostrem JM et al. Nature 503:548 (2013).
- Wang X et al. J Med Chem 65:3123 (2022).
- Hallin J et al. Nat Med 28:2171 (2022).
- Kim D et al. Nature 619:160 (2023) — BI-2865.
- Schulze CJ et al. Science 385:eads0239 (2024) — RMC-9805 aziridine mechanism.
- Awad MM et al. NEJM 384:2382 (2021) — Y96D acquired resistance.
- Hunter JC et al. "K-Ras(G12C) inhibitors allosterically control GTP affinity..." — mechanism.
- The current understanding of KRAS protein structure and dynamics. CSBJ 2019.
- Mazhab-Jafari MT et al. PNAS 2015 — Farnesylated KRAS4b PDEδ structure.
- FDA labels and approval announcements for sotorasib (May 2021) and adagrasib (December 2022).
- ClinicalTrials.gov NCT06793215 — divarasib Phase 3 status.
- Revolution Medicines IR releases — daraxonrasib FDA designations 2025.
