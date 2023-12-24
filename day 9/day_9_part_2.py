import random

random_dict = {i: random.randint(1, 10) for i in range(20)}

count = 1
for value in random_dict.values():
    count *= value

print(random_dict)
print(f"Multiplication result: {count}")