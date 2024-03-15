import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

import numpy as np

def calculate_statistics(arr):
    mean = np.mean(arr, axis=0), np.mean(arr, axis=1), np.mean(arr)
    var = np.var(arr, axis=0), np.var(arr, axis=1), np.var(arr)
    std = np.std(arr, axis=0), np.std(arr, axis=1), np.std(arr)
    return mean, var, std
