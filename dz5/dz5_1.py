def atan(x, y) :
    return y/x
x1, x2 = map(float,input().split())
y1, y2 = map(float,input().split())
z1, z2 = map(float,input().split())
if x2<0:
    x2=x2*(-1)
if y2<0:
    y2=y2*(-1)
if z2<0:
    z2=z2*(-1)
tg = [x1, x2]
atanx = atan(x1, x2)
atany = atan(y1, y2)
atanz = atan(z1, z2)
if atanx == atany and atanx == atanz and atany == atanz:
    print("Углы равны")
else:
    if atany < atanx :
        atanx = atany
        tg = [y1, y2]
    if atanz < atanx :
        acosz = atanz
        tg = [z1, z2]
    print(f'Координаты точки, для которой угол между осью абсцисс и лучом, соединяющим начало координат с точкой, минимальный {tg}')