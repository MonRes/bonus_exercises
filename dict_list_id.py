"""Załóżmy, że mamy daną listę słowników w postaci {'id': some_id, 'model': some_model}.
Używając wyrażenia listowego wygenerować listę wszystkich wartości id"""

dict_list = [{'id': 1, 'model': 'X'},
             {'id': 2, 'model': 'Y'},
             {'id' : 3, 'model': 'Z'}]

print([record['id'] for record in dict_list])
