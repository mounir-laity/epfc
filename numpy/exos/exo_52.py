"""Écrivez un programme NumPy pour trier un tableau donné par ligne et colonne dans l'ordre
croissant."""
import numpy as np

arr = np.random.randint(0,100,size=(4,4))
print(arr)
print(np.sort(arr, axis=0)) # Tri sur colonne
print(np.sort(arr, axis=1)) # Tri sur ligne