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