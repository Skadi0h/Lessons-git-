"""
Task:
    Menu is a list of dishes ( length of list == 10, create list from 10 types of dishes):

    1) Reverse order of dishes list
    2) Print table between dishes and their numbers ( indexes )
        EXAMPLE ( don't use explicit values, ex. prints with new strings )
            BMW - 0
"""
menu =["Varenichki", "Borshik", "Plov", "Oladushki", "Blinchiki", "Pelmeni", "Makaroshki", "Zrazy", "Supchik", "Kartoshechka"]
print("Dishes:", menu)
menu.reverse()
print("Reverse Dishes:" , menu)
for index, dish in enumerate(menu):
    print(f"{dish} - {index}")