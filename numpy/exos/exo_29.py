"""Écrivez un programme NumPy pour créer une matrice zéro 5x5 avec des éléments sur la diagonale
principale égaux à 1, 2, 3, 4, 5"""
import numpy as np

arr = np.zeros((5,5))
np.fill_diagonal(arr,[1,2,3,4,5])
print(arr)

# other solution
# print(np.diag([1,2,3,4,5]))