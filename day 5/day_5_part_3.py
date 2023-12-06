number = int(input("Please input number: "))
finish_list = []

while number != 0:
    if number % 2 == 1:
        finish_list.append(number)
    number -= 1
print(finish_list)