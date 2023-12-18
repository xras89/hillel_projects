import random

list_of_numbers = [random.randint(1, 100) for i in range(15)]
print(list_of_numbers)

odd = sum([i for i in list_of_numbers if i % 2 == 1])
even = sum([i for i in list_of_numbers if i % 2 == 0])

if odd > even:
    print("YES - the sum of odd numbers is larger!")
else:
    print("NO - the sum of even numbers is larger!")

print("Odd is", odd)
print("Even is", even)



