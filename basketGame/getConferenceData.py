import requests
from bs4 import BeautifulSoup
from conversions import *

def getConfData():
    URL = f'https://www.basketball-reference.com/boxscores/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    #Get Conference Data
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
        
        
    return([easternData,westernData])
