from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import Counter
import re
import string


def cleanSentence(sentence):
    sentence = sentence.split(' ')
    sentence = [word.strip(string.punctuation+string.whitespace) 
                for word in sentence]
    sentence = [word for word in sentence if len(word) > 1 or 
                (word.lower() == 'a' or word.lower() == 'i')]
    return sentence


def cleanInput(content):
    content = content.upper()
    # p = re.compile('\n')
    # content = p.sub(' ', content)
    content = re.compile('\n').sub(' ', content)
    content = bytes(content, 'UTF-8')
    content = content.decode('ascii', 'ignore')
    sentences = content.split('. ')
    return [cleanSentence(sentence) for sentence in sentences]


def getNgramsFromSentence(content, n):
    output = []
    for i in range(len(content)-n+1):
        output.append(content[i:i+n])
    return output


def getNgrams(content, n):
    content = cleanInput(content)
    ngrams = Counter()
    ngrams_list = []
    for sentence in content:
        newNgrams = [' '.join(ngram) for ngram in getNgramsFromSentence(sentence, 2)]
        ngrams_list.extend(newNgrams)
        ngrams.update(newNgrams)
    return ngrams


content = str(
    urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt').read(), 'utf-8'
)
ngrams = getNgrams(content, 2)
print(ngrams)
