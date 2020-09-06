
import requests
import datetime
from dateutil import rrule
from Parse import parse
from Calendar import makeCalendar

def handle(sola, razred, dijak):
    today = datetime.datetime.today()
    schoolyear = today.year
    if today.month < 8:
        schoolyear -= 1
    schoolyearStart = datetime.date(schoolyear, 9, 1)
    schoolyearEnd = datetime.date(schoolyear + 1, 6, 24)

    parseds = []
    mondays = []

    teden = 1
    monday = schoolyearStart + datetime.timedelta(days = -schoolyearStart.weekday())
    while teden <= 42:
        URL = "https://www.easistent.com/urniki/izpis/" + sola + "/" + str(razred) + "/0/0/0/" + str(teden) + "/" + str(dijak)
        page = requests.get(URL)
        parsed = parse(page)

        if parsed:
            parseds.append(parsed)
            mondays.append(monday)

        teden += 1
        monday += datetime.timedelta(weeks = 1)

    return makeCalendar(parseds, mondays)
