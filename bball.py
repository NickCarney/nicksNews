import requests
from bs4 import BeautifulSoup
import time
from conversion import *
 
URL = f'https://www.basketball-reference.com/boxscores/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")


content = soup.find(id='content')
date = content.find('h1')
date = date.text

print(date)
print('----------------------------------------\n\n')

games = soup.find(class_='game_summaries')
games = games.find_all(class_='game_summary expanded nohover')

for game in games[1:]:
    tables = game.find_all('table')

    #table1 = tables[0]
    table2 = tables[1]
    table3 = tables[2]

    # #Get data from first table
    # team1, team2 = table1.find_all('tr')
    # team1 = team1.find_all('td')
    # team2 = team2.find_all('td')

    # team1Name = team1[0].text
    # team1Score = int(team1[1].text)

    # team2Name = team2[0].text
    # team2Score = int(team2[1].text)
    # OT = team2[2].text.strip()      #If no OT empty string, else 'OT'


    #Get data from second table
    data = {}

    table2body = table2.find('tbody')
    team1Data, team2Data = table2body.find_all('tr')

    team1Data = team1Data.find_all('td')
    team1Name = team1Data[0].find('a').text
    team1Data = [int(i.text) for i in team1Data[1:]]
   
    team2Data = team2Data.find_all('td')
    team2Name = team2Data[0].find('a').text
    team2Data = [int(i.text) for i in team2Data[1:]]

    if len(team2Data) == 5:
        data[team1Name] = {1:team1Data[0], 2:team1Data[1], 3:team1Data[2], 4:team1Data[3], 5:team1Data[4], 'T':sum(team1Data)}         #Dictionary within a dictionary
        data[team2Name] = {1:team2Data[0], 2:team2Data[1], 3:team2Data[2], 4:team2Data[3], 5:team2Data[4], 'T':sum(team2Data)}

    else:
        data[team1Name] = {1:team1Data[0], 2:team1Data[1], 3:team1Data[2], 4:team1Data[3], 'T':sum(team1Data)}         #Dictionary within a dictionary
        data[team2Name] = {1:team2Data[0], 2:team2Data[1], 3:team2Data[2], 4:team2Data[3], 'T':sum(team2Data)}


    
    #Get third table data
    pts, trb = table3.find_all('tr')

    pts = pts.find_all('td')
    trb = trb.find_all('td')

    ptsName, ptsTeam = pts[1].text.split('-')
    ptsScore = int(pts[2].text)

    trbName, trbTeam = trb[1].text.split('-')
    trbScore = int(trb[2].text)

    data['pts'] = {'name':ptsName, 'team':ptsTeam, 'points':ptsScore}
    data['trb'] = {'name':trbName, 'team':trbTeam, 'points':trbScore}



    
    for key in data:
        print(f'{key} : {data[key]}')


    print('\n----------------------------------------\n')
    #This should be a function that returns the data dictionary


conferenceSection = soup.find(class_='standings_confs data_grid section_wrapper')
easternConf, westernConf = conferenceSection.find_all('table')
easternData = {}
westernData = {}

easternRows = easternConf.find_all('tr')
easternHeader = easternRows[0]
easterRows = easternRows[1:]
easternHeader = [i.text for i in easternHeader.find_all('th')]

for data in easterRows:
    team = data.find('th').text
    data = data.find_all('td')
    data = [checkFloat(i.text) for i in data]

    easternData[team] = data

westernRows = westernConf.find_all('tr')
westernHeader = westernRows[0]
westernRows = westernRows[1:]
westernHeader = [i.text for i in westernHeader.find_all('th')]

for data in westernRows:
    team = data.find('th').text
    data = data.find_all('td')
    data = [checkFloat(i.text) for i in data]

    westernData[team] = data
    
    
print(easternData,westernData)