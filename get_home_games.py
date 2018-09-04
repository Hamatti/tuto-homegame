from bs4 import BeautifulSoup
import urllib2


url = 'http://www.tutohockey.fi/fi/ottelut/otteluohjelma'

soup = BeautifulSoup(urllib2.urlopen(url))

tbodies = soup.table.find_all('tbody')

games = []
for tbody in tbodies:
    for tr in tbody.find_all('tr'):
        tds = tr.find_all('td')
        home_g = [td for td in tds if tds[3].string == 'TUTO Hockey']
        if home_g:
            date = home_g[0].string
            print date
            time = home_g[1].string
            place = home_g[2].string
            home = home_g[3].string
            away = home_g[4].string
            games.append([date, time, place, home, away])

import unicodecsv

writer = unicodecsv.writer(open('tutohomegames-2017.csv', 'w'), encoding='utf-8')

writer.writerows(games)
