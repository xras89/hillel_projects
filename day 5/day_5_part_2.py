matrix = []
n = 5

for i in range(n):
    line = ["", "", "", "", ""]
    matrix.append(line)
for line in matrix:
    print(line)

print()

# Вписати числа в діагональ матриці з ліва на право
for i in range(n):
    matrix[i][i] = 10 + i

for line in matrix:
    print(line)

print()

# Вписати числа в діагональ матриці з право на ліво
for i in range(n):
    matrix[i][n - 1 - i] = 14 - i

for line in matrix:
    print(line)
