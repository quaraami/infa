a=float(input("Введите сумму покупки \n"))
if a<=20:
    print("Скидка не предоставляется")
    print("Стоимость покупки", a, "Размер скидки 0.0")
else:
    print("Вам предоставлена скидка в размере", round((a*0.35),2))
    print("Сумма к оплате", round((a*0.65),2))
