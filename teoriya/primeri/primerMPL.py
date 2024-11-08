import numpy as np # вводим mathplotlib
x = np.array([1, 2, 3, 4, 5]) #координаты по x
y = np.array([25, 32, 34, 20, 25]) #координаты по y
from matplotlib import pyplot as plt
plt.plot(x, y) #вводим оси x,y
plt.xlabel('Ось х') #Подпись для оси х
plt.ylabel('Ось y') #Подпись для оси y
plt.xlim(-10, 10) #задаем предел значений x
plt.title('Первый график') #Название
plt.plot(x, y, color='red', marker='+', markersize=15) #С помощью Matplotlib
#можно настроить отображение любого графика. Например, мы можем изменить цвет
#линии, а также выделить точки, координаты которых задаём в переменных
plt.show()