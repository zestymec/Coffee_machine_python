from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed(0)

def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)

def move_Left():
    tim.left(10)

def move_Right():
    tim.right(10)


screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="Down", fun=move_backward)
screen.onkey(key="Left", fun=move_Left)
screen.onkey(key="Right", fun=move_Right)
screen.exitonclick()
