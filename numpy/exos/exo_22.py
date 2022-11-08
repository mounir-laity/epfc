import numpy as np

arr = np.arange(0,21)
for i in range(len(arr)):
    if 9 <= i <= 15:
        arr[i] = -arr[i]
print(arr)