import random

n = int(input("Please input N number (must be > 5): "))
m = int(input("Please input M number (must be > 5): "))

print()

if n > 5 and m > 5:
    matrix = [[random.randint(1, 100) for j in range(n)] for i in range(m)]

    for i in range(m):
        print(*matrix[i], end="\n")

    print()

    for i in range(m):
        matrix[i][-1], matrix[i][-2] = matrix[i][-2], matrix[i][-1]

    for i in range(m):
        print(*matrix[i], end="\n")
else:
    print("The entered value is less than or equal to 5")