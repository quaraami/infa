import math

# Функция для вычисления площади треугольника по формуле Герона
def triangle_area(x, y, z):
    p = (x + y + z) / 2
    return round(math.sqrt(p * (p - x) * (p - y) * (p - z)),2)

# Проверка существования треугольника
def is_valid_triangle(x, y, z):
    return x + y > z and x + z > y and y + z > x

# Функция для ввода сторон треугольника через пробел и проверки их корректности
def get_triangle_sides():
    while True:
        try:
            # Ввод трёх сторон через пробел
            sides = list(map(float, input('Введите стороны треугольника через пробел (a b c): ').split()))
            if len(sides) != 3:
                print('Ошибка: нужно ввести три стороны.')
                continue
            a, b, c = sides
            if is_valid_triangle(a, b, c):
                return a, b, c
            else:
                print('Ошибка: стороны не образуют треугольник. Попробуйте снова.')
        except ValueError:
            print('Ошибка: введите корректные числа.')

# Список для хранения площадей треугольников
areas = []

# Ввод сторон трёх треугольников
for i in range(1, 4):
    print(f'Введите стороны {i}-го треугольника: ')
    a, b, c = get_triangle_sides()
    areas.append(triangle_area(a, b, c))

# Вывод площадей треугольников
for i in range(3):
    print(f'Площадь {i + 1}-го треугольника: {areas[i]}')

# Проверка, равны ли площади всех трёх треугольников
if areas[0] == areas[1] == areas[2]:
    print('Треугольники равновеликие')
else:
    print('Треугольники не равновеликие')