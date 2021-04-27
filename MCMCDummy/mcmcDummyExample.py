#Markov Chain Example
#Random Walk

import random
import collections
import numpy as np
import scipy.stats as scistat
import matplotlib.pyplot as plt
import math

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

def standardDeviation(ordDict, mean):
    accumulator = 0
    for val in ordDict:
        accumulator += (val - mean)**2
    sd = accumulator / len(ordDict)
    sd = math.sqrt(sd)
    sd = abs(sd - mean) / sd
    return sd

def createGraph(ordDict, mean):
    #Plotting Observed Values
    x_vals = []
    y_vals = []
    for k,v in ordDict.items():
        x_vals.append(k)
        y_vals.append(v)
    plt.plot(x_vals, y_vals, label='observed')

    #Plotting Gaussian For Reference
    stdev1 = standardDeviation(ordDict, mean)
    w_vals = np.arange(30, 70, 0.1)
    z_vals = scistat.norm(mean, stdev1)
    plt.plot(w_vals, z_vals.pdf(w_vals), linestyle='dashed', label='gaussian')

    #Creating Graph
    plt.xlabel('Distance from Origin')
    plt.ylabel('Occurance')
    plt.title('Steps from origin over 10,000 trials')
    plt.legend()

#function calls
trials = 10000
accumulator = 0
x_y_values = {}

for j in range(trials):
    trial = runExperiment()
    accumulator += trial
    if trial not in x_y_values:
        x_y_values.update({trial: 1})
    else:
        x_y_values[trial] += 1
        
for key in x_y_values:
    x_y_values[key] /= trials

average = accumulator / trials
ordered_vals = collections.OrderedDict(sorted(x_y_values.items()))

print("In {} trials, I average {} steps from origin".format(trials, average))

createGraph(ordered_vals, average)
plt.show()

