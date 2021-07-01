import copy
import random
from collections import Counter
# Consider using the modules imported above.

class Hat:
    def __init__(self, **hats):
        self.contents = []
        self.num_balls = 0
        for key, value in hats.items():
            for  i in range(int(value)):
                self.contents.append(key)
            self.num_balls += int(value)
    def draw(self, balls_num):
        if balls_num >= len(self.contents):return self.contents
        drawn = []
        for i in range(balls_num):
            removed = self.contents.pop(int(random.random()*len(self.contents)))
            drawn.append(removed)
        return drawn

def experiment(hat, expected_balls, num_drawn, num_experiments):
    if num_drawn > hat.num_balls: num_drawn = hat.num_balls
    experiments = []
    for i in range(0, num_experiments):
        experiments.append(random.sample(hat.contents, num_drawn))
    exp_count = []
    for i in experiments:
        exp_count.append(Counter(i))
    success = 0
    for i in exp_count:
        succ = True
        for k,v in expected_balls.items():
            if v > i[k] :
                succ = False
                break
        if succ:success += 1
    return success/num_experiments