import unittest
from python_repo.src.merge_the_tools.util import merge_the_tools

class MyTestCase(unittest.TestCase): #import unittesting
    def test1(self):
        # s=AABCAAADA
        # k=3
        actual_output = merge_the_tools()
        expected_output = 'AB\nCA\nAD'
        self.assertEqual(actual_output, expected_output)

    def test2(self):
        # s=lolkok
        # k=2
        actual_output = merge_the_tools()
        expected_output = 'lo\nlk\nok'
        self.assertEqual(actual_output, expected_output)

    def test3(self):
        # s=satyay
        # k=3
        actual_output = merge_the_tools()
        expected_output = 'sat\nya'
        self.assertEqual(actual_output, expected_output)
