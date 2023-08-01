import requests
import csv

from bs4 import BeautifulSoup

URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')
print(soup.prettify())
'''quotes = [] # empty list to store quotes

table = soup.find()'''