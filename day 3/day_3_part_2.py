import math

value = int(input ("Please enter value: "))

def solution(x):
    # YOUR CODE HERE
    y1 = x * x
    y2 = math.sin(x)
    y3 = math.exp(x)

    min_v = min(y1, y2, y3)
    max_v = max(y1, y2, y3)

    # min_v = y1
    # if y2 < min_v:
    #     min_v = y2
    # if y3 < min_v:
    #     min_v = y3
    #
    # max_v = y1
    # if y2 > max_v:
    #     max_v = y2
    # if y3 > max_v:
    #     max_v = y3

    return min_v, max_v


# # Обчислення значень функцій
# y1 = value * value
# y2 = math.sin(value)
# y3 = math.exp(value)
#
# # Знаходження мінімуму
# y_min = y1
# if y2 < y_min:
#     y_min = y2
# if y3 < y_min:
#     y_min = y3
#
# # Знаходження максимуму
# y_max = y1
# if y2 > y_max:
#     y_max = y2
# if y3 > y_max:
#     y_max = y3

y_min, y_max = solution(value)

print("The minimum value:", y_min)
print("The maximum value:", y_max)

