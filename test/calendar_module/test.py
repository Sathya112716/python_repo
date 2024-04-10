
import unittest #import unittesting
from python_repo.src.calendar_module.util import find_day


class TestCalAvg(unittest.TestCase):
    def test1(self):
        #date_input="03 22 2024"
        actual_output= find_day()
        expected_output = "FRIDAY"
        self.assertEqual(actual_output, expected_output)#Using the calendar module calculatd the expected output

    def test2(self):
        #date_input="03 11 2024"
        actual_output = find_day()
        expected_output = "MONDAY"
        self.assertEqual(actual_output, expected_output)

    def test3(self):
        #date_input="03 03 2024"
        actual_output = find_day()
        expected_output = "SUNDAY"
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
