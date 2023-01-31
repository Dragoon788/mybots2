#!/usr/bin/python3

from pathlib import Path
from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
	def __init__(self):
		for i in range(0, c.populationSize):
			if Path("brain" + str(i) + ".nndf").is_file():
				os.system("rm brain" + str(i) + ".nndf")
			if Path("data/fitness" + str(i) + ".nndf").is_file():
				os.system("rm data/fitness" + str(i) + ".txt")
		self.parents = {}
		self.nextAvailableID = 0

		for i in range(0,c.populationSize):
			self.parents[i] = SOLUTION(self.nextAvailableID)
			self.nextAvailableID = self.nextAvailableID + 1

	def Evolve(self):
		self.Evaluate(self.parents)
		self.parents[0].Evaluate("GUI")
		for currentGeneration in range(c.numberOfGenerations):
			self.Evolve_For_One_Generation()


	def Evolve_For_One_Generation(self):
		self.Spawn()
		self.Mutate()
		self.Evaluate(self.children)
#		self.Select()
		self.Print()


	def Spawn(self):
		self.children = {}
		for i in self.parents:
			self.children[i] = copy.deepcopy(self.parents[i])
			self.children[i].Set_ID(self.nextAvailableID)
			self.nextAvailableID = self.nextAvailableID + 1
	def Mutate(self):
		for i in self.children:
			self.children[i].Mutate()

	def Evaluate(self, solutions):
		for parent in solutions.values():
			parent.Start_Simulation("DIRECT")
		for parent in solutions.values():
			parent.Wait_For_Simulation_To_End()
	def Select(self):
		if (self.parent.fitness > self.child.fitness):
			self.parent = self.child
		else:
			print("PARENT IS BETTER")
	def Print(self):
		for key in self.parents:
			print("")
			print(self.parents[key].fitness, self.children[key].fitness)
			print("")
	def Show_Best(self):
#		self.parent.Evaluate("GUI")
		pass
	def Set_ID(self, ID):
		self.myID = ID
