def verification(list_of_numbers, sum_of_num):
    """
    The function takes as input parameters: a list of numbers of any length and a number.
    The function checks whether there is a sequence of 2 numbers in the list of sequences whose
    sum is equivalent to the number passed by the 2nd parameter.
    Args:
        list_of_numbers:
        sum_of_num:

    Returns:
    True, if we have sum in list or
    False, if we don't have
    """
    for i in range(len(list_of_numbers)):
        for j in range(i+1, len(list_of_numbers)):
            if list_of_numbers[i] + list_of_numbers[j] == sum_of_num:
                return True
    return False


# True,  4 + 3 = 7
numbers = [1, 2, 3, 4, 5]
target_sum = 7
print(verification(numbers, target_sum))

# False,  != 35
numbers = [11, 15, 25, 2]
target_sum = 35
print(verification(numbers, target_sum))
