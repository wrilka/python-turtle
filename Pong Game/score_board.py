from turtle import Turtle, clear

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(70, 240)
        self.write(f"{self.l_score}", align="center", font=("Courier", 30, "normal"))
        self.goto(-70, 240)
        self.write(f"{self.r_score}", align="center", font=("Courier", 30, "normal"))

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
