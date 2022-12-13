import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.linear_model import SGDRegressor
import numpy as np
from joblib import dump, load
from os.path import exists

filename = "appart.csv"
df = pd.read_csv(filename)
df.columns = ["superficie", "prix"]
x = np.array(df["superficie"]).reshape(-1,1)
y = np.array(df["prix"])

model_file = "model.pkl"
wanted_score = 0.75
if exists(model_file):
    model = load(model_file)
    coeff = model.score(x, y)
else:
    model = SGDRegressor(max_iter=1000,eta0=0.015)
    model.fit(x,y)
    coeff = model.score(x, y)
    if coeff >= wanted_score:
        pkl_filename = "model.pkl"
        with open(pkl_filename, 'wb') as file:
            dump(model, file)
print(f'Coeff R2 = {coeff}')
print(model.predict([[20]]))
plt.scatter(x,y)
plt.plot(x, model.predict(x), c='red', lw = 3)
plt.show()