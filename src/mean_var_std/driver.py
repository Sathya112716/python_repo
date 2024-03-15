import logging

from util import calculate_statistics

X, Y = map(int, input().split())
arr = []
for _ in range(X):
    arr.append(list(map(int, input().split())))

mean, var, std = calculate_statistics(arr)

logging.debug(mean)
logging.debug(var)
logging.debug(std)

