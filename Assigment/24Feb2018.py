import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(15)
y = np.random.rand(15)

plt.rcParams['figure.figsize'] = 10,10

plt.grid(x,y)
plt.show()
