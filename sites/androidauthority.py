import cfscrape
from bs4 import BeautifulSoup
import service.telegram as telegram

class AndroidAuthority:
    def __init__(self):
        pass

    def latest_news(self):
        scraper = cfscrape.create_scraper()
        res = scraper.get('https://www.androidauthority.com/news/')
            
        soup = BeautifulSoup(res.content, 'lxml')
        top_news = soup.find('div', { 'id': 'page' })
        # print(top_news)
        first_news = top_news.find('div', { 'class': [ 'aa_hfp_container', 'add-active' ] })
        # print(first_news)

        return {
            'title': first_news.find('h3').text,
            'url': first_news.find('a', { 'class': 'overlay-link' })['href']
        }