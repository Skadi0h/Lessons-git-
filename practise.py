"""
Cycles usages:
    - for iterating on smth ( eng. iterating - перечислять )
    - for search smth in iterable
    - for filling smth ( чтобы наполнить список, словарь и т.д )
"""

"""
Task 1 ( Find Klement )
    Print index of "Klement"
    
    names = ["James", "Bob", "Jessica", ...., "Klement", "XYZ"]  # Неизвестно, сколько имен
    
    i = 0
    for name in names:
        i += 1
        if name == "Klement":
            break
            
    print("Index of Klement =", i )  
"""

# # EXAMPLE OF SEARCH:
# names = ["James", "Bob", "Jessica", 1, 1241421, 2242, 24242, 24, "Klement", "XYZ"]  # Неизвестно, сколько имен
#
# attempts = 0
#
# for name in names:
#     if name == "Klement":
#         break
#     attempts += 1
#
# print("Index of Klement:", attempts)
# print("Short version:", names.index("Klement"))
# print(names[attempts])


"""
Task 2 ( Find substring in string )
Find start end end index of substring in string.
( Найди начало и конец подстроки в строке )

String = sequence of chars
ex.
    string_var = "Добро пожаловать в игру!"
    substring_var = "в игру!"
"""

# string_var = "Добро пожаловать в игру!"
# substring_var = "в игру!"
#
# start_of_substring = 0
# end_of_substring = 0
# for char in string_var:
#     ...
# print("Correct:", string_var[start_of_substring: end_of_substring] == substring_var)

"""
Task 3 ( Calculate factorial of some number )

Example:
    factorial = 1 * 2 * 3 * 4 * 5
"""
number = 5
factorial = 1  # результат должен сохраниться тут

# пиши код тут





# Код ниже - не трогать
def factorial_check(_number: int) -> int:
    if _number == 0:
        return 1
    return factorial_check(_number - 1) * _number


print("Correct: ", factorial_check(number) == factorial)
