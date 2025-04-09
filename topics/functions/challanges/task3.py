"""
 Create function, that can merge two dictionaries.

Result mapping ( dict ) should contain all keys from both dictionaries.
When keys are duplicated -> get value from second dictionary.
"""
import pytest


# mapping_one = {
#     'a': 10,
#     'b': 20,
#     'c': 30
# }
#
# mapping_two = {
#     'a': 30,
#     'c': 50,
#     'f': 40
# }
#
# # result
# mapping_result = {
#     'a': 10,
#     'b': 20,
#     'c': 30,
#     'f': 40
# }
def copy(from_, to):
    for key, value in from_.items():
        to[key] = value

def merge_mappings(a, b):
    c = {}
    copy(from_=a, to=c)
    copy(from_=b, to=c)
    return c
















@pytest.mark.parametrize(
    'a,b,expected',
    (
        ({'a': 10, 'b': 20}, {'a': 20}, {'a': 20, 'b': 20}),
    )
)
def test_merge_mappings(a, b, expected) -> None:
    assert merge_mappings(a, b) == expected
