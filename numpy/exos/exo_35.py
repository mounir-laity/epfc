"""Ecrivez un programme NumPy pour enregistrer un tableau donné dans un fichier binaire ."""
import numpy as np
from os.path import join
arr = [1,2,3]
np.save(join("files","array"), arr)