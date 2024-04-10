import unittest #import unittesting
from python_repo.src.linear_algebra.util import calculate_determinant

class MyTestCase(unittest.TestCase):
    def test1_find_the_determinant_value(self):
        # N = 2
        # matrix_value = [[1.1, 1.1], [1.1, 1.1]]
        actual_output = calculate_determinant()
        expected_output = 0.0
        self.assertAlmostEqual(actual_output, expected_output)

    def test2_find_the_determinant_value(self):
        # N = 2
        # matrix_value = [[1.1, 1.2], [1.1, 1.1]]
        actual_output = calculate_determinant()
        expected_output = 0.0
        self.assertAlmostEqual(actual_output, expected_output)

    def test3_find_the_determinant_value(self):
        # N = 2
        # matrix_value = [[1.2, 1.2], [1.1,1.1]]
        actual_output = calculate_determinant()
        expected_output = 0.0
        self.assertAlmostEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
