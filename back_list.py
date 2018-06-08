"""Napisać program wypisujący elementy danej listy od tyłu"""

list = [0, 1, 7, 3, 4]

for i in range(len(list)-1, -1, -1):
    print(list[i])