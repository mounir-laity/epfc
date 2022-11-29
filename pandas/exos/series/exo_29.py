import numpy as np
import pandas as pd

ser = pd.Series(['Jan 2015', 'Feb 2016', 'Mar 2017', 'Apr 2018', 'May 2019'])
day = 15
ser = ser.map(lambda x: f"{str(day)} {x}")
print(ser)