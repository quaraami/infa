import pandas as pd
#можно задать индексы буквами
my_series2 = pd.Series([5, 6, 7, 8, 9, 10], index=['a', 'b', 'c', 'd', 'e', 'f'])
print(my_series2["f"])
#Делать выборку по нескольким индексам и осуществлять групповое присваивание
print(my_series2[['a', 'b', 'f']])
my_series2[['a', 'b', 'f']] = 0
print(my_series2)
#Фильтровать Series как душе заблагорассудится, а также применять 
#математические операции и многое другое
print(my_series2[my_series2 > 0])
print(my_series2[my_series2 > 0] * 2)
