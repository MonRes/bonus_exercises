"""Załóżmy, że informacje o sukcesie i czasie wykonania zadania http przechowujemy w
słowniku, którego kluczami są:
- url - url zapytania
- status - zmienna logiczna mówiąca o powodzeniu lub nie
- response_time - (opcjonalnie) czas odpowiedzi
Zdefiniować przykładową listę z kilkoma opisanymi powyżej rekordami. Napisać program,
który dla każdego urla wypisze ilość udanych oraz nieudanych zapytań, a także średnią czasu odpowiedzi
zapytań, które się nie powiodły"""

http_record = [{'url' : 'http//google.pl', 'status': True, 'response_time': 30},
               {'url' : 'http//wp.pl', 'status': False, 'response_time': 22},
                {'url': 'http//google.pl', 'status': False, 'response_time': 32},
               {'url': 'http//google.pl', 'status': False, 'response_time': 12},
               {'url': 'http//wp.pl', 'status': True, 'response_time': 50},
               {'url': 'http//wp.pl', 'status': True, 'response_time': 53}]


total_by_url = {}

for record in http_record:
    url = record['url']
    if url not in total_by_url:
        total_by_url[url] = {'True': 0, 'False': 0, 'ResponseTime': 0}

    if record['status'] == True:
        total_by_url[url]['True'] += 1
        total_by_url[url]['ResponseTime'] += record['response_time']
    else:
        total_by_url[url]['False'] += 1
for x in total_by_url:
    total_by_url[x]['ResponseTime'] = total_by_url[x]['ResponseTime'] / total_by_url[x]['True']

print(total_by_url)

