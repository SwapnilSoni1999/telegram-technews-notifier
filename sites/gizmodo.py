import requests
from bs4 import BeautifulSoup
import json
import service.telegram as telegram

class Gizmodo:
    def __init__(self):
        pass

    def latest_post(self):
        res = requests.get('https://gizmodo.com/tag/technology')
        soup = BeautifulSoup(res.content, 'lxml')
        news_section = soup.find('div', { 'class': ['sc-17uq8ex-0','fXQFHn'] })
        article = news_section.find('article')
        
        data = article.find('div', { 'class': [ 'js_editor-tools', 'sc-1i9kufk-0', 'cKYknA' ] })['data-state']
        return {
            'title': article.find('h2').text,
            'url': json.loads(data)['postPermalink']
        }
