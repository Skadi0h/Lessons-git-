
"""
Task 2

You are given a list of numbers. Count how many of them are even.

Hint: number % 2 == 0 IS EVEN.
"""
list_of_numbers = [int(x) for x in input('Enter numbers: ').split(',')]
count_of_even_numbers = 0
for number in list_of_numbers:
    if number % 2 == 0:
        count_of_even_numbers += 1
print(count_of_even_numbers)
