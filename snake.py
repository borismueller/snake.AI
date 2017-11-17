import numpy as np
import random
from tkinter import *

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
        self.snakeDirection = self.directions['East']
        self.score = 0
        #self.initGame(dimension, seed)
        #self.render()

    def step(self, action):
        """Act with action upon enviroment """

        (headY, headX) = self.snake[0]

        if (action == 0):
            #go left
            if (self.snakeDirection == 0):
                #North
                self.snake.insert(0, (headY, headX - 1))
                self.snakeDirection = 3
            elif (self.snakeDirection == 1):
                #East
                self.snake.insert(0, (headY - 1, headX))
                self.snakeDirection = 0
            elif (self.snakeDirection == 2):
                #South
                self.snake.insert(0,(headY, headX + 1))
                self.snakeDirection = 1
            elif (self.snakeDirection == 3):
                #West
                self.snake.insert(0, (headY + 1, headX))
                self.snakeDirection = 2

        if (action == 1):
            #go right
            if (self.snakeDirection == 0):
                #North
                self.snake.insert(0, (headY, headX + 1))
                self.snakeDirection = 1
            elif (self.snakeDirection == 1):
                #East
                self.snake.insert(0, (headY + 1, headX))
                self.snakeDirection = 2
            elif (self.snakeDirection == 2):
                #South
                self.snake.insert(0,(headY, headX - 1))
                self.snakeDirection = 3
            elif (self.snakeDirection == 3):
                #West
                self.snake.insert(0, (headY - 1, headX))
                self.snakeDirection = 0

        elif (action == 2):
            #go forward, change head position
            if (self.snakeDirection == 0):
                #North
                self.snake.insert(0, (headY - 1, headX))
            elif (self.snakeDirection == 1):
                #East
                self.snake.insert(0, (headY, headX + 1))
            elif (self.snakeDirection == 2):
                #South
                self.snake.insert(0,(headY + 1, headX))
            elif (self.snakeDirection == 3):
                #West
                self.snake.insert(0, (headY, headX - 1))


        #check if we ate an apple
        (x, y) = self.snake[0]
        if not self.eatApple(x, y):
            #reset last part of snake, because we didn't eat an apple
            (a, b) = self.snake.pop()
            self.field[a][b] = self.fieldState['Empty']
            reward = 0
        else:
            reward = 1

        #redraw snake
        #TODO kill snake when it hits itself
        for snek in self.snake:
            (x, y) = snek
            try:
                self.field[x][y] = self.fieldState['Snake']
            except IndexError:
                #self.reset()
                #we ran into a wall :C
                return (self.field, self.snakeDirection, True, reward)
            snek = self.field[x][y]



        #add new snake head
        (x, y) = self.snake[0]
        self.field[x][y] = self.fieldState['SnakeHead']

        return (self.field, self.snakeDirection, False, reward)

    def reset(self):
        """Reset enviroment """
        self.field = []
        self.snake = []

        self.initGame(self.dimension, self.seed)

        return (self.field, self.snakeDirection, False, 0)

    def render(self, master, w):
        """Render enviroment """
        for i in range(self.dimension):
            for j in range(self.dimension):
                if (self.field[i][j] == 3):
                    w.create_rectangle(20*i, 20*j, 20*i+20, 20*j+20, fill="red")
                    #print("@", end=" ")
                elif (self.field[i][j] == 2):
                    w.create_rectangle(20*i, 20*j, 20*i+20, 20*j+20, fill="green")
                    #print("o", end=" ")
                elif (self.field[i][j] == 1):
                    w.create_rectangle(20*i, 20*j, 20*i+20, 20*j+20, fill="lightgreen")
                    #print(".", end=" ")
                else:
                    w.create_rectangle(20*i, 20*j, 20*i+20, 20*j+20, fill="white")
                    #print(" ", end=" ")
                #print(self.field[i][j], end=" ")
            print("")
        master.update()

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
        self.dimension = dimension
        self.initApple(dimension, appleSeed)
        self.initSnake()

    def initApple(self, dimension, seed):
        #TODO sometimes recurses forever
        #random.seed(seed)
        posY = random.randint(0, dimension - 1)

        if self.field[seed][posY] == 0:
            #position is empty
            self.field[seed][posY] = self.fieldState['Apple']
            self.applePos = (seed, posY)
        else:
            #try again
            self.initApple(dimension, posY)

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

    def eatApple(self, x, y):
        if (x, y) == self.applePos:
            self.score += 1
            self.initApple(self.dimension, self.seed)
            return True
        else:
            return False
