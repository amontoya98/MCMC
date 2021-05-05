#Analyzing Data

import csv
import matplotlib.pyplot as plt

#function definitions
def createGraph(ordDict):
    x_vals = []
    y_vals = []
    for k,v in ordDict.items():
        x_vals.append(k)
        y_vals.append(v)
    plt.plot(x_vals, y_vals, label='observed')
    #Creating Graph
    plt.xlabel('Omega')
    plt.ylabel('Occurances')
    plt.title('Appoximated Size of Omega')
    plt.legend()

def mean(ordDict):
    acc = 0
    n=0
    for k,v in ordDict.items():
        acc += k*v
        n+= v
    mean = acc / n
    return mean

#function calls
results = {}

with open('results_file.csv', mode='r') as results_file:
    csv_reader = csv.reader(results_file, delimiter=':')
    for row in csv_reader:
        results.update({float(row[0]):float(row[1])})

print("Mean = ", mean(results))
createGraph(results)
plt.show()



            
