import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c
import links as l

class LINK:
    def __init__ (self, variable, index):
        self.var = variable
        self.i = index
    def make_lN_str (self):
        return "Link-" + self.var + str(self.i)
    def i_after_str(self, string):
        if ('x' in string):
            i = int(string.split('x')[1])
        if ('y' in string):
            i = int(string.split('y')[1])
        if ('z' in string):
            i = int(string.split('z')[1])

        return i + 1

    def Send_Link(self):
        if (self.i == 0):
            posi = [0,0,c.max_height]
            lN = "Head"      
            c.linkNames.append(lN)
            if(self.i in c.random_sensor_locs[0]):
                pyrosim.Send_Cube(lN, pos=posi, size=c.random_sizes_x[self.i], color_name='<material name="Green">', color_code='		<color rgba="0 128 0 1.0"/>')
            else:
                pyrosim.Send_Cube(lN, pos=posi, size=c.random_sizes_x[self.i], color_name='<material name="Cyan">', color_code='		<color rgba="0 191 255 1.0"/>')    
        else:
            if (self.var == "x"):
                random_sizes = c.random_sizes_x
                posi = [c.random_sizes_x[self.i][0]/2, 0, 0]
                i = 0
            elif (self.var == "y"):
                random_sizes = c.random_sizes_y
                posi = [0, c.random_sizes_y[self.i][1]/2, 0]
                i = 1
            elif (self.var == "z"):  # change this to check "z"
                random_sizes = c.random_sizes_z
                posi = [0, 0, c.random_sizes_z[self.i][2]/2]
                i = 2
            lN = self.make_lN_str()
            c.linkNames.append(lN)

            if self.i in c.random_sensor_locs[i]:
                pyrosim.Send_Cube(lN, pos=posi, size=random_sizes[self.i], color_name='<material name="Green">', color_code='		<color rgba="0 128 0 1.0"/>')
            else:
                pyrosim.Send_Cube(lN, pos=posi, size=random_sizes[self.i], color_name='<material name="Cyan">', color_code='		<color rgba="0 191 255 1.0"/>')

class JOINT:
    def __init__(self,link1, link2):
        self.lN1 = link1
        self.lN2 = link2
    def make_jN_str(self):
        return self.lN1.make_lN_str() + "_" + self.lN2.make_lN_str()
    def Send_Joint(self):
        if (self.lN1 == self.lN2):
            raise ValueError("Cannot pass in the same link")
        if (self.lN1.i == 0):
            lN = "Head"
            nextlN = self.lN2.make_lN_str()
            jN = "Head" + "_" + self.lN2.make_lN_str()
            c.jointNames.append(jN)
            if (self.lN2.var == "x"):
                posi = [c.random_sizes_x[self.lN1.i][0]/2, 0, c.max_height]
                jX = "0 1 1"
            if (self.lN2.var == "y"):
                posi = [0, c.random_sizes_x[self.lN1.i][1]/2, c.max_height]
                jX = "0 0 1"
            if (self.lN2.var == "z"):
                posi = [0, 0, c.max_height + c.random_sizes_x[self.lN1.i][2]/2]
                jX = "1 1 0"
            pyrosim.Send_Joint(jN, lN, nextlN, type = "revolute", position = posi, jointAxis = jX)
        if (self.lN1.i >= 1):
            lN = self.lN1.make_lN_str()
            nextlN = self.lN2.make_lN_str()
            jN = self.make_jN_str()
            c.jointNames.append(jN)

            posi = [0,0,0]
            jX = ["1","1","1"]
            
            ##IF STATEMENTS DETERIME THE CHANGE IN X,Y,Z POSITION
            if (self.lN1.var == "x"):
                random_sizes = c.random_sizes_x
                posi[0] = random_sizes[self.lN1.i][0]/2
                jX[0] = str(0)
            if (self.lN1.var == "y"):
                random_sizes = c.random_sizes_y
                posi[1] = random_sizes[self.lN1.i][1]/2 
                jX[1] = str(0)               
            if (self.lN1.var == "z"):
                random_sizes = c.random_sizes_z
                posi[2] = random_sizes[self.lN1.i][2]/2
                jX[2] = str(0)                   
            
            if (self.lN2.var == "x"):
                jX[0] = str(0)
                if (self.lN1.var == self.lN2.var):
                    posi[0] = random_sizes[self.lN1.i][0]
                else:
                    posi[0] = random_sizes[self.lN1.i][0]/2
            if (self.lN2.var == "y"):
                jX[1] = str(0)
                if (self.lN1.var == self.lN2.var):
                    posi[1] = random_sizes[self.lN1.i][1]
                else:
                    posi[1] = random_sizes[self.lN1.i][1]/2
            if (self.lN2.var == "z"):
                jX[2] = str(0)
                if (self.lN1.var == self.lN2.var):
                    posi[2] = random_sizes[self.lN1.i][2]
                else:
                    posi[2] = random_sizes[self.lN1.i][2]/2

            #SENDING IN THE JOINTS DEPENDING ON WHERE THE CHANGES ARE
            jX_str = " ".join(jX)
            pyrosim.Send_Joint(jN, lN, nextlN, type = "revolute", position = posi, jointAxis = jX_str)

def Create_Snakey():
    dir = ["x","y","z"]
    LINKS = []
    for i in range(0, c.bodylen-1):
        LINKS.append(LINK(random.choice(dir), i))
    for i in range(len(LINKS)-1):
        link = LINKS[i]
        next_link = LINKS[i+1]			
        if (i == len(LINKS)-2):
            link.Send_Link()
            max_i= i
        else:
            link.Send_Link()
            Joint = JOINT(link, next_link)
            Joint.Send_Joint()
    # for link in LINKS:
    #     while (len(c.linkNames) < 4*c.bodylen):
    #         for i in range(link.i_after_str(c.linkNames[max_i]), 4*c.bodylen):
    #             next_link = l.LINK(random.choice(dir), i)
    #             print(i)
    #             if (i == 4*c.bodylen-2):
    #                 link.Send_Link()
    #                 max_i= i
    #             else:
    #                 link.Send_Link()
    #                 Joint = l.JOINT(link, next_link)
    #                 Joint.Send_Joint()
    # print(LINKS)

# def Build_Creature():
#     dir = ["x", "y", "z"]
#     LINKS = []

#     link = LINK("x", 0)
#     link.Send_Link()
#     # next_link = LINK("y", 1)
#     # Joint = JOINT(link, next_link)

#     LINKS.append(link)
#     i = 1
#     # LINKS.append(next_link)
#     for link in LINKS:
#         print(link)
#         joint_count = 0
#         # for i in range (1, c.bodylen-1):
#     # for link in LINKS:
#         # if (i == 0):
#         #     link = LINKS[i]
#         #     next_link = LINK(random.choice(dir), i)
#         #     LINKS.append(next_link)
#         # else:
#         # link = LINKS[i]
#         while(i < c.bodylen-1):
#             next_links = [LINK("x", i), LINK("y", i), LINK("z", i)]
#             if not (next_links[0] in LINKS):
#                 LINKS.append(next_links[0])
#                 joint = JOINT(link, next_links[0])
#                 joint.Send_Joint()
#                 next_links[0].Send_Link()
#                 i = i+1
#             if not (next_links[1] in LINKS):
#                 LINKS.append(next_links[1])
#                 joint = JOINT(link, next_links[1])
#                 joint.Send_Joint()
#                 next_links[1].Send_Link()
#                 i = i+1     
#             if not (next_links[2] in LINKS):
#                 LINKS.append(next_links[2])
#                 joint = JOINT(link, next_links[2])
#                 joint.Send_Joint()
#                 next_links[2].Send_Link()
#                 i = i+1          

        
#     print(LINKS)
    # link.Send_Link()
    # Joint.Send_Joint()
    # next_link.Send_Link()
    
            
def Create_Lizardy():
    dir = ["x", "y", "z"]
    random_skel_dir = dir[random.randint(0,2)]
    LINKS =[]
    j = 0
    def build_in_one_dir (d, list):
        for i in range(0,10):
            list.append(l.LINK(d, i))
            j = j+1
        for i in range(len(list)-1):
            link = list[i]
            next_link = list[i+1]		
            if (i == len(list)-2):
                link.Send_Link()
            else:
                link.Send_Link()
                Joint = l.JOINT(link, next_link)
                Joint.Send_Joint()

    build_in_one_dir("y", LINKS)


    # LEGS = [random.randint(0,10) for i in range (len(LINKS))]
    # for i in LEGS:
    #     BUILD_LEGS = []
    #     BUILD_LEGS.append(LINKS[i])
    #     build_in_one_dir("x", BUILD_LEGS)
        


