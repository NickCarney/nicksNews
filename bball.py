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
        if('data-stat' in row):
            name = row.get('th')
            print(name.text)
        data = row.find_all('td',class_=True)
        for datum in data:   
            #if(datum['class']):
            print(datum['class'][0],end=":")        
            print(datum.text)
    print()

    