import json
import time


class BubbleSort:
    """Tri à Bulles (Bubble Sort) — O(n²)."""

    def __init__(self, data, fichier_sortie, delai=0.02):
        self.data = data
        self.fichier_sortie = fichier_sortie
        self.delai = delai

    def _sauvegarder(self):
        with open(self.fichier_sortie, 'w', encoding='utf-8') as f:
            json.dump(self.data, f)
        time.sleep(self.delai)

    def trier(self):
        n = len(self.data)
        for i in range(n):
            echange = False
            for j in range(0, n - i - 1):
                if self.data[j]["hue"] > self.data[j + 1]["hue"]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    echange = True
            self._sauvegarder()
            if not echange:
                break