import re
text = 'Инициальные аббревиатуры пишутся прописными буквами: ООН, МИД, РФ. Точки или пробелы между буквами не ставятся, но между двумя самостоятельно употребляющимися аббревиатурами используется пробел: ИРЯ РАН, МИД РФ.'
print("Найденные аббревиатуры:", re.findall(r'[А-Я]{2,}(?:\s+[А-Я]{2,})*', text))