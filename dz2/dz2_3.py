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
            