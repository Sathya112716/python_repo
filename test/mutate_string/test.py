
import unittest
from python_repo.src.mutate_string.util import mutate_string


class TestCalAvg(unittest.TestCase):
    def test_mutate_string(self):
        actualoutput = mutate_string("sathya",2,'u')
        expectedoutput = "suthya"
        self.assertEqual(actualoutput, expectedoutput) ##second position is mutated

    def test_mutate_string(self):
        actualoutput = mutate_string("ravi", 4,'l')
        expectedoutput = "ravl"
        self.assertEqual(actualoutput, expectedoutput) ##4th position

    def test_mutate_string(self):
        actualoutput = mutate_string("ambika", 6,'y')
        expectedoutput = "ambiky"
        self.assertEqual(actualoutput, expectedoutput) #6th posotion

if __name__ == '__main__':
    unittest.main()