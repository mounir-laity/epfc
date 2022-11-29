import numpy as np
import pandas as pd

ser = pd.Series(["01 Jan 2015","10-02-2016","20180307"," 2014/05/06","2016-04-12","2019-04-06T11:20"])
ser = pd.to_datetime(ser)
print(ser)