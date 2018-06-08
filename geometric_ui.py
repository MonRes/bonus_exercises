"""Napisać moduł geometryczny zawierający funkcję do obliczania pola figur
(kwadrat, prostokąt, koło). Przetestować jego działanie przykładowym programem"""

import geometric_module

decission = int(input('Jeśli chcesz obliczyć pole trójkąta wybierz [1], jeśli kwadratu wybierz [2], jeśli prostokąta wybierz [3]: '))

if decission == 1:
    a = float(input('Podaj długość boku: '))
    h = float(input('Podaj wysokość: '))
    print('Pole trójkąta wynosi: ', geometric_module.pole_trojkata(a, h))
elif decission == 2:
    a = float(input('Podaj długość boku: '))
    print('Pole kwadratu wynosi: ', geometric_module.pole_kwadratu(a))
elif decission == 3:
    a = float(input('Podaj długość pierwszego boku: '))
    b = float(input('Podaj długość drugiego boku: '))
    print('Pole prostokąta wynosi: ', geometric_module.pole_prostokata(a, b))
else:
    print('Wprowadziłeś niepoprawną wartość. Program został zakończony')

