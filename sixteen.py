"""Napisać program wypisujący daną liczbę naturalną w postaci szesnastkowej"""

a = 1030283746
list = []


while (a / 16) >  16:
    a = (a / 16)
    list.append(int(a % 16))

for idx, number in enumerate(list):
    if number == 10:
        list.append(str('A'))
    elif number == 11:
        list.append(str('B'))
    elif number == 12:
        list.append(str('C'))
    elif number == 13:
        list.append(str('D'))
    elif number == 14:
        list.append(str('E'))
    elif number == 15:
        list.append(str('F'))



print('Podana liczba w postaci szesnastkowej to: ', list)
