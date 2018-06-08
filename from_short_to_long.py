"""Napisać program wypisujący daną listę słów w kolejności od najkrótszego do najdłuższego"""

list = ['AB', 'A', 'CDS', 'B', 'FGHHTT']
list2 = []

for word in list:
    list2.append(len(word))

list2.sort()
print(list2)