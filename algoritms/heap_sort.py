import json
import time


class HeapSort:
    """Tri par Tas (Heap Sort) — O(n log n)."""

    def __init__(self, data, fichier_sortie, delai=0.02):
        self.data = data
        self.fichier_sortie = fichier_sortie
        self.delai = delai

    def _sauvegarder(self):
        with open(self.fichier_sortie, 'w', encoding='utf-8') as f:
            json.dump(self.data, f)
        time.sleep(self.delai)

    def _tamiser(self, n, i):
        plus_grand = i
        gauche = 2 * i + 1
        droite = 2 * i + 2

        if gauche < n and self.data[gauche]["hue"] > self.data[plus_grand]["hue"]:
            plus_grand = gauche
        if droite < n and self.data[droite]["hue"] > self.data[plus_grand]["hue"]:
            plus_grand = droite

        if plus_grand != i:
            self.data[i], self.data[plus_grand] = self.data[plus_grand], self.data[i]
            self._tamiser(n, plus_grand)

    def trier(self):
        n = len(self.data)

        # Construction du tas (max-heap)
        for i in range(n // 2 - 1, -1, -1):
            self._tamiser(n, i)
        self._sauvegarder()

        # Extraction un par un
        for i in range(n - 1, 0, -1):
            self.data[0], self.data[i] = self.data[i], self.data[0]
            self._tamiser(i, 0)
            self._sauvegarder()


TEST_LIST = [12, 43, 0, -125, 9805, 54, 9014, 3, 1, 7]

class TestHeapSort:
    def sort(lst):
        arr = list(lst)        
        n = len(arr)
        
        # Max-Heap 
        for i in range(n // 2 - 1, -1, -1):         # FROM END 
            TestHeapSort._heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]     
            TestHeapSort._heapify(arr, i, 0)   
        return arr
    
    
    def _heapify(arr, n, i):
        largest = i         
        left = 2 * i + 1     
        right = 2 * i + 2   
        
        if left < n and arr[left] > arr[largest]:
            largest = left
            
        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            TestHeapSort._heapify(arr, n, largest)  


sorted_list = TestHeapSort.sort(TEST_LIST)
print("Відсортований:", sorted_list)