
import unittest
from python_repo.src.python_string_formatted.util import print_formatted


class TestCase(unittest.TestCase):
    def print_formatted(self):
        self.assertEqual(print_formatted(4), '  1   1   1   1\n  2   2   2  10\n  3   3   3  11\n  4   4   4 100')

if __name__ == '__main__':
    unittest.main()
