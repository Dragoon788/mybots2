import numpy
import pybullet as p
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c
import links as l



class LINK:
    def __init__ (self, variable, solution, prev_pos):
        self.var = variable
        self.i = solution.gindex
        self.tracker = {"x": 0, "y": 0, "z":0}
        self.abs_pos = [prev_pos[0], prev_pos[1], prev_pos[2]]
        self.s = solution
        solution.gindex = solution.gindex + 1

        if (self.var == "x"):
            self.abs_pos[0] = self.abs_pos[0] + (self.s.random_sizes[self.i][0]/2)
        elif (self.var == "y"):
            self.abs_pos[1] = self.abs_pos[1] + (self.s.random_sizes[self.i][1]/2)
        elif (self.var == "z"):  
            self.abs_pos[2] = self.abs_pos[2] + (self.s.random_sizes[self.i][2]/2)

        if (self.i == 0):
            self.abs_pos = [0,0, solution.max_height]

        self.xMin = self.abs_pos[0] - self.s.random_sizes[self.i][0]
        self.xMax = self.abs_pos[0] + self.s.random_sizes[self.i][0]
        self.yMin = self.abs_pos[1] - self.s.random_sizes[self.i][1]
        self.yMax = self.abs_pos[1] + self.s.random_sizes[self.i][1]
        self.zMin = self.abs_pos[2] - self.s.random_sizes[self.i][2]
        self.zMax = self.abs_pos[2] + self.s.random_sizes[self.i][2]   
        
        solution.link_positions.append(self.abs_pos)
        solution.minsxmax.append([self.xMin, self.xMax, self.yMin, self.yMax, self.zMin, self.zMax])         


    def make_lN_str (self):
        return "Link-" + self.var + str(self.i)

    def Send_Link(self):

        if (self.i == 0):
            posi = [0,0,self.s.max_height]
            lN = self.make_lN_str()     
            self.s.linkNames.append(lN)
            if(self.i in self.s.random_sensor_locs):
                pyrosim.Send_Cube(lN, pos=posi, size=self.s.random_sizes[self.i], color_name='<material name="Green">', color_code='		<color rgba="0 0 100 1.0"/>')
            else:
                pyrosim.Send_Cube(lN, pos=posi, size=self.s.random_sizes[self.i], color_name='<material name="Blue">', color_code='		<color rgba="2 1 139 1.0"/>')    
            self.s.links.append(self)


                # c.link_positions.append([self.xMin, self.xMax, self.yMin, self.yMax, self.zMin, self.zMax])       
        else:
            self.check_for_int()
            if (self.var == "x"):
                random_sizes = self.s.random_sizes
                posi = [random_sizes[self.i][0]/2, 0, 0]
                # print(random_sizes[self.i])
            elif (self.var == "y"):
                random_sizes = self.s.random_sizes
                posi = [0, random_sizes[self.i][1]/2, 0]
            elif (self.var == "z"):  # change this to check "z"
                random_sizes = self.s.random_sizes
                posi = [0, 0, random_sizes[self.i][2]/2]

            ## Checking for intersections
            

            lN = self.make_lN_str()
            self.s.linkNames.append(lN)

            if self.i in self.s.random_sensor_locs:
                pyrosim.Send_Cube(lN, pos=posi, size=random_sizes[self.i], color_name='<material name="Green">', color_code='		<color rgba="0 0 100 1.0"/>')
            else:
                pyrosim.Send_Cube(lN, pos=posi, size=random_sizes[self.i], color_name='<material name="Blue">', color_code='		<color rgba="1 1 139 1.0"/>')
            self.s.links.append(self)

            # c.link_positions.append([self.xMin, self.xMax, self.yMin, self.yMax, self.zMin, self.zMax])
        # self.check_for_int()
    def Send_Existing_Link(self):

        if (self.i == 0):
            posi = [0,0,self.s.max_height]
            lN = self.make_lN_str()     

            if(self.i in self.s.random_sensor_locs):
                pyrosim.Send_Cube(lN, pos=posi, size=self.s.random_sizes[self.i], color_name='<material name="Green">', color_code='		<color rgba="0 0 100 1.0"/>')
            else:
                pyrosim.Send_Cube(lN, pos=posi, size=self.s.random_sizes[self.i], color_name='<material name="Blue">', color_code='		<color rgba="2 1 139 1.0"/>')    

                # c.link_positions.append([self.xMin, self.xMax, self.yMin, self.yMax, self.zMin, self.zMax])       
        else:
            self.check_for_int()
            if (self.var == "x"):
                random_sizes = self.s.random_sizes
                posi = [self.s.random_sizes[self.i][0]/2, 0, 0]
                # c.abs_pos[0] = 
            elif (self.var == "y"):
                random_sizes = self.s.random_sizes
                posi = [0, self.s.random_sizes[self.i][1]/2, 0]
            elif (self.var == "z"):  # change this to check "z"
                random_sizes = self.s.random_sizes
                posi = [0, 0, self.s.random_sizes[self.i][2]/2]
            lN = self.make_lN_str()

            if self.i in self.s.random_sensor_locs:
                pyrosim.Send_Cube(lN, pos=posi, size=random_sizes[self.i], color_name='<material name="Green">', color_code='		<color rgba="0 0 100 1.0"/>')
            else:
                pyrosim.Send_Cube(lN, pos=posi, size=random_sizes[self.i], color_name='<material name="Blue">', color_code='		<color rgba="1 1 139 1.0"/>')

    def check_for_int(self):
        def x_check():
            for pos in self.s.minsxmax:
                if (self.xMax > pos[0] and self.xMax < pos[1]):
                    xdif = self.xMax - pos[0]
                    # c.random_sizes[self.i][0] = c.random_sizes[self.i][0] - dif
                    return [True, xdif]
                elif (self.xMin > pos[0] and self.xMin < pos[1]):
                    xdif = pos[1] - self.xMin
                    # c.random_sizes[self.i][0] = c.random_sizes[self.i][0] - dif
                    return [True, xdif]
                else:
                    return [False, 0]
        def y_check():
            for pos in self.s.minsxmax:
                if (self.yMax > pos[2] and self.yMax < pos[3]):
                    ydif = self.yMax - pos[2]
                    # c.random_sizes[self.i][1] = c.random_sizes[self.i][1] - dif
                    return [True, ydif]
                elif (self.yMin > pos[2] and self.yMin < pos[3]):
                    ydif = pos[3] - self.yMin 
                    # c.random_sizes[self.i][1] = c.random_sizes[self.i][1] - dif
                    return [True, ydif]
                else:
                    return [False, 0]
        def z_check():
            for pos in self.s.minsxmax:
                if (self.zMax > pos[4] and self.zMax < pos[5]):
                    zdif = self.zMax - pos[4]
                    # c.random_sizes[self.i][2] = c.random_sizes[self.i][2] - dif
                    return [True,zdif]
                elif (self.zMin > pos[4] and self.zMin < pos[5]):
                    zdif = pos[5] - self.zMin
                    # c.random_sizes[self.i][2] = c.random_sizes[self.i][2] - dif
                    return [True, zdif]
                else:
                    return [False, 0]
        if (x_check()[0] and y_check()[0] and z_check()[0]):
            # self.s.random_sizes[self.i][0] = self.s.random_sizes[self.i][0] - x_check()[1]
            # self.s.random_sizes[self.i][1] = self.s.random_sizes[self.i][1] - y_check()[1]
            # self.s.random_sizes[self.i][2] = self.s.random_sizes[self.i][2] - z_check()[1]
            # print ("IT OVERLAPS!", self.xMin, self.xMax, self.yMin, self.yMax, self.zMin, self.zMax)
            pass
                
class JOINT:
    def __init__(self,link1, link2, solution):
        self.lN1 = link1
        self.lN2 = link2
        self.s = solution
        
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
            self.s.jointNames.append(jN)
            if (self.lN2.var == "x"):
                posi = [self.s.random_sizes[self.lN1.i][0]/2, 0, self.s.max_height]
                jX = "0 0 1"
            if (self.lN2.var == "y"):
                posi = [0, self.s.random_sizes[self.lN1.i][1]/2, self.s.max_height]
                jX = "0 0 1"
            if (self.lN2.var == "z"):
                posi = [0, 0, self.s.max_height + self.s.random_sizes[self.lN1.i][2]/2]
                jX = "1 0 0"
            pyrosim.Send_Joint(jN, lN, nextlN, type = "revolute", position = posi, jointAxis = jX)
            self.s.joints.append(self)
        if (self.lN1.i > 0):
            lN = self.lN1.make_lN_str()
            nextlN = self.lN2.make_lN_str()
            jN = self.make_jN_str()
            self.s.jointNames.append(jN)

            posi = [0,0,0]
            jX = ["1","1","1"]
            
            ##IF STATEMENTS DETERIME THE CHANGE IN X,Y,Z POSITION
            if (self.lN2.var == "x"):
                posi[0] = self.s.random_sizes[self.lN1.i][0]/2
                jX[0] = str(0)
                jX[1] = str(0)
            if (self.lN2.var == "y"):
                posi[1] = self.s.random_sizes[self.lN1.i][1]/2 
                jX[0] = str(0)     
                jX[1] = str(0)          
            if (self.lN2.var == "z"):
                posi[2] = self.s.random_sizes[self.lN1.i][2]/2
                jX[1] = str(0)
                jX[2] = str(0)
                   
            
            if (self.lN2.var == "x"):
                # jX[0] = str(0)
                if (self.lN1.var == self.lN2.var):
                    posi[0] = self.s.random_sizes[self.lN1.i][0]
                else:
                    posi[0] = self.s.random_sizes[self.lN1.i][0]/2
            if (self.lN2.var == "y"):
                # jX[1] = str(0)
                if (self.lN1.var == self.lN2.var):
                    posi[1] = self.s.random_sizes[self.lN1.i][1]
                else:
                    posi[1] = self.s.random_sizes[self.lN1.i][1]/2
            if (self.lN2.var == "z"):
                # jX[2] = str(0)
                if (self.lN1.var == self.lN2.var):
                    posi[2] = self.s.random_sizes[self.lN1.i][2]
                else:
                    posi[2] = self.s.random_sizes[self.lN1.i][2]/2

            #SENDING IN THE JOINTS DEPENDING ON WHERE THE CHANGES ARE
            jX_str = " ".join(jX)
            # print(jX_str)
            pyrosim.Send_Joint(jN, lN, nextlN, type = "revolute", position = posi, jointAxis = jX_str)
            self.s.joints.append(self)
    def Connect_Links(self):
        if (self.lN1.tracker[self.lN2.var] == 1):
            raise ("Cannot append to link in the same direction twice")
        elif(self.lN2.tracker[self.lN1.var] == 1):
            raise ("Cannot append to link in the same direction twice")
        elif (self.lN1.make_lN_str() in self.s.linkNames):
            self.Send_Joint()
            self.lN2.Send_Link()
            self.lN1.tracker[self.lN2.var] = 1
        elif(self.lN2.make_lN_str() in self.s.linkNames):
            self.Send_Joint()
            self.lN1.Send_Link()
            self.lN2.tracker[self.lN1.var] = 1
        elif(self.lN2.make_lN_str() in self.s.linkNames and self.lN1.make_lN_str() in c.linkNames):
            raise ("Cannot build from two existing links")
        else: 
            self.lN1.Send_Link()
            self.Send_Joint()
            self.lN2.Send_Link()
    def Send_Existing_Joint(self):
        if (self.lN1 == self.lN2):
            raise ValueError("Cannot pass in the same link")
        if (self.lN1.i == 0):
            lN = self.lN1.make_lN_str()
            nextlN = self.lN2.make_lN_str()
            jN = lN + "_" + nextlN
            if (self.lN2.var == "x"):
                posi = [self.s.random_sizes[self.lN1.i][0]/2, 0, self.s.max_height]
                jX = "0 0 1"
            if (self.lN2.var == "y"):
                posi = [0, self.s.random_sizes[self.lN1.i][1]/2, self.s.max_height]
                jX = "0 0 1"
            if (self.lN2.var == "z"):
                posi = [0, 0, self.s.max_height + self.s.random_sizes[self.lN1.i][2]/2]
                jX = "1 0 0"
            pyrosim.Send_Joint(jN, lN, nextlN, type = "revolute", position = posi, jointAxis = jX)
        if (self.lN1.i > 0):
            lN = self.lN1.make_lN_str()
            nextlN = self.lN2.make_lN_str()
            jN = self.make_jN_str()

            posi = [0,0,0]
            jX = ["1","1","1"]
            
            ##IF STATEMENTS DETERIME THE CHANGE IN X,Y,Z POSITION
            if (self.lN2.var == "x"):
                posi[0] = self.s.random_sizes[self.lN1.i][0]/2
                jX[0] = str(0)
                jX[1] = str(0)
            if (self.lN2.var == "y"):
                posi[1] = self.s.random_sizes[self.lN1.i][1]/2 
                jX[0] = str(0)     
                jX[1] = str(0)          
            if (self.lN2.var == "z"):
                posi[2] = self.s.random_sizes[self.lN1.i][2]/2
                jX[1] = str(0)
                jX[2] = str(0)
                   
            
            if (self.lN2.var == "x"):
                # jX[0] = str(0)
                if (self.lN1.var == self.lN2.var):
                    posi[0] = self.s.random_sizes[self.lN1.i][0]
                else:
                    posi[0] = self.s.random_sizes[self.lN1.i][0]/2
            if (self.lN2.var == "y"):
                # jX[1] = str(0)
                if (self.lN1.var == self.lN2.var):
                    posi[1] = self.s.random_sizes[self.lN1.i][1]
                else:
                    posi[1] = self.s.random_sizes[self.lN1.i][1]/2
            if (self.lN2.var == "z"):
                # jX[2] = str(0)
                if (self.lN1.var == self.lN2.var):
                    posi[2] = self.s.random_sizes[self.lN1.i][2]
                else:
                    posi[2] = self.s.random_sizes[self.lN1.i][2]/2

            #SENDING IN THE JOINTS DEPENDING ON WHERE THE CHANGES ARE
            jX_str = " ".join(jX)
            # print(jX_str)
            pyrosim.Send_Joint(jN, lN, nextlN, type = "revolute", position = posi, jointAxis = jX_str)


def Build_Creature(solution):
    dir = ["x","y", "z"]
    terminal_edges = []

    # c.linkNames.append(link.make_lN_str())
    starting_link = LINK("x", solution, [0,0,0])
    # print("THIS IS MY STARTING  LINKS ABS POS", starting_link.abs_pos)
    

    for i in range(0, solution.bodylen):
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
            if (solution.curr_bodylen == solution.bodylen):
                break
            # If selected input has already been called, skip iteration
            if selected_input in called_inputs:
                selected_input = random.choice(list(set(dir) - set(called_inputs)))
            link2 = LINK(selected_input, solution, starting_link.abs_pos)
            joint = JOINT(starting_link, link2, solution)
            solution.curr_bodylen = solution.curr_bodylen+1

            # Call Joint.connect with selected input
            joint.Connect_Links()

            # Add selected input to list of called inputs
            called_inputs.append(selected_input)
            terminal_edges.append(link2)
        if (i == solution.bodylen-1):
            break
        if (len(terminal_edges) != 0):
            starting_link = random.choice(terminal_edges)
            terminal_edges.remove(starting_link)
        # print(len(solution.links))
    # print(solution.link_positions)


def Build_Existing_Creature(solution):
    for joint in solution.joints:
        joint.Send_Existing_Joint()
    for link in solution.links:
        link.Send_Existing_Link()


