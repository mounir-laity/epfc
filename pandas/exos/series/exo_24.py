import numpy as np
import pandas as pd

ser = pd.Series(data=["php","python","c#","15","mounir","paSSwOrd"])
ser = ser.map(lambda x: x[0].upper()+x[1:-1]+x[-1].upper())
print(ser)