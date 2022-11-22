import pandas as pd

data = [100,200,"pythons",300.12,400]
ser = pd.Series(data)
ser = pd.to_numeric(ser,errors="coerce")
print(ser)