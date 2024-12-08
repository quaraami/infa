import pandas as pd

# Создание первых двух DataFrames
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
print(f'Первая база данныx \n {df1}')
print(f'Вторая база данныx \n {df2}')
# Конкатенация DataFrames по вертикали
result_vertical = pd.concat([df1, df2])

print("Результат вертикальной конкатенации:")
print(result_vertical)