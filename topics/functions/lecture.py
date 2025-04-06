from typing import Any


def add(a: int, b: int) -> int:
    result = a + b
    return result


def add(a, b):
    return a + b


def divide(*, a: int, b: int) -> float:
    if b == 0:
        raise ZeroDivisionError('Division by zero not allowed')
    return a / b


# print(divide(a=10, b=2))


# *args
def sum_our(*args: int) -> int:
    result = 0
    for number in args:
        result += number
    return result


print(sum_our(10, 9, 0, 363764, 43894, 4957847))


# **kwargs

def multiply(*, multiplier: int, **kwargs: Any) -> dict[str, Any]:
    for key, value in kwargs.items():
        kwargs[key] = int(value) * multiplier
    return kwargs


print(multiply(multiplier=10,))
