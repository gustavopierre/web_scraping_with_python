from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import datetime
import random
import re

random.seed(datetime.datetime.now())


def getLinks(articleUrl):
    url = f'https://en.wikipedia.org{articleUrl}'
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')
    return bs.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))


def getHistoryIPs(pageUrl):
    # Este é o formato das páginas de histórico de revisões
    # https://en.wikipedia.org/w/index.php?title=Python&action=history
    pageUrl = pageUrl.replace('/wiki/', '')
    historyUrl = 'https://en.wikipedia.org/w/index.php?title={}&action=history'.format(pageUrl)
    print('history url is: {}'.format(historyUrl))
    html = urlopen(historyUrl)
    bs = BeautifulSoup(html, 'html.parser')
    # encontra apenas os links cuja classe seja 'mw-anonuserlink' e
    # tenha endereços ip em vez de nomes de usuário
    ipAddresses = bs.findAll('a', {'class': 'mw-anonuserlink'})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList


links = getLinks('/wiki/Python_(programming_language)')

while (len(links) > 0):
    for link in links:
        print('-'*20)
        historyIPs = getHistoryIPs(link.attrs['href'])
        for historyIP in historyIPs:
            print(historyIP)
    newLink = links[random.randint(0, len(links)-1)].attrs['href']
    links = getLinks(newLink)
