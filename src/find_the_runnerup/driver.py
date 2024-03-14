import logging
from util import find_runner_up_score
n = int(input("enter the number:"))
scores = list(map(int, input("enter the input:").split()))

runner_up_score = find_runner_up_score(n,scores)
logging.debug(runner_up_score)
