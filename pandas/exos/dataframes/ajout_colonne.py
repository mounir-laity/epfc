import pandas as pd

d = {'one' : pd.Series([1, 2, 3],index=['a', 'b', 'c']),'two' : pd.Series([1, 2, 3, 4],index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame.from_dict(d)
print(df)
df["three"] = pd.Series(["PHP","Python","Java"],index=["a","b","d"])
print(df)