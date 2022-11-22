import pandas as pd

ser1 = pd.Series([1,2,3,4,5])
ser2 = pd.Series([2,4,6,8,10])
for i in ser1.values:
    if i not in ser2.values:
        print(i, end=" ")