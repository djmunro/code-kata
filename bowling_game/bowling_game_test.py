import unittest

from bowling_game.bowling_game import Game


class BowlingGameTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_roll_zeros(self):
        self.roll_many(0, 20)
        self.assertEqual(0, self.game.score())

    def test_roll_ones(self):
        self.roll_many(1, 20)
        self.assertEqual(20, self.game.score())

    def test_one_spare(self):
        self.roll_spare()
        self.game.roll(3)
        self.roll_many(0, 17)
        self.assertEqual(16, self.game.score())

    def test_one_strike(self):
        self.roll_strike()
        self.game.roll(3)
        self.game.roll(4)
        self.roll_many(0, 16)
        self.assertEqual(24, self.game.score())

    def test_perfect_game(self):
        self.roll_many(10, 12)
        self.assertEqual(300, self.game.score())

    def roll_many(self, pins, times):
        for _ in range(times):
            self.game.roll(pins)

    def roll_spare(self):
        self.game.roll(5)
        self.game.roll(5)

    def roll_strike(self):
        self.game.roll(10)
