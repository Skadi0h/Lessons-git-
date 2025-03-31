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
number = input("Write number: ")
int_number = int(number)


numbers = []
i = 10**(len(number) - 1)

while True:
    numbers.append(
        int(
            (int_number // i) % 10
        )
    )
    if i == 1:
        break
    i /= 10


if numbers == numbers[::-1]:
    print("Your number is palimdromes!")
else:
    print("Not this time!")
