from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_scoring()
    
    def update_scoring(self):
        self.clear()
        self.goto(100, 230)
        self.write(f"{self.r_score}", font=("Arial", 50, "normal"))
        self.goto(-100, 230)
        self.write(f"{self.l_score}", font=("Arial", 50, "normal"))


    def r_scored(self):
        self.r_score += 1
        self.update_scoring()
    
    def l_scored(self):
        self.l_score += 1
        self.update_scoring()
    
    def game_finish(self):
        self.goto(0, 0)
        self.color("white")
        self.write("GAME OVER!", align="center", font=("Arial", 40, "normal"))
    