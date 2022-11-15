"""Ecrivez un programme NumPy pour enregistrer un tableau donné dans un fichier texte et le charger. Gérez également les headers"""
import numpy as np
from os.path import join

names = ["Mounir", "Julien", "Jean"]
points = [12.5,15,7]
filename = "array4.txt"
path = join("files",filename)

np.savetxt(delimiter=",",header=",".join(names),fname=path,X=points)


arr = np.loadtxt(fname=path)
print(arr)