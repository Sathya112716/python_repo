import unittest #import unittesting
from python_repo.src.min_max_axis.util import min_max

class TestMinimumMaximum(unittest.TestCase):
    def test1_minimum_maximum(self):
        #arr = [[2, 5], [3, 7], [1, 3], [4, 0]]  # Define the input array
        actual_output = min_max()  # Call min_max function with the input array
        expected_output = 3
        self.assertEqual(actual_output, expected_output)

    def test2_minimum_maximum(self):
        #arr = [[3, 5], [3, 4], [1, 3], [4, 0]]  # Define the input array
        actual_output = min_max()  # Call min_max function with the input array
        expected_output = 3
        self.assertEqual(actual_output, expected_output)
    def test3_minimum_maximum(self):
        #arr = [[2, 3], [1, 2], [1, 3]]  # Define the input array
        actual_output = min_max()  # Call min_max function with the input array
        expected_output = 1
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
