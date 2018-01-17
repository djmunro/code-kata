import unittest

from bowling.game import Game


class GameTest(unittest.TestCase):

    def test_ball1_0_ball2_0_scores_0(self):
        game = Game()
        game.roll(0)
        self.assertEqual(0, game.score)
