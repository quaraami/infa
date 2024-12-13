#1
arr = [[1, 2, 3], [5, 4, 6], [2, 12, 8]]
brr = list() #создаем пустой список
for i in range(3): #задаем цикл
    brr.append(arr[i][2]) #в пустой список загоняем значения из 3 столбца
print(brr) #печатаем эту строку
print(max(brr)) #печатаем максимальное значение из 3 столбца
print(max(arr[1])) #печатаем максимально значение из 2 строки

#2
arr = [[1, -2, 3], [-5, 4, -6], [2, 12, 8], [6, -9, 10]]
print("Исходный массив:")
for i in arr:
   print(' '.join(list(map(str, i))))
for i in range(len(arr)):
  for j in range(len(arr[i])):
    if arr[i][j] > 0:
      arr[i][j] = 1
    else:
      arr[i][j] = 0
print("Полученный массив:")
for i in arr:
  print(' '.join(list(map(str, i))))

#3
arr = [[5, 12, 7], [10, 8, 6], [9, 4, 11]]
for i in arr:
   print(' '.join(list(map(str, i))))
s = 0
s1 = 0
s2 = 0
c = 0
c1 = 0
c2 = 0
for i in range(3):
    s += arr[0][i]
    s1 += arr[1][i]
    s2 += arr[2][i]
    c += arr[i][0]
    c1 += arr[i][1]
    c2 += arr[i][2]
if s == s1 == s2 == c == c1 ==c2:
    print("Это магический квадрат!")
else:
    print("Это не магический квадрат(")

#4
n = int(input())
arr = list()
flag= True
for i in range(n):
  brr = list()
  for i in range(n):
    brr.append(int(input()))
  arr.append(brr) #заполняю матрицу
for i in arr:
   print(' '.join(list(map(str, i)))) #вывожу матрицу
for k in range(n):
    for l in range(k):
        if arr[k][l] != arr[l][k]: #сравниваю значения с 
            #зеркальными координатами и если они не равны
            flag=False #опускаю флаг
            break #завершаю работу модуля
        print(arr[k][l], arr[l][k], flag)
if flag != False: #если флаг поднят, матрица симметрична
    print('Матрица симметрична')
else: #если опущен матрица не симметрична
    print('Матрица не симметрична')

#5
arr = [[5, 2, 17], [10, 3, 9], [9, 4, 13], [4,5,9]]
for i in arr:
   print(' '.join(list(map(str, i)))) 
s = 0
s1 = 0
s2 = 0
s3 = 0
for i in range(3):
    s += arr[0][i]
    s1 += arr[1][i]
    s2 += arr[2][i]
    s3 += arr[3][i]
print(max(s, s1, s2, s3))

#6
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