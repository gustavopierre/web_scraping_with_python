#!/usr/bin/python3
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs = BeautifulSoup(html.read(), 'html.parser')
for sibling in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
    print(sibling)
