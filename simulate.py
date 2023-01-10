#!/usr/bin/python3

import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy

physicsClient = p.connect(p.GUI, options="--opengl2")
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")


p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)


for x in range(0,10000000):
	time.sleep(1/300)
	p.stepSimulation()
	backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	print(backLegTouch)

p.disconnect()
