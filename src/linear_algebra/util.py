import numpy as np

def calculate_determinant():
    n = int(input())
    matrix = []
    for _ in range(n):
        row = list(map(float, input().split()))
        matrix.append(row)
    determinant = round(np.linalg.det(matrix), 2)
    return determinant
