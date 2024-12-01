import re
text = input()
print(len(re.findall(r"\b[a-zа-я][a-zа-я-]*\b", text)))