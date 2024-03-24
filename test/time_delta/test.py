
import unittest
from python_repo.src.time_delta.util import get_time_difference


class MyTestCase(unittest.TestCase):
    def test1(self):
        #n=2
        #time1,time2,timestamp1,timestamp2="Sun 10 May 2015 13:54:36 -0700,Sun 10 May 2015 13:54:36 -0000,Sat 02 May 2015 19:54:36 +0530,Fri 01 May 2015 13:54:36 -0000
        actual_output=get_time_difference()
        expected_output=(25200,88200)
        self.assertEqual(actual_output,expected_output)
 # add assertion here


if __name__ == '__main__':
    unittest.main()
