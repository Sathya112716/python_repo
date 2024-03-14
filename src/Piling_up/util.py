import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
def can_stack_cubes(test_cases):
    results = []
    for cubes in test_cases:
        left = 0
        right = len(cubes) - 1
        prev_cube = float('inf')

        while left <= right:
            if cubes[left] <= cubes[right]:
                if cubes[right] <= prev_cube:
                    prev_cube = cubes[right]
                    right -= 1
                else:
                    results.append("No")
                    break
            else:
                if cubes[left] <= prev_cube:
                    prev_cube = cubes[left]
                    left += 1
                else:
                    results.append("No")
                    break
        else:
            results.append("Yes")

    return results
