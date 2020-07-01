
import requests
import webbrowser
import re
import sys
from bs4 import BeautifulSoup

url = 'https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html'

page = requests.get(url)


soup = BeautifulSoup(page.content, 'html.parser')

exchange = {}

for row in soup.select('tbody tr'):
    row_text = [x.text for x in row.find_all('td')]
    exchange[row_text[0]] = row_text[1]

print(exchange)
print(exchange.get('EUR'))
print(len(exchange.items()))























