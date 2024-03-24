
import unittest
from python_repo.src.find_the_runnerup.util import find_runner_up_score


class TestCalAvg(unittest.TestCase):
    def test_find_runner_up_score(self):
        #n = 5
        #scores = [4,6,1,7,9]
        actual_output = find_runner_up_score()
        expected_output = 7
        self.assertEqual(actual_output, expected_output)

    def test1_find_the_runnerup(self):
        #n = 6
        #scores=[8,4,5,2,9,3]
        actual_output = find_runner_up_score()
        expected_output = 8
        self.assertEqual(actual_output, expected_output)

    def test2_find_the_runnerup(self):
        #n = 3
        #scores = [4,1,5]
        actual_output = find_runner_up_score()
        expected_output =4
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
