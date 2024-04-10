
import datetime
import logging #import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def find_day():
    date_input=input("Enter the date:")
    month, day, year = map(int, date_input.split())
    day_of_the_week = datetime.date(year, month, day).weekday()
    days=['Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday','Sunday']
    logging.debug(days[day_of_the_week])

    return days[day_of_the_week].upper()
