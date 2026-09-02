from turtle import Turtle, Screen
import random

is_race_on = False
Screen = Screen()
Screen.setup(width=500, height=400)
decision = Screen.textinput(
    title="Make your decision", prompt="Which trutle will win the race? Enter a code :"
)
colors = ["red","blue","pink","green","purple","orange"]
yaxis = 200
all_turtle = []
for turtle in range(0,6):
    turtle = Turtle(shape="turtle")
    color = random.choice(colors)
    turtle.color(color)
    turtle.penup()
    turtle.goto (x=-250 , y=yaxis)
    yaxis -= 40
    all_turtle.append(turtle)


if decision:
    is_race_on = True
while  is_race_on:
    for turtle in all_turtle:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


Screen.exitonclick()
