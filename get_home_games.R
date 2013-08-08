## Preprocessing - reading the game schedule and writing a csv of the home games

URL <- 'http://www.tutohockey.fi/fi/ottelut/otteluohjelma-2013-14'

table <- as.data.frame(readHTMLTable(URL))
names(table) <- c('date', 'time', 'place', 'home', 'away')

games <- table[-6]
games <- games[13:64,]

home_games <- games[games$home == 'TUTO Hockey',]

write.csv(home_games, file="tutohomegames.csv")