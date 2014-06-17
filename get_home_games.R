## Preprocessing - reading the game schedule and writing a csv of the home games
# Dependencies: XML

library(XML)

URL <- 'http://www.tutohockey.fi/fi/ottelut/otteluohjelma-2014-15'

table <- as.data.frame(readHTMLTable(URL))
names(table) <- c('date', 'time', 'place', 'home', 'away')

# Drop the "extra info" column
games <- table[-6]

# Only consider regular season games
games <- games[13:67,]

# Only home games
home_games <- games[games$home == 'TUTO Hockey',]

write.csv(home_games, file="tutohomegames.csv")