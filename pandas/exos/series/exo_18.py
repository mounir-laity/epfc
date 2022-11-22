import pandas as pd

ser1 = pd.Series([1.001,25.12,14.211,3.1415196,40,-5.22])
quantilles = ser1.describe()
quantilles = quantilles.reindex(["min","25%","50%","75%","max","std","count"])
print(list(quantilles[:-2]))