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