"""Załóżmy, że informacje o sukcesie i czasie wykonania zadania http przechowujemy w
słowniku, którego kluczami są:
- url - url zapytania
- status - zmienna logiczna mówiąca o powodzeniu lub nie
- response_time - (opcjonalnie) czas odpowiedzi
Zdefiniować przykładową listę z kilkoma opisanymi powyżej rekordami. Napisać program,
który dla każdego urla wypisze ilość udanych oraz nieudanych zapytań, a także średnią czasu odpowiedzi
zapytań, które się nie powiodły"""

http_record = [{'url' : 'http//google.pl', 'status': 'TRUE', 'response_time': 30},
               {'url' : 'http//wp.pl', 'status': 'FALSE', 'response_time': 22},
                {'url': 'http//google.pl', 'status': 'FALSE', 'response_time': 32},
               {'url': 'http//google.pl', 'status': 'FALSE', 'response_time': 12},
               {'url': 'http//wp.pl', 'status': 'TRUE', 'response_time': 50},
               {'url': 'http//wp.pl', 'status': 'TRUE', 'response_time': 53}]


total_by_url = {}
count_by_url = {}

for record in http_record:
    url = record['url']
    if url in total_by_url:
        total_by_url[url] += record['status']
        count_by_url[url] += 1
    else:
        total_by_url[url] = record['status']
        count_by_url[url] = 1
for url in count_by_url:
    print(count_by_url)


