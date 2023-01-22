#!/usr/bin/python3

import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import constants as c
import os

class MOTOR:
	def __init__(self, jointName):
		self.jointName = jointName

	def MotorCommand(self, amplitude, frequency, offset, t):
		targetAngles = numpy.linspace(0, 2*numpy.pi*frequency + offset,t)
		return (numpy.sin(targetAngles))*amplitude

	def Set_Value (self, robot, desiredAngle):
#		desiredAngle2 = 0*desiredAngle+desiredAngle
#		print(desiredAngle2)
		pyrosim.Set_Motor_For_Joint(
		bodyIndex = robot.robotId,
		jointName = self.jointName,
		controlMode = p.POSITION_CONTROL,
		targetPosition = desiredAngle,
		maxForce = 50)
