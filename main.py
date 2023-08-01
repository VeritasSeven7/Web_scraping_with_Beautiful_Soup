import requests
import csv

from bs4 import BeautifulSoup

URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

quotes = [] # a list to store quotes

table = soup.find('div', attrs = {'id':'all_quotes'})

print(soup.prettify())
#print(table.prettify())