"""
Task 5
Count and print the count of digits in a given string.
"""
user_string = input("Write something:")
i = 0
count_of_digits = 0
cloud_for_number = ["0","1","2","3","4","5","6","7","8","9"]
while i < len(user_string):
    if user_string[i] in cloud_for_number:
        count_of_digits += 1
    i += 1
print(count_of_digits)