import turtle as t
import random

tmu = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


tmu.speed("fastest")
current_heading = tmu.heading()
gameover = False
while not gameover: 
    tmu.circle(100)
    tmu.color(random_color())
    tmu.setheading(tmu.heading() + 1)
    position = tmu.heading()
    if current_heading == position:
        gameover = True



screen = t.Screen()
screen.exitonclick()
