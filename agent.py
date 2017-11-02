import snake
import random

class Agent(object):
    def __init__(self, episodes=100000, dimension=10, seed=3):
        self.snake = snake.Snake()
        self.snake.initGame(10, 3)
        self.randomAction(episodes)

    def randomAction(self, episodes, render=True):
        actions = self.snake.actionSpace

        actions = self.snake.actionSpace
        for i in range(episodes):
            self.snake.render()
            self.snake.step(random.choice(list(actions.items()))[1])
            print("score::", self.snake.score)
            print("episode: ", i)
