from util import find_runner_up_score
import logging
n = int(input("enter the number:"))
scores = list(map(int, input("enter the input:").split()))

runner_up_score = find_runner_up_score(n,scores)
logging.debug(runner_up_score)
