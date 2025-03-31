"""
Task 9
Simple calculator that performs +, -, *, / operations.
User can repeatedly enter numbers and an operation.
Enter 'q' as the operation to quit the program.
"""
while True:
    first_number = input("Write the first number:")
    if first_number == "q":
        break
    operation = input("Write an operation:")
    second_number = input("Write the second number:")
    if operation == "+":
        result = float(first_number) + float(second_number)

    elif operation == "-":
        result = float(first_number) - float(second_number)

    elif operation == "*":
        result = float(first_number) * float(second_number)

    elif operation == "/":
        result = float(first_number) / float(second_number)

    else:
        print()
    print(result)