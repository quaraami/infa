arr = [[5, 2, 17], [10, 3, 9], [9, 4, 13]]
for i in arr:
   print(' '.join(list(map(str, i))))
s = 0
s1 = 0
s2 = 0
for i in range(3):
    s += arr[0][i]
    s1 += arr[1][i]
    s2 += arr[2][i]
print(max(s, s1, s2))