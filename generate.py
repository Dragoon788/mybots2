#!/usr/bin/python3

import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

x = 1.5
y = 0
z = 1.5

x2 = 0
y2 = 0
z2 = 0.5

x3 = 0
y3 = 0
z3 = 0.5

x4 = 0
y4 = 0.5
z4 = 0

x5 = 0
y5 = 0.5
z5 = 0

x6 = 0
y6 = 0
z6 = -0.5

x7 = 0
y7 = 0
z7 = -0.5

def Create_World():
	pyrosim.Start_SDF("world.sdf")
	pyrosim.Send_Cube(name="world.sdf", pos=[10,0,0.5], size=[length, width, height])
	pyrosim.End()

def Create_Robot():
	pyrosim.Start_URDF("body.urdf")
#	pyrosim.Send_Cube(name="Link0", pos=[x,y,z], size=[length, width, height])
#	pyrosim.Send_Joint(name="Link0_Link1", parent="Link0", child="Link1",type="revolute", position=[0,0,1])
#	pyrosim.Send_Cube(name="Link1", pos=[x2,y2,z2], size=[length, width, height])
#	pyrosim.Send_Joint(name="Link1_Link2", parent="Link1", child="Link2",type="revolute", position =[0,0,1])
#	pyrosim.Send_Cube(name="Link2", pos=[x3,y3,z3], size=[length, width, height])
#	pyrosim.Send_Joint(name="Link2_Link3", parent="Link2", child="Link3",type="revolute", position =[0,0.5,0.5])
#	pyrosim.Send_Cube(name="Link3", pos=[x4,y4,z4], size=[length, width, height])
#	pyrosim.Send_Joint(name="Link3_Link4", parent="Link3", child="Link4",type="revolute", position =[0,1,0])
#	pyrosim.Send_Cube(name="Link4", pos=[x5,y5,z5], size=[length, width, height])
#	pyrosim.Send_Joint(name="Link4_Link5", parent="Link4", child="Link5",type="revolute", position =[0,0.5,-0.5])
#	pyrosim.Send_Cube(name="Link5", pos=[x6,y6,z6], size=[length, width, height])
#	pyrosim.Send_Joint(name="Link5_Link6", parent="Link5", child="Link6",type="revolute", position =[0,0,-1])
#	pyrosim.Send_Cube(name="Link6", pos=[x7,y7,z7], size=[length, width, height])

	pyrosim.Send_Cube(name="Torso", pos=[x,y,z], size=[length, width, height])
	pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg",type="revolute", position=[1,0,1])
	pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5], size=[length, width, height])
	pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg",type="revolute", position =[2,0,1])
	pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[length, width, height])
	

	pyrosim.End()

Create_World()
Create_Robot()

#for n in range(0,9):
#	for n2 in range(0,4):
#		for n3 in range (0,4):
#					pyrosim.Send_Cube(name="Box", pos=[x+(1*n2),y+(1*n3),z+(1*n)], size=[(0.9**n)*length, (0.9**n)*width, (0.9**n)*height])

