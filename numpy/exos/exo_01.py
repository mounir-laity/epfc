"""Écrivez un programme NumPy pour obtenir la version numpy et afficher la configuration de
construction numpy."""
import numpy as np

print(f"Numpy's version is : {np.__version__}")

print(f"Numpy's configuration :")
print(np.show_config())