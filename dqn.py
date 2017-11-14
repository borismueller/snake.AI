import snake
import numpy as np
import random
import tensorflow as tf
from collections import deque
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

from termcolor import colored

class DQNetwork(object):
    def __init__(self, state_size=100, learning_rate=0.8117, epsilon=0.606):
        #learning_rate = 0.8117 after testing
        #Epsilon = 0.606 after testing
        self.state_size = state_size
        self.learning_rate = learning_rate
        self.gamma = 0.2
        self.epsilon = epsilon
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.memory = deque(maxlen=2000)
        self.initSnake()
        self.action_size = len(self.snake.actionSpace)
        self.initModel()

    def initSnake(self, dimension=10, seed=3):
        self.snake = snake.Snake()
        self.snake.initGame(10, 3)

    def initModel(self):
        model = Sequential()

        model.add(Dense(100, input_dim=10, activation='relu'))
        model.add(Dense(100, activation='relu'))
        model.add(Dense(100, activation='relu'))
        model.add(Dense(self.action_size, activation='linear'))

        model.compile(loss='mse', optimizer=Adam(lr=self.learning_rate))

        self.model = model
        return model

    def act(self, state):
        if np.random.randn() <= self.epsilon:
            #chooes random action
            return random.choice(list(self.snake.actionSpace.items()))[1]
        else:
            #predict action based on model
            actions = self.model.predict(state)
            return np.argmax(actions[0])

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def replay(self, batch_size):
        try:
            minibatch = random.sample(self.memory, batch_size)
        except Exception as e:
            #happens when the first epsiodes aren't long enough
            pass

        for state, action, reward, next_state, done in minibatch:
            #make reward our target if done
            target = reward

            if not done:
                #predict future discounted reward
                target = (reward + self.gamma * np.amax(self.model.predict(next_state)[0]))

        #predict future reward based on current state using our network
        target_f = self.model.predict(state)
        target_f[0][action] = target

        #train the network
        self.model.fit(state, target_f, epochs=1, verbose=0)

    def train(self, episodes=20, render=False):
        tot_score = 0
        high_score = 0
        for i in range(episodes):
            state = self.snake.reset()[0]
            self.initSnake()

            for frame in range(1000):
                if render:
                    self.snake.render()
                    print("")
                action = self.act(state)

                next_state, next_dir, done, reward = self.snake.step(action)
                self.remember(state, action, reward, next_state, done)
                state = next_state
                if (self.epsilon * self.epsilon_decay >= self.epsilon_min):
                    self.epsilon *= self.epsilon_decay

                if done:
                    tot_score += self.snake.score
                    if self.snake.score > high_score:
                        high_score = self.snake.score
                    if self.snake.score > 0:
                        print(colored("episode: {}/{} score: {}, after: {} frames".format(i, episodes, self.snake.score, frame), "green"))
                    else:
                        print("episode: {}/{} score: {}, after: {} frames".format(i, episodes, self.snake.score, frame))
                    break

            self.replay(3)
        print("done after {} episodes, total score: {}, efficency: {}/{} = {}, high score: {}".format(episodes, tot_score, episodes, tot_score, tot_score/episodes, high_score))
        return(tot_score/episodes, high_score)

    def save(self, name):
        self.model.save_weights(name)

    def load(self, name):
        self.model.load_weights(name)
