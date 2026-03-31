import json
import colorsys
import random
import threading

from controller.sorting import lancer_tous_les_tris, ALGORITHMES
from view import afficher_multi_tris


def generer_donnees(fichier_sortie="data_couleurs.json", nombre_couleurs=360):
    donnees = []
    for i in range(nombre_couleurs):
        hue = i / nombre_couleurs
        r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        donnees.append({"id_origine": i, "hue": hue, "rgb": [r, g, b]})

    random.shuffle(donnees)

    with open(fichier_sortie, 'w', encoding='utf-8') as f:
        json.dump(donnees, f, indent=4)

    print(f"[*] {nombre_couleurs} couleurs mélangées → '{fichier_sortie}'")


if __name__ == "__main__":
    # 1. Générer les données mélangées
    generer_donnees("data_couleurs.json", 360)

    # 2. Lancer tous les tris en arrière-plan (threads)
    thread_tri = threading.Thread(
        target=lancer_tous_les_tris,
        args=("data_couleurs.json",),
        daemon=True
    )
    thread_tri.start()

    # 3. Afficher la visualisation (bloquant — fenêtre matplotlib)
    afficher_multi_tris(ALGORITHMES)
