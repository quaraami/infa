import pandas as pd
import numpy as np
s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([5, 6, 7, 8, 9])

s3 = pd.Series(np.union1d(s1, s2)) # получаем объединенный Series без повтороений
s4 = pd.Series(np.intersect1d(s1, s2)) # получаем пересекающиеся данные
s5 = s3[~s3.isin(s4)] # отбираем все данные, кроме пересекающихся
print(s5)