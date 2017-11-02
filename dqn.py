import snake
import numpy as np
import random
from collections import deque
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

class DQNetwork(object):
    def __init__(self, state_size=100, num_hidden=24, learning_rate=0.1):
        self.state_size = state_size
        self.num_hidden = num_hidden
        self.learning_rate = learning_rate
        self.gamma = 0.95
        self.epsilon = 1.0
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
        num_hidden = self.num_hidden
        model = Sequential()

        model.add(Dense(num_hidden, input_dim=10, activation='relu'))
        model.add(Dense(num_hidden, activation='relu'))
        model.add(Dense(self.action_size, activation='linear'))

        model.compile(loss='mse', optimizer=Adam(lr=self.learning_rate))

        self.model = model

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
        minibatch = random.sample(self.memory, batch_size)

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

    def train(self, episodes=100):
        for i in range(episodes):
            state = self.snake.reset()[0]
            self.initSnake()

            for frame in range(100):
                #snake.render()
                action = self.act(state)

                next_state, next_dir, done, reward = self.snake.step(action)

                self.remember(state, action, reward, next_state, done)

                state = next_state

                if done:
                    print("episode: {}/{} score: {}".format(i, episodes, self.snake.score))
                    break

            self.replay(32)
