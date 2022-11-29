import numpy as np
import pandas as pd

np.random.seed(1005)
ser = pd.Series(np.random.randint(1,10,10))
print(ser)
ser = ser.diff().tolist()
print(ser)