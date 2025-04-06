"""
Make function, that should find numbers in string.

Function should return list of numbers, that present in string.
If string doesn't contain any numbers - return [-1]

NOTE:
    Numbers can consist of several digits.
Example:
    our_string = "Дом на улице Вишневского 21"
    result = [21]
"""

user_string = "Дом7 на ули57це 3Виш67невск3ого 21"


def find_numbers_in_string(message: str) -> list[int]:
    result = []
    string_tempery = ""

    for element in message + " ":
        if element.isdigit():
            string_tempery += element
        elif string_tempery:
            result.append(int(string_tempery))
            string_tempery = ""
    if result:
        return result
    return [-1]


# import pytest
#
#
# @pytest.mark.parametrize(
#     'test_string, expected_result',
#     (
#         ("Дом7 на ули57це 3Виш67невск3ого 21", [7, 57, 3, 67, 3, 21]),
#         ('Дом на улице 36', [36]),
#         ('21, 33, 44, 55, Rolex', [21, 33, 44, 55])
#     )
# )
# def test_find_numbers_in_string(
#     *,
#     test_string: str,
#     expected_result: list[int]
# ) -> None:
#     assert find_numbers_in_string(test_string) == expected_result

