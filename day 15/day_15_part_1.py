#  Миколі потрібно перевірити, чи можливо із представлених відрізків умовної довжини сформувати трикутник.

# Для цього він вирішив створити клас TriangleChecker, який приймає лише позитивні числа.
# За допомогою методу is_triangle() повертаються такі значення (залежно від ситуації):
# (Потрібно згадати правило для трикутника та довжин його сторін)
# - Ура, можна побудувати трикутник!;
# - З негативними числами нічого не вийде!;
# - Потрібно вводити тільки числа!;
# – Жаль, але з цього трикутник не зробити.

# Створіть для Миколи класи  TriangleChecker, Triangle та класс ExtTriangle який від перших двух класів успадковує властивості
# - для перевірки створити обєкти трикутника з класу ExtTriangle та викликати метод is_triangle()  таким чином  щоб продемонструвати усі 4 можливі відповіді

# Triangle - відповідає за отримання значень сторін трикутника при створенні об'єкта.

class Triangle():
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c


class TriangleChecker():
    def is_triangle(self):
        if type(self.side_a) is int and type(self.side_b) is int and type(self.side_c) is int:
            if self.side_a > 0 and self.side_b > 0 and self.side_c > 0:
                if not (self.side_a + self.side_b > self.side_c and
                        self.side_a + self.side_c > self.side_b and
                        self.side_b + self.side_c > self.side_a):
                    return f"You can't create a triangle using these sides! ({self.side_a},{self.side_b},{self.side_c})"
                else:
                    return f"Wow, you can build a triangle! ({self.side_a},{self.side_b},{self.side_c})"
            else:
                return f"Nothing will work with negative numbers! ({self.side_a},{self.side_b},{self.side_c})"
        else:
            return f"You need to enter only numbers! ({self.side_a},{self.side_b},{self.side_c})"


class ExtTriangle(Triangle, TriangleChecker):
    pass


# Test #1
test_1 = ExtTriangle(4, 2, 3)
print(test_1.is_triangle())
# Test #2
test_2 = ExtTriangle(4, 4, 9)
print(test_2.is_triangle())
# Test #3
test_3 = ExtTriangle(2, 8, -2)
print(test_3.is_triangle())
# Test #4
test_4 = ExtTriangle(3, 5, "-")
print(test_4.is_triangle())
