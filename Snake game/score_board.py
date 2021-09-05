from turtle import Turtle, mode

FONT = ("Arial", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as h_sc:
            self.high_score = int(h_sc.read())
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.score_board()

    def score_board(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.high_score}" , align="center", font=FONT)
    
    def reset_score_board(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as high_s:
                high_s.write(f"{self.high_score}")
        self.score = 0
        self.score_board()

    def increase_score(self):
        self.score += 1
        self.score_board()