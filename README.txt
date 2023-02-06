For this bipedal robot, I used the robot's orientation to maintain an
upright position and was able to maintain that position.

I accomplished both these tasks using the Select function in parallelHillClimber.py.
For orientation, within the Get_Fitness function for robot.py, I found the orientation of the robot using
the p.GetBasePositionAndOrientation(). From there, since orientation is a Quarternion,
I had to convert it into Euler angles to help me understand how to maintain 
the upright position. To do this I used p.getEulerFromQuaternion() and determined
that an upright position is when a = 0, y = 0, and b = 0. I used the same procedure
for selecting movement fitness, and applied it to balancing. I added the sums of the 
Euler angles and iterated through multiple generations until I was left with an upright standing
Robot. Each generation selected for the Euler angles sums that were less than the previous generation.

Later I tried to implement walking by implementing a movement fitness that determined which robots
moved the most to the left. Unfortunately, this didn't really allow the robot to walk. Overall,
the robot focused on the balancing rather than walking.


