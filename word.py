"""Napisać program tworzący listę słów z podanego łańcucha znaków.
Przez słowo rozumiemy dowolny podłańcuch, zawierający jedynie znaki alfanumeryczne.
Na przykład dla łańcucha znaków 'Spam&eggs+-/bar baz' program powinien utworzyć listę:
['spam', 'eggs', 'bar', 'baz']"""
import string

word = 'some$things%are*illusion'

words_list = []
current_word = []
sep = string.ascii_letters

for char in word:
    if char in sep:
        current_word.append(char)
    elif char is not sep:
        words_list.append(''.join(current_word))
        current_word = [] #co tu się stało?
words_list.append(''.join(current_word))

print(words_list)
