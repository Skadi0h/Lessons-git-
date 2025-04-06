"""
Task 9

Filter list of numbers, that can be divided ( non-zero )

"""

list_of_numbers = [int(x) for x in input('Enter numbers: ').split(',')]

list_of_numbers_without_zero = []
for number in list_of_numbers:
    if number != 0:
        list_of_numbers_without_zero.append(number)
print(list_of_numbers_without_zero)