import numpy as np
import pandas as pd

ser = pd.Series(data=["php","python","c#","15","mounir","paSSwOrd"])
ser = ser.map(lambda x: len(x))
print(ser)