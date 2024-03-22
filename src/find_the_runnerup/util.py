import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
def find_runner_up_score(n,scores):
    uniq_scores = sorted(set(scores), reverse=True)
    return uniq_scores[1]  if len(uniq_scores) > 1 else "No second maximum found"


