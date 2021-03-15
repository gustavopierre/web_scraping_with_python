#!/usr/bin/python3
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen(r'http://pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs)
