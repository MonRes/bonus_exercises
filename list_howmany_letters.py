"""Zdefiniować listę składającą się z kilku łańcuchów znaków. Następnie, używając wyrażenia listowego wygenerować listę,
zawierającą długości poszczególnych znaków"""

lst = ['ABF', '%^&', 'FDGDFF', 'SDFFDSSSDDD', 'hjhjjfj', 'a', 'a']

print([len(string) for string in lst])