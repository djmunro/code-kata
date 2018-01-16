import unittest

from prime_factors.prime_factors import PrimeFactors


class PrimeFactorsTest(unittest.TestCase):
    def list(self, *args):
        list = []
        for i in args:
            list.append(i)
        return list

    def test_one(self):
        self.assertEqual(self.list(), PrimeFactors.generate(1))

    def test_two(self):
        self.assertEqual(self.list(2), PrimeFactors.generate(2))

    def test_three(self):
        self.assertEqual(self.list(3), PrimeFactors.generate(3))

    def test_four(self):
        self.assertEqual(self.list(2, 2), PrimeFactors.generate(4))

    def test_six(self):
        self.assertEqual(self.list(2, 3), PrimeFactors.generate(6))

    def test_eight(self):
        self.assertEqual(self.list(2, 2, 2), PrimeFactors.generate(8))

    def test_nine(self):
        self.assertEqual(self.list(3, 3), PrimeFactors.generate(9))
