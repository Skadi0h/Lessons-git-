"""
Task 3
Simple number guessing game.
The program keeps asking the user to guess the number until it is correct.
"""
import random

random_n = random.randint(0, 100)
user_guess = 0
while user_guess != random_n:
    user_guess = int(input("Write your variant:"))
    if user_guess > random_n:
        print("Too much, try again:")
    elif user_guess < random_n:
        print("Too small, try again:")
    else:
        print("Correct answer!" , random_n)