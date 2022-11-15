"""Écrivez un programme NumPy pour enregistrer deux tableaux donnés dans un seul fichier au format
compressé (format .npz) et chargez-le."""
import numpy as np
from os.path import join

array = np.array([7,8,9])
filename = "array2.npz"
path = join("files",filename)
np.savez(path)

saved = np.load(path)
print(saved)