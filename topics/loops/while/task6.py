"""
Task 6
Reverse the digits of a given string and print the result.
"""
user_message = input("Write your message(write everything that you want):")
i = 0
digits_substring = ""
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
while i < len(user_message):
    symbol = user_message[i]

    if symbol in digits:
        digits_substring += symbol

    i += 1
print(digits_substring[::-1])
