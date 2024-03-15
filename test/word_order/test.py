import unittest
from python_repo.src.word_order.util import count_word_occurrences


class TestCountWordOccurrences(unittest.TestCase):
    def test_word_counting(self):
        n = 4
        words = ['bcdef', 'abcdefg', 'bcde', 'bcdef']
        expected_result = {'bcdef': 2, 'abcdefg': 1, 'bcde': 1}
        self.assertEqual(count_word_occurrences(n, words), expected_result)

if __name__ == '__main__':
    unittest.main()