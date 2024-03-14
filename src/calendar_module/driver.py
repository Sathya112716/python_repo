from util import find_day

import logging

date_input =input("Enter the date (MM DD YYYY): ")
month, day, year = map(int, date_input.split())
day_of_the_week = find_day(month, day, year)
logging.debug("The day on {} {} {} is: {}".format(month, day, year, day_of_the_week))



