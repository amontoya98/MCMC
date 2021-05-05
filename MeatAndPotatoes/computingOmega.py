#Random Matrix Generator

#X is the sample space of 3x3 square matrices with entries in {0,1}
# such that no two 1's are adjacent

#Find |X|

import numpy as np
import random as rand
import collections
import matplotlib.pyplot as plt
import csv

#function definitions
def genMatrix(dimension):
    M = np.zeros( (dimension,dimension) )
    
    for i in range(dimension):
        for j in range(dimension):
            if i == j == 0:
                M[i][j] += rand.randint(0,1)
            elif i == 0:
                if M[i][j-1] != 1:
                    M[i][j] += rand.randint(0,1)
            else:
                 if M[i][j-1] != 1 and M[i-1][j] != 1:
                    M[i][j] += rand.randint(0,1)
    return M

def compareMatrices(mat, zero, dimension):
    for i in range(dimension):
        for j in range(dimension):
            if mat[i][j] == zero[i][j]:
                continue
            else:
                return 1
    return 0

def runTrial(zero, dimension, chain):
    matches = 0
    for i in range(chain):
        matches += compareMatrices(zero, genMatrix(dimension), dimension)
    return matches

        
def write_csv(ordDict):
    with open('results_file.csv', mode='w') as results_file:
        results_writer = csv.writer(results_file, delimiter=':', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for k, v in ordDict.items():
            results_writer.writerow([k, v])

#function calls
size = 3
chainLength = 10000
trials = 1000
M_0 = np.zeros( (size, size) )
results = {}

for _ in range(trials):
    result = chainLength//(chainLength - runTrial(M_0, size, chainLength))
    if result not in results:
        results.update({result: 1})
    else:
        results[result] += 1

for key in results:
    results[key] /= trials

ordered_results = collections.OrderedDict(sorted(results.items()))

write_csv(ordered_results)


