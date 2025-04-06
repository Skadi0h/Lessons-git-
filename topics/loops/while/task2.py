"""
Task 2
Ask the user for a number (N), then calculate and print the sum of all numbers from 1 to N.
n = int(input(...))
"""
n = int(input("Enter your number:"))
counter = 1
summe = 0
while counter <= n:
    summe += counter
    counter += 1

print(summe)