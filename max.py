"""Napisać program znajdujący max element danej listy"""

list = [8, 12, 4, 3, 2, 1020]

for idx, value in enumerate(list):
    if idx == 0:
        current_max = value
    elif current_max < value:
        current_max = value


print('Max', current_max)