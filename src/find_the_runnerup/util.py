import logging #import util

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
def find_runner_up_score():
    n = int(input("enter the number:"))
    scores = list(map(int, input("enter the input:").split()))

    uniq_scores = sorted(set(scores), reverse=True)
    return uniq_scores[1]  if len(uniq_scores) > 1 else "No second maximum found"
logging.debug(find_runner_up_score())

