#!/usr/bin/python3
import matplotlib.pyplot
import numpy

backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')
#print (backLegSensorValues)

matplotlib.pyplot.plot(backLegSensorValues, label =  'Back Leg')
matplotlib.pyplot.plot(frontLegSensorValues, label = 'Front Leg')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
