#1
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

#2
import os

def print_docs(directory):
    for root, dirs, files in os.walk(directory):
        # Выводим путь к текущей директории
        print(f"Directory: {root}")
        
        # Выводим все файлы в этой директории
        if files:
            print("Files:")
            for file in files:
                print(file)
                
        # Выводим все поддиректории (если есть)
        if dirs:
            print("Subdirectories:")
            for subdir in dirs:
                print(subdir)
            
        print("-" *40)

directory = 'C:/Program Files/Google'
print_docs(directory)

#3
def longest_words(file):
    t=open(file, 'r', encoding='utf-8')
    text = t.read()
    words = text.split()
    maxlen = max(len(word) for word in words)
    longest_words_list = [word for word in words if len(word) == maxlen]
    return longest_words_list

article = 'article.txt'
otvet = longest_words(article)
print(otvet)

#4
def redactor():
    import os
    
    # Шаг 1: Предложение ввести имя файла
    filename = input("Введите имя текстового файла: ")
    filename += ".txt"
    
    # Проверка существования файла
    if os.path.exists(filename):
        print(f"Файл с именем '{filename}' уже существует.")
        overwrite = input("Хотите заменить существующий файл? (yes/no): ")
        if overwrite != "yes":
            return
    
    # Шаг 2: Создание/открытие файла для записи
    f = open(filename, 'w', encoding="utf-8") 
    print(f"Файл '{filename}' создан.")
    while True:
            line = input()
            
            # Если введена пустая строка или специальный символ, сохранить файл и выйти
            if not line or line.startswith('@'):
                f.close
                break
            
            # Запись строки в файл с переводом на новую строку
            f.write(line + "\n")
    
    print(f"Файл '{filename}' сохранен.")

if __name__ == "__main__":
    redactor()
