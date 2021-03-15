import requests
from bs4 import BeautifulSoup

class Content:
    """
    Classe base comum para todos os artigos/paginas
    """


    def __init__(self, topic, title, body, url):
        self.topic = topic
        self.url = url
        self.title = title
        self.body = body


    def print(self):
        """
        Uma funcao flexivel de exibicao controla a saida
        """
        print('New article found for topic: {}'.format(self.topic))
        print('TITLE: {}'.format(self.title))
        print('BODY:\n {}'.format(self.body))
        print('URL: {}'.format(self.url))


class Website:
    """
    Contem informacoes sobre a estrutura do site
    """
    def __init__(self, name, url, searchUrl, resultListing, resultUrl, 
                 absoluteUrl, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.searchUrl = searchUrl
        self.resultListing = resultListing
        self.resultUrl = resultUrl
        self.absoluteUrl = absoluteUrl
        self.titleTag = titleTag
        self.bodyTag = bodyTag


class Crawler:

    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')


    def safeGet(self, pageObj, selector):
        
        childObj = pageObj.select(selector)
        if childObj is not None and len(childObj) > 0:
            return childObj[0].get_text()
        return ''
    

    def search(self, topic, site):
        """
        Pesquisa um dado site em busca de um dado
        topico e registra todas as paginas encontradas
        """
        bs = self.getPage(site.searchUrl + topic)
        searchResults = bs.select(site.resultListing)
        for result in searchResults:
            url = result.select(site.resultUrl)[0].attrs['href']
            # verifica se a url [e relativa ou absoluta
            if (site.absoluteUrl):
                bs = self.getPage(url)
            else:
                bs = self.getPage(site.url + url)
            if bs is None:
                print('something  was wrong with that page or URL. Skipping!')
                return
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(topic, title, body, url)
                content.print()

crawler = Crawler()

siteData =[
    ['O\'Reilly Media', 'https://www.oreilly.com', 'http://ssearch.oreilly.com/?q=', 
        'article.product-result', 'p.title a', True, 'h1', 
        'section#product-description'],
    ['Reuters', 'https://www.reuters.com', 'https://www.reuters.com/search/news?blob=', 
        'div.search-result-content', 'h3.search-result-title a', False, 'h1', 
        'div.StandardArticleBody_body_1gnLA'],
    ['Brookings', 'https://www.brookings.edu', 'https://www.brookings.edu/search/?s=', 
        'div.list-content article', 'h4.title a', True, 'h1', 
        'div.post-body']
]

sites = []

for row in siteData:
    sites.append(Website(row[0], row[1], row[2], row[3],
                         row[4], row[5], row[6], row[7]))

topics = ['python', 'data science']

for topic in topics:
    print('GETTING INFO ABOUT: ' + topic)
    for targetSite in sites:
        crawler.search(topic, targetSite)
