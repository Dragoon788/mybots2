#!/usr/bin/python3

from world import WORLD
from robot import ROBOT

import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import time
import constants as c

class SIMULATION:
	def __init__(self, directOrGUI, solutionID):

		self.directOrGUI = directOrGUI
		self.solutionID = solutionID

		if(directOrGUI == "GUI"):
			self.physicsClient = p.connect(p.GUI)
		elif(directOrGUI == "DIRECT"):
			self.physicsClient = p.connect(p.DIRECT)
		else:
			return TypeError("Not either GUI or DIRECT")
#		self.physicsClient = p.connect(p.DIRECT, options="--opengl2")
		p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
		p.setAdditionalSearchPath(pybullet_data.getDataPath())
		p.setGravity(0,0,-9.8)
		self.world = WORLD()
		self.robot = ROBOT(solutionID)

	def Run(self):
		for i in range(0,c.t):
			p.stepSimulation()
			self.robot.Sense(i)
			self.robot.Think()
			self.robot.Act()
			if (self.directOrGUI == "GUI"):
				time.sleep(1/200)
			else:
				pass


#
	def __del__(self):
		p.disconnect()
	def Get_Fitness(self):
		self.robot.Get_Fitness()

