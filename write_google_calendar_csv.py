'''
    Creates a Google calendar compatible CSV file
    from the csv file that is created with get_home_games.R

    Quick hack so it doesn't actually write csv, it just prints
    so I can append it to file via command line

    @author Juha-Matti Santala
    @licence MIT

    Usage: python write_google_calendar_csv.py >> [filename].csv
'''

from datetime import datetime, timedelta

# Print some headers, very important stuff for Google Cal

print 'Subject, Start Date, Start Time, End Date, End Time'
header = True
for line in open('tutohomegames-ajuniorit-2017.csv'):
    if header:
        header = False
        continue
    date, time, place, home, away = line.split(',')

    # Name of the event
    subject = '%s - %s' % (home.replace('"', ''), away.replace('"', ''))

    # Convert date from
    # Perjantai 12.09.14 => 9/12/2014

    day = date.split()[1]
    dates = day.split('.')
    day = '%s/%s/%s' % (dates[1], dates[0], dates[2].replace('"', ''))

    # Convert starting time from
    # 18.30 => 6.30 PM
    time = datetime.strptime(time.replace('"', ''), '%H.%M')
    start_time = time.strftime('%I:%M %p')

    # Matches end approx after 2,5 hours
    end_time = time + timedelta(hours=2.5)
    end_time = end_time.strftime('%I:%M %p')

    # Print the csv-line
    print "%s,%s,%s,%s,%s" % (subject.strip(), day, start_time, day, end_time)

