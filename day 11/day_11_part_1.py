import math

hypotenuse_calc = lambda x, y=0: math.sqrt(x ** 2 + y ** 2) if y > 0 else 'y - must be greater than 0, or no data'

# Test print
print(hypotenuse_calc(3, 4))

# Test one list
values = [3, 4, 5]
results = list(map(hypotenuse_calc, values))
print(results)

# Test two lists
x_values = [3, 4, 5]
y_values = [4, 3, 5]
results = list(map(hypotenuse_calc, x_values, y_values))
print(results)
