# number = int(input("Please enter number: "))
#
# for i in range(1, number + 1):
#     k = i ** 2
#     if k % i == i:
#         print(i,"*", i, "=", i*i)

number = int(input("Please enter the number: "))

for i in range(1, number + 1):
    num_squared = str(i ** 2)
    last_digits = num_squared[-len(str(i)):]

    if str(i) == last_digits:
        print(i, "*", i, "=", i*i)
        