import unittest
from python_repo.src.min_max_axis.util import min_max_axis

class TestMinimumMaximum(unittest.TestCase):
    def test_minimum_maximum(self):
        arr = [[2, 5],
               [3, 7],
               [1, 3],
               [4, 0]]
        result = min_max_axis(arr)
        self.assertEqual(result, 3)  # Correct the expected result to 3

if __name__ == '__main__':
    unittest.main()