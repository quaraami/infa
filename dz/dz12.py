import pandas as pd
import matplotlib.pyplot as plt

file = 'Mall_Customers.csv'
df = pd.read_csv(file, sep=',')

#2 задание
women = df.query("Genre == 'Female'")
average_income_of_women = women['Annual Income (k$)'].mean()
print(f"Средняя доходность женщин: {average_income_of_women}")

#3 задание
data = df.groupby('Genre')['Annual Income (k$)'].idxmax()
result3 = df.loc[data, ['Genre', 'CustomerID', 'Annual Income (k$)']]
print(result3)

#4 задание
men = df.query("Genre == 'Male'")

plt.figure(figsize=(10, 6))
plt.scatter(men['Age'], men['Annual Income (k$)'], color = '#006400')
plt.xlabel('Возраст')
plt.ylabel('Доход')
plt.title('Зависимость доходов от возраста для мужчин')
plt.grid(True)
plt.show()