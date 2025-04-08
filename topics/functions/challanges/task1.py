"""
Task 1
Refactor code by using functions instead of direct math operators.

Notes:
*Refactoring - the process of restructuring existing source without changing its external behavior.
**Рефикторинг - процесс реструктуризации существующего исходного кода без изменения его внешнего поведения.
https://en.wikipedia.org/wiki/Code_refactoring

Hint:
def plus(first_number: int, second_number: int) -> int:
    ...
"""

result = 0


while True:
    first_number = input("Write the first number:")
    if first_number == "q":
        break
    operation = input("Write an operation:")
    second_number = input("Write the second number:")
    if operation == "+":
        result = float(first_number) + float(second_number)

    elif operation == "-":
        result = float(first_number) - float(second_number)

    elif operation == "*":
        result = float(first_number) * float(second_number)

    elif operation == "/":
        result = float(first_number) / float(second_number)
    else:
        print('Error')
        exit()

print(result)