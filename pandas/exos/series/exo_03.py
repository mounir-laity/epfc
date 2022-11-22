import pandas as pd
import numpy as np

ser1 = pd.Series([2,4,6,8,10])
ser2 = pd.Series([1,3,5,7,9])

print(f"addition result : \n{ser1+ser2}")
print(f"substraction result : \n{ser1-ser2}")
print(f"multiplication result : \n{ser1*ser2}")
print(f"division result : \n{ser1/ser2}")