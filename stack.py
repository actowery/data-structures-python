#these functions were created following along with
#http://algosaur.us/data-structures-basics/
import random

#Fills array with random integers
#params:        size: size of the array output / number of elements
#               rng: upper bound integer for random selection
def fillRandArray(size,  rng):
    myary = []
    print("Creating an array starting with "+ str(size) +" random numbers with range 1-"+str(rng))
    for i in range (1,  size):
        myary.append(random.randint(0, rng))
    print(myary)
    return myary


def push(s, elem):
    s.append(elem)
    print("You have added " + str(s[len(s)-1]))
    print("Now in array:")
    print (s)
    return s
#here the very first index is removed, at the front of the line
#remember, the first index is 0!
def customPop(s):
    print("You have deleted " + str(s[len(s)-1]))
    s.pop(len(s)-1)
    print("Now in array:")
    print (s)
    return s





#here is an example of a stack working with random pushes and pops:
stack_example = fillRandArray(7, 100)
for x in range (0,7):
	coinflip = random.randint(0,1)
	if coinflip:
		#we will pop
		stack_example = customPop(stack_example)
	else:
		#we will append
		y = random.randint(1,100)
		stack_example = push(stack_example, y)
