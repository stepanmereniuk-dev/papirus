import json
import time


class CombSort:
    """Tri à Peigne (Comb Sort) — O(n²) pire cas, O(n log n) en moyenne."""

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
        ecart = n
        retrecissement = 1.3
        trie = False

        while not trie:
            ecart = int(ecart / retrecissement)
            if ecart <= 1:
                ecart = 1
                trie = True

            for i in range(n - ecart):
                if self.data[i]["hue"] > self.data[i + ecart]["hue"]:
                    self.data[i], self.data[i + ecart] = self.data[i + ecart], self.data[i]
                    trie = False

            self._sauvegarder()

TEST_LIST = [12,43,0,-125,9805,54,9014,3,1,7]

class TestCombSort:
    def sort(lst):
        arr = list(lst)
        n = len(arr)
        gap = n
        
        while gap > 1:
            gap = max(1, int(gap / 1.3))
           
            for i in range(n - gap):
                if arr[i] > arr[i + gap]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
        
        return arr
print(TestCombSort.sort(TEST_LIST))