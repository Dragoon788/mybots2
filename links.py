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
        self.i = c.gindex
        self.tracker = {"x": 0, "y": 0, "z":0}
        c.gindex = c.gindex + 1

        self.xMin = c.abs_pos[0] - c.random_sizes[self.i][0]
        self.xMax = c.abs_pos[0] + c.random_sizes[self.i][0]
        self.yMin = c.abs_pos[1] - c.random_sizes[self.i][1]
        self.yMax = c.abs_pos[1] + c.random_sizes[self.i][1]
        self.zMin = c.abs_pos[2] - c.random_sizes[self.i][2]
        self.zMax = c.abs_pos[2] + c.random_sizes[self.i][2]

    def make_lN_str (self):
        return "Link-" + self.var + str(self.i)

    def Send_Link(self):
        self.check_for_int()
        if (self.i == 0):
            posi = [0,0,c.max_height]
            lN = self.make_lN_str()     
            c.linkNames.append(lN)
            if(self.i in c.random_sensor_locs):
                pyrosim.Send_Cube(lN, pos=posi, size=c.random_sizes[self.i], color_name='<material name="Green">', color_code='		<color rgba="34 139 34 1.0"/>')
            else:
                pyrosim.Send_Cube(lN, pos=posi, size=c.random_sizes[self.i], color_name='<material name="Blue">', color_code='		<color rgba="0 0 139 1.0"/>')    

                c.link_positions.append([self.xMin, self.xMax, self.yMin, self.yMax, self.zMin, self.zMax])       
        else:
            if (self.var == "x"):
                random_sizes = c.random_sizes
                posi = [c.random_sizes[self.i][0]/2, 0, 0]
            elif (self.var == "y"):
                random_sizes = c.random_sizes
                posi = [0, c.random_sizes[self.i][1]/2, 0]
            elif (self.var == "z"):  # change this to check "z"
                random_sizes = c.random_sizes
                posi = [0, 0, c.random_sizes[self.i][2]/2]
            lN = self.make_lN_str()
            c.linkNames.append(lN)

            if self.i in c.random_sensor_locs:
                pyrosim.Send_Cube(lN, pos=posi, size=random_sizes[self.i], color_name='<material name="Green">', color_code='		<color rgba="34 139 34 1.0"/>')
            else:
                pyrosim.Send_Cube(lN, pos=posi, size=random_sizes[self.i], color_name='<material name="Blue">', color_code='		<color rgba="0 0 139 1.0"/>')

            c.link_positions.append([self.xMin, self.xMax, self.yMin, self.yMax, self.zMin, self.zMax])

    def check_for_int(self):
        for pos in c.link_positions:
            if (self.zMax > pos[4] and self.zMax < pos[5]):
                c.random_sizes[self.i][2] = c.random_sizes[self.i][2]/1.03
            elif (self.zMin < pos[5] and self.zMin > pos[4]):
                c.random_sizes[self.i][2] = c.random_sizes[self.i][2]/1.03

            elif (self.yMax > pos[2] or self.yMax < pos[3]):
                c.random_sizes[self.i][1] = c.random_sizes[self.i][1]/1.03
            elif (self.yMin < pos[3] or self.yMin > pos[2]):
                c.random_sizes[self.i][1] = c.random_sizes[self.i][1]/1.03

            elif (self.xMax > pos[0] and self.xMax < pos[1]):
                c.random_sizes[self.i][0] = c.random_sizes[self.i][0]/1.03
            elif (self.xMin < pos[1] or self.xMin > pos[0]):
                c.random_sizes[self.i][0] = c.random_sizes[self.i][0]/1.03
        # print(c.random_sizes)
            #     if (self.xMin < pos[1]):
            #         dif = pos[1] - self.xMin
            #         c.random_sizes[self.i][0] = c.random_sizes[self.i][0] - dif
            #     elif (self.xMax > pos[0]):
            #         dif = self.xMax - pos[pos][0]
            #         c.random_sizes[self.i][0] = c.random_sizes[self.i][0] - dif

            # if (self.zMax > pos[4] or self.zMin < pos[5]):
            #     if (self.yMin < pos[3]):
            #         dif = pos[3] - self.yMin
            #         c.random_sizes[self.i][1] = c.random_sizes[self.i][1] - dif
            #     elif (self.yMax > pos[2]):
            #         dif = self.yMax - pos[2]
            #         c.random_sizes[self.i][1] = c.random_sizes[self.i][1] - dif


            # if (self.xMin > pos[0] and self.xMax < pos[1] and self.yMin > pos[2] and self.yMax < pos[3]):
            #     if (self.zMin < pos[5]):
            #         dif = pos[5] - self.zMin
            #         c.random_sizes[self.i][2] = c.random_sizes[self.i][2] - dif
            #     elif (self.zMax > pos[4]):
            #         dif = self.zMax - pos[4]
            #         c.random_sizes[self.i][2] = c.random_sizes[self.i][2] - dif


class JOINT:
    def __init__(self,link1, link2):
        self.lN1 = link1
        self.lN2 = link2
        
    def make_jN_str(self):
        # if (self.make_jN_str() in c.jointNames):
        #     raise ("Joint already exists")
        return self.lN1.make_lN_str() + "_" + self.lN2.make_lN_str()
    def Send_Joint(self):
        if (self.lN1 == self.lN2):
            raise ValueError("Cannot pass in the same link")
        if (self.lN1.i == 0):
            lN = self.lN1.make_lN_str()
            nextlN = self.lN2.make_lN_str()
            jN = lN + "_" + nextlN
            c.jointNames.append(jN)
            if (self.lN2.var == "x"):
                posi = [c.random_sizes[self.lN1.i][0]/2, 0, c.max_height]
                jX = "0 0 1"
            if (self.lN2.var == "y"):
                posi = [0, c.random_sizes[self.lN1.i][1]/2, c.max_height]
                jX = "0 0 1"
            if (self.lN2.var == "z"):
                posi = [0, 0, c.max_height + c.random_sizes[self.lN1.i][2]/2]
                jX = "1 0 0"
            pyrosim.Send_Joint(jN, lN, nextlN, type = "revolute", position = posi, jointAxis = jX)
        if (self.lN1.i > 0):
            lN = self.lN1.make_lN_str()
            nextlN = self.lN2.make_lN_str()
            jN = self.make_jN_str()
            c.jointNames.append(jN)

            posi = [0,0,0]
            jX = ["1","1","1"]
            
            ##IF STATEMENTS DETERIME THE CHANGE IN X,Y,Z POSITION
            if (self.lN2.var == "x"):
                posi[0] = c.random_sizes[self.lN1.i][0]/2
                jX[0] = str(0)
                jX[1] = str(0)
            if (self.lN2.var == "y"):
                posi[1] = c.random_sizes[self.lN1.i][1]/2 
                jX[0] = str(0)     
                jX[1] = str(0)          
            if (self.lN2.var == "z"):
                posi[2] = c.random_sizes[self.lN1.i][2]/2
                jX[1] = str(0)
                jX[2] = str(0)
                   
            
            if (self.lN2.var == "x"):
                # jX[0] = str(0)
                if (self.lN1.var == self.lN2.var):
                    posi[0] = c.random_sizes[self.lN1.i][0]
                else:
                    posi[0] = c.random_sizes[self.lN1.i][0]/2
            if (self.lN2.var == "y"):
                # jX[1] = str(0)
                if (self.lN1.var == self.lN2.var):
                    posi[1] = c.random_sizes[self.lN1.i][1]
                else:
                    posi[1] = c.random_sizes[self.lN1.i][1]/2
            if (self.lN2.var == "z"):
                # jX[2] = str(0)
                if (self.lN1.var == self.lN2.var):
                    posi[2] = c.random_sizes[self.lN1.i][2]
                else:
                    posi[2] = c.random_sizes[self.lN1.i][2]/2

            #SENDING IN THE JOINTS DEPENDING ON WHERE THE CHANGES ARE
            jX_str = " ".join(jX)
            print(jX_str)
            pyrosim.Send_Joint(jN, lN, nextlN, type = "revolute", position = posi, jointAxis = jX_str)
    def Connect_Links(self):
        if (self.lN1.tracker[self.lN2.var] == 1):
            raise ("Cannot append to link in the same direction twice")
        elif(self.lN2.tracker[self.lN1.var] == 1):
            raise ("Cannot append to link in the same direction twice")
        elif (self.lN1.make_lN_str() in c.linkNames):
            self.Send_Joint()
            self.lN2.Send_Link()
            self.lN1.tracker[self.lN2.var] = 1
        elif(self.lN2.make_lN_str() in c.linkNames):
            self.Send_Joint()
            self.lN1.Send_Link()
            self.lN2.tracker[self.lN1.var] = 1
        elif(self.lN2.make_lN_str() in c.linkNames and self.lN1.make_lN_str() in c.linkNames):
            raise ("Cannot build from two existing links")
        else: 
            self.lN1.Send_Link()
            self.Send_Joint()
            self.lN2.Send_Link()


def Create_Snakey():
    dir = ["x","y","z"]
    LINKS = []
    for i in range(0, c.bodylen-1):
        LINKS.append(LINK(random.choice(dir), c.gindex))
    for i in range(len(LINKS)-1):
        link = LINKS[i]
        next_link = LINKS[i+1]			
        if (i == len(LINKS)-2):
            link.Send_Link()
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
def Build_Creature():
    dir = ["x","y", "z"]
    LINKS = []
    terminal_edges = []

    # c.linkNames.append(link.make_lN_str())
    starting_link = LINK("x", 5)


    for i in range(0, c.bodylen):
        selected_input = random.choice(dir)
    # Randomly select number of times to call Joint.connect
        num_calls = random.randint(1, 3)

        # Keep track of which inputs have been called
        called_inputs = []

        # Call Joint.connect a random number of times
        for i in range(num_calls):
            # If all inputs have been called, break out of loop
            if len(called_inputs) == 3:
                break
            if (c.curr_bodylen == c.bodylen):
                break
            # If selected input has already been called, skip iteration
            if selected_input in called_inputs:
                selected_input = random.choice(list(set(dir) - set(called_inputs)))
            link2 = LINK(selected_input, 5)
            joint = JOINT(starting_link, link2)
            c.curr_bodylen = c.curr_bodylen+1

            # Call Joint.connect with selected input
            joint.Connect_Links()

            # Add selected input to list of called inputs
            called_inputs.append(selected_input)
            terminal_edges.append(link2)
        if (i == c.bodylen-1):
            break
        starting_link = random.choice(terminal_edges)
        terminal_edges.remove(starting_link)

def test_first_connect():
    link = LINK("x", 0)
    link2 = LINK("y", 0)
    link3 = LINK("z", 0)
    link4 = LINK("x", 0)

    joint1 = JOINT(link, link2)
    c.bodylen = 2
    # joint2 = JOINT(link, link2)
    joint3 = JOINT(link, link3)
    joint4 = JOINT(link, link4)

    joint1.Connect_Links()
    joint3.Connect_Links()
    # joint4.Connect_Links()

    # joint4.Connect_Links()
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
    def build_in_one_dir (d, list):
        for i in range(0,10):
            list.append(l.LINK(d, c.gindex))
        for i in range(len(list)-1):
            link = list[i]
            next_link = list[i+1]		
            if (i == len(list)-2):
                link.Send_Link()
            else:
                link.Send_Link()
                Joint = l.JOINT(link, next_link)
                Joint.Send_Joint()
    # build_in_one_dir(d, LINKS)
    # for link in LINKS:
    #     useless_list = []
    #     print("THIS IS THE LENGHT O F RANODM:" + str(len(c.random_sizes_x)))
    #     for i in range(0,10):
    #         useless_list.append(l.LINK("x", c.gindex))
    #         c.gindex = c.gindex+1
    #     for i in range(len(useless_list)-1):
    #         print(link)
    #         link = useless_list[i]
    #         useless_list[0] = link
    #         next_link = useless_list[i+1]		
    #         if (i == len(useless_list)-2):
    #             link.Send_Link()
    #         else:
    #             print(link.i)
    #             link.Send_Link()
    #             Joint = l.JOINT(link, next_link)
    #             Joint.Send_Joint()

    # LEGS = [random.randint(0,10) for i in range (len(LINKS))]
    # for i in LEGS:
    #     BUILD_LEGS = []
    #     BUILD_LEGS.append(LINKS[i])
    #     build_in_one_dir("x", BUILD_LEGS)
        


