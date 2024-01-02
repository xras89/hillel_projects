import random


def prime_generator(n, z):
    for i in range(n, z + 1):
        if i > 1:
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    break
            else:
                yield i


n = random.randint(1, 100)
z = random.randint(101, 200)

print("Prime numbers between", n, "and", z, "-->", *prime_generator(n, z), sep=' ')
