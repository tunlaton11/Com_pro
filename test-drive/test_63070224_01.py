"""63070224"""

import unittest
from tdd_63070224_01 import split_input, map_grade, cal_gpa


class SimpleTest01(unittest.TestCase):
    def test_split_input01(self):
        self.assertEqual(split_input('a, B+, b, c, C+'),
                         ['a', 'b+', 'b', 'c', 'c+'])

    def test_split_input02(self):
        self.assertEqual(split_input('a, B+, A, c, C+'),
                         ['a', 'b+', 'a', 'c', 'c+'])

    def test_split_input03(self):
        self.assertEqual(split_input('a, B+, b, A, A'),
                         ['a', 'b+', 'b', 'a', 'a'])


class SimpleTest02(unittest.TestCase):
    def test_map_grade01(self):
        self.assertEqual(
            map_grade(['a', 'b+', 'b', 'c', 'c+']), [4, 3.5, 3, 2, 2.5])

    def test_map_grade02(self):
        self.assertEqual(
            map_grade(['b', 'b+']), [3, 3.5])

    def test_map_grade03(self):
        self.assertEqual(
            map_grade(['a', 'b+', 'b', 'a', 'b']), [4, 3.5, 3, 4, 3])


class SimpleTest03(unittest.TestCase):
    def test_cal_gpa01(self):
        self.assertEqual(cal_gpa([4, 3.5, 3, 2, 2.5]), 3.0)

    def test_cal_gpa02(self):
        self.assertEqual(cal_gpa([4, 4, 4, 4]), 4.0)

    def test_cal_gpa03(self):
        self.assertEqual(cal_gpa([4, 3.5]), 3.75)


unittest.main()
