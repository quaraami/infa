string = "Привет: мир: сегодня"
new_string=string.replace(':','%')
j = 0
for i in string:
    if i == ':':
        j+=1
print(f"Новая строка: {new_string}")
print(f"Количество замен: {j}")