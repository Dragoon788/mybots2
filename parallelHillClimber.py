#!/usr/bin/python3

from pathlib import Path
from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
	def __init__(self):
		path1 = os.listdir("/home/francisvelasco2025/mybots2-git")
		path2 = os.listdir("/home/francisvelasco2025/mybots2-git/data")
		for item in path1:
			if item.endswith(".nndf"):
				os.system("rm " + item)
		for item in path2:
			if item.endswith(".txt"):
				os.system("rm data/" + item)
		self.parents = {}
		self.nextAvailableID = 0

		for i in range(0,c.populationSize):
			self.parents[i] = SOLUTION(self.nextAvailableID)
			self.nextAvailableID = self.nextAvailableID + 1

	def Evolve(self):
		self.parents[0].Evaluate("GUI")
		self.parents[0].Wait_For_Simulation_To_End()

#		self.parents[0].Evaluate("DIRECT")
		for currentGeneration in range(c.numberOfGenerations):
			self.Evolve_For_One_Generation()
		Best_Parent = self.Show_Best(self.parents)
		Best_Parent.Start_Simulation("GUI")

	def Evolve_For_One_Generation(self):
		self.Spawn()
		self.Mutate()
		self.Evaluate(self.children)
#		self.Print()
		self.Select()


	def Spawn(self):
		self.children = {}
		for i in self.parents:
			self.children[i] = copy.deepcopy(self.parents[i])
			self.children[i].Set_ID(self.nextAvailableID)
			self.nextAvailableID = self.nextAvailableID + 1
	def Mutate(self):
		for i in self.children:
#			print(self.children[i])
			self.children[i].Mutate()

	def Evaluate(self, solutions):
		for parent in solutions.values():
			parent.Start_Simulation("DIRECT")
		for parent in solutions.values():
			parent.Wait_For_Simulation_To_End()
	def Select(self):
		for i in self.parents:
			if (self.parents[i].movement_fitness > self.children[i].movement_fitness or
			    self.parents[i].xOrientation_fitness < self.children[i].xOrientation_fitness):
				self.parents[i] = self.children[i]
			elif(self.parents[i].movement_fitness < self.children[i].movement_fitness):
				print("Parent is better")
			else:
				print("PARENT IS BETTER")
	def Print(self):
		for key in self.parents:
#			print(self.parents[key].weights)
			print("\nMovement Fitness")
			print(self.parents[key].movement_fitness, self.children[key].movement_fitness)
			print("")
			print("xOrientation Fitness")
			print(self.parents[key].xOrientation_fitness, self.children[key].xOrientation_fitness)
#			print("")
#			print("yOrientation Fitness")
#			print(self.parents[key].yOrientation_fitness, self.children[key].yOrientation_fitness)
#			print("")
#			print("zOrientation Fitness")
#			print(self.parents[key].zOrientation_fitness, self.children[key].zOrientation_fitness)
#			print("")

	def Show_Best(self, parents):
		winner_fitness = 100000
		winner = None
		for i in parents:
			if (parents[i].movement_fitness < winner_fitness):
				winner_fitness = parents[i].movement_fitness
				winner = parents[i]
		return winner

	def Set_ID(self, ID):
		self.myID = ID


