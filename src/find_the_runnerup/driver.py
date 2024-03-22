import logging
from python_repo.src.find_the_runnerup.util import find_runner_up_score

n = int(input("enter the number:"))
scores = list(map(int, input("enter the input:").split()))

logging.debug(find_runner_up_score(n,scores))