import unittest #import unittesting
from python_repo.src.piling_up.util import can_stack_cubes

class TestCanStackCubes(unittest.TestCase):
    def test1(self):
        # 2
        # 6
        #4 3 2 1 3 4
        # 3
        # 1 3 2
        actual_output=can_stack_cubes()
        expected_output='No'
        self.assertEqual(actual_output,expected_output)

    def test2(self):
        # 1
        # 5
        #1 2 3 4 5
        # 2
        # 1 4 5
        actual_output=can_stack_cubes()
        expected_output='Yes'
        self.assertEqual(actual_output,expected_output)
if __name__ == '__main__':
    unittest.main()