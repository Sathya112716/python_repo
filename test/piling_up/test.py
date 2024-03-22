import unittest
from python_repo.src.Piling_up.util import can_stack_cubes

class TestCanStackCubes(unittest.TestCase):
    def can_stack_cube(self):
        self.assertEqual(can_stack_cubes(6, [4, 3, 2, 1, 3, 4]), "Yes")
        self.assertEqual(can_stack_cubes(3, [1, 3, 4]), "No")

if __name__ == '__main__':
    unittest.main()