import pandas as pd


ser = pd.Series([1,2,3,4,5,6,7,8,9,5,3])
mean = ser.mean()
std = ser.std()
print(f"The mean is {mean}")
print(f"The std is {std}")