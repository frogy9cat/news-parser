# from bs4 import BeautifulSoup
import requests
import json
from datetime import datetime, timezone



url = "https://newsapi.org/v2/everything?q=apple&from=2024-08-07&to=2024-08-07&sortBy=popularity&apiKey=f7abe08883c6489d881d5b98be2a16aa"
news = []

response = requests.get(url).json()
articles = response['articles']


for i in range(0, 12):
    article = articles[i]
    new_article = {}

    new_article['title'] = article['title']
    new_article['author'] = article['author']
    new_article['text'] = article['content']
    new_article['link'] = article['url']
    
    publishDate = article['publishedAt'][:10]
    publishTime = article['publishedAt'][11:19]
    DateTime = publishDate + " " + publishTime
    DateTime = datetime.strptime(DateTime, '%Y-%m-%d %H:%M:%S')
    DateTime_utc = DateTime.replace(tzinfo=timezone.utc).timestamp()
    new_article['DateTime_utc'] = DateTime_utc

    # with open('result.json', '+a') as json_file:
    #     writable = json.dumps(new_article)
    #     json_file.write(writable)
    news.append(new_article)

# all_news = {'news': f'{news}'}
# print(all_news)
with open('result.json', 'w+') as json_file:
    writable = json.dumps(news)
    json_file.write(writable)