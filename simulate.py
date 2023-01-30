#!/usr/bin/python3

from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1]
simulation = SIMULATION(sys.argv[1])
simulation.Run()


