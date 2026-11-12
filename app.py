import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# =================================
# 1. TITRE
# =================================

st.title("Percolation Simulation")
st.write("Interactive Python Simulation on Percolation Models")

# =================================
# 2. PARAMETRES
# =================================

N = 10
probabilites = [0.2, 0.5, 0.7, 1.0]

# =================================
# 3. MODELE DE PERCOLATION
# =================================

def percolation(N, P):
    grille = np.random.rand(N, N) < P
    return grille.astype(int)

# =================================
# 4. BOUTON DE SIMULATION
# =================================

if st.button("Run Simulation"):

    fig, axes = plt.subplots(1, 4, figsize=(14, 4))

    for i, P in enumerate(probabilites):

        grille = percolation(N, P)

        axes[i].imshow(
            grille,
            cmap="Blues",
            vmin=0,
            vmax=1
        )

        axes[i].set_title(f"P = {P}")
        axes[i].set_xticks(range(N))
        axes[i].set_yticks(range(N))
        axes[i].grid(True)

        st.write(f"Grid for P = {P}")
        st.write(grille)

    plt.tight_layout()

    st.pyplot(fig)
    plt.close(fig)

    st.success("Simulation completed!")
