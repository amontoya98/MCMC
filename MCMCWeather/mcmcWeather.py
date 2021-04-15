#MCMC
#Probability of the Weather

import random

#function definitions
def genMarkovDays(n):
    climate = "SR"
    days = ""
    days += random.choice(climate)
    for i in range(1, n):
        if days[i-1] == 'S':
            weather = random.choices(climate, weights=(90,10), k=1)
        elif days[i-1] == 'R':
            weather = random.choices(climate, weights=(50,50), k=1)
        weatherToday = weather[0]
        days += weatherToday
    return days

def calcProbability(string):
    dct = {}
    for letter in string:
        if letter not in dct:
            dct.update({letter: 1})
        else:
            dct[letter] += 1
    for val in dct:
        dct[val] /= len(string)
    return dct

#function calls
chain = genMarkovDays(1000)
probability = calcProbability(chain)

print(probability)
