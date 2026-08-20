import turtle as t
import random

colours = ["CornflowerBlue","DarkOrchid", "TndianRed" , "DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]
tim = t.Turtle()

for i in range(3, 10):
    tim.color(random.choice(colours))
    angle = 360 / i
    for _ in range(i):
        tim.forward(100)
        tim.right(angle)
