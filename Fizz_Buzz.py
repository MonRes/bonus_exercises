"""Napisać program wypisujący na ekran liczby od 0 do 100 z następującymi wyjątkami:
- dla liczb podzielnych przez 3 i przez 5 wypisać FizzBuzz
- dla liczb podzielnych przez 3 wypisać Fizz
- dla liczb podzielnych przez 5 wypisać Buzz
"""

for i in range(0, 100):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)