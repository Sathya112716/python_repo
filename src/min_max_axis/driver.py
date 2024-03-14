import logging
import numpy as np

from util import min_max_axis

n, m = map(int, input('enter the numbers(n m)').split())
arr = []
for _ in range(n):
        row = list(map(int, input().split()))
        arr.append(row)
axis = int(input("Enter axis (0 for columns, 1 for rows, None for overall): "))
rslt = min_max_axis(arr,axis)
logging.debug(rslt)

