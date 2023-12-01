number = input("Please input number: ")

our_number_list = []

for i in number:
    if i in our_number_list:
        print("Yes")
        break
    our_number_list.append(i)
else:
    print("No")