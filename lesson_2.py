#Zadanie
#1
a= float(input())
b= float(input())
c= float(input())
if float.is_integer(a) and float.is_integer(b) and float.is_integer(c): #проверка на целостность
    if a < b and a < c:
        print("Наименьшее число", a)
    else:
        if b < c:
            print("Наименьшее число",b)
        else:
            print("Наименьшее число",c)
    
else:
    print("Ошибка, вводи целые!")

#HomeWork
#1
a = float(input("Введите делимое"))
b = float(input("Введите делитель"))
if b==0: #проверка условия что делитель не равен нулю
    print("На ноль делить нельзя!") #вывод если делитель равен нулю
else:
    print(a/b) #вывод если делитель не равен нулю

#2
a=float(input("Введите сумму покупки \n"))
if a<=20:
    print("Скидка не предоставляется")
    print("Стоимость покупки", a, "Размер скидки 0.0")
else:
    print("Вам предоставлена скидка в размере", round((a*0.35),2))
    print("Сумма к оплате", round((a*0.65),2))

#3
a=float(input("Введите номер месяца \n"))
if a<1 or a>12 or not float.is_integer(a): #Проверка на правильность ввода
    print("Введите номер месяца в правильном формате")
    exit()
else:
    if a==1 or a==2 or a==12:
        print("Зима")
    else:
        if a<=5 and a>=3:
            print("Весна")
        else:
            if a<=8 and a>=6:
                print("Лето")
            else:
                print("Осень")
b=int(a)
months=["январь", "ферваль","март","апрель","май","июнь","июль","август","сентябрь","октябрь","ноябрь","декабрь"]
print(months[b-1])
            
