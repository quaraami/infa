import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
x1 = np.linspace(-5, 5, 500) #граница изнений аргумента в левой части графика
x2 = np.linspace(-5 , 5 , 500)
p=0
# Определение функций
def f1(x):
    return x**3-x

def f2(x):
    return 2*x-1

# Разница функций для нахождения пересечений
def diff(x):
    return f1(x) - f2(x)

# Нахождение точек пересечения
x_roots = fsolve(diff, [-2, 0, 2])  # Три предположительных корня
y_roots = f1(x_roots)
plt.axvline(p, color='black', linewidth=1)
plt.axhline(y=0, color='black', linewidth=1)
plt.plot(x1, f1(x1), color='#00FFFF', linewidth=1, label=r"$\mathcal{F} = {x^3-x}$")
plt.plot(x2, f2(x2), color='#DC143C', linewidth=1, label=r"$\mathcal{F} = {2*x-1}$")
plt.scatter(x_roots, y_roots, color='green', linewidth=1)
plt.xlabel('Ось х')
plt.ylabel('Ось f(x)')
plt.legend() #вывод легенды
plt.xlim(-3,3) #задаем диапозон построения x
plt.ylim(-5,5) #задаем диапозон построения y
plt.grid()
plt.show()

