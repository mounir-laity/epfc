import pandas as pd

def append_data(serie,data):
    data_to_add = pd.Series(data)
    serie = serie.append(data_to_add)
    return serie

ser = pd.Series(["100","200","pythons","300.12","400"])
data = ["500","php"]
print(append_data(ser, data))
