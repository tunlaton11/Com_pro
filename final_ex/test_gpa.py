import unittest
from gpa import split_input, map_grade, cal_grade


class SimpleTest(unittest.TestCase):
    def test_split_input_01(self):
        self.assertEqual(split_input("A, B+, b, C, c+, A"),
                         ['a', 'b+', 'b', 'c', 'c+', 'a'])

    def test_split_input_02(self):
        self.assertEqual(split_input("C, B+, A, a, c+, C"),
                         ['c', 'b+', 'a', 'a', 'c+', 'c'])

    def test_split_input_03(self):
        self.assertEqual(split_input("B, b+, a, c, c+, B"),
                         ['b', 'b+', 'a', 'c', 'c+', 'b'])

    def test_map_grade_01(self):
        self.assertEqual(
            map_grade(['a', 'b+', 'b', 'c', 'c+', 'a']), [4, 3.5, 3, 2, 2.5, 4])


unittest.main()
