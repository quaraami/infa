import numpy as np
import os
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

dir = os.getcwd()
def f(a):
   return np.sin(a) + a + a * np.sin(a**2)

x = np.linspace(-10, 10, 1000)

plt.plot(x, f(x), color='red', linewidth=1)
plt.grid()
# plt.show()
plt.savefig(dir + '/my_first_dependence.svg', dpi=300)
plt.annotate('wtf', (0, 0), (2.5, 10))
plt.show()