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
		self.Start_Simulation(directOrGUI)

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
		pyrosim.Send_Cube(name="Torso", pos=[0,0,2.5], size=[length, width, height])
		pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg",type="revolute", position=[0,-0.5,2.5], jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="LeftLeg", pos=[0,0,-0.5], size=[0.2,0.2,1.0])
		pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg", child="LeftLowerLeg", type="revolute", position=[0,0,-1], jointAxis= "0 1 0")
		pyrosim.Send_Cube(name ="LeftLowerLeg", pos=[0,0,-0.5], size=[0.2,0.2,1])
		pyrosim.Send_Joint(name="LeftLowerLeg_LeftFoot", parent = "LeftLowerLeg", child="LeftFoot", type="revolute", position=[0,0,-1], jointAxis= "0 1 0")
		pyrosim.Send_Cube(name="LeftFoot", pos=[0,0,-0.25], size=[1.0,0.5,0.5])

		pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg",type="revolute", position=[0,0.5,2.5], jointAxis = "0 1 0")
		pyrosim.Send_Cube(name="RightLeg", pos=[0,0,-0.5], size=[0.2,0.2,1.0])
		pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg", child="RightLowerLeg", type="revolute", position=[0,0,-1.0], jointAxis= "0 1 0")
		pyrosim.Send_Cube(name ="RightLowerLeg", pos=[0,0,-0.5], size=[0.2,0.2,1])
		pyrosim.Send_Joint(name="RightLowerLeg_RightFoot", parent = "RightLowerLeg", child="RightFoot", type="revolute", position=[0,0,-1.0], jointAxis= "0 1 0")
		pyrosim.Send_Cube(name="RightFoot", pos=[0,0,-0.25], size=[1.0,0.5,0.5])

		pyrosim.End()

	def Create_Brain(self):
		length = 1
		width = 1
		height = 1

		pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

#		pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")
#		pyrosim.Send_Sensor_Neuron(name = 1, linkName = "BackLeg")
#		pyrosim.Send_Sensor_Neuron(name = 2, linkName = "FrontLeg")
		pyrosim.Send_Sensor_Neuron(name = 0, linkName = "LeftLeg")
		pyrosim.Send_Sensor_Neuron(name = 1, linkName = "RightLeg")
#		pyrosim.Send_Sensor_Neuron(name = 0, linkName = "FrontLowerLeg")
#		pyrosim.Send_Sensor_Neuron(name = 1, linkName = "BackLowerLeg")
		pyrosim.Send_Sensor_Neuron(name = 2, linkName = "LeftLowerLeg")
		pyrosim.Send_Sensor_Neuron(name = 3, linkName = "RightLowerLeg")
		pyrosim.Send_Sensor_Neuron(name = 4, linkName = "LeftFoot")
		pyrosim.Send_Sensor_Neuron(name = 5, linkName = "RightFoot")

#		pyrosim.Send_Motor_Neuron(name = 4, jointName = "Torso_BackLeg")
#		pyrosim.Send_Motor_Neuron(name = 5, jointName = "Torso_FrontLeg")
#		pyrosim.Send_Motor_Neuron(name = 6, jointName = "Torso_LeftLeg")
#		pyrosim.Send_Motor_Neuron(name = 7, jointName = "Torso_RightLeg")
#		pyrosim.Send_Motor_Neuron(name = 8, jointName = "FrontLeg_FrontLowerLeg")
#		pyrosim.Send_Motor_Neuron(name = 14, jointName = "BackLeg_BackLowerLeg")
		pyrosim.Send_Motor_Neuron(name = 6, jointName = "LeftLeg_LeftLowerLeg")
		pyrosim.Send_Motor_Neuron(name = 7, jointName = "RightLeg_RightLowerLeg")
		pyrosim.Send_Motor_Neuron(name = 8, jointName = "LeftLowerLeg_LeftFoot")
		pyrosim.Send_Motor_Neuron(name = 9, jointName = "RightLowerLeg_RightFoot")


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
#		fitnessFileName2 = "data/fitness2-" + str(self.myID) + ".txt"
		while not (os.path.exists(fitnessFileName)):
			time.sleep(0.01)
		f = open(fitnessFileName, "r")
		lines = f.readlines()

		self.movement_fitness = float(lines[0])
		self.xOrientation_fitness = float(lines[1])
#		self.yOrientation_fitness = float(lines[2])
#		self.zOrientation_fitness = float(lines[3])
#		print(self.fitn)
#		f2.close()
#		print("THIS IS MY FITNESS FILE" + str(self.fitness))

#		print("THIS IS MY SELF.ID:" + str(self.myID))
		os.system("rm " + fitnessFileName)
#		os.system("rm " + fitnessFileName2)
#		os.system("ls data")

	def Set_ID(self, ID):
		self.myID = ID
