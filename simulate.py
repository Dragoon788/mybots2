#!/usr/bin/python3

import pybullet as p
import time

physicsClient = p.connect(p.GUI, options="--opengl2")

for x in range(0,1000):
	p.stepSimulation()
	time.sleep(1/60)
	print(x)

p.disconnect()

