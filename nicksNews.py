import requests
from bs4 import BeautifulSoup
from pprint import pprint
from datetime import datetime
 
# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
print("date and time =", dt_string)

url = 'https://www.premierleague.com/tables'
data = requests.get(url)

#print(data.text)

my_data = []

html = BeautifulSoup(data.text, 'html.parser')
articles = html.select('tr')
print(articles)

rank = 0
counter = 0
print("Premier League Table on",dt_string)
for article in articles:
    rank+=1
    #name = article.select('.teamName')[0].get_text()
    #str = "a./clubs/1/"+name+"/overview"   
    #my_data.append({rank: name})
    row = article.findAll('td')
    currPosition = row[1].find('span', {'class': 'value'})
    prevPosition = row[1].find('span', {'class': 'resultHighlight'}).text.strip()
    team = row[2].find('span', {'class': 'long'}).text

    gamesPlayed = row[3].text

    gamesWon = row[4].text
    gamesLoss = row[6].text
    draws = row[5].text
    goalsFor = row[7].text
    goalsAg = row[8].text
    goalDiff = row[9].text.strip()
    points = row[10].text
    formAbv = []
    for form in row[11].find_all('li'):
        formAbv.append(form.find('abbr').text)
    
    print(team,gamesPlayed,gamesWon,draws,gamesLoss,goalsFor,goalsAg,goalDiff,points,formAbv)

#pointsList = html.find_all('a', class_=None)
# table = html.find('table')
# body = html.find('tbody')
# rows = html.find_all('tr')
# for row in rows:
#     #print(row)
    
#     #my_data.append({"row": row})
#     row = row.find_all('td')
#     currentPos = row[1].find('span',{'class':'value'}).text
#     lastPos = row[1].find('span',{'class':'resultHighlight'}).text
#     break
        
pprint(my_data[:20])
