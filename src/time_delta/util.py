import logging
from datetime import datetime

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def get_time_difference():
    num_testcases = int(input().strip())
    for _ in range(num_testcases):
        timestamp1 = input().strip()
        timestamp2 = input().strip()

        date_format = "%a %d %b %Y %H:%M:%S %z"
        time1 = datetime.strptime(timestamp1, date_format)
        time2 = datetime.strptime(timestamp2, date_format)

        time_difference = abs((time1 - time2).total_seconds())
        yield int(time_difference)
for time_difference in get_time_difference():
    logging.debug(time_difference)



