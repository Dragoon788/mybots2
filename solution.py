#!/usr/bin/python3
import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:
	def __init__(self, nextAvailableID):
		self.weights = c.numMotorNeurons*numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons) - 1
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
		pyrosim.Send_Cube(name="Torso", pos=[0,0.5,1], size=[length, width, height])
		pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg",type="revolute", position=[1,0,1])
		pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5], size=[length, width, height])
		pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg",type="revolute", position =[0,0.5,1])
		pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0], size=[0.2,1,0.2])
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

		for currentRow in range (0,c.numSensorNeurons):
			for currentColumn in range (0,c.numMotorNeurons):
				pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn+c.numSensorNeurons, weight = self.weights[currentRow][currentColumn])
		pyrosim.End()


	def Mutate(self):
#		print(self.weights)
		self.weights[random.randint(0,c.numSensorNeurons-1)][random.randint(0,c.numMotorNeurons-1)] = random.uniform(-1,1)
#		print(self.weights)
	def Start_Simulation(self, directOrGUI):
		self.Create_World()
		self.Create_Body()
		self.Create_Brain()
		os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2&>1 &")
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
