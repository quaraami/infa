#n = int(input()) #количество строк
#m = int(input()) #количество столбцов
#arr = list()
#for i in range(n):
  #brr = list()
  #for i in range(m):
    #brr.append(float(input()))
  #arr.append(brr) #заполняю матрицу
#for i in arr:
   #print(' '.join(list(map(str, i))))
n=4
arr = [[5,2,17],
        [10,3,9], 
        [9,4,13], 
        [4,5,9]]
for i in range(n):
     print(arr[i].index(min(arr[i])))
     print(f'в строке {i}')
     print(f'минимальное значение в {i} строке {min(arr[i])}')
    


