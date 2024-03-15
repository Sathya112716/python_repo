import unittest
from python_repo.src.Iterables_Iterators.util import probability_of_letter

class TestProbability(unittest.TestCase):
    def test_case_1(self):
        result = probability_of_letter(4, ['s', 'a', 't', 'r'], 2)
        self.assertAlmostEqual(result, 0.8333, places=4)

if __name__ == "__main__":
    unittest.main()