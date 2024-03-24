
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
def can_stack_cubes():
    T = int(input())  # Number of test cases

    for _ in range(T):
        n = int(input())  # Number of cubes
        blocks = list(map(int, input().split()))
    left = 0  # Initialize left pointer
    right = n - 1  # Initialize right pointer

    prev_cube = float('inf')  # Initialize previous cube with positive infinity

    while left <= right:
        if blocks[left] >= blocks[right]:
            # Choose the leftmost cube
            if blocks[left] <= prev_cube:
                prev_cube = blocks[left]
                left += 1
            else:
                return "No"
        else:
            # Choose the rightmost cube
            if blocks[right] <= prev_cube:
                prev_cube = blocks[right]
                right -= 1
            else:
                return "No"

    return "Yes"

result = can_stack_cubes()
logging.debug(result)
