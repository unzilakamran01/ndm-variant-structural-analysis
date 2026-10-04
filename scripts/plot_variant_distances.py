import matplotlib.pyplot as plt

variants = ["M154L", "V88L", "D130N"]
distances = [9.33, 16.29, 18.00]

plt.figure(figsize=(7, 5))
plt.bar(variants, distances)
plt.ylabel("Minimum measured distance to observed Zn site (Å)")
plt.xlabel("Substitution")
plt.title("Variant Residues: Distance to Observed Zn Site")
plt.tight_layout()
plt.savefig("results/structure_analysis/variant_zinc_distances.png", dpi=300)
plt.show()
