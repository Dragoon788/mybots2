#!/usr/bin/python3
import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c
import links as l

class SOLUTION:
	def __init__(self, nextAvailableID):
		self.weights = 2*numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons) - 1
		self.myID = nextAvailableID

	def Evaluate(self, directOrGUI):
		self.Start_Simulation(directOrGUI)

	def Create_World(self):
		length = 1
		width = 1
		height =1

		pyrosim.Start_SDF("world.sdf")
		pyrosim.Send_Cube(name="world.sdf", pos=[10,0,0.5], size=[length, width, height], color_name='<material name="World">', color_code='		<color rgba="1 1 1 1"/>')
		pyrosim.End()

	def Create_Body(self):

		# print(c.random_sensor_locs)


		pyrosim.Start_URDF("body.urdf")
		#Having the robot grow in it's own direction
		# l.Create_Snakey()
		l.Build_Creature()
		# l.Create_Lizardy
		# l.test_first_connect()
		print(c.random_sensor_locs)
		print(c.linkNames)
		print(c.jointNames)

				
		pyrosim.End()

	def Create_Brain(self):
		pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
		n = 0

		for i in range(c.bodylen):
			if (c.bodylen == 0):
				break
			if (i in c.random_sensor_locs):
				pyrosim.Send_Sensor_Neuron(name = n, linkName = c.linkNames[i])
				n = n+1
	

		c.numSensorNeurons = n
		for i in c.jointNames:
			pyrosim.Send_Motor_Neuron(name = n, jointName = i)
			n= n+1
		print(f"this is my n: {n}")
		print(c.numSensorNeurons)
		print(c.numMotorNeurons)
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
		self.yOrientation_fitness = float(lines[2])
		self.zOrientation_fitness = float(lines[3])
		f.close()
#		print(self.fitn)
#		f2.close()
#		print("THIS IS MY FITNESS FILE" + str(self.fitness))

#		print("THIS IS MY SELF.ID:" + str(self.myID))
		os.system("rm " + fitnessFileName)
#		os.system("rm " + fitnessFileName2)
#		os.system("ls data")

	def Set_ID(self, ID):
		self.myID = ID
