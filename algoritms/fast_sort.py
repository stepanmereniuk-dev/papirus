import json
import time


class FastSort:
    """Tri Rapide (Quick Sort) — O(n log n) en moyenne."""

    def __init__(self, data, fichier_sortie, delai=0.02):
        self.data = data
        self.fichier_sortie = fichier_sortie
        self.delai = delai

    def _sauvegarder(self):
        with open(self.fichier_sortie, 'w', encoding='utf-8') as f:
            json.dump(self.data, f)
        time.sleep(self.delai)

    def _partition(self, bas, haut):
        pivot = self.data[haut]["hue"]
        i = bas - 1
        for j in range(bas, haut):
            if self.data[j]["hue"] <= pivot:
                i += 1
                self.data[i], self.data[j] = self.data[j], self.data[i]
        self.data[i + 1], self.data[haut] = self.data[haut], self.data[i + 1]
        self._sauvegarder()
        return i + 1

    def _tri_rapide(self, bas, haut):
        if bas < haut:
            pi = self._partition(bas, haut)
            self._tri_rapide(bas, pi - 1)
            self._tri_rapide(pi + 1, haut)

    def trier(self):
        self._tri_rapide(0, len(self.data) - 1)
        self._sauvegarder()
