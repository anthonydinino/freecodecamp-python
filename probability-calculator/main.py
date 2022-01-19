import random
import copy


class Hat:
    def __init__(self, **balls) -> None:
        contents = []
        for ball, count in balls.items():
            for i in range(count):
                contents.append(ball)
        self.contents = contents

    def draw(self, numOfDraws):
        if numOfDraws > len(self.contents):
            return self.contents
        drawn = []
        for i in range(numOfDraws):
            drawn.append(self.contents.pop(
                random.randrange(len(self.contents))))
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    matches = 0
    for i in range(num_experiments):
        match = True
        expected = copy.deepcopy(expected_balls)
        tempHat = copy.deepcopy(hat)
        drawn = tempHat.draw(num_balls_drawn)
        for ball in drawn:
            try:
                expected[ball] = expected[ball] - 1
            except:
                continue
        for ball, value in expected.items():
            if not value <= 0:
                match = False
        if(match):
            matches += 1
    return matches/num_experiments


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                         expected_balls={"red": 2, "green": 1},
                         num_balls_drawn=5,
                         num_experiments=10000)
print(probability)
