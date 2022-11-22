import pandas as pd

ser = pd.Series(data=[1,2,3,4,5], index=["Un","B","C","J","E"])
ser = ser.reindex(["B","Un","C","J","E"])
print(ser)