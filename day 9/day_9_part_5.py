string = 'Python is good language to learn and in same time we like to tell that it is cool expereance for us'

char_counts = {}

for char in string:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1

print(char_counts)