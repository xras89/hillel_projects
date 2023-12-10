import random

n = int(input("Please input number: "))

if n > 0:
    matrix = [[random.randint(10, 99) for _ in range(n)] for _ in range(n)]

    for i in range(n):
        print(*matrix[i], end="\n")

    print()

    sum_1 = sum(matrix[_][_] for _ in range(n))
    print(sum_1, " - Sum \ left(top) to right(down)")

    sum_2 = sum(matrix[_][n - 1 - _] for _ in range(n))
    print(sum_2, " - Sum / right(top) to left(down)")

    center_value = matrix[n // 2][n // 2]
    print(center_value, " - matrix central value")

else:
    print("Wrong input number")
