import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
from datetime import datetime, timedelta

def get_time_difference(timestamp1, timestamp2):
    format_str = "%a %d %b %Y %H:%M:%S %z"
    time1 = datetime.strptime(timestamp1, format_str)
    time2 = datetime.strptime(timestamp2, format_str)
    time_diff = abs(time1 - time2)
    return int(time_diff.total_seconds())
