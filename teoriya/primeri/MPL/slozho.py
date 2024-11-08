import numpy as np # вводим mathplotlib
labels = ['2017', '2018', '2019', '2020', '2021']
android_users = [85, 85.1, 86, 86.2, 86]
ios_users = [14.5, 14.8, 13, 13.8, 14.0]
from matplotlib import pyplot as plt
width = 0.35       #Задаём ширину столбцов
fig, ax = plt.subplots()

ax.bar(labels, android_users, width, label='Android', color='deeppink')
ax.bar(labels, ios_users, width, bottom=android_users,
      label='iOS', color='red') #Указываем с помощью параметра bottom, что значения в столбце должны быть выше значений переменной android_users

ax.set_ylabel('Соотношение, в %')
ax.set_title('Распределение устройств на Android и iOS')
ax.legend(loc='lower right', title='Устройства') #Сдвигаем легенду в нижний левый угол, чтобы она не перекрывала часть графика

plt.show()