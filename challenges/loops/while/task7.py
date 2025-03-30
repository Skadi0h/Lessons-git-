"""
Task 7

Check if a given number is a palindrome using a while loop.

A palindrome is a number that reads the same forward and backward.
For example: 121, 1331, 444 are palindromes.
научится отделять цифры от любого числа с помощью операции деления с остатком(остаток от деления на 10, 100, 1000, 10000, 100000 ...)
"""
# user_number = int(input("Write please number:"))
# user_number_reverse = str(user_number)[::-1]
# # while user_number > 0:
# if str(user_number) == user_number_reverse:
#     print("Your number is palimdromes!")
# else:
#     print("Not this time!")
number = int(input("Write number: "))

while number > 0:
    print(number % 10)

