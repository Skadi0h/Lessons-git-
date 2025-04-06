# Topic: Data-types ( Structures )

"""
1) Untyped language. *Type - categorical group of objects with some responsibilities.
2) Variables ( links to objects in memory ):
    my_storage = object()
3) Types of objects:
    -------IMMUTABLE----------------
    - integer, with floating decimal
    - string or bytes strings
    -------MUTABLE-----------------
    - list of something
4) Object
    Everything in Python is object.
    Object is a base thing. ( ex. "New hero without any characteristics" )
"""

# 2
my_storage = object()

# 3
# Number
number_integer: int = 10
number_floating: float = 10.2

# Strings
regular_string: str = 'Vanya'
bytes_string: bytes = b'Vanya'

# List
# Enumerates from 0!
# Index of BMW value == 0

# ["BMW", "MERCEDES", "ALFA-ROMEO"]
#   0         1            2

car_brands: list[str] = ["BMW", "Mercedes", "Alfa-Romeo"]

car_brands.append("Volvo")  # Step 1

print("Step 1. ( add Volvo ) Car brands =", car_brands)

car_brands.remove("Mercedes")  # Step 2

print("Step 2. ( Remove Mercedes ) Car brands =", car_brands)

car_brands.insert(1, "Ferrari")  # Step 3

print("Step 3. ( Insert Ferrari at pos 1) Car brands =", car_brands)

car_brands[1] = "Dacia"  # Step 4

print("Step 4. ( Replace Ferrari with Dacia ) Car brands =", car_brands)
