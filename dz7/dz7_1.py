def read_last(lines, file): #создаем функцию 
    #которая печатает файл и выводит построчно последние строки
    if lines > 0: #проверка числа на "знак"
        f = open(file, encoding='utf-8') #открываем файл
        file_lines = f.readlines()[-lines:]
        for line in file_lines:
            print(line.strip())
    else:
        print('Введите целое положительное число')

def proverka(T,F): #функция чтобы проверить,
    #не больше ли запрашиваемых строк, чем исходных
    if T > F:
        print("Количество запрашиваемых строк превышает количество существующих в файле")
        exit()


n = int(input()) #вводим количество запрашиваемых строк
count = 0
f = open("article.txt", encoding='utf-8')
for line in f:
    count += 1
f.close
proverka(n,count)
read_last(n, "article.txt")

