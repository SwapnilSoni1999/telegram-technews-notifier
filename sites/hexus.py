import requests
from bs4 import BeautifulSoup
import service.telegram as telegram

class Hexus:
    def __init__(self):
        pass

    def latest_news(self):
        res = requests.get('https://hexus.net/tech/')
        soup = BeautifulSoup(res.content, 'lxml')
        articles = soup.find('ul', { 'class': 'grid' })
        first_post = articles.find('div', { 'class': 'articlebox' })

        return {
            'title': first_post.find('h2').text.replace('\n', ''),
            'url': 'https://hexus.net' + first_post.find('a')['href']
        }
