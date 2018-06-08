"""Napisać program znajdujący wszystkie najdłuższe łańcuchy znaków na danej
liście i wypisujący je w kolejności alfabetycznej"""

strings = ['ABC', 'GFG', 'CDA', 'a', 'b', 'c', 'FGL']
alphabet_string = []

for idx, string in enumerate(strings):
    if idx == 0:
        current_max_len = len(string)
    if current_max_len < len(string):
        current_max_len = len(string)
        print(string)
    if current_max_len == len(string):
        alphabet_string.append(string)

alphabet_string.sort() #sortowanie alfabetyczne

print(alphabet_string)
