import json
import time


class FusionSort:
    """Tri Fusion (Merge Sort) — O(n log n)."""

    def __init__(self, data, fichier_sortie, delai=0.02):
        self.data = data
        self.fichier_sortie = fichier_sortie
        self.delai = delai

    def _sauvegarder(self):
        with open(self.fichier_sortie, 'w', encoding='utf-8') as f:
            json.dump(self.data, f)
        time.sleep(self.delai)

    def _fusionner(self, gauche, milieu, droite):
        copie_gauche = self.data[gauche:milieu + 1]
        copie_droite = self.data[milieu + 1:droite + 1]

        i = j = 0
        k = gauche

        while i < len(copie_gauche) and j < len(copie_droite):
            if copie_gauche[i]["hue"] <= copie_droite[j]["hue"]:
                self.data[k] = copie_gauche[i]
                i += 1
            else:
                self.data[k] = copie_droite[j]
                j += 1
            k += 1

        while i < len(copie_gauche):
            self.data[k] = copie_gauche[i]
            i += 1
            k += 1

        while j < len(copie_droite):
            self.data[k] = copie_droite[j]
            j += 1
            k += 1

        self._sauvegarder()

    def _tri_fusion(self, gauche, droite):
        if gauche < droite:
            milieu = (gauche + droite) // 2
            self._tri_fusion(gauche, milieu)
            self._tri_fusion(milieu + 1, droite)
            self._fusionner(gauche, milieu, droite)

    def trier(self):
        self._tri_fusion(0, len(self.data) - 1)
        self._sauvegarder()
