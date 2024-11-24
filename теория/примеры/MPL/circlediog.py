import numpy as np # вводим mathplotlib
vals = [24, 17, 53, 21, 35]
labels = ["Ford", "Toyota", "BMW", "Audi", "Jaguar"]
from matplotlib import pyplot as plt
plt.pie(vals, labels=labels, shadow=False, autopct='%1.1f%%')
plt.title("Распределение марок автомобилей на дороге")
plt.show()