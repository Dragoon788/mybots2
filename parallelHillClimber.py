#!/usr/bin/python3

from pathlib import Path
from solution import SOLUTION
import constants as c
import copy
import os
import matplotlib.pyplot as plt

class PARALLEL_HILL_CLIMBER:
	def __init__(self):

		os.system("rm data/brain*.nndf")
		os.system("rm data/fitness*.txt")
		self.parents = {}
		self.nextAvailableID = 0
		self.graphv = {}
		self.Best_Parents = None

		for i in range(0,c.populationSize):
			self.parents[i] = SOLUTION(self.nextAvailableID)
			self.nextAvailableID = self.nextAvailableID + 1
			self.graphv[i] = []

	def Evolve(self):
		for parent in self.parents.values():
			parent.Start_Simulation("GUI")
			parent.Wait_For_Simulation_To_End()
		# self.Evaluate(self.parents, "GUI")
		# i = 0
#		self.parents[0].Evaluate("DIRECT")
		for currentGeneration in range(c.numberOfGenerations):
			print("GENERATION #" + str(currentGeneration))
			self.Evolve_For_One_Generation()

		self.Best_Parents = self.parents
		# Best_Parent.Start_Simulation_Best("GUI")
		# Best_Parent.Wait_For_Simulation_To_End()

	def Evolve_For_One_Generation(self):
		self.Spawn()
		self.Mutate()
		self.Evaluate(self.children, "DIRECT")
		# self.Print()
		
		self.Select()


	def Spawn(self):
		self.children = {}
		for i in self.parents:
			self.children[i] = copy.deepcopy(self.parents[i])
			self.children[i].Set_ID(self.nextAvailableID)
			self.nextAvailableID = self.nextAvailableID + 1

	def Mutate(self):
		for i in self.children:
			# print(self.children[i])
			self.children[i].Mutate()


	def Evaluate(self, solutions, method):
		for parent in solutions.values():
			parent.Start_Simulation(method)

		for parent in solutions.values():
			parent.Wait_For_Simulation_To_End()

	def Select(self):
		for i in self.parents:

			if (self.parents[i].movement_fitness > self.children[i].movement_fitness): 

				self.parents[i] = self.children[i]
				# print("Child is better")
			self.graphv[i].append(abs(self.parents[i].movement_fitness))

	def Print(self):
		for key in self.parents:
#			print(self.parents[key].weights)
			print("\nMovement Fitness")
			print(self.parents[key].movement_fitness, self.children[key].movement_fitness)
			print("")


	def Show_Best(self, parents):

		winner = self.parents[0]
		for i in parents:
			if (self.parents[i].movement_fitness < winner.movement_fitness):

				winner = parents[i]
		winner.Start_Simulation_Best("GUI")
		x = [i for i in range (0, c.numberOfGenerations)]
		for i in self.graphv:
			print(x, self.graphv[i])
			plt.plot(x, self.graphv[i], label = "seed " + str(i+1))
		plt.legend()
		plt.show()
			

	def Set_ID(self, ID):
		self.myID = ID


