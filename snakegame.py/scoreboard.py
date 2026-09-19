from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0 , 250)
        self.color("white")
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()

    def upda_Scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))


    def increase_score(self):
        self.score +=1
        self.clear()
        self.upda_Scoreboard()

    def game_over(self):
        self.color("red")
        self.goto(0 , 0)
        self.write(f"Game is over Your score is  {self.score}", align="center", font=("Arial", 24, "normal"))
        
        
