import logging
import numpy as np
from util import floor_ceil_rint_calculate

arr = np.array(input().split(), float)
floor_result, ceil_result, rint_result = floor_ceil_rint_calculate(arr)

logging.debug(floor_result)
logging.debug(ceil_result)
logging.debug(rint_result)
