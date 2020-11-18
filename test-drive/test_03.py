"""63070224"""

import unittest
from ex_03_63070224 import filter_words, word_count


class SimpleTest01(unittest.TestCase):
    def test_filter_words01(self):
        self.assertEqual(filter_words(
            "he is the superman!@##"), "he is the superman")

    def test_filter_words02(self):
        self.assertEqual(filter_words(
            "the apple!! is on the table___!@#$!"), "the apple is on the table")

    def test_filter_words03(self):
        self.assertEqual(filter_words(
            "aaa  !!@$!@#@!#"), "aaa  ")


class SimpleTest02(unittest.TestCase):
    def test_word_count01(self):
        self.assertEqual(word_count("he is the superman"),
                         (['he', 'is', 'the', 'superman'], [1, 1, 1, 1]))

    def test_word_count02(self):
        self.assertEqual(word_count("aa bb cc aa"),
                         (['aa', 'bb', 'cc'], [2, 1, 1]))

    def test_word_count03(self):
        self.assertEqual(word_count("i love you very very much"),
                         (['i', 'love', 'you', 'very', 'much'], [1, 1, 1, 2, 1]))


unittest.main()
