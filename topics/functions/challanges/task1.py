"""
Task 1
Refactor code by using functions instead of direct math operators.
в
Notes:
*Refactoring - the process of restructuring existing source without changing its external behavior.
**Рефикторинг - процесс реструктуризации существующего исходного кода без изменения его внешнего поведения.
https://en.wikipedia.org/wiki/Code_refactoring

Hint:
def plus(first_number: int, second_number: int) -> int:
    ...
"""

result = 0


def plus(a: float, b: float) -> float:
    return a + b


def minus(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        print("Error")
        exit()
    return a / b


operation_mapping = {
    '+': plus,
    '-': minus,
    '*': multiply,
    '/': divide
}


while True:
    first_number = float(input("Write the first number:"))
    if first_number == 911:
        break
    operation = input("Write an operation:")
    second_number = float(input("Write the second number:"))
    if operation not in operation_mapping:
        print("Error")
        exit()
    result = operation_mapping[operation](first_number, second_number)
    print(result)
