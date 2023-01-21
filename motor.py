#!/usr/bin/python3

import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import constants as c

class MOTOR:
	def __init__(self, jointName):
		self.jointName = jointName
		self.Prepare_To_Act()


	def MotorCommand(self, amplitude, frequency, offset, t):
		targetAngles = numpy.linspace(0, 2*numpy.pi*frequency + offset,t)
		return (numpy.sin(targetAngles))*amplitude

	def Prepare_To_Act(self):
		print(self.jointName)
		if (self.jointName == b'Torso_BackLeg'):
			self.motorvalues = self.MotorCommand(c.backLeg_Amp, c.backLeg_Freq/20, c.backLeg_Ofs, c.t)
		else:
			self.motorvalues = self.MotorCommand(c.backLeg_Amp, c.backLeg_Freq, c.backLeg_Ofs, c.t)
	def Set_Value (self, robot, t):
		pyrosim.Set_Motor_For_Joint(
		bodyIndex = robot.robotId,
		jointName = self.jointName,
		controlMode = p.POSITION_CONTROL,
		targetPosition = self.motorvalues[t],
		maxForce = 50)
