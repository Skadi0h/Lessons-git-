"""
Cycles in Python

Iterable: ( eng. Iterable - перечисляемый )

Examples of iterable:
    str_number = "123" - str, строка
    numbers = [1, 2, 3] - list, список
    set_numbers = {1, 2, 3} - set, множество
    dict_numbers = {"a": 1, "b": 2, "c": 3} - dict, словарь
    tuple_numbers = (1,2,3) - tuple, кортеж

Cycle types:
    for number in numbers: ( для каждого числа в числах, где "каждое число" - элемент перечисляемого, т.е. локальная переменная цикла)
        ...

    while CONDITION: ( Пока условие верно, eng. Condition - условие, while - пока, цикл с условием остановки)
        ...

    while True: ( eng. Infinite Loop  - бексконечный цикл)
        ...
    break - ( eng. stop-cycle operator - оператор ручной остановки цикла, останавливает любой цикл)

Examples:
    for x in (1,2,3): - tuple items iteration
       print(x)

    for key, value in {"a":1, "b":2}.items(): - dict items iteration
        print(key, value)

    for x in [1,2,3]: - list items iteration
        print(x)

    for x in range(2): - range items iteration
        print(x)

    i = 0
    while True:
        print(i)
        i += 1
        if i > 10:
            break

"""

# print("tuple items iteration")
# for x in (1, 2, 3):
#     print(x)
#
# print("dict items iteration")
# for key, value in {"a": 1, "b": 2}.items():
#     print(key, value)
#
# print("list items iteration")
# for x in [1, 2, 3]:
#     print(x)
#
# print("infinite loop with break condition inside")
# i = 0
# while True:
#     print(i)
#     i += 1
#     if i >= 10:
#         break
#
# print("loop with stop condition")
# i = 0
# while i < 10:
#     print(i)
#     i += 1
#
# condition: bool  # True/False, 1/0

counter = 0
while counter <= 23:
    if counter % 2 == 0:
        print(counter)
    counter += 1
print('next after while')



