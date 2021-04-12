#Monte Carlo Example - Approximating the Area of an Irregular Shape

import random
import turtle
import time

#Function Definitions
def genRandTriangle(turt):
    turt.up()
    turt.fillcolor("blue")
    turt.begin_fill()
    x_0 = random.randint(0,100)
    y_0 = random.randint(0,100)
    turt.goto(x_0,y_0)
    turt.down()
    for _ in range(2):
        x = random.randint(0,100)
        y = random.randint(0,100)
        turt.goto(x,y)
    turt.goto(x_0,y_0)
    turt.end_fill()

def throwDarts(n, turt, canvas):
    t.up()
    misses = 0
    for _ in range(n):
        x = random.randint(0,100)
        y = random.randint(0,100)
        turt.goto(x,y)
        color = getPixelColor(x,y,canvas)
        print(color)
        if color == 'white':
                misses += 1
        return misses

def getPixelColor(a,b, canvas):
        b = -b
        ids = canvas.find_overlapping(a,b,a,b)
        if ids:
            index = ids[-1]
            color = canvas.itemcget(index, "fill")
            if color != '':
                    return color.lower()
        return 'white'

#Function Calls
wn = turtle.Screen()
wn.bgcolor("white")
canvas = wn.getcanvas()
turtle.setworldcoordinates(0, 0, 100, 100)
t = turtle.Turtle()
t.shape("circle")
genRandTriangle(t)

t.speed(0)
hits = 1000 - throwDarts(1000, t, canvas)
print(hits)
