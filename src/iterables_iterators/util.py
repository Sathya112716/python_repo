import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def probability_of_letter():
    n = int(input())
    letters = input().split()
    k = int(input())

    indices = list(range(1, n + 1))
    total_combinations = len(indices) ** k
    combinations_with_letter = 0

    for i in range(1, k + 1):
        combinations_with_letter += len(set(letters[:i]))

    probability = combinations_with_letter / total_combinations
    return probability
probability = probability_of_letter()
logging.debug("{:.4f}".format(probability))