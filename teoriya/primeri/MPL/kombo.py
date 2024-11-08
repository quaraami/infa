import numpy as np # вводим mathplotlib
x = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май']
y = [2, 4, 3, 1, 7]
from matplotlib import pyplot as plt
plt.bar(x, y, label='Величина прибыли', alpha=0.5, linewidth=7) #Параметр label позволяет задать название величины для легенды
plt.plot(x, y, color='green', marker='o', markersize=7)
plt.xlabel('Месяц года')
plt.ylabel('Прибыль, в млн руб.')
plt.title('Комбинирование графиков')
plt.legend()
plt.show()

#Параметр alpha может принимать значения от 0 до 1, где 0 — полная прозрачность, а 1 — отсутствие прозрачности.
#Теперь линейный график хорошо виден и мы можем оценивать динамику изменения прибыли.