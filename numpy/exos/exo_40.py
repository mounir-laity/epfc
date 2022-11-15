"""Écrivez un programme NumPy pour convertir une liste donnée en un tableau, puis convertissez-le à
nouveau en liste. Vérifiez que la liste initiale et la liste finale sont égales ou non."""
import numpy as np

my_list = [1.1,2.2,3.3,4,5,6]

arr = np.array(my_list)
final_list = list(arr)

if my_list == final_list:
    print(f"Les deux listes sont égales : {my_list} et {final_list}")
else:
    print(f"Les deux listes ne sont pas égales : {my_list} et {final_list}")