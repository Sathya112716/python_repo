import unittest
from python_repo.src.linear_algebra.util import calculate_determinant

class MyTestCase(unittest.TestCase):
    def test1_find_the_determinant_value(self):
        N = 2
        matrix_value = [[1.1, 1.1], [1.1, 1.1]]
        result = calculate_determinant(N, matrix_value)
        self.assertEqual(result, 0.0)

    def test_find_the_determinant_value1(self):
        N = 2
        matrix_value = [[2.2, 2.2], [2.2, 2.2]]
        result = calculate_determinant(N, matrix_value)
        self.assertEqual(result, 0.0)



if __name__ == '__main__':
    unittest.main()