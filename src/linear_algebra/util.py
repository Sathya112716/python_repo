import numpy as np
import logging #import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_determinant():
    n = int(input())
    matrix = []
    for _ in range(n):
        row = list(map(float, input().split()))
        matrix.append(row)

    determinant = np.linalg.det(matrix)
    return determinant
determinant = calculate_determinant()
logging.debug("{:.2f}".format(determinant))

