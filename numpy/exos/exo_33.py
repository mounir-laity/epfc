"""Écrivez un programme NumPy pour calculer le produit scalaire de deux vecteurs donnés."""
import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print(np.dot(arr1,arr2))

arr3 = np.array([0,2])
arr4 = np.array([2,0])

print(np.dot(arr3,arr4))