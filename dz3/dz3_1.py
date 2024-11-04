n=int(input("Введите число:"))
sum=0
if n>100:
    print("Введите число не более ста")
    exit()
for i in range(n):
    n=i+1
    n**=3
    sum +=n
    print(n)
print(f'Сумма кубов последовательности равна {sum}')