## Opening Remarks
This project focuses on creating a randomly shaped, and generated robot that grows in 3D space and evolves for movement along the x-direction. Much of the code utililzed was built off the work of the **Ludobots Subreddit**. The Subreddit served as inspiration for concepts and implemenation, as I furthered my understanding by using concepts from the learning guide.

Here is the Ludobots Subreddit: https://www.reddit.com/r/ludobots/

## Creation of Robots
The Construction of the robots depends mostly on the implementation of Link and Joint Classes within links.py, while solution.py stored information for individual robots (#of joints, # of sensors, etc.). Solution.py is also responsible for ultimately putting otgether the robot using the Link and Joint Classes.

Robots can grow in 3D because of my invariant that robots only grow in the positive x,y,z directions. Build_Creature in links.py, highlights how this works where a list keeps of which directions have been added to already to make sure two links aren't placed inside one another. Choosing a random direction, the links can choose any terminal edge from our links to build off of.

[[[![alt text]([http://url/to/img.png](https://imgur.com/vBev0gt)](https://imgur.com/vBev0gt))](https://imgur.com/vBev0gt)
](https://imgur.com/vBev0gt)

The connection of the joints was the difficult part of the this assignment. Based on what
the direction of the first link and the second link, we would have to mathmatically determine
where the joint should be placed.

The diagram here explains that process:


The Brain was created simply by looping through all my stored joints in an array and 
adding motors to each joint. For the sensors and synapses, I had a random list of x,y,z locations.
If my block was in any of those indexes, it would turn green and a synapse would be added.

## Mutating Robots

## Evolving Robots

## Running the Code
