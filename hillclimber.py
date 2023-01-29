#!/usr/bin/python3

from solution import SOLUTION
import constants as c
import copy

class HILL_CLIMBER:
	def __init__(self):
		self.parent = SOLUTION()
	def Evolve(self):
		self.parent.Evaluate()
		for currentGeneration in c.numberOfGenerations:
			self.Spawn()
			self.Mutate()
			self.child.Evaluate()
			self.Select()
	def Spawn(self):
		self.child = copy.deepcopy(self.parent)

	def Mutate(self):
		pass
	def Evaluate(self):
		pass
	def Select(self):
		pass
