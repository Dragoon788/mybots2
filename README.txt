For this bipedal robot, I used the robot's orientation to maintain an
upright position and measured how far left the robot moved. 

I accomplished both these tasks using the Select function in parallelHillClimber.py.
For orientation, within the Get_Fitness function for robot.py, I found the orientation of the robot using
the p.GetBasePositionAndOrientation(). From there, since orientation is a Quarternion,
I had to convert it into Euler angles to help me understand how to maintain 
the upright position. To do this I used p.getEulerFromQuaternion() and determined
that an upright position is when a = 0, y = 0, and b = 0. On top of our previous
fitness function that tracked leftward movement by checking whether the distance traveled
was less than the parent, I also used this space to determine whether parent[a] > child[a].
Same procedure was done for the other two Euler angles. This means that our Select()
was designed to pick out robots that moved to the left and maintained an upright position.

