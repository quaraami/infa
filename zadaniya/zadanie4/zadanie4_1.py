stroka = "егерь стол парта пенал телефон ель евтух адреналин эквалайзер"
count = 0
for i in stroka.split(" "):
    if i.strip()[0] == 'е':
        count +=1
print(count)