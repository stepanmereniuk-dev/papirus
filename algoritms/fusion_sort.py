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

TEST_LIST = [12, 43, 0, -125, 9805, 54, 9014, 3, 1, 7]

class TestMergeSort:
    
    def sort(lst):
        if len(lst) <= 1:  # Stop reccursion
            return lst
        

        mid = len(lst) // 2
        left = lst[:mid]            
        right = lst[mid:]         

        left_sorted = TestMergeSort.sort(left)
        right_sorted = TestMergeSort.sort(right)
        
        return TestMergeSort._merge(left_sorted, right_sorted)

    def _merge(left, right):
        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

sorted_list = TestMergeSort.sort(TEST_LIST)
print(sorted_list)
