# KRAS enrichment set — provenance & limitations

Built 2026-05-26T16:03:40.182534 by build_enrichment_set.py

## Actives (40)
- Source: ChEMBL target CHEMBL2189121 (GTPase KRas), pChEMBL >= 6.0 (<= 1 uM).
- Filtered to drug-like small molecules: MW 250-650, rotatable bonds <= 15, amide groups <= 4
  (removes peptides / PPI-disruptor macrocycles).
- 422 of the drug-like actives come from an assay whose description mentions "G12D".

## Decoys (600)
- Source: drug-like ChEMBL molecules (MW 250-650), excluding any KRAS active.
- DUD-E-style property matching to each active (tolerances: MW +/-35.0, logP +/-1.5,
  HBD +/-1, HBA +/-3, rotatable +/-3).
- Topological dissimilarity enforced: ECFP4 Tanimoto < 0.35 to EVERY active.
- Target 15 decoys/active.

## Honest limitations
- This is an ENGINE SANITY CHECK, not a publication-grade G12D-selectivity benchmark.
- Many KRAS actives in ChEMBL are G12C covalent chemotypes docked here non-covalently into
  the G12D (7RPZ) pocket; pocket occupancy is similar but this is not a covalent treatment.
- Decoys are PRESUMED inactive (not experimentally confirmed non-binders).
- Property matching reduces, but does not eliminate, trivial-feature enrichment bias.
