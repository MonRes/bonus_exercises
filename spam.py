"""Napisać program, który  wstawi łańcuch znaków 'spam' do listy przed każdym wystąpieniem elementu 'eggs'"""

eggs_list = ['eggs', 1, 'foo', 'eggs', 'dashboard', 2, 3, 'eggs']
eggs =[]
for idx, value in enumerate(eggs_list):
    if value == 'eggs':
        eggs.append('spam')
        eggs.append(value)
    else:
        eggs.append(value)

print(eggs)



