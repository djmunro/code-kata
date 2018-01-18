class Game(object):
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        total = 0
        frame_index = 0
        for frame in range(10):
            if self.is_strike(frame_index):  # strike
                total += self.strike_bonus(frame_index)
                frame_index += 1
            elif self.is_spare(frame_index):
                total += self.spare_bonus(frame_index)
                frame_index += 2
            else:
                total += self.sum_of_balls_in_frame(frame_index)
                frame_index += 2
        return total

    def strike_bonus(self, frame_index):
        return 10 + self.rolls[frame_index + 1] + self.rolls[frame_index + 2]

    def is_strike(self, frame_index):
        return self.rolls[frame_index] == 10

    def is_spare(self, frame_index):
        return self.rolls[frame_index] + self.rolls[frame_index + 1] == 10

    def spare_bonus(self, frame_index):
        return 10 + self.rolls[frame_index + 2]

    def sum_of_balls_in_frame(self, frame_index):
        return self.rolls[frame_index] + self.rolls[frame_index + 1]
