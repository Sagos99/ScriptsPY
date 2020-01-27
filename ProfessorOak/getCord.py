import requests
from bs4 import BeautifulSoup


# Coletar e analisar a primeira página
page = requests.get('http://www.megasnipe.com.br/')
soup = BeautifulSoup(page.text, 'html.parser')

# Pegar todo o texto da div BodyText
artist_name_list = soup.find(class_='BodyText')

# Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
# artist_name_list_items = artist_name_list.find_all('a')

import ipdb; ipdb.set_trace()