start = 1  # Начало диапазона
end = 20  # Конец диапазона
sum_even = 0
for i in range(1, 21):
    if i % 2 == 0:
        # Добавляем число к сумме
        sum_even += i
print(f"Сумма чётных чисел от {start} до {end}: {sum_even}")
