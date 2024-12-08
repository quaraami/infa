import pandas as pd

# Создание первых двух DataFrames
df1 = pd.DataFrame({'A': [6, 4], 'B': [6, 4]})
df2 = pd.DataFrame({'A': [6, 4], 'B': [6, 4]})
print(f'Первая база данныx \n {df1}')
print(f'Вторая база данныx \n {df2}')
# Конкатенация DataFrames по вертикали
result_vertical = pd.concat([df1, df2])

print("Результат вертикальной конкатенации:")
print(result_vertical)
result_horizontal_merge = pd.merge(df1, df2, on =['A', 'B']) #из df1 и df2 выбирает совпадающие
#значения по столбцам А и В
print("Результат горизонтальной конкатенации:")
print(result_horizontal_merge)
