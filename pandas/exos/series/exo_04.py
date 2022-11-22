import pandas as pd
import numpy as np

ser1 = pd.Series([2,4,6,8,10])
ser2 = pd.Series([1,3,5,7,10])
print(f"Equals : \n{ser1 == ser2}")
print(f"Greater than : \n{ser1 > ser2}")
print(f"Lesser than : \n{ser1 < ser2}")