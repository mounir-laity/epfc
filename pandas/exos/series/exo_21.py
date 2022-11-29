import numpy as np
import pandas as pd

np.random.seed(1005)
ser = pd.Series(np.random.randint(1,100,100))
print(ser[ser % 5 == 0].index)