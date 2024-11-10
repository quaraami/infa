import numpy as np # вводим mathplotlib
import os
from matplotlib import pyplot as plt
p=0
x1 = np.linspace(-25, p - 0.01, 500)
x2 = np.linspace(25, p + 0.01, 500)
a=1
b=1
dir = os.getcwd()
def f(x):
    return (x**b + a**b)/x**b
l1=plt.plot (x1, f(x1))
l2=plt.plot (x2, f(x2))
plt.plot (x1, f(x1), color='blue', label=r"$\mathcal{F} = \frac{x^b+a^b}{x^b}$")
plt.plot (x2, f(x2), color='blue')
plt.axvline(p, color='red', linestyle='--', label='Точка разрыва', linewidth=1)
plt.xlabel('Ось х')
plt.ylabel('Ось f(x)')
plt.grid(True)
plt.legend()
plt.xlim(-25,25)
plt.ylim(-10,10)
plt.title('Функции типа (x**b + a**b)/x**b при разных значениях a и b')
plt.savefig(dir + '/zadanie9_1', dpi=300)
plt.show()