import re
nomera='А123ВС178 О456СН52 КВ99951 ЕУ777666'
print('Список номеров частных автомобилей:', re.findall(r'\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}\b', nomera))
print('Список номеров такси', re.findall(r'\b[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}\b', nomera)) 