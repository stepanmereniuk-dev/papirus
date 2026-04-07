import json
import time


class SelectionSort:
    """Tri par Sélection (Selection Sort) — O(n²)."""

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
            min_idx = i
            for j in range(i + 1, n):
                if self.data[j]["hue"] < self.data[min_idx]["hue"]:
                    min_idx = j
            self.data[i], self.data[min_idx] = self.data[min_idx], self.data[i]
            self._sauvegarder()
            
            
class TestSelectionSort:
    def sort(lst):
        arr = list(lst)x
        n = len(arr)
        
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        return arr
