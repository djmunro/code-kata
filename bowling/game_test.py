import unittest

from bowling.game import Game


class GameTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_ball1_0_ball2_0_scores_0(self):
        self.roll_frame(0, 0)
        self.assertGameScoreIs(0)

    def test_ball1_1_ball2_0_scores_1(self):
        self.roll_frame(1, 0)
        self.assertGameScoreIs(1)

    def roll_frame(self, first_ball, second_ball):
        self.game.roll(first_ball)
        self.game.roll(second_ball)

    def assertGameScoreIs(self, score):
        self.assertEqual(score, self.game.score)
