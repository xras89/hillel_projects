number = int(input("Please input number: "))

i = 1
while True:
    sqr = i ** 2
    if sqr >= number:
        break

    print(sqr)
    i += 1