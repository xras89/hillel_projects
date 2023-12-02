n = 1
list = []
while n != 0:
    n = int(input("Please input the number: "))
    if n != 0:
        list.append(n)

print("")

sum_list = sum(list)
print("Sum of numbers", sum_list)
len_list = len(list)
avg_number = sum_list/len_list
print("Arithmetic average", avg_number)
max_number = max(list)
print("Maximum number", max_number)
min_number = min(list)
print("Maximum number", min_number)

even = 0
odd = 0

for i in list:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers in total:", even)
print("Odd numbers in total:", odd)
