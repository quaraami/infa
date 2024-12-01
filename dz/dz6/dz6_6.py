n = int(input("Введите количество строк:")) #количество строк
m = int(input("Введите количество столбцов:")) #количество столбцов
arr = list()
for i in range(n):
  brr = list()
  for i in range(m):
    brr.append(int(input()))
  arr.append(brr) #заполняю матрицу
print("Исходная матрица:")
for i in arr:
   print(' '.join(list(map(str, i)))) #вывожу матрицу
for i in range(n):
    h = arr[i].index(min(arr[i])) #задаю переменную которая при каждом 
    #цикле меняется на индекс минимального числа в каждой строчке
    for j in range(m):
      if arr[i][h] % 2 == 0: #проверяю это число на четность
            arr[i][h] = 0 
      else:
          arr[i][h] = 1
print("Новая матрица:")
for i in arr:
   print(' '.join(list(map(str, i)))) #вывожу новую матрицу


