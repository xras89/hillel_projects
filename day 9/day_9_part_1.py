dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}

dictionary_3 = {**dictionary_1, **dictionary_2}

# Еще один вариант
dictionary_4 = dict(dictionary_1, **dictionary_2)

# и еще один
dictionary_1.update(dictionary_2)

print(dictionary_3)
print(dictionary_4)
print(dictionary_1)
