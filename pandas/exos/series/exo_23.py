import numpy as np
import pandas as pd

np.random.seed(1005)
ser1 = pd.Series(np.random.randint(1,100,10))
ser2 = pd.Series(np.random.randint(1,100,10))
print(ser1)
print(ser2)
print(ser1[ser1.isin(ser2)].index)