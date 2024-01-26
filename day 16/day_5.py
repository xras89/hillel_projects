""" Дано натуральне число n.
Надрукуйте всі n-значні непарні натуральні числа в порядку спадання.
Приклад:
ввід: 10
результат: [9, 7, 5, 3, 1]"""


def odd_list_gen(num: int) -> list:
    """The function gets the number and returns a list with odd numbers"""

    finish_list = []
    while num != 0:
        if num % 2 == 1:
            finish_list.append(num)
        num -= 1
    return finish_list
