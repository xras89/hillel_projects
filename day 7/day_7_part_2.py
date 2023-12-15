number = int(input("Please input number: "))

for i in range(number+1):
    a = str(i)
    b = str(10**i)
    # print("{:>2} {:>16}".format(a, b))
    print(a.rjust(len(str(number))), (b.rjust(number + 1)))
