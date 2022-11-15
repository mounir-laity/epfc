import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,3*np.pi,0.2)
y = np.sin(x)
plt.plot(y)
plt.show()