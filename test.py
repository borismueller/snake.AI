import dqn

d = dqn.DQNetwork()
#d.train(1000, False)
#d.train(1000, True, 100)
#no speed limit
d.train(100, True, False)