"""
Task 9
Simple calculator that performs +, -, *, / operations.
User can repeatedly enter numbers and an operation.
Enter 'q' as the operation to quit the program.
"""
# while True:
#     first_number = input("Write the first number:")
#     if first_number == "q":
#         break
#     operation = input("Write an operation:")
#     second_number = input("Write the second number:")
#     if operation == "+":
#         result = float(first_number) + float(second_number)
#
#     elif operation == "-":
#         result = float(first_number) - float(second_number)
#
#     elif operation == "*":
#         result = float(first_number) * float(second_number)
#
#     elif operation == "/":
#         result = float(first_number) / float(second_number)
#
#     else:
#         print()
#     print(result)


# TODO: 9/12 Done! cc. A


# with Exceptions and map

# operations_map = {
#     '+': lambda x, y: x + y,
#     '-': lambda x, y: x - y,
#     '*': lambda x, y: x * y,
#     '/': lambda x, y: x / y
# }
#
# while True:
#     first_number = input("Write the first number: ")
#     if first_number == "q":
#         break
#     operation = input("Write an operation: ")
#     second_number = input("Write the second number: ")
#     try:
#         if operation in operations_map:
#             result = operations_map[operation](first_number, second_number)
#         else:
#             raise ValueError('Not supported operator')
#     except ValueError as e: # print('error')
#         print('Try again! Choose operator from: +, -, *, /')
#         continue
#     except ZeroDivisionError as e:
#         print('Try again! You cannot divide by zero')
#         continue
#     print(result)


# one-line calculator
# loc = {}
# while True:
#     exec(input(), globals(), loc)
#     print(loc['result'])