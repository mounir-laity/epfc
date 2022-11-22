import pandas as pd

ser = pd.Series([i for i in range(11)])
#Print values < 6

ser = ser[ser < 6]
print(ser)