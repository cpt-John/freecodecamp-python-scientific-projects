import copy
import random


class Hat:
    def __init__(self, **kwargs: dict) -> None:
        self.contents = []
        for i in kwargs:
            self.contents.extend([i]*kwargs[i])

    def draw(self, n: int) -> list:
        random.shuffle(self.contents)
        selected = self.contents[:n].copy()
        self.contents = self.contents[n:].copy()
        return selected


def experiment(hat: Hat, expected_balls: dict, num_balls_drawn: int, num_experiments: int) -> float:
    required_combination = []
    for i in expected_balls:
        required_combination.extend([i]*expected_balls[i])
    success = 0
    for experiment in range(num_experiments):
        is_subset = True
        test_hat = copy.copy(hat)
        actual_drawn = test_hat.draw(num_balls_drawn)
        for ball in required_combination:
            try:
                actual_drawn.remove(ball)
            except:
                is_subset = False
                break
        success += 1 if is_subset else 0
    return success/num_experiments
