import re
t = input()
i=t.lower ()
print(f'новая строчка:{i.replace('н', '!')}, кол-во символов:{len(max(re.findall(r'н+', i)))}')
#{len(max(re.findall(r'н+', text)))}') вывести длинну строки(len)
#из наибольшего (max) вхождения символов н в строку текст re.findall(r'н+', text)
#Н и н - РАЗНЫЕ СИМВОЛЫ