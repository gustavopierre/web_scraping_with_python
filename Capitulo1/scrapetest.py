#!/usr/bin/python3
from urllib.request import urlopen

html = urlopen(r'https://pythonscraping.com/pages/page1.html')
print(html.read())
print(type(html))
