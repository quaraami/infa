#Zadanie
#1
stroka = "егерь стол парта пенал телефон ель евтух адреналин эквалайзер"
count = 0
for i in stroka.split(" "):
    if i.strip()[0] == 'е':
        count +=1
print(count)

#2
string = "Привет: мир: сегодня: я:учу:Python:"
new_string=string.replace(':','%')
j = 0
for i in string:
    if i == ':':
        j+=1
print(f"Новая строка: {new_string}")
print(f"Количество замен: {j}")

#HomeWork
#1
import re
t = input()
i=t.lower ()
print(f'новая строчка:{i.replace('н', '!')}, кол-во символов:{len(max(re.findall(r'н+', i)))}')
#{len(max(re.findall(r'н+', text)))}') вывести длинну строки(len)
#из наибольшего (max) вхождения символов н в строку текст re.findall(r'н+', text)
#Н и н - РАЗНЫЕ СИМВОЛЫ

#2
t = input()
f = t[t.find('(')+1:t.find(')')] #выбираем интервал от "(" до ")"
print(f)

#3
str = "амортизация абстракция алапеция аллегория анафора фара корректор коллектор грунт почва" 
 
for i in str.split():
    if(i.startswith("а") and i.endswith("я")):
        print(i)