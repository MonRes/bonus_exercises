"""Napisać funkcję filter non alphabetic(text), która dla danego łańcucha znaków zwróci łańcuch
powstały przez pominięcie z niego wszystkich znaków będacych znakami alfanumerycznymi"""
import string

def filter_non_alphabetic(text):

    sep = string.ascii_letters

    for letter in text:
        if letter not in sep:
            text = text.replace(letter, '')
    print(text)

print(filter_non_alphabetic('jdklsjdls$566hjkdhk'))
