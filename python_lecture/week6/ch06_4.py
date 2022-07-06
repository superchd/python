import turtle
import random

turtle.shape("turtle")
colors = ['red','green','magenta', 'blue', 'black']
turtle.penup( )
turtle.screensize(500,500)
turtle.setup(330,330)
for i in range(11) :
    r = i / 11
    for k in range(11) :
        x = i*20 - 150
        y = k*20 - 150
        s = (1 - i / 11) / 11 * k
        
        turtle.goto( x, y )
        turtle.color(r + s, 0, 0)
        turtle.stamp( )
turtle.done( )
