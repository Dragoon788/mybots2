#!/usr/bin/env python3

import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import pickle
import constants as c


#for i in range (0,2):
#	os.system("python3 generate.py")
#	os.system("python3 simulate.py")

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()

phc.Show_Best(phc.Best_Parents)


with open('phc' + str(9) + '.pickle', 'wb') as f:
    pickle.dump(phc, f)
