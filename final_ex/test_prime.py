import unittest
from prime import check_prime


class SimpleTest(unittest.TestCase):
    def test_prime_01(self):
        self.assertEqual(check_prime(5), True)

    def test_prime_02(self):
        self.assertEqual(check_prime(4), False)

    def test_prime_03(self):
        self.assertEqual(check_prime(10), False)

    def test_prime_04(self):
        self.assertEqual(check_prime(11), True)

    def test_prime_05(self):
        self.assertTrue(check_prime(29))


unittest.main()
