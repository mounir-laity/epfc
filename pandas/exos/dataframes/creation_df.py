import numpy as np
import pandas as pd

# Création d'un dataframe en spécifiant les index et colonnes
# ar = np.array([[1.1, 2, 3.3, 4], [2.7, 10, 5.4, 7], [5.3, 9, 1.5,15]])
# df = pd.DataFrame(ar, index = ['a1', 'a2', 'a3'], columns = ['A', 'B', 'C', 'D'])
# print(df)

# Création d'un dataframe avec des données de différents type
# data = [["Alex",12],["Bob",74]]
# df = pd.DataFrame(data, columns=["Name","Age"])
# print(df)

# Création à l'aide d'un dictionnaire
# d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),'two' : pd.Series([1, 2, 3, 4], index=['a','b', 'c', 'd'])}
# df = pd.DataFrame(d)
# print(df)

# Utilisation de orient pour définit les clés comme index
# df = pd.DataFrame.from_dict({'A': [1.1, 2.7, 5.3], 'B': [2,10, 9], 'C': [3.3, 5.4, 1.5]}, orient="index")
# print(df)
# Idem mais les clés sont des colonnes
df = pd.DataFrame.from_dict({'A': [1.1, 2.7, 5.3], 'B': [2,10, 9], 'C': [3.3, 5.4, 1.5]}, orient="columns")
# print(df)
# Sélection d'une colonne
print(df["B"])