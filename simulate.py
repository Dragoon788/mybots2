#!/usr/bin/python3

from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
simulation = SIMULATION(directOrGUI, solutionID)
# print("THRUUREWIOHAFPOSIHFOSDJFAN AISJFPASIOJDFASPIDJA ISOFJ PASIOFJ IA")
simulation.Run()

#print(1)
#print(2)
#print(3)
#print(4)
#print(5)
#
simulation.Get_Fitness()


