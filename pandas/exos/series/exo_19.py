import pandas as pd
import matplotlib.pyplot as plt

ser = pd.Series([1,4,5,6,3,5,4,5,8,9,6,2,1,3,6,7])

occurences = ser.value_counts()
print(occurences)
plt.hist(ser)
plt.show()