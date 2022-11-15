"""Ecrivez un programme NumPy pour créer une matrice 10x10, dans laquelle les éléments sur les
bordures seront égaux à 1, et à l'intérieur de 0."""
import numpy as np

arr = np.zeros((8,8))
arr = np.pad(arr, constant_values=1, pad_width=1)
print(arr)
print(arr.shape)