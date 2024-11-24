import pandas as pd
#Если Series напоминает нам словарь, где ключом является индекс,
# а значением сам элемент, то можно сделать так
my_series3 = pd.Series({'a': 5, 'b': 6, 'c': 7, 'd': 8})
print(my_series3)
print('d' in my_series3)
#У объекта Series и его индекса есть атрибут name,
#задающий имя объекту и индексу соответственно.
my_series3.name = 'numbers'
my_series3.index.name = 'letters'
print(my_series3)
#Индекс можно поменять "на лету", присвоив список атрибуту index объекта Series
my_series3.index = ['A', 'B', 'C', 'D']
print(my_series3)
