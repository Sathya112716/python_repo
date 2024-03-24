import unittest
from python_repo.src.iterables_iterators.util import probability_of_letter

class TestProbability(unittest.TestCase):
    def test_case_1(self):
        #indices=4,letters=aacd,k=2
        actual_output= probability_of_letter()
        expected_output="0.125"
        self.assertEqual(actual_output,expected_output)

    def test_case_2(self):
        #indices=5,letters=sghig,k=3
        actual_output= probability_of_letter()
        expected_output="0.024"
        self.assertEqual(actual_output,expected_output)

    def test_case_3(self):
        #indices=5,letters=cdefg,k=2
        actual_output= probability_of_letter()
        expected_output="0.08"
        self.assertEqual(actual_output,expected_output)
if __name__ == "__main__":
    unittest.main()