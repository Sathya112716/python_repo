from python_repo.src.collections_namedtuples.util import calculate_average
import unittest
class MyTestCase(unittest.TestCase):
    def test1(self):
        #n=5,columns=5
        # ID         MARKS      NAME       CLASS
        # 1          97         Raymond    7
        #2          50         Steven     4
        #3          91         Adrian     9
        #4          72         Stewart    5
        #5          80         Peter      6   "
        actual_output = calculate_average()
        expected_output = 78.00
        self.assertEqual(actual_output, expected_output)  # Using the calendar module calculatd the expected output

    def test2(self):
        #n=2
        #ID         MARKS      NAME       CLASS
        #1          98        Sathya      6
        #2          78        Eniyan     4
        actual_output = calculate_average()
        expected_output = "88.0"
        self.assertEqual(actual_output, expected_output)

    def test3(self):
        # n=3
        #MARKS      CLASS      NAME       ID
        #92         2          Calum      1
        #82         5          Scott      2
        #94         2          Jason      3
        actual_output = calculate_average()
        expected_output = "89.33"
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
        unittest.main()
