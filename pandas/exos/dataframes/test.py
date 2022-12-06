import numpy as np
import pandas as pd

filename = "covid.csv"
pd.set_option('display.max_columns', None)
df = pd.read_csv(filename)
df["Active"] = df["Confirmed"] - df["Deaths"] - df["Recovered"]
average_death_rate = (df["Deaths"] / df["Confirmed"]).mean()
average_recovery_rate = (df["Recovered"] / df["Confirmed"]).mean()
print(f"In average, {average_death_rate*100:.2f}% of people died from covid.")
print(f"In average, {average_recovery_rate*100:.2f}% of people recovered from covid.")
