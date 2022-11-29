import numpy as np
import pandas as pd

np.random.seed(1005)
ser = pd.Series(np.random.randint(1,100,100))
positions_to_take = [1,5,9,8,15,24,49,77,82,93]
print(ser.take(positions_to_take))