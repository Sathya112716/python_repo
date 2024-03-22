import logging
from util import calculate_average

n = int(input())
columns = input().split()
students = [input().split() for _ in range(n)]

logging.debug(calculate_average(students))



