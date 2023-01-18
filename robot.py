#!/usr/bin/python3

import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import constants as c

from sensor import SENSOR

class ROBOT:
	def __init__(self):
		self.motors = {}
		self.robotId = p.loadURDF("body.urdf")
		pyrosim.Prepare_To_Simulate(self.robotId)
		self.values = numpy.zeros(c.t)

	def Prepare_To_Sense(self):
		self.sensors = {}
		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = SENSOR(linkName)

	def Sense(self, t):
		for i in self.sensors:
			self.sensors[i].Get_Value(t)
