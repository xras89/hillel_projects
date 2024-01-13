def longest_words(file):
    with open(file, 'r', encoding='cp1251') as f:
        content = f.read()

    words = content.split()
    max_length = max(len(word) for word in words)
    longest_words_list = [word for word in words if len(word) == max_length]

    return longest_words_list


result = longest_words('article.txt')
print(result)
