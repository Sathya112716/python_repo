
import logging
import numpy as np


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
def min_max():
    X, _ = map(int, input().split())
    array = []
    for _ in range(X):
        row = list(map(int, input().split()))
        array.append(row)
    min_values = np.min(array, axis=1)
    max_value = np.max(min_values)
    return max_value

result = min_max()
logging.debug(result)




