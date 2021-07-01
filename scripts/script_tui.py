from requests import get
import json

from help_functions import check_working_time

url_tui_cities = 'https://apigate.tui.ru/api/office/cities'
cities_codes = []
offices_list = []

# getting id's of the cities and putting it to cities_codes list

response = get(url_tui_cities)

for city in response.json()['cities']:
    cities_codes.append(city['cityId'])

# searching for offices in each city by id of city. Saving all the offices to temporary
# offices_list


for city_id in cities_codes:
    url_tui = f"https://apigate.tui.ru/api/office/list?CityId={city_id}"
    response = get(url_tui)
    for x in (response.json()['offices']):
        offices_list.append(x)

result_list = []

# creating of office-dictionaries according with a fields according to testing task
# putting all the dictionaries to result list

for tui in offices_list:
    tui_office = {
        'address': tui['address'],
        'latlon': [tui['latitude'], tui['longitude']],
        'name': tui['name'],
        'phones': tui['phones'],
        'working_hours': check_working_time(tui)
    }
    result_list.append(tui_office)

# Saving results in json-format file

with open('../results_json/tui_results.json', 'a', encoding='utf-8') as file:
    json.dump(result_list, file, indent=4, ensure_ascii=False)
