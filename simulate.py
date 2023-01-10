#!/usr/bin/python3

import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI, options="--opengl2")
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")


p.loadSDF("world.sdf")

for x in range(0,10000000):
	p.stepSimulation()
	time.sleep(1/300)
	
p.disconnect()

