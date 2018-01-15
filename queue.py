#these functions were created following along with
#http://algosaur.us/data-structures-basics/
import random
#other necessary functions to keep the above ones as dry as possible:

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

#below is a queue structure, there we follow a FIFO structure
q = []
#this means here when we add/append to the list, it goes to
#the end of the array
def insert(q, elem):
    q.append(elem)
    print("You have added " + str(q[len(q)-1]))
    print("Now in array:")
    print (q)
    return q
#here the very first index is removed, at the front of the line
#remember, the first index is 0!
def delete(q):
    print("You have deleted " + str(q[0]))
    q.pop(0)
    print("Now in array:")
    print (q)
    return q


#here is an example of a stack working with random pushes and pops:
stack_example = fillRandArray(7, 100)
for x in range (0,5):
	coinflip = random.randint(0,1)
	if coinflip:
		#we will pop
		stack_example = delete(stack_example)
	else:
		#we will append
		y = random.randint(1,100)
		stack_example = insert(stack_example, y)



