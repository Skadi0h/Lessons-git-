"""
Task 4

Given a list of words: ["Hello", "world", "!"].
Use a loop to join them into one string: "Hello world !"
"""

list_of_words = input('Enter text: ').split(' ')
sentence = ""
for word in list_of_words:
    sentence += word + " "
print(sentence)

print(" ".join(list_of_words))