import logging

from util import can_stack_cubes

if __name__ == "__main__":
    t = int(input().strip())
    test=[]
    for _ in range(t):
        n = int(input().strip())
        cubes = list(map(int, input().strip().split()))
        test.append(cubes)

    results = can_stack_cubes(test)
    for result in results:
        logging.debug(result)
