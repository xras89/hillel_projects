import random


def list_generator(x=3, y=3):
    """
    The function takes 2 parameters and generates a two-dimensional list
    filled with random integer values in the range 0 - 200.
    Args:
        x: number of lists in the main list
        y: length of items in the list

    Returns:
        The function returns the generated two-dimensional list
    """
    gen_list = [[random.randint(0, 200) for _ in range(x)] for _ in range(y)]
    return gen_list


def two_dimensional_list(list_name):
    """
    The function expects one required parameter, and it must be a two-dimensional symmetric list.
    It receives the list and prints a symmetric list in console.
    Args:
        list_name: There must be a two-dimensional symmetric list

    Returns:
        Prints a symmetric list in console
    """
    if len(list_name) == len(list_name[0]):
        for row in list_name:
            print(*[f"{num:<4}" for num in row])
    else:
        print("It's an asymmetric matrix")


# when the first function does not receive parameters
two_dimensional_list(list_generator())

print()

# when the first function receives 1 parameter
two_dimensional_list(list_generator(7))

print()

# when the first function receives 2 parameters
two_dimensional_list(list_generator(5, 5))
