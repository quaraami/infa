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
