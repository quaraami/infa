import numpy as np
import os
from matplotlib import pyplot as plt
p=0 
#ПАРАМЕТРЫ ДЛЯ ПЕРВОГО
x1 = np.linspace(-25, p - 0.01, 500)
a=1
b=1 
y1=(x1**b + a**b)/x1**b
#ПАРАМЕТРЫ ДЛЯ ВТОРОГО
x2 = np.linspace(-25, p - 0.01, 500)
d=2
h=1
y2=(x2**h + d**h)/x2**h
#ПАРАМЕТРЫ ДЛЯ ТРЕТЬЕГО
x3 = np.linspace(-25, p - 0.01, 500)
c=1
v=2
y3=(x3**v + c**v)/x3**v

dir = os.getcwd()
fig = plt.figure()
#ВЫВОД АСИМПТОТЫ И ТРЕХ ГРАФИКОВ
plt.axhline(y=0, color='black',linewidth=1)
plt.plot (x1, y1, color='blue', label=r"$\mathcal{F} = \frac{x^1+1^1}{x^1}$")
plt.plot (x2, y2, color='purple', label=r"$\mathcal{F} = \frac{x^1+2^1}{x^1}$")
plt.plot (x3, y3, color='green', label=r"$\mathcal{F} = \frac{x^2+1^2}{x^2}$")
plt.axvline(p, color='red', linestyle='--', label='Точка разрыва', linewidth=1)
plt.xlabel('Ось х') #название x
plt.ylabel('Ось f(x)') #название y
plt.grid(True) #вывод сетки
plt.legend() #вывод легенды
plt.xlim(-12,0.5) #задаем диапозон построения x
plt.ylim(-15,15) #задаем диапозон построения y
plt.title('Функции типа (x**b + a**b)/x**b при разных значениях a и b')#название

#создание врезки
axes2 = fig.add_axes([0.18,0.16,0.25,0.25]) #расположение врезки и её размер
axes2.plot(x1, y1, 'b', x2, y2, 'purple', x3, y3, 'green') #добавляем графики на врезку
plt.xlim(-8,0) #задаем диапозон построения x
plt.ylim(-3,2) #задаем диапозон построения y
plt.grid(True) #вывод сетки
plt.savefig(dir + '/zadanie9_3', dpi=300)
plt.show() #вывод графика в окно

