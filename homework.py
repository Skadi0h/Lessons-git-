"""
Task 1 ( Find substring in string )
Find start end end index of substring in string.
( Найди начало и конец подстроки в строке )

String = sequence of chars
ex.
    string_var = "Добро пожаловать в игру!"
    substring_var = "в игру!"
"""

string_var = "Добро пожаловать в игру!"
substring_var = "в игру!"

start_of_substring = 0  # результат должен сохраниться тут
end_of_substring = 0  # и тут

# пиши код тут





"""
Task 2 ( Calculate sum of lowest numbers )

Example:
    sum_numbers = 1 + 2 + 3 + 4 + 5
"""
number = 5
sum_numbers = 0  # результат должен сохраниться тут

# пиши код тут
for summe in range(1,number + 1):
    sum_numbers += summe













































# Код ниже - не трогать

def sum_check(_number: int) -> int:
    if _number == 0:
        return 0
    return sum_check(_number - 1) + _number


print("Correct Task 1:", string_var[start_of_substring: end_of_substring] == substring_var)
print("Correct Task 2:", sum_check(number) == sum_numbers)