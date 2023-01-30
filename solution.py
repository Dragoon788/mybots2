#!/usr/bin/python3
import numpy
import pyrosim.pyrosim as pyrosim
import os
import random

class SOLUTION:
	def __init__(self):
		self.weights = 2*numpy.random.rand(3,2) - 1
	def Evaluate(self):
		self.Create_World()
		self.Create_Body()
		self.Create_Brain()
		os.system("python3 simulate.py DIRECT")

		f = open("data/fitness.txt", "r")
		self.fitness = float(f.read())
		f.close()

	def Create_World(self):
		length = 1
		width = 1
		height =1

		pyrosim.Start_SDF("world.sdf")
		pyrosim.Send_Cube(name="world.sdf", pos=[10,0,0.5], size=[length, width, height])
		pyrosim.End()

	def Create_Body(self):
		length = 1
		width = 1
		height = 1

		pyrosim.Start_URDF("body.urdf")
		pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5], size=[length, width, height])
		pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg",type="revolute", position=[1,0,1])
		pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5], size=[length, width, height])
		pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg",type="revolute", position =[2,0,1])
		pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[length, width, height])
		pyrosim.End()

	def Create_Brain(self):
		length = 1
		width = 1
		height = 1

		pyrosim.Start_NeuralNetwork("brain.nndf")

		pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")
		pyrosim.Send_Sensor_Neuron(name = 1, linkName = "BackLeg")
		pyrosim.Send_Sensor_Neuron(name = 2, linkName = "FrontLeg")
		pyrosim.Send_Motor_Neuron(name = 3, jointName = "Torso_BackLeg")
		pyrosim.Send_Motor_Neuron(name = 4, jointName = "Torso_FrontLeg")

		for currentRow in range (0,3):
			for currentColumn in range (0,2):
				pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn+3, weight = self.weights[currentRow][currentColumn])
		pyrosim.End()

	def Mutate(self):
		self.weights[random.randint(0,2)][random.randint(0,1)] = random.random()*2-1
