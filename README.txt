For this homework assignment, I edited most of my files in solution.py and constants.py.
In order to get the body of the worm. I created a for-loop that loops through an random
body length, and checks 3 key values for determining how joints are put in.

1. If we are the beginning (and therefore need to put Links and joints at absolute positions)
2. If we are at the first value (therefore only need to put one Links)
3. Else; where the rest of the body is generated based off the previous joint and is
therefore predictable

To help aid in the Create_Brain() section, I also initialized a list that would put all
the links and joint names in a list.

For Create_Brain(), I looped through my joint and link lists, to add synapses for the lists
of sensors that were being added and joints as well.

For determinig where to place the sensors. I created a list that would randomly
generate five values within our body length that would be having the sensors.
In Create_Brain(), I simply looped through this list and put the sensors there.

To obtain a random body length, I simply set my variable for body length to be 
random.randint(0,20)
