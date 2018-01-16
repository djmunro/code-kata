import unittest

from prime_factors.prime_factors import PrimeFactors


class PrimeFactorsTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(self.list(), PrimeFactors.generate(1))

    def list(self):
        return []
