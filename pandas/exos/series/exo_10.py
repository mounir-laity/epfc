import pandas as pd

ser0 = pd.Series([["Rouge","Vert", "Blanc"],["Rouge","Noir"],["Jaune"]])
print(ser0)
ser0 = ser0.apply(pd.Series).stack().reset_index(drop=True)
print(ser0)