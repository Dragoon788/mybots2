#!/usr/bin/python3

import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import constants as c
import os

from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:
	def __init__(self, solutionID):
		self.solutionID = solutionID
		self.robotId = p.loadURDF("body" + solutionID + ".urdf")
		self.nn = NEURAL_NETWORK("brain" + solutionID + ".nndf")

		pyrosim.Prepare_To_Simulate(self.robotId)
		self.Prepare_To_Sense()
		self.Prepare_To_Act()

		os.system("rm brain" + solutionID + ".nndf")
		os.system("rm body" + solutionID + ".urdf")



	def Prepare_To_Sense(self):
		self.sensors = {}
		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = SENSOR(linkName)

	def Sense(self, t):
		for i in self.sensors:
			self.sensors[i].Get_Value(t)
			self.sensors[i].Save_Values()
	def Prepare_To_Act(self):
		self.motors = {}
		for jointName in pyrosim.jointNamesToIndices:
			self.motors[jointName] = MOTOR(jointName)

	def Act(self):
		for neuronName in self.nn.Get_Neuron_Names():
			if (self.nn.Is_Motor_Neuron(neuronName)):
				jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
				desiredAngle = c.motorJointRange * self.nn.Get_Value_Of(neuronName)

				for key in self.motors:
					self.motors[jointName.encode('utf-8')].Set_Value(self, desiredAngle)

	def Think(self):
		self.nn.Update()
#		self.nn.Print()
	def Get_Fitness(self):

		print("called fitness")
		basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
		basePosition = basePositionAndOrientation[0]
		xPosition = basePosition[0]

		# baseOrientation = basePositionAndOrientation[1]
		# baseEuler = p.getEulerFromQuaternion(baseOrientation)

		# xOrientation = baseEuler[0]
		# yOrientation = baseEuler[1]
		# zOrientation = baseEuler[2]

#		orientation = xOrientation + yOrientation + zOrientation

#		print("THIS IS MY XPOSITION:" + str(xPosition))
		f = open("data/tmp" + str(self.solutionID) + ".txt", "w")
		f.write(str(xPosition) + "\n")
		# f.write(str(abs(xOrientation)) +"\n")
		# f.write(str(abs(yOrientation)) + "\n")
		# f.write(str(abs(zOrientation)) + "\n")

#		f2 = open("data/tmp2" + str(self.solutionID)+ ".txt", "w")
#		f2.write(str(xOrientation))

		f.close()
#		f2.close()

#		os.system("ls data")
		os.system("mv " + " data/tmp" + str(self.solutionID) + ".txt data/fitness" + str(self.solutionID) + ".txt")
		# print (".txt data/fitness" + str(self.solutionID) + ".txt")
#		os.system("mv " + " data/tmp2" + str(self.solutionID) + ".txt data/fitness2-" + self.solutionID + ".txt")
		# os.system("ls data")
