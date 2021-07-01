import requests
from bs4 import BeautifulSoup
import json

from help_functions import pharmacy_working_hours

url_pharmacy = 'https://www.tvoyaapteka.ru/adresa-aptek/'

response = requests.get(url_pharmacy)
soup = BeautifulSoup(response.text, 'html.parser')

# Saving content of page to a temperary html file and using BeautifulSoup to operate with data
with open('../data/pharmacy_parsing.html', 'w', encoding='utf-8') as file:
    file.write(response.text)

with open('../data/pharmacy_parsing.html', encoding='utf-8') as file:
    src = file.read()

soup_ = BeautifulSoup(src, 'lxml')

pharmacy_list = []
# Filtering data to extract information related to pharmacies, saving data to pharmacy_list
for item in soup.find_all("div", {'class': 'apteka_item'}):
    pharmacy_list.append(item)

result_list = []

# creating of office-dictionaries according with a fields according to testing task
# putting all the dictionaries to result list

# Note: according  to task details there have to be one more field shown in json - phones
# Unfortunately by the date of 30JUN - 1JUL this data is not mentioned on a website.
for item in pharmacy_list:
    name = item.find('div', {'class': 'apteka_title'}).get_text().strip()
    address = item.find('div', {'class': 'apteka_address'}).get_text().strip()

    pharmacy = {
        'address': address,
        'latlon': [item.attrs['data-lat'], item.attrs['data-lon']],
        'name': name,
        'working_hours': pharmacy_working_hours(item),
    }
    result_list.append(pharmacy)

with open('../results_json/tvoya_apteka_results.json', 'a', encoding='utf-8') as file:
    json.dump(result_list, file, indent=4, ensure_ascii=False)
