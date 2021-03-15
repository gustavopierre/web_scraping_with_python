from urllib.request import urlopen
from random import randint


def wordListSum(wordList):
    sum = 0
    for word, value in wordList.items():
        sum += value
    return sum


def retrieveRandomWord(wordList):
    randIndex = randint(1, wordListSum(wordList))
    for word, value in wordList.items():
        randIndex -= value
        if randIndex <= 0:
            return word

def buildWordDict(text):
    # remove quebras de linha e aspas
    text = text.replace('\n', ' ')
    text = text.replace('"', '')

    # garante que sinais de pontuação sejam tratados como 'palavras' próprias,
    # de modo que sejam incluídos na cadeia de Markov
    punctuation = [',', '.', ';', ':']
    for symbol in punctuation:
        text = text.replace(symbol, ' {} '.format(symbol))
    
    words = text.split(' ')

    # filtra palavras vazias
    words = [ word for word in words if word != '']

    wordDict = {}

    for i in range(1, len(words)):
        if words[i-1] not in wordDict:
            # cria um novo dicionário para essa palavra
            wordDict[words[i-1]] = {}
        if words[i] not in wordDict[words[i-1]]:
            wordDict[words[i-1]][words[i]] = 0
        wordDict[words[i-1]][words[i]] += 1
    return wordDict


text = str(urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt').read(), 'utf-8')
wordDict = buildWordDict(text)

# gera uma cadeia de Markov de tamanho 100
length = 100
chain = ['I']
for i in range(0, length):
    newWord = retrieveRandomWord(wordDict[chain[-1]])
    chain.append(newWord)

print(' '.join(chain))