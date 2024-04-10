import logging #import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
import numpy as np

def print_floor_ceil_rint():
    arr = np.array(list(map(float, input().split())))
    floor_arr = np.floor(arr)
    ceil_arr = np.ceil(arr)
    rint_arr = np.rint(arr)
    return floor_arr, ceil_arr, rint_arr

floor_arr, ceil_arr, rint_arr = print_floor_ceil_rint()
logging.debug(floor_arr)
logging.debug(ceil_arr)
logging.debug(rint_arr)




