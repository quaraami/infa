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


