import requests
from bs4 import BeautifulSoup

class Content:
    """
    Classe base comum para todos os artigos/paginas
    """


    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body


    def print(self):
        """
        Uma funcao flexivel de exibicao controla a saida
        """
        print('URL: {}'.format(self.url))
        print('TITLE: {}'.format(self.title))
        print('BODY:\n {}'.format(self.body))


class Website:
    """
    Contem informacoes sobre a estrutura do site
    """
    def __init__(self, name, url, titleTag, bodyTag):
        self.name = name
        self.url = url
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
        """
        Funcao utilitaria usada para obter uma string de conteudo de um
        objeto BeautifulSoup e um seletor. Devolve uma string
        vazia caso nenhum objeto seja encontrado para um dado seletor
        """
        selectedElems = pageObj.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            return '\n'.join([elem.get_text() for elem in selectedElems])
        return ''
    

    def parse(self, site, url):
        """
        Extrai conteudo de um dado URL de pagina
        """
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(url, title, body)
                content.print()

crawler = Crawler()

siteData =[
    ['O\'Reilly Media', 'http://oreilly.com', 'h1', 'section#product-description'],
    ['Reuters', 'http://reuters.com', 'h1', 'div.StandardArticleBody_body'],
    ['Brookings', 'https://www.brookings.edu', 'h1', 'div.post-body'],
    ['New York Times', 'https://www.nytimes.com', 'h1', 'p.css-exrw3m evys1bk0'],
]

websites = []

for row in siteData:
    websites.append(Website(row[0], row[1], row[2], row[3]))

crawler.parse(websites[0], 'http://shop.oreilly.com/product/0636920028154.do')
crawler.parse(websites[1], 'http://reuters.com/article/us-usa-epa-pruitt-idUSKBN19W2D0')
crawler.parse(websites[2], 'https://www.brookings.edu/blog/techtank/2016/03/01/idea-to-retire-old-methods-of-policy-education/')
crawler.parse(websites[3], 'https://www.nytimes.com/2018/01/28/business/energy-environment/oil-boom.html')
