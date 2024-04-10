import unittest#import unittesting
from python_repo.src.find_the_percentage_problem.util import calc_average

class TestCalcAverage(unittest.TestCase):
    def test_calc_average(self):
        #n=2
        #student=Harsh 25 26.5 28
        #        Anurag 26 28 30
        #query_name=Harsh
        actual_output = calc_average()
        expected_output = '26.50'
        self.assertEqual(actual_output, expected_output)

    def test1_calc_average(self):
        #n = 3
        #student_data = ['ravi 10 20 79', 'ambika 33 66 77', 'priya 45 12 34']
        #query_name = 'ambika'
        actual_output = calc_average()
        expected_output = '58.67'
        self.assertEqual(actual_output, expected_output)

    def test2_calc_average(self):
        #n = 3
        #student_data = ['anu 23 44 67', 'avini 11 22 33', 'tharani 55 66 77']
        #query_name = 'avini'
        actual_output = calc_average()
        expected_output = '22.00'
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
