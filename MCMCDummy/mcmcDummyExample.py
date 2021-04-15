#Markov Chain Example
#Random Walk

import random

#function definitions

def tossCoin():
    toss = random.randint(1,2)
    return toss

def runExperiment():
    walks = 100
    distance = 0
    for i in range(walks):
        flip = tossCoin()
        if flip == 1:
            distance += 1
    return distance 

#function calls
trials = 10000
accumulator = 0
for j in range(trials):
    accumulator += runExperiment()

average = accumulator / trials

print("In {} trials, I average {} steps from origin".format(trials, average))
