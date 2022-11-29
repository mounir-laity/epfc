import matplotlib.pyplot as plt
import numpy as np


x = np.linspace( 0, 10, 100)
plt.plot(x, np.sin(x), '-')
plt.plot(x, np.cos(x), '--')
plt.title("On the same plot")
plt.figure() # create a plot figure
# create the first of two panels and set current axis
plt.subplot( 2, 1, 1) # (rows, columns, panelnumber)
plt.title("On two different subplots")
plt.plot(x, np.sin(x))
# # create the second panel and set current axis
plt.subplot( 2, 1, 2)
plt.plot(x, np.cos(x))
plt.show()