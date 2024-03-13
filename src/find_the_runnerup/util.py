import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
def find_runner_up_score(n,scores):
    unique_scores = sorted(set(scores), reverse=True)
    return unique_scores[1]