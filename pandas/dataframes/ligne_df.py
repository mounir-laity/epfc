import pandas as pd

df = pd.DataFrame.from_dict({'A': [1.1, 2.7, 5.3], 'B': [2,10, 9], 'C': [3.3, 5.4, 1.5]}, orient="index")
print(df)

# Sélection selon l'index défini (ici la chaîne de caractères)
# print(df.loc["A"])

# Sélection selon un indice numérique (0 étant la première ligne)
# print(df.iloc[2]) # Sélection troisième ligne

# Sélection de plusieurs lignes grâce au slicing
# print(df[1:3])

# Ajout de ligne
# df2 = pd.DataFrame([[5, 6], [7, 8]], columns=['a','b'], index=["D","E"])
# df = pd.concat([df,df2])
# print(df)

# Suppression de ligne
# df.drop("C", inplace=True)
# print(df)

# Idem
# df.drop(index="C", inplace=True)
# print(df)

# Suppression de colonne
# df.drop("b",axis=1,inplace=True)
# print(df)

# Idem
# df.drop(columns="b", inplace=True)
# print(df)