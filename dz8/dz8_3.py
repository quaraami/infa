import re
letter = 'Уважаемые! Если вы к 09:00 не вернёте чемодан, то уже в 09:00:01 я за себя не отвечаю.'
zamena= r'((?:[01]\d|2[0-3])\:(?:[0-5]\d)(?:\:[0-5]\d)?)'
result = re.sub(zamena, "(TBD)", letter)
print(result)
