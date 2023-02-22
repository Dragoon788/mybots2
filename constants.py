#!/usr/bin/python3

import numpy
import random

t = 4000

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

def MotorCommand(amplitude, frequency, offset, t):
	targetAngles = numpy.linspace(0, 2*numpy.pi*frequency + offset,t)
	return (numpy.sin(targetAngles))*amplitude

maxForce = 50
numberOfGenerations = 1
populationSize = 1
motorJointRange = 1
bodylen = random.randint(1,30) 
random_sensor_locs = [[random.randint(0,(bodylen)) for i in range(random.randint(0,7))] for j in range(0,3)]

linkNames = []

jointNames =[]


numSensorNeurons = len(random_sensor_locs[0])+len(random_sensor_locs[1])+len(random_sensor_locs[2])
numMotorNeurons = bodylen-2
random_dir = []
random_sizes_x = [[random.random() for i in range(0,10)] for i in range(0,bodylen)]
random_sizes_y = [[random.random() for i in range(0,10)] for i in range(0,bodylen)]
random_sizes_z = [[random.random() for i in range(0,10)] for i in range(0,bodylen)]

max_height_x = max(l[2] for l in random_sizes_x)
max_height_y = max(l[2] for l in random_sizes_y)
max_height_z = max(l[2] for l in random_sizes_z)

max_height = max([max_height_x, max_height_y, max_height_z])