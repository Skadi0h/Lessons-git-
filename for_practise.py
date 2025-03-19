
name = 'Vasya Pupkin'

for symbol in name:     # definition
    # body of cycle
    print(symbol)

numbers = range(1000)
sum_of_numbers = 0

for number in numbers:
    sum_of_numbers += number

print(sum_of_numbers)

cities = ["Kyiv", "Boston", "Munich", "Mykolaiv"]

# example_city = "Hamburg"
# if example_city.startswith('H'):
#     ...
for mcity in cities:
    if mcity.startswith('M'):
        for symbol in mcity:
            print(symbol)
    else:
        print(mcity)

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

# INDEX-es
# example_name = "Vasya"
# counter = 0
#
# for letter in example_name:
#     print(letter, counter)
#     counter += 1

cities = ["Kyiv", "Boston", "Munich", "Mykolaiv", "Barcelona"]
counter = 0
for bcity in cities:
    if bcity.startswith('B'):
        print(counter)
    else:
        print(bcity)
    counter += 1

# enumerate
for counter, bcity in enumerate(cities):
    if bcity.startswith('B'):
        print(counter)
    else:
        print(bcity)

# short-reverse, slice-reverse
reversed_cities = cities[::-1]
print(reversed_cities)

# slice of iterable ( strings, lists, etc )
string_var = "Добро пожаловать в игру!"

def select(*, start_number, end_number) -> str:
    return string_var[start_number: end_number]

dobro = string_var[0:5]
print(dobro)
igry = string_var[19: 23]
print(igry)
report = string_var[6:16]
print(report)
rreport = report[::- 1]
print(rreport)

string_var = "Добро пожаловать в игру!"
for counter, symbol in enumerate(string_var[::- 1]):
    print(counter, symbol)

