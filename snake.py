import numpy as np
import random

class Snake(object):
    """SNAKE GAME :)=)))))))))))))))"""
    def __init__(self, dimension=8):
        self.dimension = dimension
        self.seed = random.randint(0, 10)
        self.action_space = {'Left': 0, 'Right': 1, 'Nothing': 2}

    def step(self, action):
        """Act with action upon enviroment """
        # TODO:

    def reset(self):
        """Reset enviroment """
        # TODO:
        
    def render(self):
        """Render enviroment """
        # TODO: do this last

    def close(self):
        """End everything & clean up """
        # TODO: not very important

    def seed(self, seed):
        """ set seed for all random actions """
        # TODO:
