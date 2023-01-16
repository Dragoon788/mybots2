#!/usr/bin/python3

from world import WORLD
from robot import ROBOT

import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import constants as c

class SIMULATION:
	def __init__(self):
#		self.ITER_STEPS  = c.t
		# connect to engine
		self.physicsClient = p.connect(p.GUI, options="--opengl2")
		p.setAdditionalSearchPath(pybullet_data.getDataPath())
		#set gravity
		p.setGravity(0,0,-9.8)
		self.world = WORLD()
		self.robot = ROBOT()

#	def startupsim:
#		for i in range(0,t):
#		       time.sleep(1/100)
#		       p.stepSimulation()
#		       c.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#		       c.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#		#      print(frontLegSensorValues)
#
#		       pyrosim.Set_Motor_For_Joint(
#		       bodyIndex = robotId,
#		       jointName = b'Torso_BackLeg',
#		       controlMode = p.POSITION_CONTROL,
#		       targetPosition = c.backLegMotorCommand[i],
#		       maxForce = 50)
#
#		       pyrosim.Set_Motor_For_Joint(
#		       bodyIndex = robotId,
#		       jointName = b'Torso_FrontLeg',
#		       controlMode = p.POSITION_CONTROL,
#		       targetPosition = c.frontLegMotorCommand[i],
#		       maxForce = 50)
	def __del__(self):
		p.disconnect()
