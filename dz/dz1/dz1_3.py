import math
L = float(input("Введите длинну маятника в метрах: "))
T=(round(2*math.pi*math.sqrt(L/9.81),2)) #вычисляем период
print (T)#вывод результата
#print(str(round(2*math.pi*math.sqrt(L/9.81),2)))
