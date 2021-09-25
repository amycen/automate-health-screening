import json
import requests
from bs4 import BeautifulSoup
from string import Template
from re import search
from datetime import datetime

NYC_SCHOOLS_URL = 'https://www.schools.nyc.gov/'
START_YEAR = 2021
END_YEAR = 2022
CALENDAR_URL_TEMPLATE = Template(f'{NYC_SCHOOLS_URL}about-us/news/$start-$end-school-year-calendar')

def is_school_closed(date, calendar):
    if date in calendar:
        print("YES")
    else:
        print("NO")


def get_calendar():
    calendar = []
    calendar_url = CALENDAR_URL_TEMPLATE.substitute({'start': 2021, 'end': 2022})
    r = requests.get(calendar_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    headers = soup.find_all('th')
    calendar_keys = []
    for header in headers:
        calendar_keys.append(header.string.strip())
    rows = soup.tbody.children
    
    year = START_YEAR
    for row in rows:
        #refactor to dynamic unpack based on headers size
        date, _, comment = row.contents
        if "schools close" in comment.text:
            date_text = date.text.strip()
            if "Jan" in date_text.split()[0]:
                year = END_YEAR
            # tidy up soft hyphen
            date_text = date_text.replace('\xad', '')
            date_text = date_text.replace('\u00ad', '')
            date_text = date_text.replace('\N{SOFT HYPHEN}', '')
            # for some weird reason their - character is unicode 8211
            if chr(8211) in date_text:
                start, end = date_text.split(chr(8211))
                month, start_day = start.split()
                month = month.strip()
                for day in range(int(start_day.strip()), int(end.strip())+1):
                    calendar.append(f'{month} {day} {year}')
            # elif "-" in date_text:
            #     start, end = date_text.split("-")
            else:
                calendar.append(f'{date_text} {year}')
    return calendar

cal = get_calendar()
today = datetime.today().strftime("%B %#d %Y")
is_school_closed(today, cal)