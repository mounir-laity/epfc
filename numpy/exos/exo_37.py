""" Ecrivez un programme NumPy pour enregistrer un tableau donné dans un fichier texte et le charger."""
import numpy as np
from os.path import join

arr = np.array([7,7,7,8,9,9,6,2])
filename = "array3.txt"
path = join("files", filename)
np.savetxt(path, arr)

file = np.loadtxt(path)
print(file)