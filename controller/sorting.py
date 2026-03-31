import json
import copy
import time
import threading

from algoritms.fast_sort import FastSort
from algoritms.bubble_sort import BubbleSort
from algoritms.sort_by_selection import SelectionSort
from algoritms.fusion_sort import FusionSort
from algoritms.heap_sort import HeapSort
from algoritms.comb_sort import CombSort

ALGORITHMES = [
    {"nom": "Tri Rapide (Quick Sort)", "classe": FastSort, "fichier": "models/data_fast_sort.json"},
    {"nom": "Tri à Bulles (Bubble Sort)", "classe": BubbleSort, "fichier": "models/data_bubble_sort.json"},
    {"nom": "Tri par Sélection", "classe": SelectionSort, "fichier": "models/data_selection_sort.json"},
    {"nom": "Tri Fusion (Merge Sort)", "classe": FusionSort, "fichier": "models/data_fusion_sort.json"},
    {"nom": "Tri par Tas (Heap Sort)", "classe": HeapSort, "fichier": "models/data_heap_sort.json"},
    {"nom": "Tri à Peigne (Comb Sort)", "classe": CombSort, "fichier": "models/data_comb_sort.json"},
]


def lancer_tous_les_tris(fichier_source, delai=0.02):
    with open(fichier_source, 'r', encoding='utf-8') as f:
        donnees_originales = json.load(f)

    threads = []
    for algo in ALGORITHMES:
        donnees_copie = copy.deepcopy(donnees_originales)

        # Écrire l'état initial (mélangé) dans le fichier de chaque algo
        with open(algo["fichier"], 'w', encoding='utf-8') as f:
            json.dump(donnees_copie, f)

        trieur = algo["classe"](donnees_copie, algo["fichier"], delai)
        thread = threading.Thread(target=trieur.trier, name=algo["nom"], daemon=True)
        threads.append(thread)

    # Petit délai pour laisser le viewer s'initialiser
    time.sleep(2)

    for thread in threads:
        thread.start()

    return threads
