import turtle as t

tim = t.Turtle()

for i in range(1, 10):
    angle = 360 / i
    for _ in range(i):
        tim.forward(100)
        tim.right(angle)
