#определяем простые числа от 0 до N
n = int(input())
lst = []
for i in range(2, n):
    for j in range(2, i):
        if i % j == 0:
            # если делитель найден, число не простое.
            break
    else:
        lst.append(i) #набираем в строку lst простые числа
print(lst)
for i in range(len(lst)):
    s=format(lst[i], "b") #задаем переменную s равную lst[i] в двоичной системе записи
    flag = True
    string  = '' #задаем пустую строку
    for i in range (len(s)): #задаем цикл длинной s
        if s[i]!= ' ': #задаем условие что пока s[i] не пустое 
            string +=s[i] #добавляем символы в пустую string
    for i in range(len(s)//2): #задаем цикл, длинна которого равна половине длинны s
        if string[i] != string[-1-i]: #задаем условие которое сравнивает символы по порядку 
            #с начала и с конца строки и если они не равны
            flag = False #опускаем флаг
            break #прекращаем работу данного модуля
    print(s) if flag else None #выводим строку s если она палиндром (флаг поднят)
    #если флаг опущен то "ничего"
            
