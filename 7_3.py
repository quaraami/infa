def check_data_type(user_input):
    if isinstance(user_input, int) or isinstance(user_input, float):
        print("Это число.")
    elif isinstance(user_input, str):
        print("Это строка.")
    else:
        print("Это что-то другое.")

# Запрашиваем ввод у пользователя
user_input = input("Пожалуйста, введите данные: ")