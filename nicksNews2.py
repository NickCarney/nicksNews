import requests
from bs4 import BeautifulSoup
 
URL = f'https://www.premierleague.com/tables?team=FIRST&co=1&se=489&ha=-1'
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
table = soup.find('table')
#tbody = table.find('tbody')
rows = table.find_all('tr')
head = table.find('thead')

th = head.find_all('th')
print(th[1].text.strip(),th[2].text.strip(),th[3].text.strip(),th[4].text.strip(),th[5].text.strip(),th[6].text.strip(),th[7].text.strip(),th[8].text.strip(),th[9].text.strip(),th[10].text.strip())

#print()
counter=0
for row in rows:
    counter+=1
    #print(row)
    row = row.find_all('td')
    currPosition = row[1].find('span', {'class': 'value'}).text
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
    if(counter==19):
        break