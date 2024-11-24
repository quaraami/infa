import numpy as np # вводим mathplotlib
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #задаем координаты x
y = [25, 32, 34, 20, 25, 23, 21, 33, 19, 28] #задаем координаты y
from matplotlib import pyplot as plt
plt.scatter(x, y, color='black', edgecolors='deeppink', linewidth=2)
plt.xlim(-10, 10) #задаем предел значений x
plt.ylim(0, 100) #задаем предел значений y
plt.show()