import pandas as pd

ser = pd.Series([1,4,5,6,3,5,4,5,8,9,6,2,1,3,6,7])

occurences = ser.value_counts()
for element in occurences:
    if occurences[element] == occurences[0]:
        pass