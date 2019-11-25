import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import service.telegram as telegram

class Digit:
    def __init__(self):
        pass      

    def latest_news(self):
        res = requests.get('https://www.digit.in/news/')
        digit_soup = BeautifulSoup(res.content ,'lxml')
        top_section = digit_soup.find('div', { 'class': 'block-newstop' })
        first_news = top_section.find('div', { 'class': 'review-main' })
        return {
            'title': first_news.find('a')['title'],
            'url': first_news.find('a')['href'],
            'time': int(time.time())
        }
