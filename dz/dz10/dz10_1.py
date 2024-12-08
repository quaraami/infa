import pandas as pd
list = list('abcdefghik')
massiv = [0, 1, 2, 3, 4, 5, 6, 7, 8]
dict = ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine']
 
s1 = pd.Series(list)
s2 = pd.Series(massiv)
s3 = pd.Series(dict)
 
print(s1)
print(s2)
print(s3)