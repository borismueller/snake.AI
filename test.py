import dqn

d = dqn.DQNetwork()
#d.train(10000, False)
#d.train(1000, True, True)
#no speed limit
d.train(1000, True, False)