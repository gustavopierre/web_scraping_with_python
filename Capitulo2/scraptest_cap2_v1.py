#!/usr/bin/python3
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs = BeautifulSoup(html.read(), 'html.parser')
# nameList = bs.findAll('span', {'class': 'green'})
# nameList = bs.findAll(['h1', 'h2', 'h3', 'h4', 'h5','h6'])
nameList = bs.findAll('span', {'class': {'green', 'red'}})
print(nameList)
print(type(nameList))
for name in nameList:
    print(name.get_text())
