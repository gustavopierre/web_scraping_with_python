from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import Counter


def cleanSentence(sentence):
    sentence = sentence.split(' ')
    sentence = [word.strip(string.punctuation+string.whitespace) for word in sentence]
    sentence = [word for word in sentence if len(word) > 1 or (word.lower() == 'a' or word.lower() == 'i')]
    return sentence
    
    
def cleanInput(content):
    p = re.compile('\n|[\[\d+\]]')
    content = p.sub(' ', content)
    content = bytes(content, 'UTF-8')
    content = content.decode('ascii', 'ignore')
    sentences = content.split('. ')
    return [cleanSentence(sentence) for sentence in sentences]


def getNgramsFromSentece(content, n):
    output = []
    for i in range(len(content)-n+1):
        output.append(content[i:i+n])
    return output


def getNgrams(content, n):
    content = cleanInput(content)
    ngrams = Counter()
        
    for sentence in content:
        newNgrams = [' '.join(ngram) for ngram in getNgramsFromSentece(sentence, 2)]
        ngrams.update(newNgrams)
    return ngrams


html = urlopen('https://en.wikipedia.org/wiki/Python_(programming_language)')
bs = BeautifulSoup(html, 'html.parser')
content = bs.find('div', {'id':'mw-content-text'}).get_text()
ngrams = getNgrams(content, 2)
print(ngrams)
print(f'2-grams count is : {str(len(ngrams))}')
