import requests
from bs4 import BeautifulSoup
import service.telegram as telegram

class TechRadar:
    def __init__(self):
        pass

    def latest_news(self):
        res = requests.get('https://www.techradar.com/in/news')
        soup = BeautifulSoup(res.content, 'lxml')
        first_post = soup.find('div', { 'id': 'Item1' })

        return {
            'title': first_post.find('a')['aria-label'].replace('\n', ''),
            'url': first_post.find('a')['href']
        }