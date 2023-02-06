#!/usr/bin/python3

import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import constants as c
import os

class SENSOR:
	def __init__(self, linkName):
		self.values = numpy.zeros(c.t)
		self.linkName = linkName

	def Get_Value(self,t):
		self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

	def Save_Values(self):
#		numpy.save('data/SensorValues.npy', self.values)
		numpy.save(os.path.join('data', self.linkName + "sensor"), self.values)
