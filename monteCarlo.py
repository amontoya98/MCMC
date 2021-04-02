#Monte Carlo Example - Approximating the Area of an Irregular Shape

import random
import turtle

#Function Definitions
def genRandShape():
	pass

def throwDart():
	pass

#Function Calls
done = False

while not done:
	yn = str(input("Would you like to Perform a Monte Carlo Simulation? ==> (Y/N)"))
	if yn == 'N':
		done = True
	else:
		getRandShape()
