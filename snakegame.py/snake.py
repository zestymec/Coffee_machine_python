from turtle import Turtle

starting_position = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.segments = []

    def create_snake(self):
        for position in starting_position:
            new_segment = Turtle("square")
            new_segment.color(self.color)
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(20)
