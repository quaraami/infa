def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Тестирование функции
n = 5
result = factorial(n)
print(f"{n}! = {result}")