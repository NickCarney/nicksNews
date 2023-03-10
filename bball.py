import requests
from bs4 import BeautifulSoup
from conversion import *
 
URL = f'https://www.basketball-reference.com/boxscores/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
table = soup.find('table')

head = table.find('thead')
for table in soup.find_all('table'):
    rows = table.find_all('tr')
    for row in rows:
        name = row.get('data-stat')
        print(name)
        data = row.find_all('td')
        for datum in data:           
            print(checkNone(datum.text), end=',')
    print()

    