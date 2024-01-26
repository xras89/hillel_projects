"""
Створити файл в якому підключаєте кожен з створених модулей
і продемонструвати виклик функцій/класів."""

from day_5 import odd_list_gen
from day_16 import special_summ

print("First function example:")
number = int(input("Please input any number: "))
print(f"Result of first function: {odd_list_gen(number)}")

print()

print("Second function example:")
value = special_summ()
print(f"Result of second function:: {value}")
