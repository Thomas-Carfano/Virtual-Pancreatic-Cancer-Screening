# PARP1 (Poly [ADP-ribose] polymerase 1) enrichment set — provenance & limitations

Built 2026-05-26T20:13:37.968964 by build_enrichment_set.py

## Actives (40)
- Source: ChEMBL target CHEMBL3105 (PARP1 (Poly [ADP-ribose] polymerase 1)), pChEMBL >= 6.0 (<= ~1 uM).
- Filtered to drug-like small molecules: MW 250-650, rotatable bonds <= 15, amide groups <= 4
  (removes peptides / PPI-disruptor macrocycles).

## Decoys (586)
- Source: drug-like ChEMBL molecules (MW bracketing the actives), excluding any known active.
- DUD-E-style property matching per active (tolerances: MW +/-35.0, logP +/-1.5,
  HBD +/-1, HBA +/-3, rotatable +/-3).
- Topological dissimilarity enforced: ECFP4 Tanimoto < 0.35 to EVERY active.
- Target 15 decoys/active.

## Honest limitations
- This is an ENGINE SANITY CHECK, not a publication-grade selectivity benchmark.
- Decoys are PRESUMED inactive (not experimentally confirmed non-binders).
- Property matching reduces, but does not eliminate, trivial-feature enrichment bias.
