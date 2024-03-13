
import logging
import numpy as np


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
def min_max_axis(arr,axis):
    array= np.array(arr)
    min_axis = np.min(array,axis=axis)
    return np.max(min_axis)


