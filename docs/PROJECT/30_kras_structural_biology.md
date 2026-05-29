# 30. KRAS Structural Biology — Atom-Level Foundation for Docking

**Purpose of this document.** Everything you need to know about the KRAS protein so that when you sit down at a computer and dock a compound against it, you understand what the atoms are doing, why the score is what it is, and why your choice of structure, conformation, and binding-site definition matters more than your choice of ligand. This is the science foundation for the practical pipeline in later notes.

**Conventions used here.**
- "Residue 12" means the twelfth amino acid in the KRAS protein chain, counting from the N-terminus. KRAS is 189 residues total.
- "Switch I" and "Switch II" refer to two short, mobile loops that change shape when KRAS turns ON or OFF. These are the most important regions in this document.
- Single-letter amino acid codes (G = glycine, D = aspartate, C = cysteine, V = valine, R = arginine, Q = glutamine, H = histidine, T = threonine, Y = tyrosine) are used throughout. "G12D" means "glycine at position 12 has been replaced by aspartate."
- PDB IDs (4-character codes like `7RPZ`) refer to entries in the Protein Data Bank — the public archive of experimentally determined 3D structures of biological molecules. You can load any of them into PyMOL with `fetch 7RPZ`.
- Energies are reported in kilocalories per mole (kcal/mol). More negative is more favorable binding.

---

## 1. The KRAS protein at a glance

KRAS is a small GTPase (a protein that binds and slowly hydrolyzes guanosine triphosphate, GTP, into guanosine diphosphate, GDP). It is the most frequently mutated oncogene in human cancers, and it is mutated in roughly 90% of pancreatic ductal adenocarcinomas (PDAC), with G12D being the single most common variant in PDAC (~40% of PDAC cases).

The full protein is 189 amino acids long and breaks cleanly into two pieces:

```
   N-term                                                            C-term
     |                                                                  |
     |<-------- G-domain (residues 1-166) ----------->|<-- HVR  --->|
     |                                                |  (167-189) |
     |  catalytic core, GTP/GDP-binding, switches,    |  membrane  |
     |  Mg2+ coordination, effector interface         |  anchor    |
     |                                                |  + farnesyl|
     |  -- this is what crystallographers see --      |  -- this   |
     |                                                |     is     |
     |                                                |  disordered|
     |                                                |  in most   |
     |                                                |  PDBs --   |
```

### 1a. The G-domain (residues 1–166)

This is the structured, well-folded "head" of the protein. It is a classic small-GTPase fold: a central six-stranded beta-sheet sandwiched by five alpha-helices. Almost every published KRAS crystal structure shows only this region. The G-domain contains five short, conserved sequence motifs called the **G-box motifs (G1–G5)**, each one responsible for a specific contact with the bound nucleotide.

| Motif | Residues | Sequence | Function |
|-------|----------|----------|----------|
| G1 (P-loop) | 10–17 | `GxxxxGK[ST]` | Wraps the phosphates of GTP/GDP; cradles the beta- and gamma-phosphates |
| G2 (Switch I) | 30–40 | `T` at residue 35 is key | Contacts gamma-phosphate of GTP; coordinates Mg2+ |
| G3 (Switch II / DxxG) | 57–60 | `DxxG` (D57, G60) | Contacts gamma-phosphate via G60 backbone; D57 coordinates Mg2+ |
| G4 (NKxD) | 116–119 | `NKxD` | Reads the guanine base, providing GTP/GDP specificity |
| G5 (SAK / EXSAK) | 145–147 | `SAK` | Stabilizes guanine binding |

The **P-loop** (G1) is the "phosphate-binding loop" — a glycine-rich loop that wraps tightly around the negatively charged phosphates of GTP. The fact that residue 12 sits at the bottom of the P-loop, with its side chain pointing directly toward the gamma-phosphate, is the central reason G12 mutations are so devastating. There is no room there for anything bigger than a hydrogen atom (which is what glycine's "side chain" is).

### 1b. Switch I and Switch II — the conformational switches

These are two short loops that physically rearrange depending on whether the bound nucleotide is GTP or GDP. They are the reason this protein is called a "molecular switch."

- **Switch I (residues 30–40)** — contains threonine 35 (T35), whose hydroxyl group coordinates the magnesium ion that bridges the beta- and gamma-phosphates of GTP. When the gamma-phosphate leaves (becoming GDP), T35 loses its anchor and Switch I springs outward.
- **Switch II (residues 60–76)** — contains glycine 60 (G60), whose backbone amide hydrogen-bonds to the gamma-phosphate, and glutamine 61 (Q61), which positions the catalytic water molecule that attacks the gamma-phosphate during hydrolysis. Switch II is much longer and more dynamic than Switch I.

When KRAS is **GTP-bound (ON)**, both switches are clamped down on the nucleotide. The "effector lobe" face of the protein is then in the conformation that allows RAF kinase, PI3K, and other downstream effectors to bind and propagate the growth signal.

When KRAS is **GDP-bound (OFF)**, both switches relax outward, becoming flexible and disordered. The effector face is no longer competent for binding RAF/PI3K. The cell is now "off" for growth.

### 1c. The hypervariable region (HVR, residues 167–189)

The last ~23 residues are intrinsically disordered (floppy, no fixed structure). They end in a four-residue motif called **CAAX** (Cys-aliphatic-aliphatic-any), specifically `-CVIM` in KRAS4B. After translation, three things happen to this tail:

1. **Farnesylation** — a 15-carbon hydrophobic lipid is attached to C185 via a thioether bond. This is what anchors KRAS into the inner leaflet of the plasma membrane.
2. **Proteolytic cleavage** — the last three residues (-VIM) are clipped off.
3. **Carboxymethylation** — the new C-terminal carboxylate (on C185) is methylated.

Just upstream of C185, KRAS4B (the main isoform) has a **polybasic stretch** of lysines (the "K-cluster": K175, K176, K177, K178, K179, K180). These positively charged residues are attracted to negatively charged phospholipid headgroups (PIP2, PS) in the inner leaflet, which further anchors KRAS to the membrane.

Recent work shows KRAS spends most of its time in a "membrane-distal" state where the G-domain floats freely above the membrane, tethered only by the HVR and farnesyl, but tumbles into a "membrane-proximal" state where the G-domain itself contacts the lipid bilayer. The orientation of the G-domain relative to the membrane is now thought to gate effector access. For our docking purposes, the HVR is usually deleted from the model — but it matters for understanding why structures look the way they do.

### 1d. Cellular regulators

KRAS does not work alone. Two classes of proteins control its on/off state:

- **GEFs (Guanine nucleotide Exchange Factors)** — SOS1 and SOS2 — pry GDP out of KRAS so that the much more abundant cellular GTP can rush in. This turns KRAS ON.
- **GAPs (GTPase Activating Proteins)** — NF1 (neurofibromin) and RASA1 (p120-GAP) — stick a critical "arginine finger" into KRAS's active site to accelerate GTP hydrolysis ~10⁵-fold. This turns KRAS OFF.

KRAS mutations break the OFF switch. Specifically, they make KRAS resistant to GAPs.

---

## 2. GTP/GDP cycling — how a normal switch works

The catalytic cycle of wild-type KRAS:

```
       (GTP abundant in cytoplasm: ~500 micromolar)
                        |
                        v
      [KRAS-GDP] --(SOS1: GEF)--> [KRAS-empty] --(GTP)--> [KRAS-GTP-Mg2+]
        OFF                          intermediate           ON
                                                              |
                                                              | binds RAF/PI3K
                                                              v
                                                       effector signaling
                                                              |
                                                              v
                                                       (NF1 or RASA1: GAP)
                                                              |
                                                              v
                                                  hydrolysis: GTP -> GDP + Pi
                                                              |
                                                              v
                                                          [KRAS-GDP]
                                                            OFF
```

### 2a. The hydrolysis chemistry

The reaction is **GTP + H2O -> GDP + inorganic phosphate (Pi)**. At the atomic level, a single water molecule, held in place by Q61, performs a nucleophilic attack on the gamma-phosphorus of GTP. This breaks the bond between the beta-gamma oxygen and the gamma-phosphorus, releasing inorganic phosphate.

The catalytic machinery has three critical pieces:
- **G60 backbone NH** stabilizes the transition state by hydrogen-bonding to the gamma-phosphate oxygen.
- **Q61 side chain** orients the attacking water.
- **T35-coordinated Mg2+** holds the phosphates in the right geometry.

Intrinsically, this reaction is slow (half-life of minutes to hours). GAPs accelerate it ~10⁵-fold by inserting an "arginine finger" (R789 in NF1, R789 in p120-GAP) into the active site, which stabilizes the developing negative charge on the gamma-phosphate during the transition state.

### 2b. The Mg2+ ion

A single magnesium ion sits in the active site coordinated by:
- Two oxygens from GTP (beta- and gamma-phosphate)
- The hydroxyl of S17 (P-loop)
- The hydroxyl of T35 (Switch I)
- Two water molecules

Without Mg2+, KRAS cannot bind GTP productively. The Mg2+ is essential for organizing the chemistry.

---

## 3. Hotspot mutations atom-by-atom

Roughly 98% of KRAS oncogenic mutations occur at just three residues: G12, G13, and Q61. The mutations share a common consequence — they slow or abolish GTP hydrolysis — but they achieve it through different atomic mechanisms.

### 3a. Why G12 is special

Glycine has no side chain (just a hydrogen). It sits at the bottom of the P-loop, immediately next to the gamma-phosphate of GTP and immediately next to where the GAP arginine finger needs to insert during catalysis. There is literally no room for any side chain larger than -H. Any substitution introduces a steric and/or electronic clash that:

1. **Blocks the GAP arginine finger** from entering productively (the GAP can't accelerate hydrolysis).
2. **Disrupts the geometry of the transition state** for intrinsic hydrolysis.
3. **Perturbs the position of Q61 and the catalytic water.**

The result: GTP cannot be efficiently hydrolyzed. KRAS gets stuck in the ON state, and the cell receives a constant "grow" signal.

### 3b. The major G12 mutations

| Mutation | Side chain added | Charge | Bulk | Why it matters | PDAC prevalence |
|----------|------------------|--------|------|----------------|----------------|
| **G12D** | -CH2-COO⁻ (carboxylate) | Negative | Medium | The carboxylate electrostatically clashes with the gamma-phosphate (both negative) and forms an extra H-bond network that disrupts Q61 positioning. The Asp side chain can also displace the catalytic water. | ~40% (the most common PDAC driver) |
| **G12V** | -CH(CH3)2 (isopropyl) | Neutral | Bulky aliphatic | Pure steric block of the GAP arginine finger. Most "rigid" of the G12 mutants — locks KRAS in ON state mechanically. | ~30% |
| **G12R** | -(CH2)3-NH-C(NH2)2⁺ (guanidinium) | Strongly positive | Long, charged | Reaches across the active site, can form a salt bridge with the gamma-phosphate. Distinctive in PDAC — much rarer in lung. Resistant to certain inhibitor scaffolds because the bulky basic side chain occupies the pocket entrance. | ~15% |
| **G12C** | -CH2-SH (thiol) | Neutral (but reactive) | Small | The cysteine thiol is a chemical handle. Drugs can be designed with electrophiles (acrylamides) that form a covalent bond to S of C12. This is what made sotorasib and adagrasib possible. Rare in PDAC (~1%), dominant in lung. | ~1–2% PDAC, ~13% lung |

### 3c. G13 and Q61 mutations

- **G13D** — Same chemistry as G12D but one residue downstream. The aspartate carboxylate still disrupts the catalytic geometry, but G13 sits slightly farther from the gamma-phosphate, so the effect is somewhat milder. G13D is enriched in colorectal cancer. Structurally, G13D mutants show less drastic Switch II distortion than G12D.
- **Q61H, Q61L, Q61R** — Q61 is the residue that positions the catalytic water. Any substitution destroys this water-positioning function and abolishes intrinsic hydrolysis directly (without needing to also block GAPs). Q61R is particularly interesting: the arginine side chain forms a new H-bond with the T35 backbone in Switch I, which actually **restricts access to the Switch II pocket** — so Q61R mutants are harder to drug with SII-P inhibitors. Q61 mutations are common in NRAS and HRAS-driven cancers (e.g., melanoma); rarer in PDAC.

### 3d. The consequence shared by all of these

Every hotspot mutation produces a KRAS that:
1. Hydrolyzes GTP much more slowly (intrinsic and GAP-mediated rates both drop 10- to 100-fold).
2. Spends the majority of its time in the GTP-bound (ON) state.
3. Maintains constitutive RAF -> MEK -> ERK signaling, plus PI3K -> AKT signaling.

But — crucially for drug design — each mutation also subtly reshapes the protein's local geometry and dynamics. The cysteine in G12C is a chemical handle. The aspartate in G12D creates a unique electrostatic pocket. The valine in G12V creates a hydrophobic protrusion. These differences are what allow allele-specific inhibitors.

---

## 4. The Switch-II pocket — the cryptic-pocket breakthrough

For decades, KRAS was considered "undruggable." Its surface looked smooth and featureless. The GTP-binding site was buried too deep and bound GTP too tightly (picomolar affinity) for any drug to displace it competitively. There were no obvious pockets to grip.

### 4a. Ostrem et al. 2013 — the fragment screen that changed everything

The breakthrough came from Kevan Shokat's lab at UCSF. They reasoned that KRAS G12C had a unique vulnerability: a cysteine thiol that could form a covalent bond with an appropriately designed electrophile. They synthesized a library of small "fragment" molecules (each tipped with an acrylamide or vinyl sulfone electrophile) and screened them against KRAS G12C-GDP for covalent labeling of C12.

The hits did something nobody expected: when they soaked in the fragments and got crystal structures, they revealed a **completely new pocket** in KRAS that did not exist in any prior crystal structure. The pocket sat just beneath Switch II, between the alpha2 helix (Switch II) and the central beta-sheet of the G-domain.

They named it the **Switch-II Pocket (SII-P)**. The defining residues that line it are:

- **H95, Y96** — at the top, in the alpha3 helix
- **D69, M72** — in the alpha2 helix (Switch II)
- **V9, G10, K16** — in the P-loop
- **R68, Y71** — on the back wall
- **T58, A59, G60** — in the loop entering Switch II
- **G12 (or C12 in G12C)** — at the bottom, where the covalent bond forms

### 4b. Why this pocket is "cryptic"

A **cryptic pocket** is a binding site that is not visible in the apo (unliganded) crystal structure but opens up upon ligand binding (or under specific dynamic conditions). The SII-P is cryptic because:

- In WT KRAS-GDP crystal structures, Switch II is positioned such that the pocket entrance is closed.
- In WT KRAS-GTP, Switch II is locked down on the nucleotide and the pocket is closed.
- In **G12C-GDP**, Switch II is more flexible and the pocket can sample an open state, particularly when a ligand is present to stabilize the open form.

This is why the pocket is mutant-selective in practice: mutant KRAS has subtly different Switch II dynamics that allow the pocket to open more often.

### 4c. Covalent vs non-covalent engagement

The first generation of SII-P drugs (sotorasib, adagrasib, divarasib) all rely on the **acrylamide warhead** strategy: a Michael acceptor (electrophilic vinyl carbonyl) that reacts irreversibly with the thiol of C12. The acrylamide is held in position by a "scaffold" that occupies the SII-P, and the warhead is positioned to attack C12.

For G12D, there is no cysteine. Instead, **MRTX1133** uses a bridged amine that forms a salt bridge with the aspartate-12 carboxylate. The amine is protonated (positively charged) at physiological pH and is held in position by the rest of the molecule occupying SII-P with picomolar affinity (KD ≈ 0.2 pM). This is the first non-covalent SII-P inhibitor with drug-like potency.

The **RMC tri-complex** strategy (RMC-6236, RMC-9805) is different: these drugs occupy the **SI/SII interface on GTP-bound (ON-state) KRAS** while simultaneously presenting a binding face for the intracellular chaperone cyclophilin A (CypA). The resulting CypA-drug-KRAS ternary complex sterically blocks effector binding without ever competing with GTP. RMC-9805 carries a small aziridine warhead that reacts covalently with the D12 carboxylate — the first covalent G12D drug.

---

## 5. Drug binding modes — table

The following table lists the drugs whose PDB structures are most directly useful to load and inspect. For docking validation, you will want to **re-dock the co-crystallized ligand** into its own structure and check that AutoDock Vina (or equivalent) recovers the experimental pose within ~2 Å RMSD. If it does, the box and scoring are working.

| Drug | Mutation | PDB ID | State | Key interactions | Mechanism | Status (2026) |
|------|----------|--------|-------|------------------|-----------|---------------|
| **Sotorasib (AMG-510)** | G12C | **6OIM** | GDP, OFF | Covalent C12-S to acrylamide; H-bond to H95, Y96; hydrophobic to V9, M72; pi-stack to Y96 | Covalent, OFF-state SII-P binder | FDA-approved (Lumakras, 2021) |
| **Adagrasib (MRTX849)** | G12C | **6UT0** | GDP, OFF | Covalent C12-S; H-bond to Y96 (key); pyrimidine occupies pocket; cyanomethyl group | Covalent, OFF-state SII-P binder | FDA-approved (Krazati, 2022) |
| **Divarasib (GDC-6036)** | G12C | **9PZY** (also 7T47) | GDP, OFF | Covalent C12-S; H-bond to protonated H95 N3; tighter pocket fit than sotorasib | Covalent, OFF-state SII-P binder | FDA-approved (Roche, 2024) |
| **MRTX1133** | G12D | **7RPZ** | GDP, OFF | Bridged amine salt bridge to D12 carboxylate; water-mediated H-bond to G10 and T58; ethynyl-CH H-bond to bridging water; deep SII-P fit | Non-covalent, OFF-state SII-P binder, KD 0.2 pM | Phase 2 (Mirati / BMS) |
| **RMC-6236 (daraxonrasib)** | pan-RAS ON | **9BG6** (G12V), **9BGC** (G12R), **9BG5** (G13D), **9BGB** (Q61H), **9BG0** (NRAS WT) | GTP, ON | Tri-complex: drug bridges SI/SII of RAS to CypA face; macrocyclic; H-bonds, hydrophobic, pi-pi | Non-covalent tri-complex, ON-state pan-RAS | Phase 3 (Revolution Medicines) |
| **RMC-9805 (zoldonrasib)** | G12D | **9CTB** | GTP, ON | Tri-complex with CypA; aziridine warhead covalent to D12 carboxylate; SI/SII interface | Covalent tri-complex, ON-state G12D-selective | Phase 1/2 (Revolution Medicines) |
| **BI-2865** | pan-KRAS (G12C, G12D, G12V, G13D, WT — selective vs HRAS/NRAS) | **8AZV** | GDP, OFF | Occupies a pocket adjacent to SII-P; KRAS-isoform-selective via H95 contact (HRAS/NRAS have Q95) | Non-covalent, OFF-state pan-KRAS, reversible | Tool compound (Boehringer Ingelheim) |

A few things worth noting from this table:

- The first three drugs all target **the same pocket (SII-P) in the same state (GDP-OFF)** on the same residue (C12), but their scaffolds differ enough to produce different resistance profiles in patients.
- Y96 is the most common point of acquired resistance — a Y96D mutation breaks the H-bond that adagrasib and sotorasib rely on.
- MRTX1133's picomolar affinity comes from filling SII-P more completely than the G12C drugs do, plus the salt bridge to D12.
- The RMC tri-complex drugs work at the **opposite face** of the protein (ON state, effector interface) and represent a completely different drug-design philosophy.
- BI-2865 demonstrates that **pan-KRAS** activity is possible — it exploits the difference between H95 (KRAS) and Q95 (HRAS/NRAS) to selectively engage KRAS regardless of mutation.

### 5a. SMILES strings for reference compounds

You can paste these directly into RDKit or OpenBabel to generate 3D coordinates for docking.

| Compound | SMILES (approximate; verify against PubChem before publication) |
|----------|-------|
| MRTX1133 | `CN1CCN(CC1)C[C@@H]2COCCN2c3nc(N4CC5CC4CN5C(=O)C=C)c6c(n3)c(F)c(c(c6F)C#C)O` (verify on PubChem CID 156588992) |
| Sotorasib | `CC1=CC(=C(C=C1)F)N2C(=O)N(C(C(=N2)N3CCN(CC3)C(=O)C=C)C)C4=C(C=CC=C4F)O` (verify on PubChem CID 137278711) |
| Adagrasib | Verify on PubChem CID 138611145 |
| Divarasib | Verify on PubChem CID 156419821 |

For the actual pipeline, the **safest path is to extract the ligand directly from the PDB file** (with PyMOL: `save ligand.mol2, resn LIG`), then optimize with `obabel ligand.mol2 -O ligand.pdbqt --gen3d`. Skip the SMILES round-trip when possible.

---

## 6. Other pockets — including ones not yet exploited

The SII-P is not the only pocket on KRAS. Several others have been characterized, and a few have produced clinical or preclinical compounds.

### 6a. The Switch-I/II (SI/SII) interface

This is the face of KRAS where effectors (RAF, PI3K) actually bind. In WT GTP-bound KRAS, this surface is well-defined and competent for effector engagement. The RMC tri-complex drugs (RMC-6236, RMC-9805) target this interface by recruiting CypA as a chaperone — the drug alone cannot bind tightly, but together with CypA it forms a stable shield.

For "monomeric" (non-tri-complex) drug design, this surface is considered very difficult to drug directly because:
- Effector binding is large, flat, and protein-protein in nature.
- The protein-protein interaction has high intrinsic affinity (nanomolar) and competing with it is hard.

### 6b. The A59 / back-of-Switch-II pocket

A shallow groove behind Switch II, near residue A59, has been identified by fragment-screening but has not produced a clinical compound. It is in the same general region as SII-P but on the opposite face of Switch II. Some pan-KRAS scaffolds make contact here.

### 6c. The KRB-456 pocket (SI/SII allosteric, G12D-selective)

KRB-456, reported in 2023, is a G12D-selective binder that occupies an allosteric pocket spanning Switch I and Switch II, distinct from SII-P. It is in early discovery but illustrates that even more allosteric pockets exist on KRAS.

### 6d. Cryptic pockets identified by long MD

Computational studies (notably from the Bowman group's PocketMiner, the Shukla group's enhanced-sampling work, and several mixed-solvent MD studies) have identified additional transient pockets on KRAS that are not visible in any single crystal structure but appear briefly during the protein's conformational dance:

- A pocket adjacent to G60 that opens during Switch II "unfolding" events
- A pocket on the alpha3 helix face
- An interfacial pocket near the predicted dimer interface (KRAS may homodimerize on the membrane; this is contested)
- A pocket between the C-terminal helix alpha5 and the central beta-sheet

These are hypotheses awaiting experimental validation but represent the frontier of cryptic-pocket discovery.

### 6e. The KRAS dimer interface

There is ongoing debate about whether KRAS forms functional homodimers on the membrane. NMR, crosslinking, and some cryo-EM data suggest a transient dimer interface mediated by the alpha4 and alpha5 helices. If real, this interface is potentially druggable. Inhibitors that disrupt the dimer interface (without engaging the active site) are being explored.

### 6f. Standard computational pocket-detection tools

For your own pipeline, you can run these against any KRAS structure to confirm SII-P and look for others:

- **fpocket** — geometric pocket detection, fast, easy to script
- **P2Rank** — machine-learning pocket prediction with druggability score
- **FTMap** — fragment-based hotspot mapping (web server or local)
- **DoGSiteScorer** — pocket detection with druggability score
- **SiteMap** (Schrödinger, commercial) — gold-standard but paid

Run two or three of these on the apo KRAS structure (PDB 4OBE) and on a SII-P-occupied structure (PDB 7RPZ) and compare — the SII-P will appear only in the latter.

---

## 7. KRAS dynamics — why MD matters

A static crystal structure is a snapshot. The real protein is a moving, breathing object that samples a distribution of conformations. For KRAS in particular, the **dynamic** behavior is what makes cryptic-pocket discovery possible and what differentiates WT from mutant.

### 7a. WT vs G12D dynamic differences

NMR relaxation experiments and long molecular dynamics simulations agree:

- WT KRAS-GDP and G12D-GDP have **similar average structures** (overlay closely).
- But G12D shows **increased flexibility** at Switch II, the alpha3 helix, and the loop connecting them.
- The increased flexibility means the SII-P opens transiently in G12D more often than in WT.
- The aspartate side chain itself shows high mobility, which translates into entropy gain — partially compensating for the energetic cost of mutation.

This is why MRTX1133 (and the G12D-specific RMC compounds) can be designed as G12D-selective: the mutant samples the open SII-P conformation often enough for ligand binding to be productive, while the WT essentially does not.

### 7b. Excited states and slow motion

Recent paramagnetic NMR work has identified a low-population "excited state" of active GTP-bound KRAS in which Switch II flips into an alternative conformation. This excited state has different effector-binding properties and is populated more in G12D than in WT. It is a candidate target for new allosteric drugs.

### 7c. Encounter complex with effectors

When KRAS-GTP meets RAF, the initial contact is dynamic (an "encounter complex") before it locks into the final tight complex. Drugs that perturb the encounter complex without abolishing the final complex could have unique pharmacology.

### 7d. Membrane-bound vs solution conformations

KRAS in solution (what NMR sees) is different from KRAS on the membrane (what the cell sees). On the membrane:
- The G-domain can orient in at least two distinct ways relative to the lipid surface.
- One orientation occludes the effector-binding face (auto-inhibited).
- The other exposes it (active).

This orientation equilibrium is shifted by mutations, by membrane lipid composition, and by drugs.

### 7e. Cryptic pocket opening on the µs–ms timescale

Pocket opening events for SII-P happen on the microsecond-to-millisecond timescale — far too slow for standard nanosecond MD. To capture them you need:

- **Long MD** (multi-microsecond, typically aggregated via parallel runs and stitched with Markov state models)
- **Mixed-solvent MD** (cosolvents like xenon, isopropanol, or benzene probe transient pockets)
- **Metadynamics or steered MD** to bias the system toward pocket opening
- **Enhanced sampling along normal modes** (a recent and effective approach for KRAS)

For a Mac-based pipeline, running multi-microsecond MD locally is unrealistic. The practical alternative: use an **ensemble of published crystal structures** as a proxy for the conformational ensemble. Re-dock against each member and look for compounds that score well across the ensemble (this is "ensemble docking").

---

## 8. Docking science primer — what a score means

You will run AutoDock Vina (or GNINA, AutoDock-GPU, smina, etc.) and get a number back. Here is what that number means and does not mean.

### 8a. What Vina computes

AutoDock Vina's score is an **empirical estimate of binding free energy in kcal/mol**. More negative = more favorable. The scoring function is a weighted sum of:
- Gauss attractive terms (close hydrophobic contacts)
- Repulsive terms (steric clash)
- Hydrogen-bond terms
- Hydrophobic terms
- Torsional entropy penalty (penalizes flexible ligands)

The function was trained on a set of ~1000 known protein-ligand complexes. It is fast (seconds per ligand) and reasonably accurate at **identifying near-native poses** for ligands that are similar to its training set.

### 8b. How to interpret a Vina score

Rough thumb rules, for a small drug-like ligand binding to a normal-sized pocket:

| Score (kcal/mol) | Interpretation |
|------------------|----------------|
| > -5 | Essentially noise; the ligand isn't really binding |
| -5 to -7 | Marginal; weak interaction, possibly a false positive |
| -7 to -9 | Promising; this is where most active drugs fall |
| -9 to -11 | Strong; comparable to typical clinical candidates |
| < -11 | Very strong; either a real lead, an artifact (clashing or unphysical pose), or a very large/flexible ligand |

Important caveats:
- **A score below -11 is suspicious** in a docking-only context. Check the pose carefully. The most common reason for a very low score is the ligand wrapped into an unphysical conformation that exploits the scoring function's gauss term.
- **MRTX1133 with KD = 0.2 pM should "score" near -18 kcal/mol** by basic free-energy arithmetic (ΔG = -RT ln Kd ≈ -17.5 kcal/mol at 310 K for KD = 0.2 pM). Vina will not return that; expect -13 to -15 for the experimental pose. Vina systematically compresses the dynamic range — extreme high-affinity binders score "only" moderately well.
- **Relative ranks matter more than absolute numbers.** If you dock a library and compound A scores -9.2 while compound B scores -8.8, that does not mean A binds better. Differences within ~1 kcal/mol are inside the noise of the scoring function.

### 8c. Pose vs score

A **good pose with a mediocre score** is more reliable than a **bad pose with a great score**. A "good pose" means:
- The ligand sits inside the intended pocket (not floating).
- Key chemical features make plausible contacts (acrylamide near C12, basic amine near D12, etc.).
- No serious clashes with protein atoms.
- Hydrogen-bond donors and acceptors are properly oriented.

Always visualize. A 30-second look in PyMOL will catch problems no score can flag.

### 8d. Positive-control rediscovery

The standard validation step before any virtual screen:

1. Take your prepared protein (e.g., KRAS G12D from 7RPZ).
2. Extract the co-crystallized ligand (MRTX1133).
3. Re-dock that ligand into the same protein structure.
4. Check that Vina returns a top-ranked pose within 2 Å RMSD of the crystal pose.

If this succeeds, your box, your scoring, and your ligand preparation are working. If it fails, fix it before running anything else.

A more rigorous version: dock a small panel of known binders (sotorasib, adagrasib, MRTX1133) and decoys (random drug-like molecules) and confirm the binders rank higher than the decoys. This is the **enrichment** test.

### 8e. Lipinski's rule of 5 and PDAC-specific considerations

Lipinski's "rule of 5" for oral drug-likeness:
- Molecular weight ≤ 500 Da
- LogP ≤ 5 (lipophilicity)
- Hydrogen-bond donors ≤ 5
- Hydrogen-bond acceptors ≤ 10

Many KRAS inhibitors are at or beyond these limits (MRTX1133 has MW ~600 Da; macrocyclic tri-complex drugs like RMC-6236 are well above), reflecting how hard the target is.

For PDAC specifically: pancreatic tumors are surrounded by a dense stromal barrier that limits drug penetration. Drugs need:
- Reasonable plasma stability and half-life
- Ability to penetrate the desmoplastic stroma (paradoxically, sometimes higher lipophilicity helps here)
- Tolerance of low-perfusion, hypoxic, acidic tumor microenvironment

This is why simply hitting KRAS in a cell-free assay is not enough. But for the docking pipeline, these are downstream considerations; the immediate goal is pose and engagement.

### 8f. The "magic methyl" problem

A single methyl group added in the right place can swing potency 100×. Conversely, the wrong methyl can kill activity entirely. This is why hit-to-lead optimization is a wet-lab process and why even the best docking score is a starting hypothesis, not a finished drug.

---

## 9. Recent (2023–2026) structural breakthroughs

### 9a. The tri-complex revolution

Revolution Medicines has demonstrated that the **ON-state** of mutant RAS, long considered undruggable because GTP binds with picomolar affinity, can be drugged via the tri-complex strategy. RMC-6236 (daraxonrasib) is a pan-RAS-ON inhibitor in Phase 3 for KRAS-mutant solid tumors including PDAC. RMC-9805 (zoldonrasib) is G12D-ON-selective and uses an aziridine warhead — the first covalent G12D drug. Crystal structures (PDB 9BG0/9BG5/9BG6/9BGB/9BGC and 9CTB) show the drug bridging the RAS effector face to CypA.

### 9b. MRTX1133 and the non-covalent SII-P

MRTX1133 (Mirati / BMS) is the first non-covalent G12D SII-P inhibitor with drug-like potency (KD ≈ 0.2 pM). PDB 7RPZ shows it bound to KRAS G12D-GDP, with a bridged amine engaging the D12 carboxylate. It is in Phase 2 trials, with focus on PDAC. Its discovery rewrote the playbook for what is achievable with rational structure-based design.

### 9c. Pan-KRAS inhibitors

BI-2865 (Boehringer Ingelheim, PDB 8AZV, 2023) demonstrated that **pan-KRAS** activity is achievable — inhibiting all major KRAS mutants while sparing HRAS and NRAS. This is a major shift because it suggests a single drug might be able to address heterogeneous tumors with multiple KRAS subclones.

### 9d. Cryo-EM of KRAS-effector complexes

2023–2025 has seen multiple cryo-EM structures of full KRAS-RAF1-MEK1-14-3-3 assemblies (~4 Å resolution), showing how KRAS recruits RAF in the context of its autoinhibited regulatory complex. These structures are too low-resolution for ligand docking but are gold for understanding the systems biology of RAS signaling.

### 9e. AlphaFold3, Boltz-2, and the structure-prediction revolution

By mid-2026:
- **AlphaFold3** can predict protein-ligand complexes with reasonable accuracy and has been shown to recover known KRAS-drug binding modes for trained scaffolds. It is less reliable for novel chemotypes and for cryptic pockets it has not "seen."
- **Boltz-2** approaches free-energy-perturbation accuracy for binding affinity prediction at 1000× lower compute, achieving Pearson correlation of ~0.62 with experimental affinities — a major advance for triaging virtual screens.
- For practical use against KRAS: AlphaFold3 and Boltz-2 are best used as **rescoring tools** for Vina hits, not as primary screens. They complement docking; they do not replace it.

### 9f. Cryptic pockets via MD + cosolvents + MSMs

The Bowman group (PocketMiner), the Shukla group (enhanced-sampling MD), and others have characterized previously unknown transient pockets on KRAS through long MD simulations combined with mixed-solvent probes. Several of these pockets are now being targeted by industry programs.

---

## 10. Things to load and look at — PyMOL / ChimeraX commands

Open PyMOL (`brew install --cask pymol` on Mac if you haven't already), then run the following.

### 10a. The canonical comparison: WT vs G12D, OFF state

```pymol
# Fetch wild-type KRAS in GDP form (OFF)
fetch 4OBE, async=0
# Fetch G12D in GDP form bound to MRTX1133 (OFF, drug-bound)
fetch 7RPZ, async=0

# Align them
align 7RPZ and polymer, 4OBE and polymer

# Color schemes
hide everything
show cartoon
color gray80, 4OBE
color salmon, 7RPZ

# Highlight the residue 12 environment
select res12_wt, 4OBE and resi 12
select res12_mut, 7RPZ and resi 12
show sticks, res12_wt or res12_mut
color yellow, res12_wt
color red, res12_mut

# Show GDP and Mg2+
show sticks, resn GDP
show spheres, resn MG
color orange, resn GDP
color magenta, resn MG

# Show MRTX1133
select mrtx, 7RPZ and resn 6KW
show sticks, mrtx
color cyan, mrtx

# Show Switch I and Switch II
color blue, 4OBE and resi 30-40 or 7RPZ and resi 30-40
color green, 4OBE and resi 60-76 or 7RPZ and resi 60-76

# View
zoom mrtx, 6
```

What you should see: the G12D aspartate side chain pointing into the SII-P, the MRTX1133 bridged amine sitting right next to it, GDP and Mg2+ in the canonical nucleotide pocket, Switch I (blue) and Switch II (green) flanking the binding site, and a clear "pocket" where MRTX1133 has displaced or reshaped the Switch II loop.

### 10b. The G12C drug family — three drugs in one view

```pymol
fetch 6OIM, async=0   # KRAS G12C + sotorasib
fetch 6UT0, async=0   # KRAS G12C + adagrasib
fetch 9PZY, async=0   # KRAS G12C + divarasib

align 6UT0, 6OIM
align 9PZY, 6OIM

hide everything
show cartoon, 6OIM
color gray80, 6OIM

# Show all three drugs at the same site
show sticks, 6OIM and not polymer and not resn GDP and not resn MG
show sticks, 6UT0 and not polymer and not resn GDP and not resn MG
show sticks, 9PZY and not polymer and not resn GDP and not resn MG

color cyan, 6OIM and not polymer and not resn GDP and not resn MG
color magenta, 6UT0 and not polymer and not resn GDP and not resn MG
color yellow, 9PZY and not polymer and not resn GDP and not resn MG

# Highlight C12 and the key contacting residues
select sii_p_residues, 6OIM and resi 12+95+96+71+72+58+59+60+68
show sticks, sii_p_residues
color orange, sii_p_residues

zoom sii_p_residues, 4
```

You will see three drugs overlaid in the same SII-P, each with their distinct scaffolds, all anchored via covalent bond to C12, all making H-bonds to Y96 or H95. The conservation of binding mode despite chemical diversity is striking.

### 10c. The tri-complex

```pymol
fetch 9BG6, async=0   # daraxonrasib + KRAS G12V + CypA

hide everything
show cartoon
color skyblue, chain A
color salmon, chain B
# (one chain will be KRAS, the other CypA — inspect to identify)
show sticks, organic
color yellow, organic
zoom organic, 6
```

You will see the macrocyclic drug bridging two proteins. The unique geometry — KRAS on one side, CypA on the other, drug in between — is what makes this a different class of inhibitor.

### 10d. Residues to memorize

When you're docking and inspecting poses, these are the residues to look for and check contacts to:

- **G12 / G12D / G12C** — the target. Any G12-selective drug must engage this residue's side chain (covalently for G12C, electrostatically for G12D).
- **H95, Y96** — the SII-P H-bond donors. Most SII-P drugs make a key H-bond to one of these (especially Y96 for adagrasib and sotorasib; H95 N3 for divarasib).
- **D69, M72, R68, Y71** — the alpha2 helix face of the pocket; these form the back wall.
- **T58, A59, G60** — the floor of the pocket.
- **V9, G10, K16** — the P-loop entrance.
- **Q61** — catalytic glutamine; key for hydrolysis; useful sanity check.
- **T35** — Switch I anchor; coordinates Mg2+.

---

## 11. What this means for our docking pipeline

Concrete implications, ordered by importance:

### 11a. Choose the right protein structure

For G12D-targeting compounds, **start with PDB 7RPZ** (KRAS G12D + MRTX1133 + GDP). It is:
- The right mutation (G12D)
- The right state (GDP-OFF)
- Has the SII-P **open** (because MRTX1133 is bound, stabilizing the open form)
- Recent and good resolution

Pull the protein-only file (delete the MRTX1133 ligand and waters; keep GDP and Mg2+). This becomes your "receptor."

If you want to be more thorough, run an **ensemble docking** with PDB 7RPZ plus a couple of other G12D structures so that compounds are scored against multiple snapshots of Switch II. But for a first-pass pipeline, 7RPZ alone is fine.

For G12C: use **6OIM** (sotorasib-bound) or **6UT0** (adagrasib-bound). Pick the one whose pocket geometry best matches the chemotype you are designing.

For pan-RAS-ON exploration: use **9BG6** (tri-complex), but be aware that the tri-complex pocket is very different and requires CypA in the system.

### 11b. Define the docking box around SII-P

Center the docking box on the **bound ligand's center of mass** in your reference structure. For 7RPZ with MRTX1133:
- Center coordinates: approximately the center of mass of the bound MRTX1133. Extract with `centerofmass mrtx` in PyMOL.
- Box size: 22 × 22 × 22 Å is generous and safe. Smaller (16 × 16 × 16) is more restrictive but biased toward the known pose. Larger boxes find more "false binding" elsewhere; smaller boxes can miss valid alternate poses.

For G12D compounds, the box must extend from the depth of the pocket (near G10, T58) up to the H95/Y96 plane and out to the alpha2 helix face. Anchor mentally: imagine a 20 Å cube centered roughly above the gamma-phosphate of GDP, slightly toward Switch II.

### 11c. Always run positive-control rediscovery

Before scoring any new compound, re-dock MRTX1133 (extracted from 7RPZ) back into the prepared receptor. The top pose should be within ~2 Å RMSD of the crystal pose, and the score should be ~-12 to -14 kcal/mol. If it isn't, your preparation is broken — fix it before going further.

### 11d. Validate with a panel, not a single compound

Build a small benchmark set:
- **Active binders** — MRTX1133, BI-2865, plus 5–10 published G12D ligands
- **Decoys** — 50–100 random drug-like molecules (e.g., from DUD-E or generated with random scaffolds)
- Dock all of them; verify that active binders rank above decoys

If your enrichment factor is <2× at top 5%, do not trust the pipeline for novel compounds.

### 11e. Focus on the right contacts

When scoring new compounds, look for poses that:
- Have a polar/positive group near D12 (electrostatic complementarity)
- Have an H-bond donor near Y96 N or O (the canonical anchor)
- Fill the back of the pocket (D69, M72, R68 region) with hydrophobic mass
- Do not clash with G10 or T58 at the floor

### 11f. Don't trust the score alone

Re-rank top hits with at least one of:
- **GNINA** (deep-learning rescoring, runs on CPU on Mac)
- **Boltz-2** (transformer-based affinity prediction, requires GPU but accessible via cloud)
- A simple **MM-GBSA** rescoring via OpenMM, if you have the patience

These rescoring layers usually beat raw Vina by a meaningful margin at picking the actual top binder from your top 20 candidates.

### 11g. State and conformation

Stay in the OFF state (GDP-bound) for SII-P drug design. Do not try to dock SII-P drugs against GTP-bound KRAS — the pocket isn't there, and you will get garbage scores.

For pan-RAS-ON or tri-complex work, you would need a GTP-bound starting structure and a co-receptor (CypA) — much harder. Skip this in v1 of the pipeline.

### 11h. The HVR (residues 167–189) doesn't matter for SII-P docking

Most KRAS structures used for SII-P docking only include residues 1–169 (a truncated G-domain). This is fine — the SII-P is far from the C-terminus, and the floppy HVR contributes nothing to the binding site. Use the truncated structure.

---

## 12. Sources

### KRAS structural biology fundamentals
- [The current understanding of KRAS protein structure and dynamics (CSBJ 2019)](https://www.csbj.org/article/S2001-0370(19)30464-7/fulltext)
- [The Structural Basis of Oncogenic Mutations G12, G13 and Q61 in K-Ras4B (Sci Reports 2016)](https://www.nature.com/articles/srep21949)
- [Comparative effects of oncogenic mutations G12C, G12V, G13D, and Q61H (CSBJ 2020)](https://www.csbj.org/article/S2001-0370(19)30356-3/fulltext)
- [Oncogenic G12D mutation alters local conformations and dynamics of K-Ras (Sci Reports 2019)](https://www.nature.com/articles/s41598-019-48029-z)
- [Dynamic Coupling and Entropy Changes in KRAS G12D Mutation (JMB 2025)](https://www.sciencedirect.com/science/article/abs/pii/S002228362500141X)
- [Comparative analysis of KRAS4a and KRAS4b splice variants (Sci Advances)](https://www.science.org/doi/10.1126/sciadv.adj4137)
- [Uncovering a membrane-distal conformation of KRAS (PNAS 2020)](https://www.pnas.org/doi/10.1073/pnas.2006504117)
- [Membrane interactions of the globular domain and HVR of KRAS4b (eLife)](https://elifesciences.org/articles/47654)
- [Excited-state observation of active K-Ras reveals differential dynamics (NSMB 2023)](https://www.nature.com/articles/s41594-023-01070-z)

### KRAS effectors and regulators
- [Structural insights into isoform-specific RAS-PI3Kα interactions (Nat Comms 2024)](https://www.nature.com/articles/s41467-024-55766-x)
- [KRAS interaction with RAF1 RBD and CRD (Nat Comms 2021)](https://www.nature.com/articles/s41467-021-21422-x)
- [Functional and Structural Insights into RAS Effector Proteins (PMC 2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11316660/)
- [Atomic-scale mechanisms of GDP extraction by SOS1 (bioRxiv 2024)](https://www.biorxiv.org/content/10.1101/2024.06.17.599303v1.full)
- [Cryo-EM structure of a RAS/RAF recruitment complex (Nat Comms 2023)](https://www.nature.com/articles/s41467-023-40299-6)
- [Cryo-EM structures of CRAF/MEK1/14-3-3 complexes (Nat Comms 2025)](https://ideas.repec.org/a/nat/natcom/v16y2025i1d10.1038_s41467-025-63227-2.html)

### Switch-II pocket and inhibitors
- [Ostrem et al. 2013, K-Ras(G12C) inhibitors that bind switch II (Nature)](https://www.nature.com/articles/nature12796)
- [KRAS is vulnerable to reversible switch-II pocket engagement (Nature Chem Biol 2022)](https://www.nature.com/articles/s41589-022-00985-w)
- [Biophysical and structural analysis of KRAS switch-II pocket inhibitors (PMC 2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12270674/)
- [Exploring switch II pocket conformation of KRAS(G12D) with monobodies (PNAS 2023)](https://www.pnas.org/doi/10.1073/pnas.2302485120)
- [Switch II Pocket Inhibitor Allosterically Freezes KRAS G12D (JMB 2025)](https://www.sciencedirect.com/science/article/abs/pii/S0022283625002281)
- [Discovery of KRB-456, a KRAS G12D Switch-I/II Allosteric Pocket Binder (Cancer Res Comms 2023)](https://aacrjournals.org/cancerrescommun/article/3/12/2623/732091/Discovery-of-KRB-456-a-KRAS-G12D-Switch-I-II)
- [Structural perspectives on direct drugging of RAS (Front Oncol 2024)](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2024.1394702/full)

### Specific drugs and crystal structures
- [Sotorasib AMG-510 discovery (JMC 2020)](https://pubs.acs.org/doi/10.1021/acs.jmedchem.9b01180)
- [RCSB PDB 6OIM — KRAS G12C + AMG-510](https://www.rcsb.org/structure/6OIM)
- [RCSB PDB 6UT0 — KRAS G12C + adagrasib](https://www.rcsb.org/structure/6UT0)
- [RCSB PDB 9PZY — KRAS G12C + divarasib](https://www.rcsb.org/structure/9PZY)
- [The structure of KRAS G12C bound to divarasib (Small GTPases 2025)](https://www.tandfonline.com/doi/full/10.1080/21541248.2025.2505441)
- [Discovery and characterization of divarasib GDC-6036 (JMC 2025)](https://pubs.acs.org/doi/10.1021/acs.jmedchem.5c02272)
- [MRTX1133 identification (JMC 2022)](https://pubs.acs.org/doi/10.1021/acs.jmedchem.1c01688)
- [RCSB PDB 7RPZ — KRAS G12D + MRTX1133](https://www.rcsb.org/structure/7RPZ)
- [Characterization of MRTX1133 binding (PMC 2022)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9588042/)
- [Pan-KRAS inhibitor BI-2865 (Nature 2023)](https://www.nature.com/articles/s41586-023-06123-3)
- [RCSB PDB 8AZV — KRAS + BI-2865](https://www.rcsb.org/structure/8AZV)
- [Discovery of daraxonrasib RMC-6236 (JMC 2024)](https://pubs.acs.org/doi/10.1021/acs.jmedchem.4c02314)
- [RAS(ON) Therapies — Daraxonrasib Phase III (JMC 2025)](https://pubs.acs.org/doi/10.1021/acs.jmedchem.5c01441)
- [RCSB PDB 9BG6 — daraxonrasib + KRAS G12V + CypA](https://www.rcsb.org/structure/9BG6)
- [RCSB PDB 9CTB — zoldonrasib + KRAS G12D + CypA](https://www.rcsb.org/structure/9CTB)
- [RMC-9805 discovery (Cancer Res 2024)](https://aacrjournals.org/cancerres/article/84/7_Supplement/ND03/742762/Abstract-ND03-Discovery-of-RMC-9805-an-oral)

### Reference KRAS structures
- [RCSB PDB 4OBE — KRAS WT + GDP](https://www.rcsb.org/structure/4OBE)
- [RCSB PDB 6MBU — KRAS WT (1–169) + GDP + Mg](https://www.rcsb.org/structure/6MBU)
- [RCSB PDB 6OB2 — KRAS WT + GMPPNP + NF1-GRD](https://www.rcsb.org/structure/6OB2)

### Cryptic pockets, MD, and computational
- [Exploration of Cryptic Pockets via Enhanced Sampling: KRAS G12D (JCIM 2024)](https://pubs.acs.org/doi/10.1021/acs.jcim.4c01435)
- [Pathways and mechanism of MRTX1133 binding via MD + MSM (Int J Biol Macromol 2024)](https://www.sciencedirect.com/science/article/abs/pii/S0141813024041795)
- [Inhibition mechanism of MRTX1133: MD + MSM (J Comp Aided Mol Des 2024)](https://link.springer.com/article/10.1007/s10822-023-00498-1)
- [Decrypting cryptic pockets with physics-based simulations and AI (PMC 2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12959236/)
- [Recent computational advances in cryptic binding site identification (Bioinformatics Advances 2025)](https://academic.oup.com/bioinformaticsadvances/article/5/1/vbaf156/8180504)
- [Binding modes of GDC-6036 and LY3537982 by all-atom MD (Sci Reports 2025)](https://www.nature.com/articles/s41598-025-07532-2)

### Docking, scoring, and AI structure prediction
- [AutoDock Vina 1.2.0 documentation](https://autodock-vina.readthedocs.io/_/downloads/en/latest/pdf/)
- [Optimizing protein-ligand docking through ML: Vina selection (Discover Chem 2025)](https://link.springer.com/article/10.1007/s44371-025-00246-4)
- [GNINA and AutoDock Vina benchmark for virtual screening (PMC 2024)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12388557/)
- [Vinardo scoring function (PMC 2016)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4865195/)
- [Accelerating AutoDock Vina with GPUs (PMC 2022)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9103882/)
- [AlphaFold 3 applications and performance (PMC 2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12027460/)
- [Discovery of Covalent Ligands with AlphaFold3 (JACS 2025)](https://pubs.acs.org/doi/10.1021/jacs.5c22222)
- [Boltz-2: Towards Accurate Binding Affinity Prediction (PMC 2025)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12262699/)
- [Evaluating Boltz-2 on Real Drug Targets (deepmirror 2025)](https://www.deepmirror.ai/post/boltz-2-real-drug-targets)
- [Protein Engineering with AI: OpenFold3 vs Boltz 2 vs AlphaFold 3 (Blackthorn 2025)](https://blackthorn.ai/blog/protein-engineering-with-ai/)

### Pancreatic cancer drug delivery
- [Modelling and breaking down the biophysical barriers to drug delivery in pancreatic cancer (Lab on Chip 2024)](https://pubs.rsc.org/en/content/articlehtml/2024/lc/d3lc00660c)
- [Stroma-Targeting Therapy in Pancreatic Cancer (Front Oncol 2020)](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2020.576399/full)
- [Pancreatic cancer stroma: an update on therapeutic targeting (PMC 2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8284850/)

### Compound databases (for SMILES lookup)
- [MRTX1133 — PubChem CID 156588992](https://pubchem.ncbi.nlm.nih.gov/compound/156588992)
- [Sotorasib — PubChem CID 137278711](https://pubchem.ncbi.nlm.nih.gov/compound/137278711)
- [Adagrasib — PubChem CID 138611145](https://pubchem.ncbi.nlm.nih.gov/compound/138611145)
- [Divarasib — PubChem CID 156419821](https://pubchem.ncbi.nlm.nih.gov/compound/156419821)
