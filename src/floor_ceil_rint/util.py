import logging
import numpy as np
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
def floor_ceil_rint_calculate(arr):
    np.set_printoptions(sign=' ')
    floor_result = np.floor(arr)
    ceil_result = np.ceil(arr)
    rint_result = np.rint(arr)
    return floor_result, ceil_result, rint_result


