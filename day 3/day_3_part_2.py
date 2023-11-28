import math

value = float(input ("Please enter value: "))

# Обчислення значень функцій
y1 = value * value
y2 = math.sin(value)
y3 = math.exp(value)

# Знаходження мінімуму
y_min = y1
if y2 < y_min:
    y_min = y2
if y3 < y_min:
    y_min = y3

# Знаходження максимуму
y_max = y1
if y2 > y_max:
    y_max = y2
if y3 > y_max:
    y_max = y3

print("The minimum value:", y_min)
print("The maximum value:", y_max)

