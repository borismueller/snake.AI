import numpy as np
import random
import dqn

class Optimizer(object):
    def __init__(self, seed=7, start=0.0, end=1.0, episodes=10):
        # fix random seed for reproducibility
        #np.random.seed(seed)
        #gammas = np.random.random(2)
        #epsilon_mins = np.random.random(2)
        #epsilon_decays = np.random.random(2)
        #learning_rate = np.random.random(2)

        start = 0.0
        end = 1.0
        for _ in range(20):
            if self.fun(start, end, episodes):
                start = start
                end = random.uniform(start, end)
            else:
                start = random.uniform(start, end)
                end = end
        print("start: {} end: {}".format(start, end))


    def fun(self, start, end, episodes):
        model = dqn.DQNetwork(epsilon=start)
        start_effciency = model.train(episodes=episodes)
        model = dqn.DQNetwork(epsilon=end)
        end_effciency = model.train(episodes=episodes)
        return start_effciency > end_effciency
