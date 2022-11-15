"""Écrivez un programme NumPy pour créer un tableau avec les valeurs 1, 7, 13, 105 et déterminer la
taille de la mémoire occupée par le tableau."""
import numpy as np
arr1 = np.array([1,7,13,105])
arr2 = np.array([1,7,13,105], dtype=np.int8)
arr3 = np.array([1,7,13,105], dtype=np.int16)
arr4 = np.array([1,7,13,105], dtype=np.int32)
arr5 = np.array([1,7,13,105], dtype=np.int64)
print(f"{arr1.size*arr1.itemsize} bytes")
print(f"{arr2.size*arr2.itemsize} bytes")
print(f"{arr3.size*arr3.itemsize} bytes")
print(f"{arr4.size*arr4.itemsize} bytes")
print(f"{arr5.size*arr5.itemsize} bytes")