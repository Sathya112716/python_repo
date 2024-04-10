import unittest #import unittesting
from python_repo.src.word_order.util import count_word_occurrences


class TestCountWordOccurrences(unittest.TestCase):
    def test1_word(self):
        #n = 4
        #words = ['bcdef', 'abcdefg', 'bcde', 'bcdef']
        actual_output=count_word_occurrences()
        expected_output=(3,'2 1 1')
        self.assertEqual(actual_output,expected_output)

    def test2_word(self):
        #n = 2
        #words = ['asdfg','kljh']
        actual_output=count_word_occurrences()
        expected_output=(2,'1 1')
        self.assertEqual(actual_output,expected_output)

    def test3_word(self):
        #n = 2
        #words = ['qwert','opiu']
        actual_output=count_word_occurrences()
        expected_output=(2,'1 1')
        self.assertEqual(actual_output,expected_output)

if __name__ == '__main__':
    unittest.main()