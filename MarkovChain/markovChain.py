#Markov Chain Example
#Random Walk

import random

#function definitions

def tossCoin():
    toss = random.randint(1,2)
    return toss

#function calls
walks = 100
distance = 0

for i in range(walks):
    flip = tossCoin()
    if flip == 1:
        distance += 1

print("After {} flips, I am {} steps from origin".format(walks, distance))
