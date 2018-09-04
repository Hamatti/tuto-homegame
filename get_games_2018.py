from bs4 import BeautifulSoup
from selenium import webdriver

mestis_url = 'http://mestis.fi/index.php/ottelut/runkosarja.html'
browser = webdriver.PhantomJS()
browser.get(mestis_url)
html = browser.page_source
soup = BeautifulSoup(html, 'lxml')
games = soup.findAll('div', {'class': 'sgs-stats-game-row'})

