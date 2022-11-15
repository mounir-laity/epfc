"""Écrivez un programme NumPy pour créer un vecteur avec des valeurs de 0 à 20 et changez le signe
des nombres dans la plage de 9 à 15."""
import numpy as np

arr = np.arange(0,21)
for i in range(len(arr)):
    if 9 <= i <= 15:
        arr[i] = -arr[i]
print(arr)