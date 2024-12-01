def longest_words(file):
    t=open(file, 'r', encoding='utf-8')
    text = t.read()
    words = text.split()
    maxlen = max(len(word) for word in words)
    longest_words_list = [word for word in words if len(word) == maxlen]
    return longest_words_list

article = 'article.txt'
otvet = longest_words(article)
print(otvet)