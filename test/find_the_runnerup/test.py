
import unittest
from python_repo.src.find_the_runnerup.util import find_runner_up_score


class TestCalAvg(unittest.TestCase):
    def test_find_runner_up_score(self):
        n = 3
        scores = [4,6,1,7,9]
        actualoutput = find_runner_up_score(scores)
        expectedoutput = 7
        self.assertEqual(actualoutput, expectedoutput)

    def test1_find_the_runnerup(self):
        n = 6
        scores=[8,4,5,2,9,6]
        actualoutput = find_runner_up_score(scores)
        expectedoutput = 8
        self.assertEqual(actualoutput, expectedoutput)

    def test2_find_the_runnerup(self):
        n = 3
        scores = [4,1,5,8,10]
        actualoutput = find_runner_up_score(scores)
        expectedoutput = 8
        self.assertEqual(actualoutput, expectedoutput)


if __name__ == '__main__':
    unittest.main()
