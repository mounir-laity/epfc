import pandas as pd

ser1 = pd.Series([1,2,3,4,5])
ser2 = pd.Series([2,4,6,8,10])

print(ser1[~ser1.isin(ser2)].append(ser2[~ser2.isin(ser1)]))