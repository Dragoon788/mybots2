#!/usr/bin/python3

import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy

class WORLD:
	def __init__(self):
		p.loadSDF("world.sdf")
		p.loadURDF("plane.urdf")
