import requests
import json

credentials = json.load(open('config.json', 'r'))

token = credentials['BOT_TOKEN'] # Your Bot token from config.json
chat_id = credentials['chat_id'] # Message you want to send to a specific chat!

def sendMessage(message):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    param = f'?chat_id={chat_id}&text={message}'
    request_url = url + param
    res = requests.get(request_url)
    print(res.json())

def getUpdates():
    res = requests.get(f'https://api.telegram.org/bot{token}/getUpdates')
    print(res.json())

def send_alert(source, title, url):
    sendMessage(f'New post on {source}!\n{title}\n{url}')
