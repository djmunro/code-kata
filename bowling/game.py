class Game(object):
    def __init__(self):
        self.score = 0

    def roll(self, score):
        self.score += score
