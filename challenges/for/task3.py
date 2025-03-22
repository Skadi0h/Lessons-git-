"""
Task 3

Create a list that contains the squares of numbers from 1 to N.
.append()???
"""
N = int(input('Enter number:'))
list_of_numbers = []
temporary_number = 0
for number in range(N):
    temporary_number += number**2
    list_of_numbers.append(temporary_number)
    temporary_number = 0
print(list_of_numbers)
#взять число из списка, возвести в квадрат и вернуть обратно в список
# взять число из ренджа, возвести в квадрат и положить в список
