import requests
import sys
sys.stdout.reconfigure(encoding='utf-8')


url = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'category=business&'
       'apiKey=2076819848004cae9fa59c6c3a9853cc')

response = requests.get(url)
articles = response.json()['articles']

news=[]

for article in articles:
    #print(article['title'])
    news.append("<p class='news'>"+article['title']+"</p>")
    news.append("<br>")
    

print(news)