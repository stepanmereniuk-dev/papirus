import json
import os
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

INTERVALLE_MAJ = 100  # ms entre chaque vérification


def lire_couleurs(fichier):
    try:
        with open(fichier, 'r', encoding='utf-8') as f:
            donnees = json.load(f)
            return [item["rgb"] for item in donnees]
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def afficher_multi_tris(algorithmes):
    # Attendre que tous les fichiers existent
    for algo in algorithmes:
        while not os.path.exists(algo["fichier"]):
            time.sleep(0.1)

    # Première lecture pour initialiser
    donnees_initiales = {}
    for algo in algorithmes:
        couleurs = lire_couleurs(algo["fichier"])
        while couleurs is None:
            time.sleep(0.1)
            couleurs = lire_couleurs(algo["fichier"])
        donnees_initiales[algo["fichier"]] = couleurs

    nombre_couleurs = len(list(donnees_initiales.values())[0])

    # Configuration de la figure : grille 2×3
    fig, axes = plt.subplots(2, 3, figsize=(18, 12), subplot_kw={'projection': 'polar'})
    axes = axes.flatten()

    theta = np.linspace(0.0, 2 * np.pi, nombre_couleurs, endpoint=False)
    radii = [1] * nombre_couleurs
    width = (2 * np.pi) / nombre_couleurs

    bars_dict = {}
    modif_dict = {}

    for i, algo in enumerate(algorithmes):
        ax = axes[i]
        ax.set_axis_off()
        ax.set_title(algo["nom"], pad=15, fontsize=11, fontweight='bold')

        couleurs = donnees_initiales[algo["fichier"]]
        bars = ax.bar(theta, radii, width=width, bottom=0.0,
                      color=couleurs, edgecolor=couleurs, linewidth=0.5)
        bars_dict[algo["fichier"]] = bars
        modif_dict[algo["fichier"]] = os.path.getmtime(algo["fichier"])

    def actualiser(frame):
        for algo in algorithmes:
            fichier = algo["fichier"]
            try:
                modif = os.path.getmtime(fichier)
            except FileNotFoundError:
                continue

            if modif > modif_dict[fichier]:
                couleurs = lire_couleurs(fichier)
                if couleurs and len(couleurs) == nombre_couleurs:
                    for bar, c in zip(bars_dict[fichier], couleurs):
                        bar.set_facecolor(c)
                        bar.set_edgecolor(c)
                    modif_dict[fichier] = modif

        return [bar for bars in bars_dict.values() for bar in bars]

    fig.suptitle("Visualisation des Algorithmes de Tri", fontsize=16, fontweight='bold')
    plt.tight_layout(rect=[0, 0, 1, 0.95])

    ani = animation.FuncAnimation(fig, actualiser, interval=INTERVALLE_MAJ,
                                  cache_frame_data=False, blit=False)
    plt.show()
