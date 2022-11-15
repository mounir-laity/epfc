"""Écrivez un programme NumPy pour créer une comparaison par élément (plus grand, plus grand_égal,
moins et moins_égal) de deux tableaux donnés."""
import numpy as np
arr1 = np.array([1,10,3])
arr2 = np.array([4,5,3])

print(np.greater(arr1, arr2))
print(np.less(arr1, arr2))
print(np.greater_equal(arr1, arr2))
print(np.less_equal(arr1, arr2))