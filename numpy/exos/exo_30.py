"""Écrivez un programme NumPy pour créer une matrice 4x4 dans laquelle 0 et 1 sont décalés, avec des
zéros sur la diagonale principale."""
import numpy as np

arr = np.full((4,4),0)
arr[::2,1::2].fill(1)
arr[1::2,::2].fill(1)
print(arr)