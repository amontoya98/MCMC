#Monte Carlo Example - Approximating the Area of a Random Circle

import random as rdm
import turtle
import time

global PI
PI = 3.14159

#Function Definitions
def setUp():
    wn = turtle.Screen()
    wn.setup(1000,1000)
    wn.bgcolor("white")
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-500, -500, 500, 500)
    turt = turtle.Turtle()
    turtle.colormode(255)
    turt.up()
    turtle.tracer(1000,25)
    turt.goto(0,0)
    turt.down()
    return turt

def genRandCircle(turt, r):
    turt.up()
    turt.fd(r)
    turt.down()
    turt.lt(90)
    circ = 2 * PI * r
    for _ in range(100):
        turt.fd(circ/100)
        turt.lt(360/100)

def throwDarts(n, turt, r):
    turt.up()
    strikes = 0
    for _ in range(n):
        x = rdm.randint(-500,500)
        y = rdm.randint(-500,500)
        turt.goto(x,y)
        turt.stamp()
        d2 = (x**2) + (y**2)
        if d2 > (r**2):
            turt.color(0,0,0)
            turt.stamp()
        else:
            turt.color(255,0,0)
            turt.stamp()
            strikes += 1
    return strikes
            
#Function Calls
t = setUp()
radius = rdm.randint(1,500)
genRandCircle(t, radius)
throws = 10000
hits = throwDarts(throws, t, radius)

area_t = PI*(radius**2)
area_obs = (hits/throws)*(1000**2)
print("Ratio of Approximated Area: {:.2f}".format(area_obs))
print("Actual Area: {:.2f}".format(area_t))
error = ( abs(area_t - area_obs) / area_t )* 100
print("Percent Error: {:.2f}".format(error))
