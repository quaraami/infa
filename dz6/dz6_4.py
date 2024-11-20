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