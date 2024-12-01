




















fig = plt.figure()
axes = fig.add_axes([0,0,1,1])
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]
axes.plot(x, y, marker='o', linestyle='-', color='b')

#Добавляем врезку
inset_ax = axes.inset_axes([0.65, 0.15, 0.25, 0.35])  # координаты и размеры врезки (левый нижний угол, ширина, высота)
inset_ax.plot(x, y, marker='o', linestyle='-', color='r')  # данные для врезки могут отличаться от основных

#Устанавливаем границы для врезки
x1, x2, y1, y2 = 2, 4, 20, 45  # область, которую хотим увеличить во врезке
inset_ax.set_xlim(x1, x2)
inset_ax.set_ylim(y1, y2)

# Соединяем основную ось и врезку линией
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
mark_inset(axes, inset_ax, loc1=2, loc2=4, fc="none", ec="0.5")
