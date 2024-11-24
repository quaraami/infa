def read_last(lines, file):
    if lines > 0:
        f = open(file, encoding='utf-8')
        file_lines = f.readlines()[-lines:]
        for line in file_lines:
            print(line.strip())
    else:
        print('Введите целое положительное число')

def proverka(T,F):
    if T > F:
        print("Количество запрашиваемых строк превышает количество существующих в файле")
        exit()


n = int(input())
count = 0
f = open("article.txt", encoding='utf-8')
for line in f:
    count += 1
f.close
proverka(n,count)
read_last(n, "article.txt")

