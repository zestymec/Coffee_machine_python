from turtle import Turtle, Screen
import turtle


turtle.bgcolor("white")
turtle.speed(0)  

turtle.color("red", "yellow") 

turtle.begin_fill()
while True:
    turtle.forward(200)
    turtle.left(170) 
    if turtle.pos() == (0, 0): 
        break
turtle.end_fill()

turtle.done()

# second way
from turtle import *
start = pos()

while True:
    forward(200)
    left(170)
    if distance(start) < 1:
        break