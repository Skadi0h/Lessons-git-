"""
Task 4
Ask the user to enter a password.
Repeat the prompt until the correct password is entered.
"""
password = "123Qwe56!"
user_promt = 0
try1 = 0
while user_promt != password:
    user_promt = input("Write your password:")
    if user_promt != password :
        print("Wrong, try again")
        try1 += 1
        if try1 == 3:
                print("You are blocked!!! Хакер мамкин")
                break
    else:
        print("Correct!!")