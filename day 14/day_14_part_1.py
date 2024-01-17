# Написати функцію сортування двовимірного списку МхМ (матриці) Значення М - задається користувачем з клавіатури. Може бути будь-яким цілим, позитивним числом більше 5.
# Функція повинна:
# 1. знайти суму елементів стовпців і відсортувати стовпці за зростанням цих сум.
# 2. відсортувати кожен непарний стовпець за зростанням значень знизу вгору, а кожен парний стовпець за зростанням значень зверху донизу.
# Також ваша програма повинна мати функцію виведення даного списку
#
# на екрані. При виведенні внизу кожного стовпця повинна виводитися сума елементів цього стовпця.
#
# Що можна використати:
# 1. для створення списку використовувати ТІЛЬКИ 'list comprehension' та
# генератор випадкових чисел. Діапазон випадкових чисел для заповнення списку від 1 до 50. Список має створюватися записом в один рядок.
# 2. Можна використовувати лише два списки. Перший це двомірний список розміром МхМ, другий, допоміжний, одномірний список розміром М. Використання інших списків (або колекцій) НЕДОПУСТИМО.
# 3. Можна використовувати ТІЛЬКИ ОДНУ змінну М для зберігання розміру списку плюс змінні циклів for.
# 4. Для сортування можна використовувати алгоритм бульбашкового сортування. Використання вбудованих функцій сортування – НЕДОПУСТИМО (та й не вийде їх використовувати)!
# 5. Рішення має включати ТІЛЬКИ ДВІ функції: функцію сортування (за правилами описаними вище) та функцію виведення на екран.
# Завдання вважається вирішеним правильно за умови дотримання всіх вимог. Охайне виведення на екран – вітається.

import random


def print_matrix(size_of_matrix):
    def sorting(total, our_matrix):

        for i in range(len(our_matrix[0])):
            for j in range(0, len(our_matrix[0]) - i - 1):
                if total[j] > total[j + 1]:
                    for row in our_matrix:
                        row[j], row[j + 1] = row[j + 1], row[j]
                    total[j], total[j + 1] = total[j + 1], total[j]

        for j in range(len(our_matrix)):
            if (j + 1) % 2 != 0:
                for i in range(len(our_matrix) - 1):
                    for k in range(i, len(our_matrix)):
                        if our_matrix[k][j] > our_matrix[i][j]:
                            our_matrix[k][j], our_matrix[i][j] = our_matrix[i][j], our_matrix[k][j]
            else:
                for i in range(len(our_matrix) - 1):
                    for k in range(i, len(our_matrix)):
                        if our_matrix[k][j] < our_matrix[i][j]:
                            our_matrix[k][j], our_matrix[i][j] = our_matrix[i][j], our_matrix[k][j]

    gen_matrix = [[random.randint(1, 50) for _ in range(size_of_matrix)] for _ in range(size_of_matrix)]
    list_of_sum = [sum(gen_matrix[j][i] for j in range(size_of_matrix)) for i in range(size_of_matrix)]

    print("Unsorted matrix below:")
    for number_list in gen_matrix:
        print(*[f"{num: >4}" for num in number_list])
    print()
    print(*[f"{num: >4}" for num in list_of_sum])

    sorting(list_of_sum, gen_matrix)

    print()
    print("Sorted matrix below:")
    for number_lst in gen_matrix:
        print(*[f"{num: >4}" for num in number_lst])
    print()
    print(*[f"{num: >4}" for num in list_of_sum])


matrix_size = int(input("Please input matrix size (N x N): "))
if type(matrix_size) is int and matrix_size > 5:
    print_matrix(matrix_size)
else:
    print("The number is not an integer or you have entered a number less than or equal to 5")




