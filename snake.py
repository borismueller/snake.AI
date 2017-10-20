import numpy as np
import random

class Snake(object):
    """SNAKE GAME :)=)))))))))))))))"""
    def __init__(self, dimension=9, seed=None):
        random.seed(3)
        if (seed == None):
            self.seed = random.randint(0, 10)
        else:
            self.seed = seed

        self.actionSpace = {'Left': 0, 'Right': 1, 'Nothing': 2}
        self.fieldState = {'Empty': 0, 'Snake': 1, 'SnakeHead': 2, 'Apple': 3}
        self.directions = {'North': 0, 'East': 1, 'South': 2, 'West': 3}
        self.dimension = dimension
        self.field = []
        self.snake = []
        self.snakeDirection = self.directions['North']
        self.initGame(dimension, seed)
        self.render()

    def step(self, action):
        """Act with action upon enviroment """

        print(self.snake)

        if (action == 2):
            #go forward, change head position
            oldSnake = self.snake
            (headX, headY) = self.snake[0]
            if (self.snakeDirection == 0):
                #North
                self.snake.insert(0, (headX, headY + 1))
            elif (self.snakeDirection == 1):
                #East
                self.snake.insert(0, (headX + 1, headY))
            elif (self.snakeDirection == 2):
                #South
                self.snake.insert(0,(headX, headY - 1))
            elif (self.snakeDirection == 3):
                #West
                self.snake.insert(0, (headX - 1, headY))

        #reset last part of snake
        (x, y) = self.snake.pop()
        self.field[x][y] = self.fieldState['Empty']

        for snek in self.snake:
            (x, y) = snek
            self.field[x][y] = self.fieldState['Snake']
            snek = self.field[x][y]

        #add new snake head
        (x, y) = self.snake[0]
        self.field[x][y] = self.fieldState['SnakeHead']

    def reset(self):
        """Reset enviroment """
        self.field = []
        self.snake = []

    def render(self):
        """Render enviroment """
        field = self.field
        for i in range(self.dimension):
            for j in range(self.dimension):
                print(field[i][j], end=" ")
            print("")

    def close(self):
        """End everything & clean up """
        # TODO: not very important

    def seed(self, seed):
        """ set seed for all random actions """
        # TODO:



    def initGame(self, dimension, seed):
        """Set player and first apple"""
        self.field = [[self.fieldState['Empty'] for i in range(dimension)] for j in range(dimension)]
        random.seed(seed)
        appleSeed = random.randint(0, dimension - 1)
        self.initApple(dimension, appleSeed)
        self.initSnake()

    def initApple(self, dimension, seed):
        #TODO make sure apple doenst spawn in snake
        random.seed(seed)
        posY = random.randint(0, dimension - 1)
        self.field[seed][posY] = self.fieldState['Apple']

    def initSnake(self):
        posX = 5
        posY = 4
        length = 2
        self.field[posX][posY] = self.fieldState['SnakeHead']
        self.snake.append((posX, posY))

        for i in range(1, length+1):
            self.field[posX][posY-i] = self.fieldState['Snake']
            self.snake.append((posX, posY - i))

        self.snakeDirection = self.directions['East']

    def eatApple(self):
        #TODO
        print("hahah")
