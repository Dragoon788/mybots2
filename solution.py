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
		# random.seed(nextAvailableID)

		self.gindex = 0
		self.bodylen = random.randint(1,7)
		self.curr_bodylen = 0
		self.random_sensor_locs = [random.randint(0,self.bodylen-1) for i in range(random.randint(1,self.bodylen))]
		self.linkNames = []
		self.links = []
		self.jointNames =[]
		self.joints = []
		self.numSensorNeurons = len(self.random_sensor_locs)
		self.numMotorNeurons = self.bodylen
		self.random_sizes = [[random.random() for i in range(0,3)] for i in range (0,self.bodylen+1)]
		self.max_height = max(l[2] for l in self.random_sizes)
		self.link_positions = []
		self.minsxmax = []

		self.weights = 2*numpy.random.rand(self.numSensorNeurons,self.numMotorNeurons) - 1
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

	
		pyrosim.Start_URDF("body" + str(self.myID) + ".urdf")
		#Having the robot grow in it's own direcion
		# l.Create_Snakey(self)
		# print(self.links)
		l.Build_Creature(self)

		

				
		pyrosim.End()

	def Create_Body_Existing(self):

		# print(c.random_sensor_locs)


		pyrosim.Start_URDF("body" + str(self.myID) + ".urdf")
		#Having the robot grow in it's own direction
		# l.Create_Snakey(self)
		print(self.links)
		l.Build_Existing_Creature(self)
		# l.Create_Lizardy(self)
		# l.test_first_connect(self)
		print(self.random_sensor_locs)
		print(self.linkNames)
		print(self.jointNames)
		
		pyrosim.End()		

	def Create_Brain(self):
		pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
		n = 0

		for i in range(self.bodylen):
			if (self.bodylen == 0):
				break
			if (i in self.random_sensor_locs):
				pyrosim.Send_Sensor_Neuron(name = n, linkName = self.linkNames[i])
				n = n+1
	

		self.numSensorNeurons = n
		for i in self.jointNames:
			pyrosim.Send_Motor_Neuron(name = n, jointName = i)
			n= n+1

		for currentRow in range (0,self.numSensorNeurons):
			for currentColumn in range (0,self.numMotorNeurons):
				pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn+self.numSensorNeurons, weight = self.weights[currentRow][currentColumn])
		pyrosim.End()

	def Mutate(self):
#		print(self.weights)
		self.weights[random.randint(0,self.numSensorNeurons-1)][random.randint(0,self.numMotorNeurons-1)] = random.uniform(-1,1)
#		print(self.weights)
		self.gindex = 0
		self.curr_bodylen = 0
		# self.random_sensor_locs = [random.randint(0,self.bodylen-1) for i in range(random.randint(1,self.bodylen))]
		self.linkNames = []
		self.links = []
		self.jointNames =[]
		self.joints = []
		# self.numSensorNeurons = len(self.random_sensor_locs)


		



	def Start_Simulation(self, directOrGUI):
		self.Create_World()
		# print("CREATING WORLD IS FINISHED")
		self.Create_Body()
		# print("CREATING BODY IS FINISHED")
		self.Create_Brain()
#		print("id getting simulated", self.myID)
		# print("im here")
		os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2&>1 &")

#		os.system("ls data")

	def Start_Simulation_Best(self, directOrGUI):
		self.Create_World()
		self.Create_Body_Existing()
		self.Create_Brain()
		os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID))

	def Wait_For_Simulation_To_End(self):
		fitnessFileName = "data/fitness" + str(self.myID) + ".txt"

		while not (os.path.exists(fitnessFileName)):
			time.sleep(0.01)
		f = open(fitnessFileName, "r")
		lines = f.readlines()

		self.movement_fitness = float(lines[0])

		f.close()

		os.system("rm " + fitnessFileName)

	def Set_ID(self, ID):
		self.myID = ID

	def Connect_Joints(self, loj):
		for joint in loj:
			joint.Connect_Links()
        
