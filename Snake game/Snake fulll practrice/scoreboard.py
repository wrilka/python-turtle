from turtle import Turtle
FONT  = ("Arial", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 225)
        self.write(f"Score: {self.score}", align="center", font=FONT,)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=FONT,)

    def game_finish(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align ="center", font=("Arial", 20, "bold") )