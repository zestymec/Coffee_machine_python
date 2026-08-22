# painting from extractedcolors
from index import color_list
import turtle as turtle_module
import random

turtle_module.colormode(255)

tim = turtle_module.Turtle()

tim.penup()
tim.speed('fastest')
tim.hideturtle()
tim.setheading(225)
tim.forward(350)
tim.setheading(0)
number_of_dots = 101 

for dots in range(1 , number_of_dots):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dots % 10 == 0 :
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()