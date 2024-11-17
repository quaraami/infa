def atan(x, y) :
    return y/x
x1, x2 = map(float,input().split())
y1, y2 = map(float,input().split())
z1, z2 = map(float,input().split())
dx1=0
dy1=0
dz1=0
dx2=0
dy2=0
dz2=0
if x2<0:
    dx2=x2
    x2=x2*(-1)
if y2<0:
    dy2=y2
    y2=y2*(-1)
if z2<0:
    dz2=z2
    z2=z2*(-1)
if x1<0:
    dx1=x1
    x1=x1*(-1)
if y1<0:
    dy1=y1
    y1=y1*(-1)
if z1<0:
    dz1=z1
    z1=z1*(-1)
tg = [x1, x2]
atanx = atan(x1, x2)
atany = atan(y1, y2)
atanz = atan(z1, z2)
if atanx == atany and atanx == atanz and atany == atanz:
    print("Углы равны")
else:
    if dx1!=0:
        x1=x1*(-1)
    if dy1!=0:
        y1=y1*(-1)
    if dz1!=0:
        z1=z1*(-1)
    if dx2!=0:
        x2=x2*(-1)
    if dy2!=0:
        y2=y2*(-1)
    if dz2!=0:
        z2=z2*(-1)
    if atany < atanx :
        tg = [y1, y2]
    if atanz < atanx :
        tg = [z1, z2]
    if atany < atanz :
        tg = [y1, y2]
    print(f'Координаты точки, для которой угол между осью абсцисс и лучом, соединяющим начало координат с точкой, минимальный {tg}')