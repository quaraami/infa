import pandas as pd
import matplotlib.pyplot as plt

dt = {
    'x': [1, 2, 3, 4, 5],
    'y1': [1, 4, 9, 16, 25],
    'y2': [15, 5, 35, 25, 55]
}
df = pd.DataFrame(dt)

# Построение графика
plt.figure(figsize=(8, 6))  # Устанавливаем размер фигуры
plt.plot(df['x'], df['y1'], label='y1')  # Первый график
plt.plot(df['x'], df['y2'], label='y2')  # Второй график
plt.legend()  # Легенда
plt.xlabel('x')
plt.ylabel('y1 and y2')
plt.title('Зависимости y1 и y2 от x')
plt.grid()  # Включаем сетку для удобства чтения графика
plt.show()