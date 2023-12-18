# number = int(input("Please enter the number: "))
#
# for i in range(1, number + 1):
#     num_squared = str(i ** 2)
#     last_digits = num_squared[-len(str(i)):]
#
#     if str(i) == last_digits:
#         print(i, "*", i, "=", i*i)

n = int(input("Ввести число N: "))

number = 1

while number <= n:
    square = number ** 2
    divisor = 1

    while divisor <= number:
        divisor *= 10

    last_number = square % divisor

    if last_number == number:
        print(number, "*", number, "=", square)
    number += 1