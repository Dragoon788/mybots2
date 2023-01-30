#!/usr/bin/python3

import numpy

t = 500

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

numberOfGenerations = 30
populationSize = 2
