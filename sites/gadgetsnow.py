import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import service.telegram as telegram

class GadgetsNow:
    def __init__(self):
        pass

    def get_latest_news(self):

        def getTime(s):
            taim = datetime.strptime(s, '%d %b %Y, %H:%M')
            return int(taim.timestamp())


        res = requests.get('https://www.gadgetsnow.com/latest-news')
        soup = BeautifulSoup(res.content, 'lxml')
        news_section = soup.find('div', { 'class': [ 'tech_list', 'ctn_stories' ] })
        top_post = news_section.find('li')
        return {
            'title': top_post.find('a')['title'].replace('\n', ''),
            'url': 'https://www.gadgetsnow.com' + top_post.find('a')['href'],
            'time': getTime(top_post.find('span', { 'class': 'w_bylinec' })['rodate'])
        }