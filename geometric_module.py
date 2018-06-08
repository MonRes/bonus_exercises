"""Napisać moduł geometryczny zawierający funkcję do obliczania pola figur
(kwadrat, prostokąt, koło). Przetestować jego działanie przykładowym programem"""

def pole_trojkata(a, h):

    pole_trojkata = 1 / 2 * (a * h)
    return pole_trojkata

def pole_kwadratu(a):

    pole_kwadratu = a ** 2
    return pole_kwadratu

def pole_prostokata(a, b):

    pole_prostokata = a * b
    return pole_prostokata