#!/usr/bin/python3
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs = BeautifulSoup(html.read(), 'html.parser')
for child in bs.find('table', {'id': 'giftList'}).children:
    print(child)
