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
            
TEST_LIST = [12,43,0,-125,9805,54,9014,3,1,7]

class TestBubbleSort:
    def sort(list_to_sort:list):
        arr = list(list_to_sort)
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if list_to_sort[j] > list_to_sort[j + 1]:
                    list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
        
        return list_to_sort
    
print(TestBubbleSort.sort(TEST_LIST))