import pandas as pd
import numpy as np
list = list('abcdefghik')
massiv = np.arange(10)
dict = ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine']
 
s1 = pd.Series(list)
s2 = pd.Series(massiv)
s3 = pd.Series(dict)
 
print(s1)
print(s2)
print(s3)