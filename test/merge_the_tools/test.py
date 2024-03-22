import unittest
from python_repo.src.merge_the_tools.util import merge_the_tools

class MyTestCase(unittest.TestCase):
    def test1(selfself):
        actual_input=merge_the_tools()
        expected_output="""AB
    CA
    AD
    """
        self.assertEqual(actual_input,expected_output)
        '''
    AABCAADA
    3
        '''