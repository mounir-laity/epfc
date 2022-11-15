"""Écrivez un programme NumPy pour trouver le nombre de lignes et de colonnes d'une matrice
donnée."""

import numpy as np

def find_dimensions(array):
    shape = array.shape
    if shape:
        if len(shape) < 2:
            return (1,shape[0])
        else:
            return (shape[0], shape[-1])
    print(shape)
    
    
array = np.array([[4,5,6],[7,8,9],[10,11,12],[1,2,3]])
lines, columns = find_dimensions(array)
print(f"There are {lines} lines and {columns} columns in that array.")