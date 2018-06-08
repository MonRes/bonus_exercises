"""Napisać program znajdujący najdłuższy znak na liście. W razie, gdyby na liście
znajdował się więcej niż jeden taki łańcuch, wynikiem może być dowolny z nich"""

strings = ['ghj', 'hdjahkd', 'a', 'hdhd', 'aaaa', 'bb', 'jsdhgah']

for idx, string in enumerate(strings):
    if idx == 0:
        current_max_len = len(string)
    if current_max_len < len(string):
        current_max_len = len(string)
        print(string)

