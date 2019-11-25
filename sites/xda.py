import requests
from bs4 import BeautifulSoup
import service.telegram as telegram

class XDA:
    def __init__(self):
        pass

    def latest_post(self):
        res = requests.get('https://www.xda-developers.com/category/xda-news/')
        soup = BeautifulSoup(res.content, 'lxml')
        first_post = soup.find('div', { 'class': [ 'layout_post_1', 'type-post' ] })
        return {
            'title': first_post.find('h4').text,
            'url': first_post.find('a')['href']
        }