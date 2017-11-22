import numpy as np
import random
from tkinter import *

class Snake(object):
    """SNAKE GAME :)=)))))))))))))))"""
    def __init__(self, dimension=9):
        self.actionSpace = {'Up': 0, 'Right': 1, 'Down': 2, 'Left': 3}
        self.fieldState = {'Empty': 0, 'Snake': 1, 'SnakeHead': 2, 'Apple': 3}
        self.dimension = dimension
        self.field = []
        self.snake = []
        self.score = 0

    def initGame(self, dimension):
        """Set player and first apple"""
        self.field = [[self.fieldState['Empty'] for i in range(dimension)] for j in range(dimension)]
        self.dimension = dimension
        self.initApple(dimension)
        self.initSnake()

    def initApple(self, dimension):
        self.createApple()

    def initSnake(self):
        posX = 5
        posY = 4
        length = 2
        self.field[posX][posY] = self.fieldState['SnakeHead']
        self.snake.append((posX, posY))

        for i in range(1, length+1):
            self.field[posX][posY-i] = self.fieldState['Snake']
            self.snake.append((posX, posY - i))


    def step(self, action):
        """Act with action upon enviroment """
        reward = 0
        headX, headY = self.snake[0]

        if action == 0:
            #up
            self.snake.insert(0, (headX-1, headY))

        if action == 1:
            #right
            self.snake.insert(0, (headX, headY+1))            

        if action == 2:
            #down
            self.snake.insert(0, (headX+1, headY))

        if action == 3:
            #left
            self.snake.insert(0, (headX, headY-1))

        headX, headY = self.snake[0]
        if self.checkNextAction(headX, headY):
            if self.field[headX][headY] == self.fieldState['Apple']:
                self.field = self.updateField(False)
                self.createApple()
                self.score = self.eatApple()
                reward = 1
            else:
                self.field = self.updateField(True)
                self.snake.pop()
            return (self.field, reward, self.score, False)
        else:
            return (self.field, reward, self.score, True)

    def checkNextAction(self, x, y):
        if not ((x < 0) or (y < 0)):
            try:
                self.field[x][y]
            except Exception as e:
                return (False)

            if not self.field[x][y] == self.fieldState['Snake']:
                return (True)
            else:
                return (False)
        else:
            return (False)

    def updateField(self, shorten):
        lenSnake = len(self.snake)

        for i in range(0, lenSnake-1):
            if i == 0:
                posX, posY = self.snake[0]
                self.field[posX][posY] = self.fieldState['SnakeHead']
            else:
                posX, posY = self.snake[i]
                self.field[posX][posY] = self.fieldState['Snake']

        if shorten:
            posX, posY = self.snake[lenSnake-1]
            self.field[posX][posY] = self.fieldState['Empty']

        return (self.field)

    def createApple(self):
        posX = random.randint(0, self.dimension-1)
        posY = random.randint(0, self.dimension-1)

        if not self.field[posX][posY]:
            self.field[posX][posY] = self.fieldState['Apple']
        else:
            self.createApple()


    def eatApple(self):
        self.score+=1
        return (self.score)

    def render(self, master=None, w=None, speedLimiter=None):
        """Render enviroment """
        if master and w:
            for i in range(self.dimension):
                for j in range(self.dimension):
                    if (self.field[i][j] == 3):
                        w.create_rectangle(20*j, 20*i, 20*j+20, 20*i+20, fill="red")
                    elif (self.field[i][j] == 2):
                        w.create_rectangle(20*j, 20*i, 20*j+20, 20*i+20, fill="green")
                    elif (self.field[i][j] == 1):
                        w.create_rectangle(20*j, 20*i, 20*j+20, 20*i+20, fill="lightgreen")
                    else:
                        w.create_rectangle(20*j, 20*i, 20*j+20, 20*i+20, fill="white")
            master.update()
            if speedLimiter:
                master.after(speedLimiter)
        else:
            for i in range(self.dimension):
                for j in range(self.dimension):
                    print(self.field[i][j], end=" ")
                print("")

    def reset(self):
        """Reset enviroment """
        self.field = []
        self.snake = []

        self.initGame(self.dimension)

        return (self.field, False, 0)