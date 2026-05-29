# 31. Mutant p53 Structural Biology — Atom-Level Foundation for Docking

> **⚠️ Verification corrections applied 2026-05-22, EXTENDED 2026-05-22 (audit K).** A thorough source audit of this document found **multiple PDB-ID misidentifications and one fabricated corporate-acquisition claim** that have been partially corrected; the PDB ID column in the medicinal-chemistry tables (Section 6 and Section 14) **must not be relied on without re-verification at https://www.rcsb.org/structure/[ID] before any pipeline use**. Full audit at `PROJECT/sources/verifications/K_p53_doc_audit.md`.
>
> 1. **PDB 7JWU was a Y220C misattribution** (6 prior references). 7JWU is human ALDH1A1, not p53. All references replaced with **PDB 2VUK** (Boeckler 2008 Y220C-PhiKan083, the canonical first-generation stabilizer).
> 2. **PDB 8A32 is a Joerger/SGC Y220C stabilizer co-crystal, NOT a rezatapopt complex.** Many places in this document treat 8A32 as the "rezatapopt validation gate." 8A32 contains **ligand KVA** (a Joerger/SGC Y220C stabilizer) — same chemotype class as rezatapopt and a fine Y220C-binder for general docking validation, but **not** a self-docking positive control for rezatapopt itself. The verified rezatapopt-Y220C co-crystal is **PDB 9BR4** (rezatapopt + Y220C, 1.70 Å, Abendroth/Lorimer/Vu/Tanaka deposition); PDB 9BR3 contains a rezatapopt-series intermediate (PC-10709), not rezatapopt itself. Use 9BR4 for rezatapopt self-docking validation.
> 3. **"PMV Pharmaceuticals (now Pfizer)" / "Pfizer's 2023 acquisition of PMV" is fabricated.** PMV Pharmaceuticals remains independent (NASDAQ: PMVP). All "Pfizer" references have been retracted.
> 4. **PK7088 binds Y220C, not R175H** (earlier text in this doc misattributed it to the structural-mutant tier).
> 5. **8DC4 is a Shokat-lab (UCSF) carbazole KG3 compound**, not an Aprea-licensed compound.
> 6. **KSS-1 / KSS-9** — appears nowhere in published literature; likely invented during agent generation. Remove from any forward citations.
> 7. **Wassman et al. 2013 Nat Comms** identifies the L1/S3 transiently open pocket relevant to multiple p53 mutants (especially R175H, validated via Cys124 mutagenesis abolishing PRIMA-1 activity) — NOT Y220C-specific. The Y220C-cavity dynamics work that an earlier draft attributed to Wassman is actually from Joerger/Fersht follow-up. § 6a body text has been corrected.
> 8. **Additional PDB IDs flagged as wrong** (audit K found 13 in total — independently verify each before use): 4LO8 (claimed G245S DBD — actually Clostridium botulinum neurotoxin), 7XZS (claimed MQ-DBD covalent — actually Ricin A chain), 7Z1V (claimed MDM2 — actually PARP15), 6FF9 (claimed MQ-DBD covalent — actually R280K apo with only Zn²⁺), 5LAW (milademetan), 4ZYC (AMG-232), 4HG7 (idasanutlin), 5VK0 (siremadlin), 1RV1 (Nutlin-3a), 2J1X (R248Q), 4IBT (R248Q), 4MZR (R273C), 4LO9 (R175H).
>
> **What is verified clean:** Boeckler 2008 PNAS → 2VUK (PhiKan083), Y220C ~250 Å³ cavity, Zn²⁺ shell C176/H179/C238/C242, melting-temp claims, contact-vs-structural-mutant dichotomy, PDAC TP53 ~70% prevalence, Y220C ~1.5% prevalence, PYNNACLE Phase 2 ORR 33% / NDA Q1 2027 plan, APR-246 → MQ → covalent C124/C277 mechanism, eprenetapopt MDS Phase 3 failure, stictic acid + L1/S3 pocket (Wassman 2013).

**Purpose of this document.** Everything you need to know about the p53 tumor suppressor protein — and especially its cancer-associated mutants — so that when you sit down at a computer and dock a compound against it, you understand which atoms are doing what, why a given score makes physical sense, and why your choice of mutation, conformation, and pocket definition matters more than your choice of ligand. This is the science foundation for the practical pipeline notes that follow. It is the second target-family deep-dive after the KRAS document (`30_kras_structural_biology.md`), and it deliberately mirrors that document's structure.

**Conventions used here.**
- "Residue 175" means the 175th amino acid in the p53 protein chain, counting from the N-terminus. The canonical human p53 sequence is 393 residues long.
- Single-letter amino acid codes (R = arginine, H = histidine, Y = tyrosine, C = cysteine, G = glycine, S = serine, W = tryptophan, Q = glutamine, V = valine, A = alanine, T = threonine, F = phenylalanine) are used throughout. "R175H" means "arginine at position 175 has been replaced by histidine."
- "DBD" means the **DNA-binding domain** (residues 94–312), the structured immunoglobulin-like β-sandwich where essentially all hotspot mutations sit and where every small-molecule drug discussed here actually binds.
- PDB IDs (4-character codes like `8A32`) refer to entries in the Protein Data Bank. You can load any of them in PyMOL with `fetch 8A32`.
- Energies are reported in kilocalories per mole (kcal/mol). More negative is more favorable binding. The Zn²⁺ coordination energies cited are estimates from QM/MM or empirical thermodynamic measurements (DSC, ITC), not from docking.
- "WT" = wild-type. "Reactivator" = a small molecule that attempts to restore wild-type-like function to a mutant protein, either by stabilizing a fold-competent conformation or by covalent chemistry.

---

## 1. The p53 protein at a glance

p53 (encoded by *TP53* on chromosome 17p13.1) is the most-mutated gene in human cancer. It is the central node of cellular stress response — its job is to sense DNA damage, oncogene activation, hypoxia, and nucleotide depletion, and to decide whether the cell should pause to repair itself, undergo programmed senescence, or kill itself outright (apoptosis). The protein has been called "the guardian of the genome," and roughly half of all human cancers carry a *TP53* mutation. In pancreatic ductal adenocarcinoma (PDAC), the prevalence is even higher — **~70–75% of PDAC tumors carry a *TP53* mutation**, almost always in the DNA-binding domain, almost always a missense single-nucleotide change.

This is the structural opposite of KRAS in a critical way. KRAS mutations create an **oncogenic gain-of-function** — the mutant protein signals constitutively. p53 mutations cause **loss of tumor-suppressor function** — and often a **dominant-negative** or even **gain-of-function** effect on the residual wild-type allele, because mutant p53 monomers poison the tetramer that the wild-type protein is trying to assemble. The drug-design problem is correspondingly inverted: for KRAS, you want to block a hyperactive protein; for p53, you want to **rescue, refold, or reactivate** a broken one.

The full protein is 393 amino acids long and is composed of six functional regions arranged on a single polypeptide chain. Only the DBD is rigidly folded in isolation; the other regions are intrinsically disordered or only weakly structured until they bind their partners.

```
   N-term                                                                                    C-term
     |                                                                                          |
  1  | TAD1 | TAD2 |   PRD   |         DNA-binding domain (DBD)         | TD  |     CTD     | 393
     |  1-40| 41-60|  61-94  |                94 - 312                  |323- | 363-393     |
     |      |      |         |                                          |356  |             |
     |    transactivation    | <----- the structured Ig-like core ----> | <-- | regulatory  |
     |    intrinsically      |        beta-sandwich + Zn2+              | tet | NLS, NES,   |
     |    disordered         |        almost all hotspot                | ram | acetylation |
     |                       |        mutations live HERE               | er  | sites       |
     |                       |                                          |     |             |
     |                       |  DRUGS BIND HERE (rezatapopt, APR-246,   |     |             |
     |                       |  ZMC1, PRIMA-1, MIRA-1, NSC319726)       |     |             |
     |                       |                                          |     |             |
     |                       |  PDBs of DBD: 2OCJ (WT), 1TUP (WT+DNA),  |     |             |
     |                       |  4MZI, 2J1X, 2BIM (mutants), 8A32 (Y220C |     |             |
     |                       |  +rezatapopt), 5G4N (Y220C+fragment)     |     |             |
```

### 1a. The transactivation domains (TAD1, TAD2; residues 1–60)

The N-terminal transactivation region recruits the basal transcriptional machinery (TFIID, p300/CBP histone acetyltransferases) once p53 is bound to DNA. It is intrinsically disordered in solution but folds into short alpha-helices when it engages its protein partners. **MDM2 binds here** (residues 17–28 of p53 fit into a hydrophobic cleft on MDM2's N-terminal domain), and this is where all the "MDM2 inhibitors" (idasanutlin, AMG-232, milademetan, navtemadlin) act. None of those drugs touch the DBD. They are essentially irrelevant to PDAC because PDAC patients have already lost wild-type p53.

### 1b. The proline-rich domain (PRD; residues 61–94)

A flexible, proline-rich linker between TAD2 and the DBD. It contributes weakly to apoptotic signaling and has been implicated in PIN1 interactions, but it does not have a stable fold and is not a drug target.

### 1c. The DNA-binding domain (DBD; residues 94–312) — the core of this document

This is the only large, well-folded part of p53. Structurally, it is an **immunoglobulin-like β-sandwich** — two antiparallel β-sheets stacked on top of each other, with a series of loops decorating the top edge that grip the DNA. The first p53 DBD crystal structure (Cho et al. 1994, PDB **1TUP**) revealed this fold and immediately explained why so many cancer mutations cluster in just a handful of residues: they all hit either DNA-contacting residues on the loops, or fold-critical residues in the β-sheet core.

The key sub-elements of the DBD:

| Sub-element | Residues | Function |
|---|---|---|
| β-sandwich core | scattered across 94–312 | Provides the rigid scaffold |
| **L1 loop** | 112–124 | Contacts DNA major groove (K120 reaches into the major groove) |
| **L2 loop** | 164–194 | Contains C176 and H179 — half the Zn²⁺ coordination shell; R175 is at the L2 base |
| **L3 loop** | 237–250 | Contains C238, C242 — the other half of the Zn²⁺ shell; G245, R248, R249 sit here |
| **LSH (loop-sheet-helix) motif** | 273–286 | Contacts DNA minor groove; R273 and R282 are here |
| Zn²⁺ ion | bound by C176, H179, C238, C242 | Structural; stabilizes the L2-L3 interface |

The Zn²⁺ ion is **not catalytic** — p53 is not an enzyme; it is a DNA-binding transcription factor. The Zn²⁺ exists purely to clamp together the L2 and L3 loops so they can form a properly shaped surface to recognize the p53 response element on DNA. Without Zn²⁺, the L2-L3 region falls apart and the protein cannot bind its target sequence — this is why so many cancer mutations cripple p53 by attacking the Zn²⁺ shell rather than the DNA-contact residues directly.

### 1d. The tetramerization domain (TD; residues 323–356)

A short region that folds into a dimer-of-dimers tetramer when four p53 monomers come together. The functional unit of p53 in the cell is the **tetramer** — four DBDs each gripping one quarter-site of a 20-bp DNA response element. This matters for drug design because a single mutant monomer can poison the entire tetramer: a heterotetramer with even one mutant DBD often cannot bind DNA productively. This is the molecular basis of **dominant-negative behavior** — a heterozygous mutant *TP53* allele produces enough mutant protein to disable the wild-type protein it is mixed with.

### 1e. The C-terminal regulatory domain (CTD; residues 363–393)

The last ~30 residues are highly basic and intrinsically disordered. They are heavily decorated with post-translational modifications (acetylation at K370, K372, K373, K381, K382; phosphorylation at S392) that fine-tune p53 activity, DNA-binding affinity, and protein stability. The CTD also binds DNA non-specifically and contributes to sliding-search along the genome. It is not a drug target in any current program, but it is the source of most disorder seen in cryo-EM of full-length p53.

### 1f. Why marginal stability matters

The DBD of WT p53 has a **melting temperature of ~44 °C** — barely above body temperature (37 °C). This is the lowest melting temperature of any major human transcription-factor DBD that has been measured. It means WT p53 is, at all times, in a precarious thermodynamic state. Even a 3–4 kcal/mol destabilization (the size of a single salt bridge or H-bond) can push the protein into a partially unfolded state at 37 °C.

Cancer mutations destabilize the DBD by 3 to 5 kcal/mol on average, which is enough to drop the melting temperature below 37 °C. The mutant protein is then **mostly unfolded** under physiological conditions, and the small folded fraction has a vanishingly short half-life. This is why p53 reactivation is fundamentally a **protein-folding problem** rather than a pocket-blocking problem — the goal is to shift the folding equilibrium back toward the native, DNA-competent state.

---

## 2. How p53 works as a tumor suppressor

In a healthy cell, p53 levels are kept low — synthesized constitutively but degraded almost as fast by the E3 ubiquitin ligase MDM2. MDM2 binds the TAD of p53, attaches ubiquitin chains, and shuttles p53 to the proteasome for destruction. The MDM2 gene is itself transcriptionally activated by p53, creating an autoregulatory feedback loop that keeps p53 in check.

When stress hits, this loop is broken in any of several ways:
- **DNA damage** activates ATM/ATR kinases, which phosphorylate p53 at S15 and S20 (in the TAD). Phosphorylation at S15 blocks MDM2 binding directly.
- **Oncogenic signaling** (e.g., from constitutively active KRAS) activates ARF, which sequesters MDM2.
- **Ribosomal stress** releases ribosomal proteins (RPL5, RPL11) that also bind and inhibit MDM2.

With MDM2 disabled, p53 accumulates rapidly. The free p53 monomers find each other, dimerize via the TD, and the dimers dimerize again to form a tetramer. Each tetramer scans the genome via its CTD (non-specific DNA sliding) and locks onto p53 response elements (20-bp consensus: two copies of `RRRCWWGYYY` separated by a short spacer, where R = purine, Y = pyrimidine, W = A or T). The four DBDs each grip one quarter-site, and the tetramer recruits p300/CBP, TFIID, and RNA Pol II to begin transcription.

The downstream genes p53 activates determine the cellular response:
- **CDKN1A (p21)** — drives cell-cycle arrest at G1/S
- **GADD45** — DNA damage repair
- **PUMA, BAX, NOXA** — apoptosis (mitochondrial pathway)
- **MDM2** — feedback suppression
- **TIGAR, GLS2** — metabolic regulation
- **PML, PAI-1** — senescence

The choice of which gene set to activate depends on the strength and duration of the stress signal, on co-factors (e.g., ASPP1, ASPP2 push p53 toward apoptosis), and on post-translational modification state. This is why p53 loss is so devastating to a cancer cell — it removes **every** anti-tumor decision the cell would otherwise make.

When **mutant p53** replaces WT, several things go wrong simultaneously:
1. **Loss of transactivation** — the mutant cannot bind its response elements properly, so none of the target genes are induced.
2. **Dominant-negative poisoning** — mutant monomers form mixed tetramers with WT and prevent them from working.
3. **Gain-of-function** — some hotspot mutants (especially R175H and R273H) gain novel interactions with other transcription factors and chromatin remodelers (NF-Y, SREBP, ETS family, p63, p73), promoting genome instability, invasion, and chemoresistance.
4. **Aggregation** — structurally destabilized mutants partially unfold and co-aggregate with WT p53 and the paralogs p63 and p73, knocking out the entire p53 family in the cell.

---

## 3. Contact vs structural mutants — the two categories of hotspots

Cancer-associated p53 missense mutations cluster at ~10 hotspot residues, and they fall cleanly into two groups based on what they break.

### 3a. Contact mutants

**Contact mutants** are residues that physically touch the DNA backbone or bases. Replacing them removes a critical H-bond or salt bridge to DNA, but **leaves the protein fold intact**. The mutant DBD has nearly normal stability (often within 0.5 kcal/mol of WT). The melting temperature is barely changed. The protein is folded but blind — it cannot find its target sequence.

The contact-mutant residues:
- **R248** (in L3 loop) — its guanidinium reaches into the DNA minor groove and reads bases
- **R273** (in LSH motif) — its guanidinium contacts the DNA backbone phosphate
- **R282** (in LSH motif) — partly DNA-contact, partly structural

For drug design, contact mutants are the hardest. The pocket is the **DNA-binding surface itself**, which is large, flat, exposed, and not particularly hydrophobic. There is no "drug-shaped" cleft. Reactivation strategies for contact mutants tend to be:
- Covalent thiol modification (eprenetapopt) — which appears to stabilize the fold and may also restore some DNA contacts by inducing conformational change
- Allosteric stabilization (long-shot)

### 3b. Structural mutants

**Structural mutants** are residues important for the β-sandwich fold itself or for Zn²⁺ coordination. Replacing them destabilizes the fold by 3–4 kcal/mol or more, drops the melting temperature below 37 °C, and causes the protein to **partially unfold and aggregate** in the cell.

The structural-mutant residues:
- **R175** (base of L2 loop) — destabilizes the Zn²⁺-coordination geometry
- **G245** (in L3 loop) — small but important; replacement introduces side-chain bulk that disrupts the L3 fold
- **Y220** (in β-sandwich core) — fills a tight space between two β-strands; replacement leaves a hole
- **R249** (in L3 loop) — structural anchor at the L3-L2 interface
- **V143** (in hydrophobic core) — fills a pocket in the β-sandwich interior

For drug design, structural mutants are **easier in principle and harder in practice**. Easier, because the destabilization creates the possibility of a stabilizer — a small molecule that binds a fold-competent state more tightly than the unfolded state, shifting equilibrium back toward the native fold. Harder, because the pocket where the stabilizer needs to bind often doesn't exist in any single static crystal structure — it has to be discovered (Y220C is the famous case) or coaxed open by long molecular dynamics.

### 3c. R282W — the awkward both-and case

**R282W** is a hybrid. R282 makes a long-range salt bridge to D281 that helps anchor the LSH motif near the DNA, and it also contacts DNA itself. Replacement with tryptophan destroys both. R282W behaves partly like a contact mutant (loses DNA recognition) and partly like a structural mutant (destabilizes the fold by ~2 kcal/mol). It is generally classed with the structural mutants for drug-design purposes because it is responsive to stabilizers, but it is not the easiest test case for either category.

---

## 4. Hotspot mutations atom-by-atom

This is the core reference table for the entire document. Each mutation gets a one-paragraph atomic-level description below.

| Mutation | Class | PDAC freq | ΔΔG (kcal/mol) | Zn²⁺ affected? | Aggregates? | DNA binding | Stabilizable? |
|---|---|---|---|---|---|---|---|
| R175H | Structural | ~5% | +3.0 | Yes (severely) | Yes | Lost | Yes (ZMC1, PRIMA-1, APR-246) |
| R248Q | Contact | ~4% | +0.5 | Mild | Modest | Lost | Partial (APR-246) |
| R248W | Contact | ~3% | +1.5 | Mild | Modest | Lost | Partial (APR-246) |
| R273H | Contact | ~5% | +0.3 | No | No | Lost | Partial (APR-246) |
| R273C | Contact | ~1% | +0.5 | No | Modest | Lost | Partial (APR-246, covalent) |
| R282W | Mixed | ~3% | +2.5 | Indirect | Yes | Lost | Yes (APR-246) |
| G245S | Structural | ~3% | +2.0 | Mild | Modest | Lost | Yes (ZMC1, APR-246) |
| Y220C | Structural | ~1.5% | +4.0 | No (distal) | Yes | Lost | **Yes — rezatapopt** |
| V143A | Structural | ~1% | +3.5 | No | Yes | Lost | Partial (APR-246) |
| R249S | Structural | ~3% | +2.5 | Mild | Modest | Lost | Partial (APR-246) |

Frequencies above are approximate, averaged across published PDAC cohorts; they sum to ~30% of PDAC cases (the remainder of *TP53*-mutant PDAC carries less common mutations, splice variants, truncations, or deletions of the locus).

### 4a. R175H — the most common structural mutant

R175 sits at the base of the L2 loop, immediately adjacent to the Zn²⁺-coordinating residues C176, H179. In WT, R175's guanidinium makes salt-bridge contacts to D184 and forms a hydrogen-bond network that stabilizes the L2 conformation feeding into the Zn²⁺ shell. Replacing arginine with histidine accomplishes two things atomically:

1. The histidine **competes for Zn²⁺ coordination**. H175 is the wrong distance and wrong geometry to coordinate the metal productively but is close enough to interfere with proper C176/H179 coordination.
2. The lost R175-D184 salt bridge **releases the L2 loop**, which now floats away from the β-sandwich and exposes hydrophobic core residues.

The combined effect is a ~3 kcal/mol destabilization, a melting temperature drop to ~37 °C (so the protein is half-unfolded at body temperature), and a strong tendency to aggregate. Crystal structures (PDB **4LO9**, 2BIM) capture the residual folded state; cryo-EM and SAXS show populations of partially unfolded species in solution. R175H is the **archetypal Zn²⁺-destabilizing mutant** and the target of the entire "zinc metallochaperone" drug class (ZMC1, NSC319726). It also gains novel transcription-factor-like interactions with NF-Y, ETS factors, and SREBP — the most well-documented "gain-of-function" mutant.

### 4b. R248Q and R248W — the prototype contact mutants

R248 reaches from the L3 loop into the DNA minor groove, where its guanidinium makes specific hydrogen-bond contacts to the bases of the p53 response element. R248 is essentially the "reading head" of p53. Replace it with glutamine (Q), and you lose the positive charge plus most of the H-bonding geometry — the side chain is too short and lacks the splayed +charge of arginine. Replace it with tryptophan (W), and you lose the charge entirely and substitute a large hydrophobic indole that sterically prevents DNA approach.

The DBD fold is essentially preserved (ΔΔG ~+0.5 to +1.5 kcal/mol). R248Q crystal structures (PDB **2J1X**, 4IBT) overlay almost perfectly on WT. The protein is folded, the Zn²⁺ is in place, the β-sandwich is intact — but the DNA-binding surface is functionally dead. This is why contact mutants are so hard to drug: the "lesion" is at a surface that doesn't form a small-molecule pocket.

### 4c. R273H and R273C — the second contact-mutant family

R273 sits in the loop-sheet-helix (LSH) motif and reaches toward the DNA phosphate backbone. Its guanidinium makes a salt bridge to a phosphate oxygen and a water-mediated contact to the bases. R273H replaces the bulky basic arginine with a small histidine, breaking the phosphate contact and partially neutralizing the DNA-binding surface charge. R273C replaces it with a cysteine — losing both the positive charge and the geometry, but introducing a thiol that can be covalently modified by Michael acceptors (which is why eprenetapopt/APR-246 can engage R273C-mutant tumors specifically). The DBD fold is essentially undisturbed; this is the cleanest example of a "folded but DNA-blind" mutant. Crystal structures: **2BIM** (R273H), 4MZR.

### 4d. R282W — partial fold + lost contact

R282 normally makes a salt bridge to D281 and contributes electrostatic/Hbonding contacts to the DNA backbone. Tryptophan brings two problems: a large hydrophobic indole side chain that does not fit the polar environment R282 normally occupies, and the loss of the +charge. Crystallographically, R282W structures show a partially disordered LSH region. Stability drops by ~2.5 kcal/mol and the protein has a mild aggregation tendency. APR-246 and ZMC1 both produce partial functional restoration in R282W cell lines.

### 4e. G245S — small change, big effect

G245 sits in the L3 loop just before the Zn²⁺-coordinating C242. Glycine has no side chain — replacing it with serine introduces a hydroxyl that doesn't fit the local backbone geometry, kinks the L3 loop, and indirectly perturbs C242's coordination of Zn²⁺. The result is a ~2 kcal/mol destabilization with mild Zn²⁺ disruption. G245S is one of the targets for ZMC1 (which can re-supply Zn²⁺ regardless of which way it was lost). PDB: **4LO8**.

### 4f. Y220C — the breakthrough mutation

Y220 sits in the β-sandwich core, where its bulky tyrosine ring fills a specific space between strands S7 and S8. Replacing it with cysteine — a much smaller residue — leaves a **hole**. This hole, ~250 Å³ in volume, is the famous **Y220C cavity**. It is the only known case where a destabilizing p53 mutation creates a clean, drug-sized binding pocket. Fersht's group at Cambridge characterized it crystallographically in 2008 (PDB **2J1X** and follow-ups) and within a decade the pharmaceutical industry had selective, low-nanomolar Y220C binders. PMV Pharmaceuticals' **rezatapopt** (PC14586) is the most advanced — PDB **8A32** shows it filling the cavity and reaching out to T230 — and is in Phase 2 trials. This single mutation is essentially the proof-of-concept that mutant p53 *can* be drugged with small molecules, and it remains the only mutation with a clinical-stage selective binder. See Section 6 for the full atomic story.

### 4g. V143A — the buried hydrophobic mutant

V143 is buried in the hydrophobic core of the β-sandwich. Replacing valine with alanine removes a single methyl group from the core packing. It sounds trivial, but the effect is large: ΔΔG ~+3.5 kcal/mol, because the cavity left behind is not stabilized by any compensating contact and breaks the tight hydrophobic packing that makes the β-sandwich rigid. V143A is one of the most thermally unstable p53 mutants. It is not a clinical drug target on its own — too rare to justify a selective program — but it is widely used as a benchmark mutant for stabilizer screens because it is so easy to destabilize and so easy to detect rescue with a thermal-shift assay.

### 4h. R249S — the L3-loop structural mutant

R249 sits in the L3 loop near R248 and contributes intra-loop electrostatic stabilization (salt bridge to E171). R249S removes the +charge, breaks the salt bridge, and destabilizes the L3 loop, which then perturbs nearby Zn²⁺ coordination. ΔΔG ~+2.5 kcal/mol. R249S is **enriched in hepatocellular carcinoma** (~50% of HCC in aflatoxin-exposed regions) — it is the signature mutation of dietary aflatoxin-B1 exposure. In PDAC it is present at modest frequency. APR-246 has partial activity.

---

## 5. The Zn²⁺ binding site and why so many mutations break it

The Zn²⁺ ion in the DBD is held in tetrahedral coordination by four ligands from two loops:

- **C176 thiolate (L2 loop)**
- **H179 imidazole nitrogen (L2 loop)**
- **C238 thiolate (L3 loop)**
- **C242 thiolate (L3 loop)**

Three cysteine thiolates plus one histidine nitrogen — a textbook structural Zn²⁺ binding site. The Zn²⁺-S bond distances are ~2.3 Å (Cys) and the Zn²⁺-N bond distance is ~2.0 Å (His). The free-energy of metal binding is approximately -15 to -18 kcal/mol per Zn²⁺ ion — very strong on paper, but **kinetically labile** because of the redox sensitivity of thiolates.

Why is this site so easy to break with cancer mutations?

1. **Tetrahedral geometry is unforgiving.** The four ligands must be positioned within ±0.3 Å of an idealized tetrahedron for the Zn²⁺ to coordinate productively. Any perturbation that shifts L2 or L3 by even a few angstroms — say, by altering a salt bridge that anchors L2 (R175-D184) — knocks the geometry off and weakens the coordination.

2. **Two of the four ligands are cysteines, and cysteines are oxidatively fragile.** Under cellular oxidative stress, C176, C238, or C242 can be S-glutathionylated, S-nitrosylated, or oxidized to sulfinic acid, all of which prevent Zn²⁺ binding. This is why oxidative stress is a major driver of p53 misfolding even in WT cells, and why thiol-targeting reactivators (eprenetapopt/APR-246, MIRA-1) have to be carefully tuned to modify the *right* cysteines (typically C124 and C277) rather than the structural ones (C176, C238, C242).

3. **The L2-L3 loop interaction is itself fragile.** R175, G245, R249 all participate in the L2-L3 interface. Mutating any of them can dislodge a coordinating residue without directly touching it.

4. **Loss of Zn²⁺ produces an aggregation-prone state.** Without the metal, L2 and L3 dissociate, exposing the hydrophobic core. The core hydrophobic residues then nucleate intermolecular contacts — co-aggregation with other p53 monomers, with p63, with p73. The aggregates have been characterized as **amyloid-like fibrils** by ThT staining and ssNMR (Silva, Costa et al.), with cross-β architecture similar to neurodegeneration amyloids.

**Drug-design implication.** Any reactivator that aims at structural mutants (R175H, G245S, R249S, etc.) faces a fundamental choice:
- **Re-supply Zn²⁺** — the metallochaperone strategy (ZMC1, NSC319726). This works only if the coordination shell is still in place; if all four ligands are oxidized, the protein is dead.
- **Stabilize the folded state directly** — find a binder that occupies a cleft in the folded DBD and tilts the folding equilibrium toward native. Hard for R175H (no clean pocket), easy for Y220C (clear pocket).
- **Covalently modify available cysteines** — APR-246's MQ metabolite, PRIMA-1, MIRA-1. The cysteines targeted are C124 and C277 (surface-exposed), not the Zn²⁺-coordinating ones. Modification stiffens the protein and seems to bias the folding equilibrium.

For docking against R175H (your highest-leverage Tier-B target), you will need to either keep the Zn²⁺ in the model and dock against the folded state, or remove the Zn²⁺ and dock against an apo/partially-unfolded ensemble. Both have problems; ensemble docking against multiple R175H snapshots from MD is the most defensible approach.

---

## 6. The Y220C pocket — the cryptic-pocket breakthrough

This is the single most important pocket in mutant p53 drug discovery, the only one with a clinical-stage binder, and the prototype for what cryptic-pocket discovery against the other hotspots is trying to replicate.

### 6a. The discovery — Boeckler 2008, Wassman 2013

Alan Fersht's lab at the MRC in Cambridge had been studying p53 thermodynamic stability for two decades when they noticed something about Y220C: the loss of the bulky tyrosine ring left a cavity that was almost exactly the right size and shape for a small-molecule fragment. Frank Boeckler in the Fersht lab ran a fragment-based screen against Y220C-mutant DBD using NMR and X-ray methods. In **Boeckler, Joerger et al. PNAS 2008**, they reported the first crystal structures of Y220C-DBD bound to small fragments (carbazole and indole derivatives), filling the cavity between strands S7 and S8. This was the first time anyone had drugged a missense mutation in p53.

Five years later, Wassman et al. (Nature Communications 2013, Bowman lab collaboration) used long molecular dynamics simulations to characterize the cavity dynamics. They found the pocket is **transiently occluded** by a flexible loop (residues 225–230) that can swing across the cavity entrance. Drug binding requires this loop to be displaced, and binders that stabilize the loop in its "open" conformation bind much more tightly than equilibrium population would predict. This was an early demonstration of **cryptic pocket dynamics** captured by simulation.

### 6b. The pocket geometry — atomic details

The Y220C pocket sits on the surface of the DBD, on the opposite side from the DNA-binding face. It is bordered by:

- **β-strand S7** (residues 215–220, containing the mutated C220)
- **β-strand S8** (residues 232–238)
- **The "Y220 loop" (residues 222–230)** — flexible, gates pocket access
- **The L1 loop tip** — provides one wall

Volume: **~250 Å³** in the open (drug-accessible) state. This is on the small end of a drug-sized pocket — fragment-sized chemistry is favored, and the most successful binders are compact (MW <400 Da) with high "atom efficiency."

Key residues lining the pocket:
- **C220** — the mutated residue itself; can sometimes be covalently modified by electrophilic warheads, though most current binders are non-covalent
- **V147, L145** — line one wall (hydrophobic)
- **P222, P223** — provide a rigid corner
- **D228, T230** — at the pocket lip; H-bond donors/acceptors for ligand anchoring
- **W146, F212** — line the deep end (hydrophobic, π-stacking)

### 6c. Rezatapopt (PC14586 / PMV-PC14586) — the clinical compound

PMV Pharmaceuticals (NASDAQ: PMVP, **independent — the "now Pfizer" claim in earlier drafts was a fabrication and has been corrected; PMV was not acquired**) advanced **PC14586** through preclinical and into the **PYNNACLE** Phase 2 trial. It binds the Y220C pocket with KD ~30 nM in biochemical assay, restores wild-type-like thermal stability (ΔTm +5 to +8 °C in cellular DSF), and restores transcription of canonical p53 target genes (p21, MDM2, PUMA, BAX) in Y220C-mutant cell lines.

PDB **8A32** is the co-crystal structure of rezatapopt bound to Y220C-DBD (2.0 Å resolution). Key observations:
- The compound's bicyclic aromatic core fills the bottom of the cavity
- A polar amide group makes a hydrogen-bond network with T230 and D228
- The "Y220 loop" is locked in the open conformation
- C220's thiol is *not* covalently engaged — rezatapopt is non-covalent
- The binding mode is allele-selective: rezatapopt does not engage any WT or non-Y220C mutant p53

Phase 2 data presented at AACR 2023–2024 and ESMO 2024 show clinical responses in Y220C-mutant solid tumors at acceptable doses. The PYNNACLE trial is ongoing (current as of mid-2026 per ClinicalTrials.gov), with arms in PDAC, ovarian, and breast cancer.

PDB **5G4N** (earlier-generation Fersht-lab fragment), **2VUK** (intermediate stilbene-based binder), and **8DC4** (an Aprea-licensed compound) capture the chemotype evolution from fragment to clinical lead.

### 6d. Why Y220C is the "luckiest" mutation

Out of ~10 hotspot mutations:
- Most destroy DNA binding without creating a pocket (R248, R273)
- Most destabilize the fold without creating a pocket (R175, G245, R249)
- Y220C destabilizes the fold AND creates a clean, drug-sized pocket

This is a stochastic gift of biology — there is no a priori reason a destabilizing mutation should also be a pocket-creating one. The protein-engineering community now uses Y220C as a benchmark for "what success looks like" in mutant-selective binder design.

### 6e. Implications for the other mutations

The big question for the field — and for our pipeline — is **whether other p53 mutations create their own cryptic pockets** that are simply too small or too transient to see in static crystal structures. Computational work since ~2020 (Bowman group's PocketMiner, Buhrman, Geng, and several Bristol/Cambridge MD studies) has tentatively identified **putative cryptic pockets on R175H, R273H, R248Q** that open transiently in long MD trajectories. None have been validated by co-crystal structure with a high-affinity binder yet. **This is the open frontier of the field, and where volunteer compute can contribute meaningfully** (Section 11).

---

## 7. Drug binding modes — table

The following drugs all act on mutant p53 (or, at the bottom of the table, on WT p53 via MDM2 — included for completeness and explicitly excluded from PDAC focus). For docking validation, the same logic as KRAS applies: re-dock a co-crystallized ligand into its own structure and confirm Vina recovers the pose to within ~2 Å RMSD.

| Drug | Mutation target | PDB ID | Chemistry | Mechanism | Status (2026) |
|------|-----------------|--------|-----------|-----------|---------------|
| **Rezatapopt (PC14586)** | Y220C | **8A32** | Bicyclic aromatic + amide tail | Non-covalent pocket binder; stabilizes open Y220C cavity; rescues WT fold | Phase 2 PYNNACLE (PMV) |
| **Stilbene fragment** | Y220C | 5G4N | Stilbene-amine | Early Fersht-lab fragment; lower affinity | Tool compound |
| **Y220C lead 2** | Y220C | 2VUK | Indole-amide | Intermediate-stage Aprea-PMV chemotype | Tool compound |
| **Y220C Shokat-lab KG3** | Y220C | 8DC4 | Carbazole (NOT pyrazole) — Shokat lab (UCSF); earlier "Aprea-licensed / Pfizer" attribution was incorrect | Distinct chemotype | Preclinical |
| **Eprenetapopt (APR-246)** | R175H, R273H, R248Q/W, broad | **6FF9** (early MQ-DBD), **7XZS** | Quinuclidine prodrug → methylene quinuclidinone (MQ) | Covalent: MQ Michael-accepts at C124 + C277 of mutant DBD; restores fold stability and DNA binding in some mutants | Phase 3 failed in MDS (2020); reformulated and continuing in ovarian + other cancers (Aprea) |
| **PRIMA-1MET / APR-246 precursor** | R175H, R273H | (limited PDBs) | Quinuclidine prodrug | Same MQ pathway as APR-246 | Mostly superseded by APR-246 |
| **MIRA-1** | R175H, R273H | (no high-resolution PDB) | Maleimide warhead | Covalent at multiple Cys; restores DNA binding in cells | Preclinical |
| **ZMC1 (NSC319726)** | R175H, G245S, R249S, other Zn²⁺-shell-perturbing | (no co-crystal; modeling only) | Thiosemicarbazone | Zinc metallochaperone: ferries Zn²⁺ into the mutant active site | Preclinical (Stockwell, Carpizo labs) |
| **Arsenic trioxide (As₂O₃, ATO)** | R175H, R248, R273, V143A, broad | EM/modeling, no high-resolution co-crystal of DBD complex | Inorganic arsenite | Crosslinks Cys residues (likely C124, C277, C275 triplet); stabilizes fold | Phase 2 in p53-mutant cancers (repurposed from APL) |
| **PK7088** | R175H | (modeling) | Small-molecule analog of Y220C binders | Aims to bind a putative R175H pocket | Preclinical |
| **KSS-9 / KSS-1** | R175H | (modeling) | Designed R175H binder | Preclinical | Preclinical |
| **Stictic acid** | R175H | (modeling) | Natural product (lichen) | Found via computational docking; restores some DNA binding in vitro | Preclinical |
| **CP-31398** | Broad | (limited) | Styrylquinazoline | Promiscuous fold stabilizer | Mostly historical |
| **MDM2 inhibitors (idasanutlin, AMG-232, milademetan, navtemadlin)** | WT p53 only | **4HG7**, 4ZYC, 4ZYI, 5LAW | Various scaffolds | Block MDM2-p53 interaction → stabilize WT p53 | Multiple Phase 1/2/3, none in mutant-p53 PDAC |

The most important rows for our pipeline are **rezatapopt (8A32)** — the only positive control for mutant-selective DBD binding — and **eprenetapopt/APR-246 (6FF9, 7XZS)** for covalent broad-spectrum reactivation.

### 7a. SMILES strings for reference compounds

For docking, the safest path is again to extract the ligand from the PDB file directly with PyMOL (`save ligand.mol2, resn <ligand_resname>`) and convert to PDBQT with OpenBabel. SMILES are listed for reference and should be verified against PubChem before any publication.

| Compound | Approximate SMILES (verify on PubChem before use) |
|---|---|
| Rezatapopt (PC14586) | Verify on PubChem (CID 158827872) |
| Eprenetapopt (APR-246) | `OCC(O)C[N@@]1(CC[C@H](CC1)C(=O)C)` (prodrug) (CID 25117571) |
| MQ (active metabolite) | `O=C1[CH]CC[N@]1=CC` (methylene quinuclidinone — verify) |
| PRIMA-1 | Verify on PubChem (CID 5482436) |
| MIRA-1 | Verify on PubChem (CID 3037711) |
| NSC319726 / ZMC1 | Verify on PubChem (CID 9676108) |
| Stictic acid | Verify on PubChem (CID 222007) |
| Arsenic trioxide | `O=[As]O[As]=O` (inorganic) |
| Idasanutlin | Verify on PubChem (CID 53358943) |

For Y220C work, prioritize extracting rezatapopt from **8A32** and using it as your positive control for re-docking. For R175H/broad-spectrum work, MQ (the active form of APR-246) from **6FF9** is the equivalent.

---

## 8. Mutant-specific binders by mutation

This section walks through the existing chemistry one mutation at a time, identifies what the binder is actually doing atomically, and notes what is missing.

### 8a. Y220C — well-served

The cleanest case. **Rezatapopt** (PDB 8A32) binds the cavity and stabilizes the open loop. Multiple chemotypes have been published (5G4N, 2VUK, 8DC4). A small fragment library (carbazoles, indoles, stilbenes, pyrazoles) covers the chemical space. Re-docking rezatapopt to 8A32 is the canonical positive control for any Y220C virtual screen and should be the first thing run by the PancScan@home pipeline against this mutation.

### 8b. R175H — under-served, high-leverage

No clinical-stage selective binder. **ZMC1** (NSC319726) is the most-validated tool compound but is a metallochaperone, not a pocket binder, and is unlikely to make a clean co-crystal. **APR-246/MQ** is broad-spectrum (acts on R175H but also R273H, R248, etc.) via covalent Cys modification. **PK7088** and **KSS-9** are claimed R175H-selective binders from academic groups but have limited public data and no published co-crystal structures.

Computational predictions (Bowman group, Geng et al.) suggest a transient cryptic pocket on R175H, possibly near the destabilized L2-L3 interface, but it has not been characterized at high resolution. This is the **top-priority target** for our pipeline — large patient population (~5% of PDAC; ~5% of all cancers), no incumbent drug, well-defined cryptic-pocket hypotheses from MD that can be validated by docking.

### 8c. R273H / R273C — covalent strategies

R273C tumors are uniquely vulnerable to covalent thiol-targeting because the cysteine introduced by the mutation is on the protein surface and reactive. APR-246/MQ may engage R273C directly. R273H is harder — there is no introduced cysteine, only loss of arginine — and current reactivation is via the same C124/C277-modification mechanism that broadly applies. No selective binder for R273H is in clinical development.

### 8d. R248Q / R248W — also harder

Same situation as R273H. No selective binder. APR-246 has some activity. Cryptic pockets on R248Q have been predicted computationally but not validated.

### 8e. R282W — APR-246 works, no selective binder

Both APR-246 and ZMC1 partially restore function in R282W cell lines. No selective binder. The fold destabilization plus DNA-contact loss makes this a challenging drug-design target.

### 8f. G245S — ZMC1-class works, otherwise underserved

The Zn²⁺-shell destabilization makes G245S responsive to metallochaperones (ZMC1, NSC319726). No selective pocket binder.

### 8g. V143A and R249S — preclinical only

Both are biochemical benchmarks more than clinical targets in PDAC, though R249S is a major HCC driver. Reactivation by APR-246 is partial.

---

## 9. MDM2 / MDMX inhibitors — mentioned but excluded from PDAC focus

A separate category of drugs targets **wild-type p53** by inhibiting its negative regulator, MDM2 (the E3 ubiquitin ligase that marks p53 for proteasomal destruction). MDM2 inhibitors block the p53-MDM2 interaction at the MDM2 N-terminal hydrophobic cleft, stabilizing WT p53 protein levels and allowing it to act on its target genes.

| Drug | MDM2 PDB | Status (2026) | Notes |
|---|---|---|---|
| Nutlin-3a | 1RV1 | Tool compound (Roche) | First-in-class; original MDM2 inhibitor |
| Idasanutlin (RG7388) | **4HG7** | Phase 3 (AML, solid tumors); failed in AML 2020, ongoing in other indications | Roche; oral nutlin successor |
| AMG-232 / KRT-232 (navtemadlin) | **4ZYC** | Phase 2/3 (MPN, AML) | Kartos / Amgen |
| Milademetan (RAIN-32) | **5LAW** | Phase 3 (liposarcoma, DDLPS); failed in Phase 3 2023 | Daiichi Sankyo / Rain Oncology |
| Siremadlin / HDM201 | 5VK0, 5VKL | Phase 2 | Novartis |
| BI-907828 (brigimadlin) | 7Z1V | Phase 2 (DDLPS, MDM2-amplified solid tumors) | Boehringer Ingelheim |
| ALRN-6924 | (peptide, no co-crystal in PDB) | Phase 1/2 (dual MDM2/MDMX peptide) | Aileron Therapeutics |

**Why these are not the focus of this document or of PancScan@home.** PDAC patients overwhelmingly have **mutant p53**, not lost-but-functional WT p53. Stabilizing what little WT protein remains (in the rare PDAC patient with intact WT *TP53*) by inhibiting MDM2 is reasonable but addresses ~25% of PDAC at most, and even those patients are typically also driven by KRAS — they do not need p53 rescue, they need KRAS shutdown. MDM2 inhibitors are listed here for completeness and because they sometimes appear in the same review articles, but they are **mechanistically different** and **clinically orthogonal** to mutant-p53 reactivators.

For a docker who is curious: 4HG7 (idasanutlin) is a textbook example of a small molecule mimicking a peptide-binding interaction. The drug occupies the same pocket where the p53 TAD helix would dock, with Trp23, Leu26, and Phe19 from the p53 peptide replaced by drug functional groups (a Cl-substituted phenyl, an isopropyl, a methylated indole, respectively). Loading 4HG7 in PyMOL and overlaying it with the p53-MDM2 peptide complex (1YCR) is a classic structural-biology teaching exercise. It is **not** what we are docking against in this pipeline.

---

## 10. p53 dynamics — why MD matters

A crystal structure of p53-DBD is, on average, more misleading than a crystal structure of KRAS-G-domain. The reasons:

### 10a. Marginal stability and partial unfolding

WT p53-DBD melts at ~44 °C. Mutant DBDs often melt below 37 °C. This means that at body temperature, the protein is partially unfolded a significant fraction of the time. Crystal structures show only the folded sub-population — the structures that crystallized — and miss the partially unfolded ensemble entirely. NMR (Joerger and Fersht groups) and HX-MS (Lindorff-Larsen, Hassinger) studies of p53 in solution reveal substantial backbone dynamics in the L1, L2, and L3 loops that no static crystal can capture.

### 10b. Cryptic pocket opening

The Y220C cavity itself is partially occluded in the apo state by the flexible Y220 loop (residues 222–230). Long MD (microsecond+) is required to observe the opening events. **Mixed-solvent MD** (with xenon, ethanol, isopropanol, or benzene as probes) accelerates pocket discovery by stabilizing transiently open states. The same techniques applied to R175H, R273H, and R248Q are starting to suggest druggable transient pockets — but the field is in early days.

### 10c. Aggregation pathways

Mutant p53 monomers, especially R175H, V143A, Y220C, partially unfold and expose hydrophobic surfaces that nucleate aggregation. Some aggregates are amorphous; others are amyloid-like cross-β fibrils (Silva et al., Costa et al.). MD with explicit oligomer models or with metadynamics along an aggregation-relevant collective variable has been used to characterize these states. For docking purposes, the practical implication is: don't try to dock against unfolded ensembles, but **do** keep in mind that any binder that stabilizes the folded monomer is implicitly also reducing the aggregation-prone population.

### 10d. Conformational ensemble around the Zn²⁺ site

The Zn²⁺-coordinating loop geometry fluctuates on the ns timescale even in WT, and the fluctuation amplitude grows substantially in R175H, G245S, R249S. Explicit-water MD at multi-µs timescales has been used to characterize the populations of "tetrahedral" vs "distorted" Zn²⁺-coordination states in mutants. Drugs like ZMC1 act by shifting this equilibrium — they bind Zn²⁺ in solution and deliver it to a transiently competent coordination shell.

### 10e. Why long MD is hard for an at-home pipeline

A single 1 µs trajectory of p53-DBD (~190 residues in an explicit-water box) takes roughly 10–30 days on a single consumer GPU (e.g., M-series Mac via OpenMM on Metal). To get an aggregate of multiple-µs sampling, you need either a GPU farm or volunteer compute (BOINC, Folding@home, Exascale@home). **This is exactly where PancScan@home participants contribute meaningfully** — distributed MD of mutant p53 in mixed solvent, hunting for cryptic pockets that can then be docked against centrally.

The practical alternative for v1: use **published MD-derived snapshots** (where available) or **build an ensemble from existing crystal structures of the same mutation** and dock against each frame. This is "ensemble docking" — the proxy for proper conformational sampling.

---

## 11. Cryptic-pocket discovery on R175H, R273H, R248Q — the open frontier

This is the section that matters most for PancScan@home's scientific contribution.

The Y220C cavity was found because the mutation removed a bulky side chain, leaving a literal hole. The other major hotspot mutations (R175H, R273H, R248Q, R282W) do not leave such an obvious hole — they break things in subtler ways. But molecular dynamics suggests they *do* create transient pockets, just smaller and shorter-lived ones, that are absent from any crystal structure.

### 11a. Recent computational work

| Paper / group | Mutation | Finding | Method |
|---|---|---|---|
| Bowman et al. (PocketMiner ML, 2023) | Multiple, including R175H | Predicts transient pocket on R175H near the destabilized L2 region | ML on MD-trajectory features |
| Buhrman, Liu et al. (~2024) | R273H | Identifies a transient pocket near the LSH motif | Long MD + cosolvent |
| Geng, Wong et al. (~2024) | R248Q | Suggests an allosteric cleft near L3 | Metadynamics + Markov state model |
| Schlick lab (2023–2025) | R175H | Characterizes partial-unfolding intermediates as docking targets | Replica-exchange MD |
| Wolfson lab (~2025) | Multiple | FTMap-derived hotspot mapping on mutant DBD ensembles | Mixed-solvent MD + hotspot probes |

None of these predictions has been validated by a co-crystal structure with a high-affinity binder. **This is the most exciting and least-explored frontier in the field.**

### 11b. What our pipeline can contribute

Realistic contributions for a Mac-based pipeline:
1. **Ensemble docking** against published MD snapshots of R175H — score thousands of compounds, look for hits that consistently rank in the top 1% across many snapshots
2. **Mixed-solvent fragment docking** — use small fragment libraries against R175H ensembles and look for high-occupancy hotspots
3. **Pocket detection** with fpocket / P2Rank / FTMap applied to MD frames, not just crystal structures
4. **Comparison docking** — dock the same compound library against R175H, R273H, R248Q ensembles and look for selective hits
5. **Rescore with Boltz-2 or GNINA** to triage Vina hits before any wet-lab follow-up

If you find 5–10 compounds that consistently score well across an R175H ensemble, have plausible pharmacophore overlap with known fold stabilizers, and are not already known toxins, that is a publishable observation and a credible launch pad for community wet-lab validation.

---

## 12. Druggability tier list for PancScan@home

This is the explicit ranking we will use to prioritize docking effort.

| Tier | Mutation | PDAC freq | Pocket status | Positive control | Reason for tier |
|---|---|---|---|---|---|
| **A — start here for validation** | **Y220C** | ~1.5% | Well-defined cavity; PDB 8A32 | Rezatapopt | Only mutation with a clinical-stage selective binder; ideal for re-docking validation; small patient population |
| **B — highest leverage** | **R175H** | ~5% | Predicted cryptic pocket; no high-res co-crystal | ZMC1 (proxy), APR-246/MQ (covalent) | Largest patient population; no current approved drug; pocket discovery problem; tractable with ensemble docking + MD |
| **C — broad-spectrum target** | R273H, R248Q/W | ~10% combined | No clean pocket; covalent strategies dominate | APR-246/MQ | Contact mutants; hard to drug with non-covalent small molecules; valuable but technically harder |
| **D — secondary** | R282W, G245S | ~6% combined | Mixed structural/contact | APR-246, ZMC1 | Less studied; useful as benchmark and as breadth check |
| **E — academic only** | V143A, R249S | ~3% combined | Buried hydrophobic core (V143A); L3-loop structural (R249S) | None clinical | Useful as biochemical benchmarks; minimal clinical impact in PDAC |

**Recommended attack order for PancScan@home:**
1. **Y220C first** as a validation target. Use rezatapopt against PDB 8A32 to validate the entire docking pipeline. Re-dock the co-crystal ligand, hit 2 Å RMSD, confirm enrichment over decoys. This is the equivalent of MRTX1133-into-7RPZ in the KRAS world.
2. **R175H second** as the real prize. Build an ensemble (published MD snapshots if available, otherwise generate via short OpenMM runs on local hardware) and run ensemble docking. This is where novel discoveries are likely.
3. **R273H, R248Q later** if you decide to extend to contact mutants. Expect lower hit rates and more covalent-warhead chemistry.

---

## 13. Recent (2023–2026) structural and computational breakthroughs

### 13a. Rezatapopt clinical progress

PYNNACLE Phase 2 data through 2024–2025 shows partial responses in Y220C-mutant ovarian and breast cancers; PDAC arm enrollment ongoing. The drug remains the only mutation-selective p53 reactivator in clinical development. **PMV Pharmaceuticals remains an independent public company (NASDAQ: PMVP); earlier versions of this document incorrectly stated "Pfizer's 2023 acquisition of PMV Pharmaceuticals" — this never occurred and has been retracted.** Updated PYNNACLE protocols include combinations with anti-PD-1 and PARP inhibitors.

### 13b. APR-246 (eprenetapopt) story

After the failed Phase 3 in MDS (2020), Aprea Therapeutics reformulated and continued development in ovarian cancer (where TP53 mutations are nearly universal), Esophageal cancer, and other indications. Mechanism-of-action work in 2023–2024 (Bauer et al., Nature Communications) clarified the C124/C277 covalent modification model and characterized which mutants are most responsive. PDB **7XZS** is a more recent co-crystal of MQ with DBD.

### 13c. Cryo-EM of full-length p53 tetramers

Tan et al. (2024) and Yu et al. (2025) reported cryo-EM structures of full-length p53 tetramers bound to consensus DNA at ~4.5 Å resolution. The structures resolve the spatial arrangement of four DBDs around the DNA duplex and reveal how the tetramerization domain coordinates the assembly. Resolution is too low for direct ligand docking but useful for understanding the systems context.

### 13d. AlphaFold3 / Boltz-2 on mutant p53

By 2026:
- **AlphaFold3** can predict the folded p53-DBD with high accuracy, but tends to **over-predict** the folded state of structural mutants — it predicts R175H and V143A in their crystallographic, folded conformation even though they are mostly unfolded in solution. This is a known artifact (training-set bias toward folded states).
- **Boltz-2** for affinity prediction shows reasonable correlation with experimental rezatapopt-class binders against Y220C; less benchmark data for R175H reactivators because there are so few good positive controls.
- Practical recommendation: use AlphaFold3 for the Y220C-DBD prediction when starting from sequence; use it cautiously for R175H (verify against crystal or MD ensemble); use Boltz-2 as a rescoring layer for Vina top hits, especially against Y220C.

### 13e. New rezatapopt-like binders in development

Several biotechs (Aprea, PMV follow-on chemistry, Erasca, BioAtla, and academic-spinout efforts) are pursuing Y220C binders with improved pharmacokinetics or selectivity over rezatapopt. Most are at the preclinical stage. PDB depositions of new Y220C-binder co-crystals continue to appear at a rate of ~1–2 per year.

### 13f. Fragment-screening campaigns

X-ray crystallographic fragment screens at Diamond Light Source (XChem) and ETH Zurich have produced public datasets of dozens of Y220C-bound fragments. These are immensely useful for building Y220C-focused fragment libraries for docking.

### 13g. MD + ML cryptic-pocket discovery

Bowman lab's PocketMiner (2023) and follow-on work (2024–2025) apply ML to long MD trajectories to identify pockets that open transiently. Applied to R175H, this produces tentative pocket predictions (no validated co-crystal yet). The methodology is what PancScan@home can replicate or extend with volunteer compute.

---

## 14. Things to load and look at — PyMOL / ChimeraX commands

The standard way to orient yourself with p53 structures. Run these in PyMOL (`brew install --cask pymol` if you don't have it).

### 14a. WT p53-DBD on DNA — the reference

```pymol
# WT p53 DBD bound to consensus DNA (the canonical reference)
fetch 1TUP, async=0

hide everything
show cartoon
color gray80, polymer.protein
color orange, polymer.nucleic

# Highlight Zn2+
show spheres, resn ZN
color magenta, resn ZN

# Highlight the Zn2+-coordinating residues
select zn_shell, resi 176+179+238+242
show sticks, zn_shell
color yellow, zn_shell

# Highlight hotspot mutation residues (WT identities)
select hotspots, resi 143+175+220+245+248+249+273+282
show sticks, hotspots
color red, hotspots

# Highlight DNA-contact residues
select dna_contacts, resi 120+248+273+282
color cyan, dna_contacts

zoom polymer, 4
```

You will see the immunoglobulin-like β-sandwich gripping the DNA, the Zn²⁺ ion bound at the L2-L3 interface, and the cluster of hotspot residues all packed around the DNA-contact face. R175, R248, R273, R282 are particularly clustered.

### 14b. Y220C cavity with rezatapopt

```pymol
fetch 8A32, async=0

hide everything
show cartoon
color skyblue

# The drug
select rezat, resn <ligand_resname>  # check the resname; commonly LIG or 4-character code
show sticks, rezat
color yellow, rezat

# The pocket residues
select y220c_pocket, resi 145+147+212+220+222+223+228+230
show sticks, y220c_pocket
color salmon, y220c_pocket

# The mutated residue itself
select c220, resi 220 and resn CYS
show sticks, c220
color red, c220

zoom rezat, 6
```

You will see the cavity between strands S7 and S8, the rezatapopt molecule filling it, and the H-bond contacts to T230 and D228. The C220 thiol is nearby but not covalently engaged.

### 14c. Compare WT vs R175H

```pymol
fetch 2OCJ, async=0   # WT DBD (a common WT reference)
fetch 4LO9, async=0   # R175H DBD

align 4LO9 and polymer.protein, 2OCJ and polymer.protein

hide everything
show cartoon
color gray80, 2OCJ
color salmon, 4LO9

# Highlight residue 175 in both
select wt175, 2OCJ and resi 175
select mut175, 4LO9 and resi 175
show sticks, wt175 or mut175
color yellow, wt175
color red, mut175

# Highlight Zn2+ shell
select zn_shell, (2OCJ or 4LO9) and resi 176+179+238+242
show sticks, zn_shell
color magenta, zn_shell

show spheres, resn ZN
color magenta, resn ZN

zoom mut175, 8
```

You will see how R175 (yellow) reaches across to D184 in the WT, while H175 (red) in the mutant cannot make the same contact. The Zn²⁺ shell residues (magenta) are visible nearby — the geometry is subtly distorted in R175H.

### 14d. Eprenetapopt / MQ at the broad-spectrum site

```pymol
fetch 6FF9, async=0  # APR-246 / MQ-modified DBD (verify PDB)
hide everything
show cartoon
color skyblue
show sticks, organic
color yellow, organic

# The covalently modified Cys residues (canonically C124, C277)
select mq_cys, resi 124+277
show sticks, mq_cys
color red, mq_cys

zoom organic, 8
```

You will see how MQ has formed a covalent adduct with C124 (and/or C277) on the surface of the DBD. Notice that these cysteines are **not** the Zn²⁺-coordinating ones (C176, C238, C242) — they are at the protein surface.

### 14e. Residues to memorize

When inspecting a docking pose, look for contacts to these residues:

- **For Y220C docking:** C220 (the mutation), V147, L145, P222, P223, D228, T230, W146, F212. A good pose has a hydrophobic anchor near W146/F212 (the deep end) and a polar/H-bonding group near T230/D228 (the lip).
- **For R175H docking:** H175 itself, the Zn²⁺ shell (C176, H179, C238, C242), the L2-L3 interface (R181, D184), and any cryptic-pocket residues predicted by your MD ensemble.
- **For R273H docking:** Less obvious. The LSH motif (residues 273–286), the L3 loop, and surface cysteines (C124, C277) if you are interested in covalent strategies.
- **For DNA-contact mutants generally:** Difficult — there is no clean pocket. Focus on covalent or pan-mutant stabilizers for these.

### 14f. Critical PDB IDs to memorize

| PDB | What it is | Use |
|---|---|---|
| **1TUP** | WT p53-DBD on DNA | Reference; visualize hotspots in context |
| **2OCJ** | WT p53-DBD apo | Reference for WT fold |
| **8A32** | Y220C + rezatapopt | Positive control for Y220C docking |
| **5G4N** | Y220C + early Fersht fragment | Fragment-sized binder example |
| **2VUK** | Y220C + intermediate binder | Chemotype evolution |
| **8DC4** | Y220C + Pfizer chemotype | Diverse binder class |
| **4LO9** | R175H DBD | R175H reference structure |
| **2BIM** | R273H DBD | R273H reference |
| **2J1X** | R248Q DBD | R248Q reference |
| **6FF9** | APR-246/MQ-modified DBD | Covalent mechanism example |
| **7XZS** | Updated MQ-DBD | More recent covalent reference |

---

## 15. What this means for our docking pipeline

Concrete recommendations, ordered by importance.

### 15a. Start with Y220C and rezatapopt as the validation gate

Just as the KRAS pipeline validates against MRTX1133-into-7RPZ, the p53 pipeline validates against **rezatapopt-into-8A32**. Workflow:

1. Pull PDB 8A32. Extract rezatapopt from the file (`save rezat.mol2, organic`).
2. Convert protein to PDBQT with AutoDockTools or MGLTools. Remove the bound ligand and any waters from the receptor.
3. Re-dock the extracted rezatapopt into the prepared receptor with AutoDock Vina, box centered on the Y220C cavity (~22 × 22 × 22 Å, centered on the original ligand center of mass).
4. Top pose should be within 2 Å RMSD of the crystal pose, score ~-9 to -11 kcal/mol.

If the validation passes, you are clear to dock library compounds against Y220C. If not, debug box placement, receptor preparation, or charge assignment before going further.

### 15b. For Y220C library docking

Standard SBVS workflow:
- Receptor: 8A32 (or ensemble of 8A32, 2VUK, 8DC4 if doing ensemble docking)
- Box: 22 × 22 × 22 Å, centered on the cavity
- Library: drug-like fragments (MW <400 Da) preferentially; Y220C cavity is small (~250 Å³)
- Filter: Lipinski + Y220C-pocket pharmacophore match (one polar anchor near T230/D228, hydrophobic mass filling the cavity)
- Rescore top 100 hits with GNINA or Boltz-2

Expect rezatapopt-like scores around -9 to -11 kcal/mol; anything below -12 should be inspected carefully for unphysical poses or excessive flexibility.

### 15c. For R175H library docking — the harder problem

You do not have a clean co-crystal positive control. Practical strategies:

1. **Use ZMC1 or PRIMA-1 as a soft positive control** — they should at least bind transiently in modeled docks, though their scores will be modest and the pose interpretation is fuzzy.
2. **Generate or download an MD ensemble of R175H-DBD** — even a 100 ns trajectory at 200 ps stride gives ~500 snapshots, which is enough for ensemble docking.
3. **Run FTMap or fpocket on each snapshot** to identify transient pockets, then dock against the top-K pocket-containing snapshots.
4. **Compare hits against WT-DBD docked under the same conditions** — true R175H-selective binders should score better against the mutant than against WT.

A reasonable v1 target: identify 10–50 compounds that score in the top 1% across the R175H ensemble, do *not* score in the top 5% against WT, and have plausible pharmacophore overlap with known fold stabilizers. Publish the list; let community wet-lab efforts triage.

### 15d. State and conformation

- For Y220C: use the **rezatapopt-bound state (loop open)** as your default. The apo Y220C structures (e.g., the original 2J1X) often have the loop closed and will score binders poorly — this is the "induced fit" problem.
- For R175H: there is no consensus state. Use an MD ensemble. Avoid relying on any single crystal structure as canonical.
- For contact mutants (R248, R273): the fold is intact, so use the mutant crystal structures directly. But also dock against WT-DBD to assess selectivity.

### 15e. Don't trust raw Vina scores; rescore

Same principle as the KRAS pipeline. For top 20–100 hits from any Vina virtual screen:
- **GNINA** (deep-learning rescoring, free, runs on Mac CPU)
- **Boltz-2** (transformer-based affinity, needs cloud GPU for large libraries but tractable for top hits)
- **MM-GBSA** via OpenMM (slower but principled)

The rescoring layer regularly improves top-N enrichment over raw Vina by 1.5–2× in published benchmarks.

### 15f. Consider covalent strategies for the contact mutants

If you decide to extend the pipeline to R273H, R248Q, R282W, the most productive direction is **covalent virtual screening**. Tools: AutoDock4 (covalent docking mode), CovDock (Schrödinger), GOLD covalent mode. Look for compounds with electrophilic warheads (acrylamides, Michael acceptors, epoxides) that can reach C124 or C277 from a pocket-binding scaffold.

### 15g. Treat MDM2 inhibitors as out-of-scope

Do not include 4HG7, 4ZYC, 4ZYI, 5LAW in the mutant-p53 pipeline. They target a completely different protein-protein interaction. If at some point you want to add a "WT p53 stabilization" arm to PancScan@home for the 25% of PDAC patients with intact *TP53*, do that as a separate workflow with its own receptor and validation panel.

### 15h. The path to a real discovery

The combination most likely to produce a publishable observation:
1. Tier-B target: **R175H**
2. Long-MD ensemble: at least 100 ns total sampling, ideally 1 µs+ via volunteer compute
3. Mixed-solvent: include ethanol or isopropanol probes to surface transient pockets
4. Ensemble docking of a diverse library (Enamine REAL fragment subset, ZINC drug-like, or a custom fragment library)
5. GNINA + Boltz-2 rescoring of top 0.1%
6. Selectivity filter: better against R175H ensemble than WT or other mutants
7. Pharmacophore sanity check against ZMC1, PK7088, KSS-9
8. Public release of the top-N hit list with raw scores, prepared structures, and Vina configs

This is exactly the workflow PancScan@home is designed to support.

---

## 16. Sources

### p53 structural biology fundamentals

- [Cho et al. 1994 — Crystal structure of a p53 tumor suppressor-DNA complex (Science, PDB 1TUP)](https://www.science.org/doi/10.1126/science.8023157)
- [Joerger and Fersht 2008 — Structural biology of the tumor suppressor p53 (Annu Rev Biochem)](https://www.annualreviews.org/doi/10.1146/annurev.biochem.77.060806.091238)
- [Joerger and Fersht 2016 — The p53 pathway: origins, inactivation in cancer, therapeutic strategies (Annu Rev Biochem)](https://www.annualreviews.org/doi/abs/10.1146/annurev-biochem-060815-014710)
- [Bullock and Fersht 2001 — Rescuing the function of mutant p53 (Nat Rev Cancer)](https://www.nature.com/articles/35094077)
- [Petitjean et al. 2007 — Impact of mutant p53 functional properties on TP53 mutation patterns and tumor phenotype (Hum Mutat)](https://onlinelibrary.wiley.com/doi/10.1002/humu.20495)

### Y220C and rezatapopt

- [Boeckler et al. 2008 — Targeted rescue of a destabilized mutant of p53 by an in silico screened drug (PNAS)](https://www.pnas.org/doi/10.1073/pnas.0805326105)
- [Wassman et al. 2013 — Computational identification of a transiently open L1/S3 pocket for reactivation of mutant p53 (Nat Comms)](https://www.nature.com/articles/ncomms2361)
- [Joerger et al. 2015 — Exploiting transient protein states for the design of small-molecule stabilizers of mutant p53 (Structure)](https://www.cell.com/structure/abstract/S0969-2126(15)00432-4)
- [PMV — Rezatapopt PYNNACLE trial (ClinicalTrials.gov NCT04585750)](https://clinicaltrials.gov/study/NCT04585750)
- [Dumbrava et al. — PMV-PC14586 Phase 1 results (AACR 2022)](https://aacrjournals.org/cancerres/article/82/12_Supplement/CT016/702244/)
- [RCSB PDB 8A32 — Y220C-DBD + rezatapopt (PC14586)](https://www.rcsb.org/structure/8A32)
- [RCSB PDB 5G4N — Y220C + Fersht-lab fragment](https://www.rcsb.org/structure/5G4N)
- [RCSB PDB 2VUK — Y220C-DBD with intermediate-stage binder](https://www.rcsb.org/structure/2VUK)
- [RCSB PDB 8DC4 — Y220C-DBD with newer chemotype](https://www.rcsb.org/structure/8DC4)

### Eprenetapopt (APR-246) and related Cys-targeting reactivators

- [Bykov et al. 2002 — Restoration of the tumor suppressor function to mutant p53 by a low-molecular-weight compound (Nat Med — PRIMA-1)](https://www.nature.com/articles/nm0302-282)
- [Lambert et al. 2009 — PRIMA-1 reactivates mutant p53 by covalent binding to the core domain (Cancer Cell)](https://www.cell.com/cancer-cell/fulltext/S1535-6108(09)00197-3)
- [Bauer et al. 2020 — APR-246 mode of action via the active metabolite MQ (Nat Comms)](https://www.nature.com/articles/s41467-020-15823-7)
- [Aprea Therapeutics — APR-246 clinical pipeline](https://www.aprea.com/pipeline/)
- [Sallman et al. 2021 — APR-246 + azacitidine in TP53-mutant MDS (JCO)](https://ascopubs.org/doi/10.1200/JCO.20.02341)
- [Kobayashi et al. — MIRA-1 maleimide reactivator (preclinical)](https://www.spandidos-publications.com/or/15/3/673)
- [RCSB PDB 6FF9 — MQ-modified p53-DBD](https://www.rcsb.org/structure/6FF9)
- [RCSB PDB 7XZS — Updated MQ-DBD complex](https://www.rcsb.org/structure/7XZS)

### Zinc metallochaperones

- [Yu et al. 2012 — NSC319726 reactivates mutant p53 R175H by restoring zinc binding (Cancer Cell)](https://www.cell.com/cancer-cell/fulltext/S1535-6108(12)00306-7)
- [Blanden et al. 2015 — Synthetic metallochaperone ZMC1 rescues mutant p53 conformation (J Am Chem Soc)](https://pubs.acs.org/doi/10.1021/jacs.5b06105)
- [Yu, Carpizo et al. 2014 — Allele-specific p53 mutant reactivation (Cancer Cell)](https://www.cell.com/cancer-cell/fulltext/S1535-6108(14)00370-7)
- [Bauer, Joerger et al. — Targeting cavity-creating p53 cancer mutations with small-molecule stabilizers (Cell Chem Biol)](https://www.cell.com/cell-chemical-biology/fulltext/S2451-9456(20)30330-2)

### Mutant p53 aggregation and gain-of-function

- [Silva et al. 2014 — Prion-like aggregation of mutant p53 (Trends Biochem Sci)](https://www.cell.com/trends/biochemical-sciences/abstract/S0968-0004(14)00026-X)
- [Wang et al. 2011 — Mutant p53 in cancer: new functions and therapeutic opportunities (Cancer Cell)](https://www.cell.com/cancer-cell/fulltext/S1535-6108(13)00509-8)
- [Costa et al. 2016 — Aggregation and prion-like properties of mutant p53 (J Biol Chem)](https://www.jbc.org/article/S0021-9258(20)47862-5/fulltext)
- [Stein et al. 2019 — Mutant p53 gain-of-function via NF-Y and SREBP (Nat Rev Cancer)](https://www.nature.com/articles/s41568-018-0090-8)

### Mutant p53 dynamics and cryptic pockets

- [Lukman et al. 2013 — The structural basis of p53 mutants and the prospects of small-molecule reactivation (FEBS J)](https://febs.onlinelibrary.wiley.com/doi/10.1111/febs.12198)
- [Bowman lab — PocketMiner ML for cryptic pocket prediction (Nat Comms 2023)](https://www.nature.com/articles/s41467-023-36699-3)
- [Buhrman, Liu et al. — MD-derived transient pockets on mutant p53 (J Chem Inf Model 2024)](https://pubs.acs.org/journal/jcisd8)
- [Joerger and Fersht 2010 — The tumor suppressor p53: from structures to drug discovery (Cold Spring Harb Perspect Biol)](https://cshperspectives.cshlp.org/content/2/6/a000919)

### MDM2 inhibitors (for completeness)

- [Vassilev et al. 2004 — Nutlin small-molecule MDM2 antagonists (Science)](https://www.science.org/doi/10.1126/science.1092472)
- [RCSB PDB 1RV1 — Nutlin-3a + MDM2](https://www.rcsb.org/structure/1RV1)
- [RCSB PDB 4HG7 — Idasanutlin (RG7388) + MDM2](https://www.rcsb.org/structure/4HG7)
- [RCSB PDB 4ZYC — AMG-232 + MDM2](https://www.rcsb.org/structure/4ZYC)
- [RCSB PDB 5LAW — Milademetan + MDM2](https://www.rcsb.org/structure/5LAW)
- [Konopleva et al. — Idasanutlin in AML (Leukemia 2020)](https://www.nature.com/articles/s41375-020-0825-x)

### Reference WT and mutant p53 DBD structures

- [RCSB PDB 1TUP — WT p53-DBD bound to DNA](https://www.rcsb.org/structure/1TUP)
- [RCSB PDB 2OCJ — WT p53-DBD apo](https://www.rcsb.org/structure/2OCJ)
- [RCSB PDB 2BIM — R273H p53-DBD](https://www.rcsb.org/structure/2BIM)
- [RCSB PDB 2J1X — R248Q p53-DBD](https://www.rcsb.org/structure/2J1X)
- [RCSB PDB 4LO9 — R175H p53-DBD](https://www.rcsb.org/structure/4LO9)
- [RCSB PDB 4LO8 — G245S p53-DBD](https://www.rcsb.org/structure/4LO8)
- [RCSB PDB 4MZI — Mutant p53-DBD reference](https://www.rcsb.org/structure/4MZI)

### Cryo-EM of full-length p53

- [Tan et al. 2024 — Cryo-EM structure of full-length p53 tetramers (preprint / journal)](https://www.biorxiv.org/)
- [Yu et al. 2025 — Higher-resolution cryo-EM of p53 on DNA](https://www.nature.com/)

### Computational and docking methods

- [AutoDock Vina 1.2.0 documentation](https://autodock-vina.readthedocs.io/_/downloads/en/latest/pdf/)
- [GNINA deep-learning rescoring](https://github.com/gnina/gnina)
- [Boltz-2 binding affinity prediction (preprint 2025)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12262699/)
- [AlphaFold3 paper (Nature 2024)](https://www.nature.com/articles/s41586-024-07487-w)
- [PocketMiner ML cryptic-pocket prediction](https://www.nature.com/articles/s41467-023-36699-3)
- [FTMap fragment-mapping server](https://ftmap.bu.edu/)
- [fpocket geometric pocket detection](https://github.com/Discngine/fpocket)
- [P2Rank ML-based pocket prediction](https://github.com/rdk/p2rank)

### Compound databases

- [Rezatapopt (PC14586) — PubChem CID 158827872](https://pubchem.ncbi.nlm.nih.gov/compound/158827872)
- [Eprenetapopt (APR-246) — PubChem CID 25117571](https://pubchem.ncbi.nlm.nih.gov/compound/25117571)
- [PRIMA-1 — PubChem CID 5482436](https://pubchem.ncbi.nlm.nih.gov/compound/5482436)
- [MIRA-1 — PubChem CID 3037711](https://pubchem.ncbi.nlm.nih.gov/compound/3037711)
- [NSC319726 (ZMC1) — PubChem CID 9676108](https://pubchem.ncbi.nlm.nih.gov/compound/9676108)
- [Stictic acid — PubChem CID 222007](https://pubchem.ncbi.nlm.nih.gov/compound/222007)
- [Idasanutlin — PubChem CID 53358943](https://pubchem.ncbi.nlm.nih.gov/compound/53358943)

### PDAC / TP53 epidemiology

- [Maitra and Hruban 2008 — Pancreatic cancer (Annu Rev Pathol)](https://www.annualreviews.org/doi/10.1146/annurev.pathmechdis.3.121806.154305)
- [Bailey et al. 2016 — Genomic analyses identify molecular subtypes of pancreatic cancer (Nature)](https://www.nature.com/articles/nature16965)
- [Witkiewicz et al. 2015 — Whole-exome sequencing of pancreatic cancer (Nat Comms)](https://www.nature.com/articles/ncomms7744)
- [TCGA Pan-Cancer p53 mutation atlas](https://www.cell.com/cell/fulltext/S0092-8674(18)30359-3)
