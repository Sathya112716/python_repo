import unittest
from python_repo.src.text_alignment.util import text_alignment_logo
class TestCase(unittest.TestCase):
   def test_something(self):
     expected_result = [
           '  H  ',
           ' HHH ',
           'HHHHH',
           ' HHH         HHH        ',
           ' HHH         HHH        ',
           ' HHH         HHH        ',
           ' HHH         HHH        ',
           ' HHHHHHHHHHHHHHH  ',
           ' HHHHHHHHHHHHHHH  ',
           ' HHH         HHH        ',
           ' HHH         HHH        ',
           ' HHH         HHH        ',
           ' HHH         HHH        ',
           '            HHHHH ',
           '             HHH  ',
           '              H   ',
       ]
     self.assertEqual(expected_result, text_alignment_logo(3))  ## add assertion here
if __name__ == '__main__':
   unittest.main()