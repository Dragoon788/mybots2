#!/usr/bin/python3
from world import WORLD
from robot import ROBOT

import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import time
import constants as c

class SIMULATION:
	def __init__(self):
		self.physicsClient = p.connect(p.GUI, options="--opengl2")
		p.setAdditionalSearchPath(pybullet_data.getDataPath())
		p.setGravity(0,0,-9.8)
		self.world = WORLD()
		self.robot = ROBOT()
	def __del__(self):
		p.disconnect()
