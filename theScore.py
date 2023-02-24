import requests
from bs4 import BeautifulSoup
from pprint import pprint
from datetime import datetime

url = 'https://www.thescore.com/nba/news'
data = requests.get(url)

my_data = []
teamDictionary = {}

soup = BeautifulSoup(data.content, 'html.parser')
row = soup.find('main')
articles = row.find('div', {'class': 'jsx-627093717 gameScoreRow'})
for article in articles:
    
    #games = row.find('div', {'class': 'jsx-627093717 gameScoreRow'})
    team1 = article.find('span', {'class': 'jsx-627093717 teamName'})
    score1 = article.find('span', {'class': 'jsx-627093717 teamName'})
    gameInfo = article.find('div',{'class': 'jsx-627093717 gameInfo'})
    team2 = article.find('span', {'class': 'jsx-627093717 teamName'})
    score2 = article.find('span', {'class': 'jsx-627093717 teamName'})
    print(team1,score1)
    print(gameInfo)
    print(team2,score2)
print(articles)