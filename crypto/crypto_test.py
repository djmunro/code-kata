import unittest

from crypto.crypto import Crypto


class CryptoTest(unittest.TestCase):
    def setUp(self):
        self.crypto = Crypto()

    def test_decrypt_a(self):
        self.assertMessageIs('a', '!')

    def test_decrypt_b(self):
        self.assertMessageIs('b', ')')

    def test_decrypt_foo(self):
        self.assertMessageIs('foo', '*dd')

    def assertMessageIs(self, exptected_message, encrypted_message):
        message = self.crypto.decrypt(encrypted_message)
        self.assertEqual(exptected_message, message)