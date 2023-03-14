from parallelHillClimber import PARALLEL_HILL_CLIMBER
import pickle
phc_no = int(input("Which phc would you like to look at? (No. < 10): "))

if (phc_no > 11):
    raise KeyError ("There is no phc with that number")

with open('Best_Robots/phc' + str(phc_no) + '.pickle', 'rb') as f:
    p1 = pickle.load(f)

p1.Show_Best(p1.Best_Parents)