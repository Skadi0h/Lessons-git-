"""
Task 3
Simple number guessing game.
The program keeps asking the user to guess the number until it is correct.
"""
import random

random_n = random.randint(0, 100)
user_guess = 0
while user_guess != random_n:
    user_guess = int(input("Write your variant: "))
    if user_guess > random_n:
        print("Too much, try again:")
    elif user_guess < random_n:
        print("Too small, try again:")
    else:
        print("Correct answer!", random_n)

# Done! cc. A















if input('Do you want test conditions? ').lower() in {'yes', 'y'}:
    def guess_mock(
        *,
        number_to_guess: int,
        user_number: int
    ) -> str:
        print(f'Guessing {number_to_guess} with {user_number}')
        if user_number > number_to_guess:
            return "Too much, try again:"
        elif user_number < number_to_guess:
            return "Too small, try again:"
        else:
            return "Correct answer!"


    def test_guess() -> None:
        number_to_guess = random.randint(0, 100)
        responses = [
            guess_mock(
                number_to_guess=number_to_guess,
                user_number=number
            )
            for number in range(-10000, 10000)
        ]
        assert len(
            list(
                filter(
                    lambda x: x == "Correct answer!", responses
                )
            )
        ) == 1
        print('Test guess() passed. 1 correct answer.')


    test_guess()
