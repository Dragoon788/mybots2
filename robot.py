#!/usr/bin/python3

import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim

class ROBOT:
	def __init__(self):
#		p.setAdditionalSearchPath(pybullet_data.getDataPath())
#		pyrosim.Prepare_To_Simulate(self.robot.robotId)
		self.sensors = {}
		self.motors = {}
#		self.robotId = p.loadURDF("body.urdf")
