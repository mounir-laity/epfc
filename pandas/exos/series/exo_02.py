import pandas as pd
import numpy as np


ser = pd.Series(np.array([2,4,6,8]))
l = ser.to_list()
print(l)