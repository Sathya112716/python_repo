import logging

from util import can_stack_cubes

if __name__ == "__main__":
    t = int(input().strip())
    test=[]
    for _ in range(t):
        n = int(input().strip())
        cubes = list(map(int, input().strip().split()))
        test.append(cubes)

    rslts = can_stack_cubes(test)
    for result in rslts:
        logging.debug(result)
