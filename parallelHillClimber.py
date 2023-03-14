#!/usr/bin/python3

from pathlib import Path
from solution import SOLUTION
import constants as c
import copy
import os
import matplotlib.pyplot as plt

class PARALLEL_HILL_CLIMBER:
	def __init__(self):
		# path1 = os.listdir("/home/francisvelasco2025/mybots2-git")
		# path2 = os.listdir("/home/francisvelasco2025/mybots2-git/data")
		# for item in path1:
		# 	if item.startswith("brain"):
		# 		os.system("rm brain*.nndf")
		# for item in path2:
		# 	if item.startswith("fitness"):
		# 		os.system("rm fitness*.txt")
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

		# self.bodylen = bodylen
		# self.curr_bodylen = curr_bodylen
		# self.random_sensor_locs = random_sensor_locs
		# self.linkNames = linkNames
		# self.links = links
		# self.jointNames = jointNames
		# self.joints = joints
		# self.numSensorNeurons = numSensorNeurons
		# self.numMotorNeurons = numMotorNeurons
		# self.random_sizes = random_sizes

	def Evolve(self):
		self.Evaluate(self.parents, "DIRECT")
		i = 0
#		self.parents[0].Evaluate("DIRECT")
		for currentGeneration in range(c.numberOfGenerations):
			print("GENERATION #" + str(i))
			self.Evolve_For_One_Generation()
			i= i +1
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
			# if (self.parents[i].movement_fitness > self.children[i].movement_fitness and
			# if (self.parents[i].xOrientation_fitness > self.children[i].xOrientation_fitness and
			#     self.parents[i].yOrientation_fitness > self.children[i].yOrientation_fitness and
			# 	self.parents[i].zOrientation_fitness > self.children[i].zOrientation_fitness):
			if (self.parents[i].movement_fitness > self.children[i].movement_fitness): 
				# (self.parents[i].xOrientation_fitness+ self.parents[i].yOrientation_fitness + self.parents[i].zOrientation_fitness >
				# self.children[i].xOrientation_fitness + self.children[i].yOrientation_fitness + self.children[i].zOrientation_fitness)):
				self.parents[i] = self.children[i]
				print("Child is better")
			self.graphv[i].append(self.parents[i].movement_fitness)
			# elif(self.parents[i].movement_fitness < self.children[i].movement_fitness):
			# 	print("Parent is better")
			# else:
			# 	# print("PARENT IS BETTER")
	def Print(self):
		for key in self.parents:
#			print(self.parents[key].weights)
			print("\nMovement Fitness")
			print(self.parents[key].movement_fitness, self.children[key].movement_fitness)
			print("")
			# print("xOrientation Fitness")
			# print(self.parents[key].xOrientation_fitness, self.children[key].xOrientation_fitness)
			# print("")
			# print("yOrientation Fitness")
			# print(self.parents[key].yOrientation_fitness, self.children[key].yOrientation_fitness)
			# print("")
			# print("zOrientation Fitness")
			# print(self.parents[key].zOrientation_fitness, self.children[key].zOrientation_fitness)
			# print("")

	def Show_Best(self, parents):

		winner = self.parents[0]
		for i in parents:
			if (self.parents[i].movement_fitness < winner.movement_fitness):
				# # self.parents[i].xOrientation_fitness > winner.xOrientation_fitness and
			    # # self.parents[i].yOrientation_fitness > winner.yOrientation_fitness and
				# # self.parents[i].zOrientation_fitness > winner.zOrientation_fitness):
				# self.parents[i].xOrientation_fitness+ self.parents[i].yOrientation_fitness + self.parents[i].zOrientation_fitness <
				# winner.xOrientation_fitness + winner.yOrientation_fitness + winner.zOrientation_fitness):
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


