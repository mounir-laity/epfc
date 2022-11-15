"""Écrivez un programme NumPy pour vérifier si deux tableaux sont égaux (au niveau des éléments) ou
non."""
import numpy as np

arr1 = [1,2,3,4,5]
arr2 = [6,7,8,9,10]
arr3 = [1,2,3,4,5]

print(np.all(np.equal(arr1,arr2)))
print(np.all(np.equal(arr1,arr3)))
print(np.all(np.equal(arr2,arr3)))