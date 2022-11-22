import pandas as pd
import numpy as np


p = pd.Series()
print(p)
data = np.array([-10,2,-3,4])
ind = np.array(["a","b","c","d"])
ser = pd.Series(data, index=ind)
# print(ser)
# print(ser[["a"]])
# print("c" in ser)
# print(2 in ser)
# print(2 in ser.values)
print(ser[ser > 0])