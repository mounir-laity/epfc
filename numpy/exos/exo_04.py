"""Ecrivez un programme NumPy pour tester si l'un des éléments d'un tableau donné est différent de
zéro."""
import numpy as np

arr = np.array([1,2,3,4,5,6])
arr2 = np.array([1,0, 3])
arr3 = np.array([0])
print(np.any(arr))
print(np.any(arr2))
print(np.any(arr3))

