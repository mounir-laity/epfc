import numpy as np

arr = np.array([1,2,3,4,5,6])
arr2 = np.array([1,0, np.nan, 3])
arr3 = np.array([0, np.inf])
print(np.isfinite(arr))
print(np.isfinite(arr2))
print(np.isfinite(arr3))

