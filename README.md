## Video Submission Links:
![Untitled video - Made with Clipchamp](https://user-images.githubusercontent.com/109482739/225162294-50ecf76b-8662-4db3-a52b-ced579e7aa8b.gif)

2-min Video: https://youtu.be/PF2M9zw214k

## Opening Remarks
This project focuses on creating a randomly shaped, and generated robot that grows in 3D space and evolves for movement along the x-direction. Much of the code utililzed was built off the work of the **Ludobots Subreddit**. The Subreddit served as inspiration for concepts and implemenation, as I furthered my understanding by using concepts from the learning guide.

Here is the Ludobots Subreddit: https://www.reddit.com/r/ludobots/

## Creation of Robots
The Construction of the robots depends mostly on the implementation of Link and Joint Classes within links.py, while solution.py stored information for individual robots (#of joints, # of sensors, etc.). Solution.py is also responsible for ultimately putting otgether the robot using the Link and Joint Classes:

![vBev0gt - Imgur](https://user-images.githubusercontent.com/109482739/225128071-700f0834-ac9b-423f-99e2-e808e7d7e39d.jpg)

Robots can grow in 3D because of my invariant that robots only grow in the positive x,y,z directions. Build_Creature in links.py, highlights how this works where a list keeps of which directions have been added to already to make sure two links aren't placed inside one another. Choosing a random direction, the links can choose any terminal edge from our links to build off of:

![Brain Construction - AL 396 - Imgur](https://user-images.githubusercontent.com/109482739/225128756-ba112af9-8fba-485a-be74-754a20fdec25.jpg)

Depending on which side we are appending the next link, we would need to move the change the Joint and it's axis to match the side correctly. This involved correctly identifying the shape of the link being attached as well as its direction.

The Brain was created simply by looping through all my stored joints in an array and 
adding motors to each joint. For the sensors and synapses, I had a random list of x,y,z locations.
If my block was in any of those indexes, it would turn green and a synapse would be added.

## Mutating Robots
For the mutation of robots, parallelHillClimber.py and solution.py handled most of the load of mutating and keep track of all our mutated children. Mutating the robots - which occured at each spawning of the children - involves two main components: 

  1. Changing the shape of the body and the size of the blocks
  2. Changing the weights and location of sensors Neurons

![Blank diagram (3)](https://user-images.githubusercontent.com/109482739/225190726-6c2d59ad-ea29-4148-8587-0df629e140dc.png)

The mutation did not change body length and # of sensor neurons, but it focused on developing new body shapes that were efficient for movement and identifying how the location of sensor Neurons aid in movement. Mutation happens by copying the parent in solution.py and allowing some of the values to change and pick new random variables.

![Brain Construction - AL 396 - Imgur](https://user-images.githubusercontent.com/109482739/225132356-e756ede3-2c6c-4ace-a5b3-a7ca68612566.png)

## Evolving Robots
parallelHillClimber.py handles the evolution of parents and the selection for a certain fitness. This is done in the Evolve function where a child is made by copying the parent and then reseting and allowing certain values to change (new sizes of links, new sensor locs, etc.) Then if the chosen fitness is better for the child, those children would go on and evolve themselves. 

![Blank diagram (2)](https://user-images.githubusercontent.com/109482739/225134306-24531955-c018-400d-aed2-3e40160004e6.png)

What we're left with is an evolved creature that is designed for the task we desire.

## Final Results from Research
For the final project, I ran a population of 10 robots over 500 generations for 10 random seeds. As a result, I ended with 50,000 simulations. More often than not the starting robot varied greatly from the starting robot and was hardly recognizable.

![Robot  9](https://user-images.githubusercontent.com/109482739/225157878-256d26e0-b355-409c-807e-6e847bdc851b.png)


The plot shows the evolution of 10 robots who evolve over 500 generationsThe robot tries a series of body shape and orientations that lead to the best morphology that succeeds at moving along the x-axis. More often than not, I found that the less complex the structure (the smaller the number of links), the better the robots performed. When they were more complicated, the weight of the body plus the chance there would be not enough sensors was greater. As a result, the less complex bodies tended to do better.

All the Graphs can be located here on imgur, representing the all 10 random seeds of population size 10:
[https://imgur.com/a/qT2MTYu](https://imgur.com/a/qT2MTYu)

I also analyzed the failures of the best robot ancestors by saving the data of some parallelHillClimbers that we've seen across my graphs. I concluded that when the shapes became more complex and jumbled (despite still having the same number of links), they tended to have trouble moving. As concluded above, this information from my program tells me a greater number of less complex structures moved better. 

Evolution got stuck whenever the robots had found the best solution early on. This resulted in a plateauing you can see in certain graphs provided. 

## Running the Code
You can also run your own simulation to evolve a robot that moves in the x-axis by navigating to the click.py file within the code, and run that file. 

<img width="771" alt="Screen Shot 2023-03-14 at 4 00 57 PM" src="https://user-images.githubusercontent.com/109482739/225135296-b0da983b-950f-4ca9-a62c-439e728470b9.png">

**Currently the code is optimized for running 500 generations with a population size of 10 (ran 10 times to reach a total of 50,000 simulations)
You can change these numbers within constants.py.**

Rather than running your own simulation, or you can run pre-existing robots that I found were the best robots from each of my random seeds after 500 generations. To run these, navigate to show_best.py and run the file with an input later for a number (0-9).

<img width="763" alt="Screen Shot 2023-03-14 at 4 02 46 PM" src="https://user-images.githubusercontent.com/109482739/225135581-70398f64-bb17-4af3-bedf-4387974acd2b.png">
<img width="653" alt="Screen Shot 2023-03-14 at 4 03 14 PM" src="https://user-images.githubusercontent.com/109482739/225135669-254ddbe3-f61d-4894-81c9-d9dc1c01aa3d.png">


