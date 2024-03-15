
import unittest
from python_repo.src.calendar_module.util import calendar_module


class TestCalAvg(unittest.TestCase):
    def test(self):
        actualoutput = calendar_module("28 12 2022")
        expectedoutput = "WEDNESDAY"
        self.assertEqual(actualoutput, expectedoutput)

    def test1_mutate_string(self):
        actualoutput = calendar_module("26 07 2021")
        expectedoutput = "MONDAY"
        self.assertEqual(actualoutput, expectedoutput)

    def test_mutate_string(self):
        actualoutput = calendar_module("12 10 2020")
        expectedoutput = "MONDAY"
        self.assertEqual(actualoutput, expectedoutput)

if __name__ == '__main__':
    unittest.main()
