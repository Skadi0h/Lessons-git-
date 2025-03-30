"""
Task 8
Calculate and print the factorial of a given number using a while loop.
Example: 5! = 5 × 4 × 3 × 2 × 1 = 120
"""
number = int(input("Write a number: "))
i = 1

while number > 1:
    i *= number
    number -= 1

print( "Answer:", i)