import random
import time

random_list = [random.randint(-10000, 10000) for _ in range(100000)]

# Функция простого перебора для нахождения максимального числа
def find_max_brute_force(lst):
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

# Использование встроенной функции max()
def find_max_builtin(lst):
    return max(lst)

start_time = time.time()
max_number_brute_force = find_max_brute_force(random_list)
end_time = time.time()
brute_force_time = end_time - start_time

start_time = time.time()
max_number_builtin = find_max_builtin(random_list)
end_time = time.time()
builtin_time = end_time - start_time

print(f'Максимальное число, найденное простым перебором: {max_number_brute_force}')
print(f'Максимальное число, найденное встроенной функцией: {max_number_builtin}')
print(f'\nВремя выполнения простого перебора: {brute_force_time:.10f} секунд')
print(f'Время выполнения встроенной функции: {builtin_time:.10f} секунд')