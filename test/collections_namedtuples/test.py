from python_repo.src.collections_namedtuples.util import calculate_average
import unittest
class MyTestCase(unittest.TestCase):
    def test_something(self):
        res=calculate_average()
        self.assertEqual(res, '79.33')  # add assertion here

    def test_something(self):
        res=calculate_average()
        self.assertEqual(res, '86.98')

    def test_something(self):
        res=calculate_average()
        self.assertEqual(res, '57.90')


if __name__ == '__main__':
    unittest.main()