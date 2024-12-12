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
#5

fig, ax = plt.subplots(figsize=(10, 6))
m = df[df['Genre'] == 'Male']
w = df[df['Genre'] == 'Female']
data_m = m.groupby('Annual Income (k$)')['Spending Score (1-100)'].mean()
data_w = w.groupby('Annual Income (k$)')['Spending Score (1-100)'].mean()

data_m.plot.bar(color='#00FFFF')
data_w.plot.bar(color='#DC143C')
plt.show()