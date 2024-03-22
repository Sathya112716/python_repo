import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def calculate_happiness(n, m, arr, like_set, dislike_set):
    happiness = 0
    like_set = set(like_set)
    dislike_set = set(dislike_set)

    for num in arr:
        if num in like_set:
            happiness += 1
        elif num in dislike_set:
            happiness -= 1

    return happiness
