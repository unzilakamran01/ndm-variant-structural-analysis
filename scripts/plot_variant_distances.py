import matplotlib.pyplot as plt

# Distances measured from the NDM-1 reference structure (PDB 3ZR9),
# chain A, to the observed zinc site Zn A273.
variants = ["M154L", "V88L", "D130N"]
distances = [9.33, 16.29, 18.00]
atoms = ["Met154 SD", "Val88 CG1", "Asp130 OD2"]

fig, ax = plt.subplots(figsize=(8, 5.5))

bars = ax.bar(variants, distances)

ax.set_ylabel("Distance to observed Zn A273 (Å)")
ax.set_xlabel("Substitution found in NDM-4, NDM-5 or NDM-7")
ax.set_title(
    "Selected Variant Positions in the NDM-1 Reference Structure\n"
    "PDB 3ZR9, Chain A"
)

ax.bar_label(
    bars,
    labels=[f"{d:.2f} Å\n{a}" for d, a in zip(distances, atoms)],
    padding=4,
    fontsize=9
)

ax.text(
    0.01, -0.22,
    "Distances are from specified NDM-1 residue atoms to Zn A273; "
    "they are not measurements from mutant structures.",
    transform=ax.transAxes,
    fontsize=8,
    wrap=True
)

ax.set_ylim(0, max(distances) + 5)
fig.tight_layout()

fig.savefig(
    "results/structure_analysis/variant_zinc_distances.png",
    dpi=300,
    bbox_inches="tight"
)

