import unittest

from fizz_buzz.FizzBuzz import FizzBuzz


class FizzBuzzTest(unittest.TestCase):
    def setUp(self):
        self.fizz_buzz = FizzBuzz()

    def test_of_numbers_not_divisible_by_three_or_five_is_number(self):
        self.assertThatAnswerFor(1, 1)
        self.assertThatAnswerFor(2, 2)
        self.assertThatAnswerFor(4, 4)
        self.assertThatAnswerFor(7, 7)

    def test_numbers_divisible_by_three_is_Fizz(self):
        self.assertThatAnswerFor(3, 'Fizz')
        self.assertThatAnswerFor(6, 'Fizz')

    def test_numbers_divisible_by_five_is_Buzz(self):
        self.assertThatAnswerFor(5, 'Buzz')
        self.assertThatAnswerFor(10, 'Buzz')

    def test_numbers_divisible_by_three_and_five_is_FizzBuzz(self):
        self.assertThatAnswerFor(15, 'FizzBuzz')
        self.assertThatAnswerFor(30, 'FizzBuzz')

    def test_0_throws_error(self):
        self.assertRaises(ValueError, self.fizz_buzz.of, 0)

    def test_numbers_less_than_0_throws_error(self):
        self.assertRaises(ValueError, self.fizz_buzz.of, -1)

    def assertThatAnswerFor(self, number, expected):
        self.assertEqual(expected, self.fizz_buzz.of(number))
