"""
Task 7* ( Find substring in string )
Find start end end index of substring in string.
( Найди начало и конец подстроки в строке )

String = sequence of chars
ex.
    string_var = "Добро пожаловать в игру!"
    substring_var = "в игру!"
"""

string_var = "Добро пожаловать в игру!"
substring_var = "пожаловать"

length_of_string_var = len(string_var)

first_pointer = string_var.find(substring_var)
second_pointer = length_of_string_var


for i in range(length_of_string_var):
    if string_var[first_pointer: second_pointer] == substring_var:
        break
    second_pointer -= 1


print(string_var[first_pointer: second_pointer])
