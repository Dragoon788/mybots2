#!/usr/bin/python3

import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import constants as c

from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:
	def __init__(self):
		self.robotId = p.loadURDF("body.urdf")
		self.nn = NEURAL_NETWORK("brain.nndf")

		pyrosim.Prepare_To_Simulate(self.robotId)
		self.Prepare_To_Sense()
		self.Prepare_To_Act()

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
#		self.amplitude = c.backLeg_Amp
#		self.frequency = c.backLeg_Freq
#		self.offset = c.backLeg_Ofs

#		self.MotorCommand = c.MotorCommand(self.amplitude, self.frequency, self.offset, c.t)

		for jointName in pyrosim.jointNamesToIndices:
			self.motors[jointName] = MOTOR(jointName)
			self.motors[jointName].Prepare_To_Act()


	def Act(self,t):
		for neuronName in self.nn.Get_Neuron_Names():
			if self.nn.Is_Motor_Neuron(neuronName):
				jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
				desiredAngle = self.nn.Get_Value_Of(neuronName)
				for i in self.motors:
					self.motors[i].Set_Value(self, desiredAngle)
					self.motors[i].Save_Values()
				print(neuronName, jointName, desiredAngle)
#		for i in self.motors:
#			self.motors[i].Set_Value(self, t)
#			self.motors[i].Save_Values()

	def Think(self):
		self.nn.Update()
		self.nn.Print()
