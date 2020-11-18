"""63070224"""

import unittest
from ex_02_63070224 import valid_day, valid_month, valid_year, leap_year


class SimpleTest01(unittest.TestCase):
    def test_valid_day01(self):
        self.assertEqual(valid_day(31, 10, 2001), True)

    def test_valid_day02(self):
        self.assertEqual(valid_day(12, 10, 2012), True)

    def test_valid_day03(self):
        self.assertEqual(valid_day(29, 2, 2005), False)


class SimpleTest02(unittest.TestCase):
    def test_valid_month01(self):
        self.assertEqual(valid_month(12), True)

    def test_valid_month02(self):
        self.assertEqual(valid_month(0), False)

    def test_valid_month03(self):
        self.assertEqual(valid_month(2), True)


class SimpleTest03(unittest.TestCase):
    def test_valid_year01(self):
        self.assertEqual(valid_year(2001), True)

    def test_valid_year02(self):
        self.assertEqual(valid_year(2020), True)

    def test_valid_year03(self):
        self.assertEqual(valid_year(0), False)


class SimpleTest04(unittest.TestCase):
    def test_leapyear01(self):
        self.assertEqual(leap_year(1600), True)

    def test_leapyear02(self):
        self.assertEqual(leap_year(2019), False)

    def test_leapyear03(self):
        self.assertEqual(leap_year(2000), True)


unittest.main()
