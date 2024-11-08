t = input()
f = t[t.find('(')+1:t.find(')')] #выбираем интервал от "(" до ")"
print(f)