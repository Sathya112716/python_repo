import unittest
import logging
from python_repo.src.mutate_string.util import mutate_string
class MyTestCase(unittest.TestCase):
    def test1_mutate_string(self):
        self.assertEqual(mutate_string("sathya",2,"u"),"suthya") ##second position is mutated)


if __name__ == '__main__':
    unittest.main()
