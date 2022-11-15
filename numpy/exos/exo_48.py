"""Écrivez un programme NumPy pour créer un tableau à deux dimensions avec la forme (8,5) de
nombres aléatoires. Sélectionnez des nombres aléatoires à partir d'une distribution normale (200,7)."""
import numpy as np
import matplotlib.pyplot as plt

arr = np.random.normal(200,7, size=(8,5))
plt.hist(arr)
# print(arr)
plt.show()