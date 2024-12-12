import numpy as np
import os
from matplotlib import pyplot as plt
#ПАРАМЕТРЫ ДЛЯ ПЕРВОГО
p=0 # асимптота
x1 = np.linspace(-25, p - 0.01, 500) #граница изнений аргумента в левой части графика
x2 = np.linspace(p + 0.01, 25 , 500) #граница изнений аргумента в правой части графика
a=1 #параметр а
b=1 #параметр b, степень
dir = os.getcwd()
def f(x):
    return (x**b + a**b)/x**b #расчет функции для певрого
def g(x):
    return (x**h + d**h)/x**h #расчет функции для второго
def u(x):
    return (x**v + c**v)/x**v #расчет функции для третьего

#ПАРАМЕТРЫ ДЛЯ ВТОРОГО
x11 = np.linspace(-25, p - 0.01, 500)
x21 = np.linspace(25, p + 0.01, 500)
d=2
h=1
#ПАРАМЕТРЫ ДЛЯ ТРЕТЬЕГО
x12 = np.linspace(-25, p - 0.01, 500)
x22 = np.linspace(25, p + 0.01, 500)
c=1
v=2
#ПОСТРОЕНИЕ ПЕРВОГО
l1=plt.plot (x1, f(x1)) #расчет точек графика для левой части
l2=plt.plot (x2, f(x2)) #расчет точек графика для правой части
#ПОСТРОЕНИЕ ВТОРОГО
l1=plt.plot (x11, g(x11))
l2=plt.plot (x21, g(x21))
#ПОСТРОЕНИЕ  ТРЕТЬЕГО
l1=plt.plot (x12, u(x12))
l2=plt.plot (x22, u(x22))
#ВЫВОД ПЕРВОГО
plt.plot (x1, f(x1), color='blue', label=r"$\mathcal{F} = \frac{x^1+1^1}{x^1}$") #вывод левой части
plt.plot (x2, f(x2), color='blue') #вывод правой части
#ВЫВОД ВТОРОГО
plt.plot (x11, g(x11), color='purple', label=r"$\mathcal{F} = \frac{x^1+2^1}{x^1}$")
plt.plot (x21, g(x21), color='purple')
#ВЫВОД ТРЕТЬЕГО
plt.plot (x12, u(x12), color='green', label=r"$\mathcal{F} = \frac{x^2+1^2}{x^2}$")
plt.plot (x22, u(x22), color='green')
#ВЫВОД АСИМПТОТЫ
plt.axvline(p, color='red', linestyle='--', label='Точка разрыва', linewidth=1) #строим асимптоту
plt.xlabel('Ось х')
plt.ylabel('Ось f(x)')
plt.grid(True) #вывод сетки
plt.legend() #вывод легенды
plt.xlim(-7.5,7.5) #задаем диапозон построения x
plt.ylim(-5,5) #задаем диапозон построения y
plt.title('Функции типа (x**b + a**b)/x**b при разных значениях a и b')#название
plt.savefig(dir + '/zadanie9_1', dpi=300)
plt.show() #вывод графика в окно
