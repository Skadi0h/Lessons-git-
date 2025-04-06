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

