import time
from urllib.request import urlretrieve
from PIL import Image
import pytesseract
from selenium import webdriver
import subprocess


def getImageText(imageUrl):
    urlretrieve(image, 'page.jpg')
    p = subprocess.Popen(['tesseract', 'page.jpg', 'page'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    f = open('page.txt', 'r')
    print(f.read())


# Cria um novo driver do Selenium
driver = webdriver.Chrome(executable_path='.\\chromedriver.exe')
#driver.get('https://www.amazon.com/Death-Ivan-Ilyich-Nikolayevich-Tolstoy/dp1427027277')
driver.get('https://www.amazon.com.br/dp/B003XYE7PE/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1')

time.sleep(2)

# Clica no botão para visualização prévia do livro
driver.find_element_by_id('ebooksImgBlkFront').click()
imageList = []

# Espera a página ser carregada
time.sleep(5)

while 'pointer' in driver.find_element_by_id('sitbReaderRightPageTurner').get_attribute('style'):
    # enquanto a seta da direita estiver disponível para clicar, vira as páginas
    driver.find_element_by_id('sitbReaderRightPageTurner').click()
    time.sleep(2)
    # Obtém qualquer página nova carregada (várias páginas podem ser
    # carregadas de uma só vez, mas páginas duplicadas não são
    # adicionadas em um conjunto)

    pages = driver.find_element_by_xpath('//div[@class=\'pageImage\']/div/img')
    if not len(pages):
        print('No pages found')
    for page in pages:
        image = page.get_attribute('src')
        print('Found image: {}'.format(image))
        if image not in imageList:
            imageList.append(image)
            getImageText(image)
    
    driver.quit()
