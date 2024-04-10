import unittest #import unittesting
import logging
from python_repo.src.mutate_string.util import mutate_string
class MyTestCase(unittest.TestCase):
    def test1_mutate_string(self):
        #string="priya
        #p,c=3 t
        actual_output=mutate_string()
        expected_output='prita'
        self.assertEqual(actual_output,expected_output)
    def test2_mutate_string(self):
        #string=lalitha
        #p,c=4 s
        actual_output=mutate_string()
        expected_output='lalisha'
        self.assertEqual(actual_output,expected_output)

    def test3_mutate_string(self):
        #string=ravi
        #p,c=1 c
        actual_output=mutate_string()
        expected_output='rcvi'
        self.assertEqual(actual_output,expected_output)
if __name__ == '__main__':
    unittest.main()
