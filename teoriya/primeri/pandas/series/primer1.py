import pandas as pd
my_series = pd.Series([5.9, 6, 7, 8, 9, 10, "f"])
print(my_series) #выводит весь список
print(my_series.index) #выводит Range для индексов
print(my_series.values) #выводит значение в квадратных скобках
print(my_series[4]) #выводит определённое значение