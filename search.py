#!/usr/bin/env python3

import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER


#for i in range (0,2):
#	os.system("python3 generate.py")
#	os.system("python3 simulate.py")

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()
