#!/usr/bin/python3
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
        # html = urlopen(r'http://lilacaromas.com.br/inicio.html')
    except HTTPError as e:
        print(f'Erro HTTP: {e.msg}')
        # devolve null, executa um break ou algum outro "plano B"
    except URLError as e:
        print(f'Erro de URL não achada')
    else:
        
        try:
            bs = BeautifulSoup(html.read(), 'html.parser')
            title = bs.title
        except AttributeError as e:
            print(f'Erro de Tag')
            return None
        else:
            return title

title = getTitle('http://pythonscraping.com/pages/page1.html')
if title == None:
    print('Title could not be found')
else:
    print(title)
        