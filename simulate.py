#!/usr/bin/python3

from simulation import SIMULATION

import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import random

physicsClient = p.connect(p.GUI, options="--opengl2")
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
t = 1000


p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(t)
frontLegSensorValues = numpy.zeros(t)

backLeg_Amp =  1
backLeg_Freq = 20
backLeg_Ofs = 1

frontLeg_Amp = 1/12
frontLeg_Freq = 20
frontLeg_Ofs =0

backLegSensorValues = numpy.zeros(t)
frontLegSensorValues = numpy.zeros(t)

backLeg_targetAngles = numpy.linspace(0,2*numpy.pi*backLeg_Freq + backLeg_Ofs, t)
backLegMotorCommand = (numpy.sin(backLeg_targetAngles))*backLeg_Amp

frontLeg_targetAngles = numpy.linspace(0,2*numpy.pi*frontLeg_Freq + frontLeg_Ofs, t)
frontLegMotorCommand = (numpy.sin(frontLeg_targetAngles))*frontLeg_Amp

for i in range(0,t):
	time.sleep(1/300)
	p.stepSimulation()
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#	print(frontLegSensorValues)

	pyrosim.Set_Motor_For_Joint(
	bodyIndex = robotId,
	jointName = b'Torso_BackLeg',
	controlMode = p.POSITION_CONTROL,
	targetPosition = backLegMotorCommand[i],
	maxForce = 50)

	pyrosim.Set_Motor_For_Joint(
	bodyIndex = robotId,
	jointName = b'Torso_FrontLeg',
	controlMode = p.POSITION_CONTROL,
	targetPosition = frontLegMotorCommand[i],
	maxForce = 50)

numpy.save('data/backLegSensorValues.npy', backLegSensorValues)
numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)

p.disconnect()

#simulation = SIMULATION()
