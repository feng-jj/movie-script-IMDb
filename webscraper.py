import requests
from bs4 import BeautifulSoup


r = requests.get('https://www.imdb.com/chart/top/')

print r.text[0:500]

soup  = BeautifulSoup(r.text, 'html.parser')
