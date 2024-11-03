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