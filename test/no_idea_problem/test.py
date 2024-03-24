import unittest
from python_repo.src.no_idea_problem.util import calculate_happiness

class MyTestCase(unittest.TestCase):
    def test1(self):
        #n, m = 3, 2
        #arr = [1, 5, 3]
        #set_like = {3, 1}
        #set_dislike = {5, 7}
        actual_output = calculate_happiness()
        expected_output = 1
        self.assertEqual(actual_output, expected_output)
    def test2(self):
        #n, m = 3, 1
        #arr = [1, 2, 3]
        #set_like = {3, 2}
        #set_dislike = {5, 4}
        actual_output = calculate_happiness()
        expected_output = 2
        self.assertEqual(actual_output, expected_output)

    def test3(self):
        #n, m = 4,3
        #arr = [5,3,2]
        #set_like = {1,2}
        #set_dislike = {6,5}
        actual_output = calculate_happiness()
        expected_output = 0
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
