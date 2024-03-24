import unittest
from python_repo.src.mean_var_std.util import calculate_statistics

class MyTestCase(unittest.TestCase):
    def test1_find_the_determinant_value(self):
        # input=2 2
        #       3 1
        #       4 5
        actual_mean, actual_var, actual_std = calculate_statistics()
        expected_mean = [1.5, 3.5]
        expected_var = [0.25, 0.25]
        expected_std = [0.5, 0.5]
        for actual, expected in zip((actual_mean, actual_var, actual_std), (expected_mean, expected_var, expected_std)):
            for a, e in zip(actual, expected):
                self.assertEqual(a, e)

    def test2_find_the_determinant_value(self):
        # input=2 2
        #       4 5
        #       6 7
        actual_mean, actual_var, actual_std = calculate_statistics()
        expected_mean = [4.5, 6.5]
        expected_var = [0.25, 0.25]
        expected_std = [0.5, 0.5]
        for actual, expected in zip((actual_mean, actual_var, actual_std), (expected_mean, expected_var, expected_std)):
            for a, e in zip(actual, expected):
                self.assertEqual(a, e)
    def test3_find_the_determinant_value(self):
        # input=1 1
        #       2 3
        actual_mean, actual_var, actual_std = calculate_statistics()
        expected_mean = [2.5]
        expected_var = [0.25]
        expected_std = [0.5]
        for actual, expected in zip((actual_mean, actual_var, actual_std), (expected_mean, expected_var, expected_std)):
            for a, e in zip(actual, expected):
                self.assertEqual(a, e)
if __name__ == '__main__':
    unittest.main()
