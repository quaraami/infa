a=float(input("Введите номер месяца \n"))
if a<1 or a>12 or not float.is_integer(a): #Проверка на правильность ввода
    print("Введите номер месяца в правильном формате")
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
            