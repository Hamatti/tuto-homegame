from bs4 import BeautifulSoup
import urllib2
import unicodecsv

HEADERS = ['Subject', 'Start date', 'Start time']

url = 'http://www.tutohockey.fi/fi/ottelut/otteluohjelma-2018-19'
soup = BeautifulSoup(urllib2.urlopen(url))

regular_season = soup.find_all('tbody')[2].find_all('tr')[1:]

def format_date(datestring):
    day, month, year = datestring.split('.')
    return '%s/%s/%s' % (month, day, year)

def format_time(timestring):
    hours, minutes = timestring.split(':')
    ampm = 'AM'
    if int(hours) > 12:
        hours = int(hours) - 12
        ampm = 'PM'
    return '%s:%s %s' % (hours, minutes, ampm)

games = []
for game in regular_season:
    tds = game.find_all('td')
    home_g = [td for td in tds if tds[4].string == 'TUTO Hockey']
    if home_g:
        date = format_date(home_g[1].string)
        time = format_time(home_g[2].string)
        place = home_g[3].string
        home = home_g[4].string
        away = home_g[5].string

        gamestring = '%s - %s @ %s' % (home, away, place)
        games.append([gamestring, date, time])

writer = unicodecsv.writer(open('tutohomegames-2018.csv', 'w'), encoding='utf-8')
writer.writerow(HEADERS)
writer.writerows(games)
