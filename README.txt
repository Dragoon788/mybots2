For this assignment, I designed a creature that randomly grew in 3D space by creating a function 
within links.py which would create a list of Links that were built off the of the previous link.
A random direction would be chosen in the link's constructor and therefore be built in a random direction.
Then I would loop through and make a joint connecting each of those links.

The connection of the joints was the difficult part of the this assignment. Based on what
the direction of the first link and the second link, we would have to mathmatically determine
where the joint should be placed.

The diagram here explains that process:
https://imgur.com/a/0hASMc7


The Brain was created simply by looping through all my stored joints in an array and 
adding motors to each joint. For the sensors and synapses, I had a random list of x,y,z locations.
If my block was in any of those indexes, it would turn green and a synapse would be added.

Evolution was affected fitness in 3 ways:

1. Weights of the links were changed
2. Body shaped was changed through building off different joints
3. Shapes of the cubes were changed

Fitness was selected for in the negative y direction, so the graph illustrates 25 populations over 150 generations selecting fo the best negative y fitness.

