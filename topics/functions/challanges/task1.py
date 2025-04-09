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


while True:
    first_number = input("Write the first number:")
    if first_number == "q":
        break
    operation = input("Write an operation:")
    second_number = input("Write the second number:")
    if operation == "+":
        result = plus(first_number, second_number)
    elif operation == "-":
        result = minus(a, b)
    elif operation == "*":
        result = multiply(a, b)
    elif operation == "/":
        result = divide(a, b)
    else:
        print("Error")
        exit()
    print(result)
