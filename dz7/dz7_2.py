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