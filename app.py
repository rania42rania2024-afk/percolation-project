import numpy as np
import matplotlib.pyplot as plt

# Paramètres
N = 10
probabilites = [0.2, 0.5, 0.7, 1]

def percolation(N, P):
    grille = np.random.rand(N, N) < P
    return grille.astype(int)

# Affichage des résultats
fig, axes = plt.subplots(1, 4, figsize=(14, 4))

for i, P in enumerate(probabilites):

    grille = percolation(N, P)

    axes[i].imshow(grille, cmap="Blues", vmin=0, vmax=1)
    axes[i].set_title(f"P = {P}")
    axes[i].set_xticks(range(N))
    axes[i].set_yticks(range(N))
    axes[i].grid(True)

    print(f"\nPour P = {P}")
    print(grille)

plt.tight_layout()
plt.show()
