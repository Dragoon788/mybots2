#!/usr/bin/python3
import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time

class SOLUTION:
	def __init__(self, nextAvailableID):
		self.weights = 2*numpy.random.rand(3,2) - 1
		self.myID = nextAvailableID
	def Evaluate(self, directOrGUI):
		pass

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

		pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

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

	def Start_Simulation(self, directOrGUI):
		self.Create_World()
		self.Create_Body()
		self.Create_Brain()
		os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " &")
#		os.system("ls data")

	def Wait_For_Simulation_To_End(self):

		fitnessFileName = "data/fitness" + str(self.myID) + ".txt"
		while not (os.path.exists(fitnessFileName)):
			time.sleep(0.01)
		f = open(fitnessFileName, "r")
		read_file = f.read()
#		print("THIS IS MY READ FITNESS FILE:" + str(read_file))
		self.fitness = float(read_file)
#		print(self.fitness)
		f.close()
#		print("THIS IS MY FITNESS FILE" + str(self.fitness))

#		print("THIS IS MY SELF.ID:" + str(self.myID))
		os.system("rm " + fitnessFileName)
#		os.system("ls data")

	def Set_ID(self, ID):
		self.myID = ID 
