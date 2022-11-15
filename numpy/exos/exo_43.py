"""Écrivez un programme NumPy pour trouver les données manquantes dans un tableau donné."""
import numpy as np

arr = np.array([1,2,3,4,np.nan,5,np.nan,7,8,9,np.nan])
missing = np.isnan(arr)
for i in range(len(missing)):
    if missing[i]:
        print(f"Missing value at index {i}")
        