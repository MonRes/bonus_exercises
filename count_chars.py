"""Napisać funkcję count_chars(text) przyjmując jako argument łańcuch znaków i zwracająca
słownik o kluczach 'lower', 'upper' oraz 'digits', którym odpowiadają odpowiednio liczności małych i dużych liter oraz cyfr.
Na przykład dla łańcucha znaków 'One, Two, 3' zwracana wartością powinien być słownik {'lower': 4, 'upper': 2, 'digits':1"""
import string

def count_chars(text):

    low_up_dig = {}
    low = string.ascii_lowercase
    up = string.ascii_uppercase

    for char in text:
        if char in low:
            low_up_dig['lower'] = low_up_dig.get('lower', 0) + 1
        elif char in up:
            low_up_dig['upper'] = low_up_dig.get('upper', 0) + 1
        elif char.isdigit():
            low_up_dig['digit'] = low_up_dig.get('digit', 0) + 1
        else:
            low_up_dig['others'] = low_up_dig.get('others', 0) + 1
    return low_up_dig

print(count_chars('GFHKAJDJDJadjhdjhskfhkjfs7849248264827  *^$##'))


