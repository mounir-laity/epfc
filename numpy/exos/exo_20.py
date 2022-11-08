import numpy as np

arr = np.random.random((3,4))
print(arr, "\n")
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j])