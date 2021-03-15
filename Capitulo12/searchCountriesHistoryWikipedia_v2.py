from urllib.request import urlopen
from urllib.error import HTTPError
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

def getCountry(ipAddress):
    try:
        response = urlopen('http://freegeoip.app/json/{}'.format(ipAddress)).read().decode('utf-8')
    except HTTPError:
        return None
    responseJson = json.loads(response)
    return responseJson.get('country_code')


links = getLinks('/wiki/Python_(programming_language)')

while (len(links) > 0):
    for link in links:
        print('-'*20)
        historyIPs = getHistoryIPs(link.attrs['href'])
        for historyIP in historyIPs:
            country = getCountry(historyIP)
            if country is not None:
                print(f'{historyIP} is from {country}.')
    newLink = links[random.randint(0, len(links)-1)].attrs['href']
    links = getLinks(newLink)
