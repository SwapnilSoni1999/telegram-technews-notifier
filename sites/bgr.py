import requests
from bs4 import BeautifulSoup
import service.telegram as telegram

class BGR:
    def __init__(self):
        pass

    def latest_post(self):
        res = requests.get('https://www.bgr.in/category/news/')
        soup = BeautifulSoup(res.content, 'lxml')

        top = soup.find('div', { 'class': 'top_artcl' })
        first_post = top.find('div', { 'class': 'small_art' })
        return {
            'title': first_post.find('a')['title'].replace('\n', ''),
            'url': first_post.find('a')['href']
        }