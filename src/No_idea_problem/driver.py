import logging
from util import calculate_happiness

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    like_set = list(map(int, input().split()))
    dislike_set = list(map(int, input().split()))

    happiness = calculate_happiness(n, m, arr, like_set, dislike_set)
    logging.debug(happiness)
