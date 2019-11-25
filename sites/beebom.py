import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import service.telegram as telegram

class Beebom:
    def __init__(self):
        pass
    
    def getNews(self):
        res = requests.get('https://beebom.com/category/news/')
        beebom_soup = BeautifulSoup(res.content, 'lxml')
        news_section = beebom_soup.find('div', { 'class': 'td-ss-main-content' })

        def getTime(s):
            actual_date = s.split('T')[0] +" " + s.split('T')[1].split('+')[0] + " +" + s.split('+')[1].split(':')[0]+ s.split('+')[1].split(':')[1]
            d = datetime.strptime(actual_date, "%Y-%m-%d %H:%M:%S %z")
            return int(d.timestamp())

        titles = [ 
            { 'title': post.find('h3', { 'class': 'td-module-title' }).text } 
            for post in news_section.find_all('div', { 'class': 'bee-list' }) 
        ]
        urls = [ 
            { 'url': post.find('a')['href'] } 
            for post in news_section.find_all('div', { 'class': 'bee-list' }) 
        ]
        timestamps = [
            { 'time': getTime(post.find('time')['datetime']) }
            for post in news_section.find_all('div', { 'class': 'bee-list' })
        ]
        payload = []
        for title, url, timestamp in zip(titles, urls, timestamps):
            payload.append({
                'title': title['title'],
                'url': url['url'],
                'time': timestamp['time']
            })
        return payload

    def latest_post(self):
        posts = self.getNews()
        return posts[0]