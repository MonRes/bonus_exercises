"""Program wyznaczający medianę trzech liczb"""

a = 12
b = 7
c = 1

if a > b and a < c or a < b and a > c:
    print('Mediana to: a')
elif b > a and b < c or b < a and b > c:
    print ('Mediana to: b')
elif c > a and c < b or c < a and c < b:
    print ('Mediana to: c')