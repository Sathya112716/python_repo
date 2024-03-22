import unittest
from python_repo.src.No_idea_problem.util import calculate_happiness

class MyTestCase(unittest.TestCase):
    def test1(self):
        actual_input=calculate_happiness()
        expected_output=1
        self.assertEqual=(actual_input,expected_output)
        '''
        sample input
    3 2
    1 5 3
    3 1
    5 7
        '''