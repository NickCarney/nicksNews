import requests
from bs4 import BeautifulSoup
from conversions import *


def getGameData():
    URL = f'https://www.basketball-reference.com/boxscores/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    data = {}
    
    #Get Date
    content = soup.find(id='content')
    date = content.find('h1')
    date = date.text

    data['date'] = date
   



    #Get Game Data
    games = soup.find(class_='game_summaries')
    games = games.find_all(class_='game_summary expanded nohover')

    for game in games:

        tables = game.find_all('table')

        table2 = tables[1]
        table3 = tables[2]

        #Get data from second table

        table2body = table2.find('tbody')
        team1Data, team2Data = table2body.find_all('tr')

        team1Data = team1Data.find_all('td')
        team1Name = team1Data[0].find('a').text
        team1Data = [int(i.text) for i in team1Data[1:]]
    
        team2Data = team2Data.find_all('td')
        team2Name = team2Data[0].find('a').text
        team2Data = [int(i.text) for i in team2Data[1:]]

        #account for OT, 2OT, 3OT
        if len(team2Data) == 5:
            data[team1Name] = {1:team1Data[0], 2:team1Data[1], 3:team1Data[2], 4:team1Data[3], 5:team1Data[4], 'T':sum(team1Data)}         #Dictionary within a dictionary
            data[team2Name] = {1:team2Data[0], 2:team2Data[1], 3:team2Data[2], 4:team2Data[3], 5:team2Data[4], 'T':sum(team2Data)}
       
        elif len(team2Data) == 6:
            data[team1Name] = {1:team1Data[0], 2:team1Data[1], 3:team1Data[2], 4:team1Data[3], 5:team1Data[4], 6:team1Data[5], 'T':sum(team1Data)}         #Dictionary within a dictionary
            data[team2Name] = {1:team2Data[0], 2:team2Data[1], 3:team2Data[2], 4:team2Data[3], 5:team2Data[4], 6:team2Data[5], 'T':sum(team2Data)}

        elif len(team2Data) == 7:
            data[team1Name] = {1:team1Data[0], 2:team1Data[1], 3:team1Data[2], 4:team1Data[3], 5:team1Data[4], 6:team1Data[5], 7:team1Data[6], 'T':sum(team1Data)}         #Dictionary within a dictionary
            data[team2Name] = {1:team2Data[0], 2:team2Data[1], 3:team2Data[2], 4:team2Data[3], 5:team2Data[4], 6:team2Data[5], 7:team2Data[6], 'T':sum(team2Data)}

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


    return data
