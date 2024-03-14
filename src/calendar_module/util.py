import calendar

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def find_day(month, day, year):
    weekday_index = calendar.weekday(year, month, day)
    return calendar.day_name[weekday_index].upper()
