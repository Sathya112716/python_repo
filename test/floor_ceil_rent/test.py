from python_repo.src.floor_ceil_rint.util import print_floor_ceil_rint
import unittest
#import unittesting
class MyTestCase(unittest.TestCase):
    def test1(self):
        actual_output = print_floor_ceil_rint()#input=1.1 2.2 3.3
        expected_output = "(array([1., 2., 3.]), array([2., 3., 4.]), array([1., 2., 3.]))"
        self.assertEqual(str(actual_output), expected_output)

    def test2(self):
        actual_output = print_floor_ceil_rint()#1.1 2.2 3.3 4.4 5.5
        expected_output = "(array([1., 2., 3., 4., 5.]), array([2., 3., 4., 5., 6.]), array([1., 2., 3., 4., 6.]))"
        self.assertEqual(str(actual_output), expected_output)

    def test3(self):
        actual_output = print_floor_ceil_rint() #input
        expected_output = "(array([6., 7.]), array([7., 8.]), array([7., 8.]))"
        self.assertEqual(str(actual_output), expected_output)
if __name__ == '__main__':
    unittest.main()
