#!/usr/bin/python3

import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5

x2 = 1
y2 = 0
z2 = 1.5


##pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[length, width, height])
##pyrosim.Send_Cube(name="Box2", pos=[x2,y2,z2], size=[length, width, height])

for n in range(0,9):
	for n2 in range(0,4):
		for n3 in range (0,4):
					pyrosim.Send_Cube(name="Box", pos=[x+(1*n2),y+(1*n3),z+(1*n)], size=[(0.9**n)*length, (0.9**n)*width, (0.9**n)*height])

pyrosim.End()
