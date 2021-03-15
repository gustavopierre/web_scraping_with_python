#!/usr/bin/python3
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

try:
    html = urlopen(r'http://pythonscraping.com/pages/page1.html')
    #html = urlopen(r'http://lilacaromas.com.br/inicio.html')
except HTTPError as e:
    print(e)
    # devolve null, executa um break ou algum outro "plano B"
except URLError as e:
    print('The server could not be found!')
else:
    bs = BeautifulSoup(html.read(), 'html.parser')
    print(bs.title)
