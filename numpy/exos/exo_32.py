"""Écrivez un programme NumPy pour calculer la somme de tous les éléments, la somme de chaque
colonne et la somme de chaque ligne d'un tableau donné."""
import numpy as np


arr = np.random.randint(1,10,size=(4,4))
print(arr)
print(f"Somme des éléments de la matrice : {np.sum(arr)}")
line_sum = np.sum(arr, axis=1)
column_sum = np.sum(arr, axis=0)
for i in range(len(arr)):
    print(f"Somme des éléments de la ligne n°{i} : {line_sum[i]}")
for i in range(len(arr[0])):
    print(f"Somme des éléments de la colonne n°{i} : {column_sum[i]}")