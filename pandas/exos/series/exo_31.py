import numpy as np
import pandas as pd

x = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = pd.Series([11, 8, 7, 5, 6, 5, 3, 4, 7, 1])
result = np.linalg.norm(x-y)
print(result)