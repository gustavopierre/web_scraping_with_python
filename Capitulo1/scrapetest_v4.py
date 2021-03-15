#!/usr/bin/python3
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

try:
    html = urlopen(r'http://pythonscraping.com/pages/page1.html')
    # html = urlopen(r'http://lilacaromas.com.br/inicio.html')
except HTTPError as e:
    print(f'Erro HTTP: {e.msg}')
    # devolve null, executa um break ou algum outro "plano B"
except URLError as e:
    print(f'Erro URL: {e.msg}')
else:
    
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h134
    except AttributeError as e:
        print(f'Erro: {e.msg}')
    else:
        if title == None:
            print('Title could not be found')
        else:
            print(title)
        