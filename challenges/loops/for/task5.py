"""
Task 5

You are given a list of words. Print the length of each word.
Example: ["apple", "banana", "kiwi"] → 5 6 4

Hint: length of something can be calculated by use len() function
Example:
some_list = [1,2,3,4,5]
len_of_some_list = len(some_list) → 5
"""

list_of_words = input('Enter text: ').split(' ')
len_of_word = 0
for word in list_of_words:
    len_of_word = len(word)
    print(len_of_word)
