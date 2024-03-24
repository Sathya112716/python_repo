import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def calculate_happiness():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    set_like = set(map(int, input().split()))
    set_dislike = set(map(int, input().split()))

    happiness = 0
    for num in arr:
        if num in set_like:
            happiness += 1
        elif num in set_dislike:
            happiness -= 1
    return happiness


result = calculate_happiness()
logging.debug(result)

