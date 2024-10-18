words = "евтух евтуш еблан ананас дыня персик"
count = 0
for word in words.split(" "):
    if word.strip()[0] == 'е':
        count +=1
print(count)