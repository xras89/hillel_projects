number = input("Enter a number from 3 to 9: ")

if not number.isdigit():
    print("You have entered NOT a number.")
    exit()

number = int(number)

if number < 3 or number > 9:
    print("The number must be from 3 to 9")
    exit()

print()

for i in range(1, number + 1):
    for j in range(1, i + 1):
        print(j, end='')
    for j in range(i - 1, 0, -1):
        print(j, end='')
    print()