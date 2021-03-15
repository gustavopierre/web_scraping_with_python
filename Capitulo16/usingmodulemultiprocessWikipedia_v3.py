from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
from multiprocessing import Process, freeze_support, Queue
import os
import time


def task_delegator(taskQueue, urlsQueue):
    # Inicializa com uma tarefa para cada processo
    visited = ['/wiki/Kevin_Bacon', '/wiki/Monty_Python']
    taskQueue.put('/wiki/Kevin_Bacon')
    taskQueue.put('/wiki/Monty_Python')
    while 1:
        # Verifica se há novos links em urlsQueue
        # para serem processados
        if not urlsQueue.empty():
            links = [link for link in urlsQueue.get() if link not in visited]
            for link in links:
                # Adiciona um novo link em taskQueue
                taskQueue.put(link)


def get_links(bs):
    
    links = bs.find('div', {'id': 'bodyContent'}).find_all('a', 
        href=re.compile('^(/wiki/)((?!:).)*$'))
    return [link.attrs['href'] for link in links]


def scrape_article(taskQueue, urlsQueue):
    while 1:
        while taskQueue.empty():
            # Dorme por 100ms enquanto espera a fila de tarefas
            # Isso deve ser raro
            time.sleep(.1)

        path = taskQueue.get()
        html = urlopen('http://en.wikipedia.org{}'.format(path))
        time.sleep(5)
        bs = BeautifulSoup(html, 'html.parser')
        title = bs.find('h1').get_text
        print('Scraping {} in process {}'.format(title, os.getpid()))
        links = get_links(bs)
        # Envia ao código de delegação para processamento
        urlsQueue.put(links)



if __name__ == '__main__':    
    freeze_support()
    
    processes = []
    taskQueue = Queue()
    urlsQueue = Queue()
    
    processes.append(Process(target=task_delegator, args=(taskQueue, urlsQueue,)))
    processes.append(Process(target=scrape_article, args=(taskQueue, urlsQueue,)))
    processes.append(Process(target=scrape_article, args=(taskQueue, urlsQueue,)))
    
    for p in processes:
        p.start()
    # for p in processes:
    #     p.join()
