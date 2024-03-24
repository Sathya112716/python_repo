import unittest
from python_repo.src.python_string_formatted.util import print_formatted


class TestCase(unittest.TestCase):
    def test1(self):
        # input =17
        actual_output = print_formatted()
        expected_output =17 21 11 10001
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
