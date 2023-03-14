#!/usr/bin/python3

from simulation import SIMULATION
import sys

# directOrGUI = sys.argv[1]
# solutionID = sys.argv[2]
simulation = SIMULATION(sys.argv[1], sys.argv[2])

simulation.Run()
simulation.Get_Fitness()




