import requests
from bs4 import BeautifulSoup
import service.telegram as telegram

class GSMArena:
    def __init__(self):
        pass

    def latest_post(self):
        res = requests.get('https://www.gsmarena.com/news.php3')
        soup = BeautifulSoup(res.content, 'lxml')
        top_post = soup.find('div', { 'class': 'news-item' })
        return {
            'title': top_post.find('h3').text.replace('\n', ''),
            'url': 'https://www.gsmarena.com/' + top_post.find('a')['href']
        }