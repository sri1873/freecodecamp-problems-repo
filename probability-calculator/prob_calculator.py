import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, num):
        if num <= len(self.contents):
            pass
        else:
            num = len(self.contents)
        drawn_l = (random.sample(self.contents, num))
        for i in drawn_l:
            self.contents.remove(i)
        return drawn_l


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    expected = []
    for i in range(num_experiments):
        expected_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        ball_drawn = hat_copy.draw(num_balls_drawn)
        for ball in ball_drawn:
            if ball in expected_copy:
                expected_copy[ball] -= 1

        if (all(x <= 0 for x in expected_copy.values())):
            count += 1

    probability = count / num_experiments
    return probability
