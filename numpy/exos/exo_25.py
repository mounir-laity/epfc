"""Ecrivez un programme NumPy pour créer une matrice 3x4 remplie de valeurs de 10 à 21."""
import numpy as np

arr = np.arange(10,22)
arr = arr.reshape((3,4))
print(arr)