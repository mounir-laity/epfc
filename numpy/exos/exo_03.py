"""Ecrivez un programme NumPy pour tester si aucun des éléments d'un tableau donné n'est nul."""
import numpy as np

arr = np.array([1,2,3,4,5,6])
arr2 = np.array([1,0, 3])
print(np.all(arr))
print(np.all(arr2))