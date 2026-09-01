from turtle import Turtle, Screen
import random

Screen = Screen()
# Screen.setup(width=500, height=400)
# decision = Screen.textinput(
#     title="Make your decision", prompt="Which trutle will win the race? Enter a code :"
# )
colors = ["red","blue","pink","green","purple","orange"]

for turtle in range(0,6):
    turtle = Turtle(shape="turtle")
    color = random.random(colors)
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=-250 , y=200)



Screen.exitonclick()
