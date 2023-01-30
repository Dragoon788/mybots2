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
			self.physicsClient = p.connect(p.GUI, options = "--opengl2")
		elif(directOrGUI == "DIRECT"):
			self.physicsClient = p.connect(p.DIRECT)
		else:
			return TypeError("Not either GUI or DIRECT")
#		self.physicsClient = p.connect(p.DIRECT, options="--opengl2")
		p.setAdditionalSearchPath(pybullet_data.getDataPath())
		p.setGravity(0,0,-9.8)
		self.world = WORLD()
		self.robot = ROBOT(solutionID)

	def Run(self):
		for i in range(0,c.t):
			if (self.directOrGUI == "GUI"):
				time.sleep(1/200)
			p.stepSimulation()
			self.robot.Sense(i)
			self.robot.Think()
			self.robot.Act()
			self.robot.Get_Fitness()

#		       backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#		       frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#		#      print(frontLegSensorValues)
#
#		       pyrosim.Set_Motor_For_Joint(
#		       bodyIndex = robotId,
#		       jointName = b'Torso_BackLeg',
#		       controlMode = p.POSITION_CONTROL,
#		       targetPosition = backLegMotorCommand[i],
#		       maxForce = 50)
#
#		       pyrosim.Set_Motor_For_Joint(
#		       bodyIndex = robotId,
#		       jointName = b'Torso_FrontLeg',
#		       controlMode = p.POSITION_CONTROL,
#		       targetPosition = frontLegMotorCommand[i],
#		       maxForce = 50)
#
	def __del__(self):
		p.disconnect()
	def Get_Fitness():
		self.robot.Get_Fitness()
