prices = {
    "яблоко": 50,
    "банан": 30,
    "апельсин": 70,
    "груша": 100
}

product = input("Введите название товара: ")


if product in prices:
    print(f"Цена на {product}: {prices[product]} руб.")
else:
    print("Такого товара нет в списке.")