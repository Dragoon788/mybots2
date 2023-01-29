#!/usr/bin/python3

import os
from hillclimber import HILL_CLIMBER


#for i in range (0,2):
#	os.system("python3 generate.py")
#	os.system("python3 simulate.py")

hc = HILL_CLIMBER()
hc.Evolve()
