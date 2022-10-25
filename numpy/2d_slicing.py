import numpy as np
#Exos page 17
# Exo 1
arr = np.arange(9,0,-1)
arr = arr.reshape(3,3)
print(arr)
# Exo 2
# [[3,2,1], [6,5,4], [9,8,7]]
print(arr[-1::-1])
# [9,6,3]
print(arr[:,0])
# [[9,8], [6,5]]
print(arr[:2,:2])
# [[8,7], [5,4], [2,1]]
print(arr[:,1:])
# [[9],[6],[3]]
print(arr[:,:1])