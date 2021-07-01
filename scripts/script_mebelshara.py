from requests import get
from bs4 import BeautifulSoup
import json

url_mebel = 'https://www.mebelshara.ru/contacts'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                         ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}

response = get(url_mebel, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

# Saving content of page to a temperary html file and using BeautifulSoup to operate with data
with open('../data/mebelshara_parsing.html', 'w') as file:
    file.write(soup.prettify())

with open('../data/mebelshara_parsing.html') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

# Requesting content of each shop and saving it to shops_list
shops_list = soup.find_all('div', {'class': 'shop-list'})

result_list = []


# Creating dictionaries for each shop and filling it with data requested in testing task
for shop in shops_list:
    address = shop.find('div').attrs['data-shop-address']
    name = shop.find('div').attrs['data-shop-name']
    phones = shop.find('div').attrs['data-shop-phone']
    latlon = shop.find('div').attrs['data-shop-latitude'], shop.find('div').attrs['data-shop-longitude']
    working_time = f"{shop.find('div').attrs['data-shop-mode1']}, {shop.find('div').attrs['data-shop-mode2']}"

    shop_dict = {
        'address': address,
        'name': name,
        'phones': phones,
        'latlon': latlon,
        'working_time': working_time
    }
    result_list.append(shop_dict)

# Saving results in json-format file
with open('../results_json/mebelshara_results.json', 'a', encoding='utf-8') as file:
    json.dump(result_list, file, indent=4, ensure_ascii=False)
