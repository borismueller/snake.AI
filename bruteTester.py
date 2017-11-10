import numpy as np
import random
import dqn

class Tester(object):
	def __init__(self, seed=7, episodes=10000):
		bestEpsilon = 0
		bestEfficiency = 0
		epsilon = random.uniform(0, 1)

		for i in range(100)
			model = dqn.DQNetwork(epsilon=epsilon)
			efficiency = model.train(episodes=episodes)
			if (efficiency[0] >= bestEfficiency):
				efficiencyList = list()
				for y in range(20):
					model = dqn.DQNetwork(epsilon=epsilon)
					efficiency = model.train(episodes=episodes)
					efficiencyList.append(efficiency)
					print("Internal For {} External For {}".format(y, i))
				avgEfficiency = self.avgCalc(efficiencyList)
				if (avgEfficiency >= bestEfficiency):
					bestEpsilon = epsilon
				epsilon = random.uniform(bestEpsilon - 1, bestEpsilon + 1)
				print("Epsilon {}".format(bestEpsilon))
			print("For {}".format(i))
		print("Epsilon {}".format(bestEpsilon))

	def avgCalc(self, efficiencyList):
		tot = 0
		for i in range(len(efficiencyList)):
			tot += efficiencyList[i][0]
		return tot/len(efficiencyList)