# Structural Analysis of NDM-1 Variants

## Project Overview

This project investigates sequence and structural differences among selected New Delhi metallo-beta-lactamase (NDM) variants, with a focus on NDM-1 and the substitutions observed in NDM-4, NDM-5, and NDM-7.

The analysis combines protein sequence comparison with measurements from an experimental NDM-1 structure (PDB 3ZR9). The goal is to examine whether variant-associated residues are positioned near the observed zinc site and to describe plausible local structural or physicochemical consequences of the substitutions without overstating their functional effects.

## Biological Question

How do selected amino-acid substitutions in NDM variants differ in their sequence properties and structural proximity to the observed zinc site of NDM-1?

## Variants Analyzed

- **NDM-1:** C7C422 — reference sequence
- **NDM-4:** A0A0G2ST15 — M154L
- **NDM-5:** U5TTL2 — V88L + M154L
- **NDM-7:** X5CZV5 — D130N + M154L

## Structural Analysis

The experimental NDM-1 structure used for structural analysis is **PDB 3ZR9**. The structure was determined by X-ray diffraction at 1.91 Å resolution and contains chain A corresponding to an NDM-1 beta-lactamase fragment.

The observed zinc site in this structure was examined using atom-to-atom distance measurements. Close contacts were observed for His120-NE2, His122-ND1, and His189-NE2.

Variant-associated residues were then evaluated relative to the observed zinc site:

| Substitution | Closest measured side-chain atom to observed Zn | Distance | Interpretation |
|---|---|---:|---|
| M154L | M154-SD | 9.33 Å | Not a direct Zn ligand; possible local packing/environment effect |
| V88L | V88-CG1 | 16.29 Å | Conservative hydrophobic substitution; possible local packing effect |
| D130N | D130-OD2 | 18.00 Å | Not a direct Zn ligand; removes negative charge and may alter local electrostatic/H-bond environment |

## Key Findings

1. M154L is shared by NDM-4, NDM-5, and NDM-7.
2. M154 is not a direct Zn-coordinating residue in the analyzed 3ZR9 structure.
3. V88L is a conservative hydrophobic substitution and is relatively distant from the observed Zn site.
4. D130N changes an acidic, negatively charged residue to a polar uncharged residue and is also distant from the observed Zn site.
5. NDM-5 and NDM-7 contain multiple substitutions, so the individual contribution of each substitution cannot be separated from sequence comparison alone.

## Important Limitations

The structural measurements in this project do not establish changes in catalytic activity, zinc affinity, substrate binding, minimum inhibitory concentration (MIC), or antibiotic resistance phenotype. The analysis describes structural proximity and physicochemical properties rather than experimentally proving a mechanism.

PDB 3ZR9 is an engineered NDM-1 beta-lactamase fragment (residues 42-270), rather than an untouched full-length native protein. The observed zinc-site geometry should therefore be interpreted specifically within the experimental structure analyzed.

## Project Structure



## Reproducibility

The analysis files, sequence inputs, structural file, measurements, and plotting script are organized within this repository so that the workflow can be inspected and reproduced.

## Current Scope

This repository documents sequence comparison and initial structural interpretation of selected NDM variants. Future work may investigate structural visualization, residue-level interactions, and additional computational analyses while maintaining clear separation between measured evidence and biological hypotheses.
