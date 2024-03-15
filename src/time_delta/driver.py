import logging
from util import get_time_difference


n = int(input())
for _ in range(n):
    timestamp1 = input().strip()
    timestamp2 = input().strip()
    logging.debug(get_time_difference(timestamp1, timestamp2))

