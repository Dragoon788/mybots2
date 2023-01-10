#!/usr/bin/python3

import pybullet as p
import time

physicsClient = p.connect(p.GUI, options="--opengl2")


p.loadSDF("box.sdf")

for x in range(0,1000000):
	p.stepSimulation()
	time.sleep(1/300)
	print(x)

p.disconnect()

