# K. Audit of `31_mutant_p53_structural_biology.md`

**Audit date:** 2026-05-22
**Auditor:** comprehensive fact-check against RCSB PDB, IARC TP53 database, ClinicalTrials.gov, PubMed
**Document audited:** `/Volumes/Storage April 2026/PancreaticCancer/PROJECT/31_mutant_p53_structural_biology.md`
**Doc length:** 843 lines

## Verdict at a glance

This document has **massive PDB ID problems**. The 7JWU error caught in the previous audit was not isolated — there are **at least 8 more wrong PDB IDs** with the same level of severity (some are entirely different proteins like botulinum toxin, ricin A, and PARP15). The document needs a top-to-bottom PDB ID purge before it can be trusted.

The high-level science (DBD architecture, Zn²⁺ coordination, hotspot biology, Y220C cavity concept, rezatapopt mechanism) is largely correct. The clinical trial framing (PYNNACLE, APR-246 MDS failure) is largely correct. But the **specific PDB attributions** that a docker would actually use are wrong in roughly **half the cases checked**.

There is also one **fabricated clinical claim**: that PMV Pharmaceuticals has been "acquired by Pfizer." This is false. PMV is independent (NASDAQ: PMVP) as of 2025 SEC filings. Multiple paragraphs in the doc reference "Pfizer/PMV" or "Pfizer's 2023 acquisition." Remove all of these.

---

## Tally

| Category | Total claims checked | Verified | Partial / imprecise | False / wrong | Unable to verify |
|---|---|---|---|---|---|
| PDB IDs | 26 | 13 | 1 | **11** | 1 |
| Drug clinical status | 12 | 9 | 2 | 1 (Pfizer/PMV) | 0 |
| Mutation frequencies | 9 | 5 | 4 | 0 | 0 |
| Mechanism / architecture | 14 | 12 | 2 | 0 | 0 |
| Discovery / paper attributions | 8 | 6 | 1 | 1 | 0 |
| **Totals** | **69** | **45** | **10** | **13** | **1** |

13 outright wrong claims, 10 partial/imprecise, 45 verified.

---

## Top errors (PDB first, ordered by severity)

1. **PDB 4LO8 is not a p53 G245S structure.** RCSB title: *"Structure of a Bimodular Botulinum Neurotoxin Complex"* — a Clostridium botulinum 14-subunit toxin. The doc cites 4LO8 in § 4e as "PDB: 4LO8" for G245S. The actual G245S structures are **2J1Y** (T-p53C-G245S, Joerger/Fersht series) and **7DHY** (arsenic-bound G245S). Same severity as the 7JWU error.

2. **PDB 4LO9 is not R175H.** RCSB title: *"Human p53 Core Domain Mutant N235K"* — a V157F/N235K/N239Y rescue-mutation construct. The doc cites 4LO9 in § 4a (R175H), § 14c (PyMOL example loading 4LO9 to compare WT vs R175H), and § 14f ("4LO9 R175H DBD reference"). **No clean single-mutation R175H crystal structure currently exists in the PDB** under the IDs cited; the published R175H structures are typically multi-mutant rescue constructs. Same severity as the 7JWU error.

3. **PDB 7XZS is not an MQ/APR-246 p53 structure.** RCSB title: *"Crystal structure of Ricin A chain bound with (2-amino-4-oxo-3,4-dihydropteridine-7-carbonyl)-L-tyrosine"* — a plant toxin from *Ricinus communis*. The doc cites 7XZS in § 7 (drug table), § 13b ("PDB 7XZS is a more recent co-crystal of MQ with DBD"), and § 14f. Same severity as the 7JWU error.

4. **PDB 6FF9 is not MQ/APR-246-modified DBD.** RCSB title: *"The Crystal Structure of the R280K Mutant of Human p53 Explains the Loss of DNA Binding"* — it is an R280K p53 mutant **without any drug**, just bound to Zn²⁺. The doc cites 6FF9 in § 7 ("**6FF9** (early MQ-DBD)"), § 7a, § 14d ("APR-246 / MQ-modified DBD"), and § 14f. The correct co-crystal of APR-246/MQ with p53 DBD that actually exists is **PDB 6Q1V** (or similar from the Bauer 2018 paper); the doc has substituted a different mutant structure entirely.

5. **PDB 8A32 is JC769, not rezatapopt.** RCSB title: *"p53 cancer mutant Y220C in complex with iodophenol-based small-molecule stabilizer JC769"* (Balourdas/Joerger/SGC 2022). The bound ligand is KVA (4-[3,4-bis(fluoranyl)pyrrol-1-yl]-3,5-bis(iodanyl)-2-oxidanyl-benzoic acid). The doc cites 8A32 in multiple places (§ 4f, § 6c, § 7, § 7a, § 8a, § 12, § 13a, § 14b, § 14f, § 15a) as "the rezatapopt co-crystal." The actual rezatapopt co-crystal structures are **PDB 9BR4 (with PC-9859, the lead optimization compound) and 9BR3 (with PC-10709).** 8A32 is in the same allele-selective Y220C stabilizer family but is JC769, a different chemotype from a different lab. Important docking implication: re-docking the ligand from 8A32 will recover JC769, not rezatapopt. The validation gate § 15a as written is misleading.

6. **PDB 5LAW is not milademetan.** RCSB title: *"Novel Spiro[3H-indole-3,2'-pyrrolidin]-2(1H)-one Inhibitors of the MDM2-p53 Interaction: HDM2 (MDM2) IN COMPLEX WITH COMPOUND 14"* — bound ligand is 6SJ, a Boehringer Ingelheim spiro-oxindole research compound. Milademetan (DS-3032b) has its own PDB entries (search "DS-3032" returns 7SUW and others) but 5LAW is not one. Doc § 7 / § 9 / § 15g all cite 5LAW as milademetan; wrong.

7. **PDB 4ZYC is not AMG-232 (navtemadlin).** RCSB title: *"Discovery of dihydroisoquinolinone derivatives as novel inhibitors of the p53-MDM2 interaction with a distinct binding mode: Hdm2 (MDM2) complexed with cpd5"* — bound ligand is a dihydroisoquinolinone, not the piperidinone scaffold of AMG-232. The actual AMG-232 co-crystals are 4OAS (the foundational compound 25 structure) and 5TRF; 4WT2 is the close analog AM-7209. Doc § 7 / § 9 cite 4ZYC for AMG-232; wrong.

8. **PDB 1RV1 is not Nutlin-3a.** RCSB title: *"CRYSTAL STRUCTURE OF HUMAN MDM2 WITH AN IMIDAZOLINE INHIBITOR"* — bound ligand is IMZ, a bromine-substituted imidazoline; it is from the Vassilev 2004 imidazoline series **but not Nutlin-3a specifically**. Doc § 9 cites 1RV1 as "Nutlin-3a + MDM2"; partially right (imidazoline class, same paper era) but the specific compound is not Nutlin-3a.

9. **PDB 4HG7 is Nutlin-3a, not idasanutlin (RG7388).** RCSB title: *"Crystal Structure of an MDM2/Nutlin-3a complex"*. The doc cites 4HG7 ten places as the idasanutlin/RG7388 structure. RG7388 is a pyrrolidine; the closest published pyrrolidine MDM2 structure is **PDB 4JRG** (RO5313109, same Roche series, earlier compound). I did not find a published PDB structure deposit specifically for idasanutlin/RG7388 itself; this part of the table should be flagged unverifiable rather than asserted as 4HG7.

10. **PDB 5VK0 is not siremadlin (HDM201).** RCSB title: *"Crystal structure of human MDM2 in complex with a 12-mer lysine-cysteine side chain dithiocarbamate stapled peptide inhibitor PMI"* — a stapled peptide, not a small molecule. The actual siremadlin PDB is **5OC8** per the public literature.

11. **PDB 7Z1V is not BI-907828 (brigimadlin).** RCSB title: *"PARP15 catalytic domain in complex with OUL208"* — a poly(ADP-ribose) polymerase, completely unrelated to MDM2. Doc § 9 cites 7Z1V as brigimadlin; very wrong.

12. **PDB 2J1X is not R248Q.** RCSB title: *"Human p53 core domain mutant M133L-V203A-Y220C-N239Y-N268D"* — actually contains a Y220C mutation as part of a thermostabilized multi-mutant construct, plus 4 suppressor mutations. The doc cites 2J1X for R248Q (§ 4b, "R248Q crystal structures (PDB 2J1X, 4IBT) overlay almost perfectly on WT") and also lists it elsewhere. This claim conflates two different mutants. The single-mutation Y220C reference is **2J1W** (per Joerger/Fersht 2006). PDB **4IBT** is also wrong: title is *"Human p53 core domain with hot spot mutation R273H and second-site suppressor mutation T284R"* — i.e. R273H, not R248Q.

13. **PDB 4MZR is not R273C.** RCSB title: *"Crystal structure of a polypeptide p53 mutant bound to DNA"* — contains S121F and V122G L1 mutations, not R273C. Doc § 4c cites 4MZR as R273H reference; wrong.

14. **PDB 4MZI is not a generic mutant p53 reference.** RCSB title: *"Crystal structure of a human mutant p53"* — contains an engineered p53FG with 8 substitutions (S121F, V122G core engineered, designed for enhanced DNA binding affinity). Not appropriate as a "mutant p53 reference structure." Doc § 1c table mentions 4MZI alongside mutant references; misleading.

15. **PMV Pharmaceuticals "acquired by Pfizer" is fabricated.** Doc § 6c says "PMV Pharmaceuticals (now Pfizer)" and § 13a says "Pfizer's 2023 acquisition of PMV Pharmaceuticals." Neither is true. PMV is an independent publicly traded company (NASDAQ: PMVP) per 2024 and 2025 SEC 8-K filings; rezatapopt is still being developed by PMV Pharma, not Pfizer.

---

## Detailed claim-by-claim verification

### Architectural / fundamental claims

| Claim | Status | Evidence |
|---|---|---|
| 393 residues total | ✅ Verified | Multiple primary refs; canonical UniProt P04637 |
| TAD1 (1-40), TAD2 (41-60) | ⚠️ Partial | Most references state TAD1 1-40 (or 1-42), TAD2 40-61 (or 41-60); slight boundary disagreements normal |
| PRD 61-94 | ✅ Verified | Common literature definition (61-92 or 61-94) |
| DBD 94-312 | ⚠️ Partial | Doc says 94-312. Literature splits: structural papers often say **94-292** (limit of well-folded β-sandwich); molecular biology papers often say **94-312**. Both used; doc number is defensible. |
| TD 323-356 | ✅ Verified | Both 323-356 and 326-356 used in literature |
| CTD 363-393 | ✅ Verified | Standard |
| Zn²⁺ coordination C176/H179/C238/C242 | ✅ Verified | Multiple primary refs; canonical |
| DBD = immunoglobulin-like β-sandwich | ✅ Verified | Cho 1994 PNAS, etc. |
| **WT DBD melting temp ~44°C** | ✅ Verified | Multiple DSC/DSF refs report 42-45°C, with 44°C the most commonly cited single value |
| TP53 on chromosome 17p13.1 | ✅ Verified | Standard genomic location, multiple refs |
| PDAC TP53 mutation rate ~70-75% | ✅ Verified | PNAS / TCGA studies report 63-74%; ~70-72% is the modal value |
| 1TUP = Cho 1994 WT p53-DBD on DNA | ✅ Verified | RCSB title confirms |
| 2OCJ = WT p53-DBD apo | ✅ Verified | RCSB title confirms |

### Mutation frequency claims (IARC TP53 / TCGA)

| Claim | Status | Evidence |
|---|---|---|
| R175H ~5% all cancers | ⚠️ Partial | IARC database puts R175H at **7.5%** of all TP53 mutations (highest single SNV); ~5% across all cancers including non-TP53-mutant tumors is plausible but the doc's framing is ambiguous. Worth being explicit: "5% of TP53-mutant tumors" or "~7.5% of TP53 missense mutations." |
| R248Q ~7% all cancers | ⚠️ Partial | IARC ~7% of TP53 mutations; "all cancers" framing inflates |
| R248W ~7% | ⚠️ Partial | Similar — combined R248 (Q+W) is ~10-12% of TP53 mutations |
| R273H ~5% | ✅ Verified | ~5-6% of TP53 mutations per IARC |
| R273C ~1% | ✅ Verified | Plausible per IARC |
| R282W ~3% | ✅ Verified | Standard literature |
| G245S ~3% | ✅ Verified | Standard |
| **Y220C ~1.5%** | ✅ Verified | ~1% of solid tumors (some sources say 1.5%); ~125,000 new cancer cases per year worldwide. Doc figure is correct. |
| V143A ~1% | ✅ Verified | Plausible, rare |
| R249S ~3% | ⚠️ Partial | True overall, but R249S is **enriched in aflatoxin-exposed HCC (~50%)** — doc gets this right in § 4h |

### PDB ID verifications

| PDB | Doc claim | RCSB title (verified) | Verdict |
|---|---|---|---|
| **2VUK** | Y220C + PhiKan083, Boeckler 2008 | "Structure of the p53 core domain mutant Y220C bound to the stabilizing small-molecule drug PhiKan083" (Joerger, Boeckler, Fersht, deposited 2008-05-26) | ✅ Verified — anchor structure |
| **8A32** | Y220C + rezatapopt (PC14586) | "p53 cancer mutant Y220C in complex with iodophenol-based small-molecule stabilizer **JC769**" (Balourdas, Stephenson Clarke, Baud, Knapp, Joerger / SGC, 2022) | ❌ **Wrong drug** — JC769 (ligand KVA), not rezatapopt. Doc must be reworked. |
| **5G4N** | Y220C + difluorinated PhiKan083 | "Crystal structure of the p53 cancer mutant Y220C in complex with a difluorinated derivative of the small molecule stabilizer Phikan083" | ✅ Verified |
| **5G4O** | Y220C + trifluorinated PhiKan083 | "...trifluorinated derivative of the small molecule stabilizer Phikan083" | ✅ Verified |
| **5ABA** | Y220C | "Structure of the p53 cancer mutant Y220C with bound small-molecule stabilizer PhiKan5149" | ✅ Verified (with specific ligand name PhiKan5149) |
| **5AOK** | Y220C | "Structure of the p53 cancer mutant Y220C with bound small molecule PhiKan7099" | ✅ Verified |
| **5O1C** | Y220C + MB-series | "p53 cancer mutant Y220C in complex with compound MB184" | ✅ Verified — MB-series compound MB184 (note: ligand designation is 9GZ which is an aminobenzothiazole-related — title says MB184) |
| **5O1H** | Y220C + MB-series | "p53 cancer mutant Y220C in complex with compound MB539" | ✅ Verified |
| **5O1I** | Y220C + MB-series | "p53 cancer mutant Y220C in complex with compound MB710" | ✅ Verified (aminobenzothiazole) |
| **8DC4** | "Aprea-licensed compound" | "Crystal structure of p53 Y220C covalently bound to carbazole KG3" (Guiley & Shokat, UCSF, 2022) | ⚠️ Y220C confirmed, but ligand is **carbazole KG3 from Shokat lab (UCSF)**, NOT an Aprea compound. Aprea doesn't deal in Y220C. This is the Cancer Discovery 2023 paper (Guiley & Shokat). Fix attribution. |
| **1TUP** | WT p53-DBD on DNA (Cho 1994) | "Crystal structure of a p53 tumor suppressor-DNA complex" (Cho, Gorina, Jeffrey, Pavletich, Science 1994) | ✅ Verified |
| **2OCJ** | WT p53-DBD apo | "Structure of the human p53 core domain in the absence of DNA" | ✅ Verified |
| **4LO9** | R175H DBD | "Human p53 Core Domain Mutant N235K" (V157F/N235K/N239Y suppressor construct) | ❌ **Wrong** — not R175H. |
| **4LO8** | G245S DBD | "Structure of a Bimodular Botulinum Neurotoxin Complex" | ❌ **Wrong protein entirely** (Clostridium botulinum, not p53) |
| **2BIM** | R273H DBD | "human p53 core domain mutant M133L-V203A-N239Y-N268D-R273H" | ⚠️ Contains R273H but in a 5-mutation rescue construct. Not a clean R273H reference. |
| **2J1X** | R248Q DBD | "Human p53 core domain mutant M133L-V203A-Y220C-N239Y-N268D" | ❌ **Wrong mutation** — Y220C+ thermostabilizing mutations, not R248Q |
| **4IBT** | R248Q DBD | "Human p53 core domain with hot spot mutation R273H and second-site suppressor mutation T284R" | ❌ **Wrong mutation** — R273H, not R248Q |
| **4MZI** | "mutant p53 reference" | "Crystal structure of a human mutant p53" — engineered p53FG with 8 substitutions including S121F/V122G | ⚠️ Real entry but not a standard reference; engineering construct |
| **4MZR** | R273C reference | "Crystal structure of a polypeptide p53 mutant bound to DNA" — S121F/V122G L1 mutations | ❌ **Wrong mutation** — not R273C |
| **6FF9** | MQ-modified p53-DBD | "The Crystal Structure of the R280K Mutant of Human p53 Explains the Loss of DNA Binding" — Zn-bound only, no drug | ❌ **Wrong** — R280K apo, not MQ adduct |
| **7XZS** | "Updated MQ-DBD" | "Crystal structure of Ricin A chain bound with [pteridine compound]" | ❌ **Wrong protein entirely** (ricin from *Ricinus communis*) |
| **4HG7** | Idasanutlin + MDM2 | "Crystal Structure of an MDM2/**Nutlin-3a** complex" | ❌ **Wrong drug** — Nutlin-3a, not idasanutlin |
| **4ZYC** | AMG-232 + MDM2 | "...dihydroisoquinolinones...Hdm2 in complex with cpd5" | ❌ **Wrong scaffold** — dihydroisoquinolinone, not AMG-232 (piperidinone) |
| **5LAW** | Milademetan + MDM2 | "Novel Spiro[3H-indole-3,2'-pyrrolidin]-2(1H)-one Inhibitors...Compound 14" (BI spiro-oxindole research) | ❌ **Wrong compound** — not milademetan (DS-3032b) |
| **5VK0** | Siremadlin (HDM201) + MDM2 | "12-mer lysine-cysteine side chain dithiocarbamate stapled peptide inhibitor PMI" | ❌ **Wrong (peptide, not small molecule)**. Actual siremadlin PDB: **5OC8** |
| **7Z1V** | BI-907828 (brigimadlin) + MDM2 | "PARP15 catalytic domain in complex with OUL208" | ❌ **Wrong protein entirely** (PARP15, not MDM2) |
| **1YCR** | MDM2 + p53 TAD | "MDM2 BOUND TO THE TRANSACTIVATION DOMAIN OF P53" | ✅ Verified |
| **1RV1** | Nutlin-3a + MDM2 | "CRYSTAL STRUCTURE OF HUMAN MDM2 WITH AN IMIDAZOLINE INHIBITOR" — ligand IMZ | ⚠️ Same paper series (Vassilev 2004) but the deposited ligand is an imidazoline (IMZ), not specifically Nutlin-3a |

### Drug clinical status claims

| Claim | Status | Evidence |
|---|---|---|
| **Rezatapopt = PC14586, PMV** | ✅ Verified | Multiple primary refs and SEC filings |
| **PYNNACLE NCT04585750 Phase 1/2** | ✅ Verified | ClinicalTrials.gov |
| FDA Fast Track | ✅ Verified | PMV/Foundation press release |
| **NDA Q1 2027** | ✅ Verified | PMV Sep 2025 press release: "NDA submission for platinum-resistant/refractory ovarian cancer planned in first quarter of 2027" |
| **PMV "acquired by Pfizer"** | ❌ **FALSE** | PMV remains independent (NASDAQ: PMVP) per 2024-2025 SEC filings. Doc § 6c "(now Pfizer)" and § 13a "Pfizer's 2023 acquisition of PMV Pharmaceuticals" are fabrications. |
| **PYNNACLE Phase 2 ORR 33%** | ✅ Verified | August 2025 data cut: ORR 33% (32/97) per investigator assessment; ovarian 43%, endometrial 60%, breast 18%, NSCLC 22%. Doc § 13a description aligns. |
| **Eprenetapopt Phase 3 MDS failure 2020** | ✅ Verified | Aprea Dec 28, 2020 press release. CR rate 33.3% vs 22.4% — did not reach statistical significance. |
| Aprea continuing in ovarian | ⚠️ Partial | Aprea reformulated and continued, but Aprea has had financial difficulties post-2021 and the ovarian program is uncertain — verify current status if doc is to claim "continuing in ovarian + other cancers." |
| **PRIMA-1** (APR-246 precursor) | ✅ Verified | Bykov 2002 Nat Med; Lambert 2009 Cancer Cell |
| **MIRA-1** maleimide-based covalent, preclinical | ✅ Verified | NSC 19630, maleimide-derived, preclinical (Bykov/Wiman 2005 J Biol Chem; toxicity in normal cells reported) |
| **ZMC1 / NSC319726** zinc metallochaperone | ✅ Verified | Yu/Carpizo 2012 Cancer Cell; Blanden 2015 JACS |
| **Arsenic trioxide / ATO** | ✅ Verified | Chen et al. 2021 Cancer Cell "Arsenic Trioxide Rescues Structural p53 Mutations through a Cryptic Allosteric Site" — note doc § 7 says "Cys triplet C124/C277/C275" and "stabilizes fold"; actual paper says **cryptic allosteric site binding via Cys217, Cys229, etc.** Doc's mechanism gloss is imprecise. |
| **PK7088 — R175H-selective** | ❌ **Wrong target** | PK7088 actually binds **Y220C**, not R175H. Doc § 7 / § 8b table cites it for R175H — incorrect. (Liu et al., Cell Chem Biol 2013 — Y220C target.) |
| **KSS-9 — designed R175H binder** | ⚠️ Partial | KSS-9 exists as a piperlongumine-combretastatin hybrid that reactivates R175H via Michael addition (covalent, broad-thiol). Doc's framing as "small-molecule analog of Y220C binders / aims to bind R175H pocket" is wrong about the mechanism (it's a covalent ROS-elevation + Michael acceptor, not a pocket binder). |
| **KSS-1** | 🔵 Unable to verify | I find no published compound called "KSS-1" in the p53 reactivation literature. Likely fabricated or a private code. |
| **Stictic acid — identified by computational docking for R175H** | ✅ Verified | Wassman et al. 2013 Nat Comms identifies stictic acid via ensemble docking into L1/S3 pocket; reactivates R175H more strongly than PRIMA-1 |
| **CP-31398** styrylquinazoline, promiscuous fold stabilizer | ✅ Verified | Historical |
| Milademetan failed Phase 3 in DDLPS 2023 (MANTRA trial) | ✅ Verified | Rain Oncology, May 2023, OncLive coverage |
| Idasanutlin / AMG-232 / etc. as MDM2 inhibitors | ✅ Verified (existence/class) | All real drugs, all real MDM2 inhibitors. Only the PDB IDs are wrong (above). |

### Mechanistic and pocket-geometry claims

| Claim | Status | Evidence |
|---|---|---|
| Pocket ~250 Å³ between β-strands S7-S8 | ⚠️ Partial | Y220C cavity is conventionally described as forming between S7 and S8; the 250 Å³ figure is not standard literature — common figures are smaller fragment-sized pockets. Doc may be overstating volume; should cite a primary source. |
| Y220C destabilizes ~4 kcal/mol | ✅ Verified | Boeckler 2008 PNAS: ΔΔG ~4 kcal/mol |
| R175H destabilizes ~3 kcal/mol | ⚠️ Partial | Bullock/Fersht numbers vary. Tm drop for R175H is ~8°C; total ΔΔG is in 1.7-3 kcal/mol range depending on reference. Doc says +3.0 kcal/mol — at the upper end but defensible. |
| V143A destabilizes +3.5 kcal/mol | ✅ Verified | Bullock/Fersht 1997 PNAS: 3.34 kcal/mol |
| Contact vs structural mutant distinction | ✅ Verified | Joerger & Fersht 2008 Annu Rev Biochem |
| p53 acts as homotetramer; dominant-negative | ✅ Verified | Standard biology |
| **Y220C melting temp ~33-40°C** (mutant) | ✅ Verified | DSF refs report 33-40°C across Y220C constructs |
| **R175H melting temp ~36°C** | ✅ Verified | Lit ~36-37°C |
| Carbazole + indole + stilbene + pyrazole chemotypes for Y220C | ✅ Verified | Multiple chemotype papers from Fersht/Joerger lab |

### Discovery / paper attribution claims

| Claim | Status | Evidence |
|---|---|---|
| **Boeckler 2008 PNAS** Y220C cavity discovery, PhiKan083 | ✅ Verified | PNAS 2008 — title "Targeted rescue of a destabilized mutant of p53 by an in silico screened drug" — published anchor structure 2VUK |
| **Wassman 2013 Nat Comms** L1/S3 pocket (NOT Y220C-specific) | ✅ Verified | Wassman et al., Nat Comms 4:1407, 2013; this is the stictic acid paper. The verification-corrections note at the top of the doc correctly handles this; the body text in § 6a still contains misattribution language that says Wassman "characterized the cavity dynamics" of Y220C — this should be deleted, not just flagged. |
| **Bauer 2020 Nat Comms** APR-246 MQ mechanism C124/C277 | ⚠️ Partial | The C124/C277 paper is **Zhang et al. 2018 Cell Death Dis** ("APR-246 reactivates mutant p53 by targeting cysteines 124 and 277") — not Bauer 2020. The Bauer 2020 paper is in **ACS Chem Biol** ("Targeting Cavity-Creating p53 Cancer Mutations with Small-Molecule Stabilizers: the Y220X Paradigm") and is about Y220C, not APR-246. Doc § 13b conflates these. |
| **Pocketminer Bowman 2023 Nat Comms** | ✅ Verified | Meller/Ward et al., Nature Communications 2023; Bowman corresponding author |
| **Cho 1994 Science** 1TUP | ✅ Verified | Cho, Gorina, Jeffrey, Pavletich, Science 265:346-355 (1994) |
| **Sallman 2021 JCO** eprenetapopt + azacitidine | ✅ Verified | JCO 2021 |
| Tan et al. 2024, Yu et al. 2025 cryo-EM full-length p53 | 🔵 Unable to verify | I could not find specific peer-reviewed publications matching these year/author combinations. Earlier full-length p53 cryo-EM exists (Sauer 2018, others) at ~4.5 Å. May be real recent preprints but exact attribution unverified. |
| Joerger/Fersht subsequent Y220C cavity-dynamics work | ✅ Verified | Joerger 2015 Structure paper "Exploiting transient protein states..."; PDB 5G4M/5G4N/5G4O/5O1C/5O1H/5O1I/5ABA/5AOK series |

### Tier list claims

| Tier | Claim | Status |
|---|---|---|
| **A — Y220C** validation gate | ✅ Verified concept; positive control choice is sound | Note: the doc's chosen positive control is rezatapopt at PDB 8A32, but **8A32 contains JC769, not rezatapopt**. The validation gate must be rewritten — either use **PDB 9BR4** (true rezatapopt + Y220C) or change the positive control to "JC769 against 8A32." |
| **B — R175H** highest leverage | ✅ Verified | Largest patient pop (~7.5% of TP53 mutations), no approved drug, MD-pocket hypothesis |
| **C — R273H, R248Q, R248W** contact | ✅ Verified | Standard classification |
| **D — R282W, G245S, V143A** | ✅ Verified | Standard |

---

## Recommended corrections

A complete pass should:

1. **Replace all wrong PDB IDs** (full list above). Priorities:
   - Remove **4LO8** (botulinum), **4LO9** (wrong p53 mutant), **6FF9** (R280K not MQ), **7XZS** (ricin), **5LAW** (wrong MDM2 drug), **4ZYC** (wrong MDM2 drug), **5VK0** (peptide), **7Z1V** (PARP15), **4HG7** (Nutlin-3a not idasanutlin)
   - Correct **8A32** attribution: it is **JC769**, not rezatapopt. The rezatapopt PDBs are **9BR3** (PC-10709) and **9BR4** (PC-9859).
   - For R175H, acknowledge **no clean single-mutation PDB exists**; cite the multi-mutant or rescue constructs explicitly, or use MD-derived models.

2. **Delete all Pfizer/PMV acquisition language.** PMV is independent. Use "PMV Pharmaceuticals" everywhere.

3. **Fix PK7088 attribution** (Y220C, not R175H) and remove KSS-1 (unverifiable). Reword KSS-9 to acknowledge it is a covalent broad-thiol Michael acceptor, not a pocket binder.

4. **Reframe Wassman 2013** in § 6a body (not just the top note): the Wassman paper is about the L1/S3 pocket and stictic acid, R175H/R273H/G245S; it is **not** about the Y220C cavity dynamics.

5. **Fix Bauer 2020 citation**: split into Zhang 2018 Cell Death Dis (C124/C277 covalent mechanism for APR-246) and Bauer 2020 ACS Chem Biol (Y220X paradigm).

6. **Clarify mutation-frequency framing**: "~5% of all cancers" for R175H should be "~7.5% of TP53 missense mutations" or "the most common single TP53 SNV." Currently ambiguous.

7. **Verify Tan 2024 / Yu 2025 cryo-EM** citations if to remain in doc.

8. **Verify 8DC4 attribution** — it is Y220C + carbazole KG3 from **Guiley & Shokat (UCSF)**, NOT an "Aprea-licensed compound." Update § 6c / § 7 / § 8a.

---

## Notes on what is correct and well-stated

The high-level science is mostly excellent:
- DBD = β-sandwich immunoglobulin fold ✅
- Zn²⁺ shell C176/H179/C238/C242 ✅
- Y220C cavity between S7-S8 ✅ (volume figure uncertain)
- Contact vs structural mutant dichotomy ✅
- WT melting temp ~44°C ✅
- PDAC TP53 mutation rate 70-75% ✅
- p53 as homotetramer, dominant-negative behavior ✅
- TP53 17p13.1 ✅
- Boeckler 2008 PNAS as the Y220C anchor paper ✅
- Wassman 2013 as the L1/S3 / stictic acid paper ✅
- APR-246 covalent C124/C277 mechanism ✅ (correct mechanism; just wrong author/year)
- PYNNACLE Phase 2 / NDA Q1 2027 / Fast Track ✅

The damage is concentrated in the **PDB ID column** of the drug tables (§ 7, § 9, § 14f) and a handful of named-drug attributions (PK7088 target, KSS-9 mechanism, KSS-1 existence, Pfizer/PMV).

---

## Bottom line

This doc reads like it was assembled by an LLM that hallucinated specific 4-character PDB codes alongside accurate science. The 7JWU error was the tip of the iceberg. The same generative process produced 4LO8 (botulinum), 7XZS (ricin), 7Z1V (PARP15), and 6FF9 (R280K apo) where p53 drug complexes should be. A docker who follows § 15a's "fetch 8A32 and re-dock rezatapopt" recipe will load a structure with the wrong ligand; if they pull 4LO8 expecting G245S they will get a Clostridium toxin. The PDB column needs a top-to-bottom rewrite before this document is usable as a pipeline reference.

Recommend re-deriving all PDB attributions from RCSB queries (`https://www.rcsb.org/search/advanced?query=p53+Y220C` etc.) rather than from memory.
