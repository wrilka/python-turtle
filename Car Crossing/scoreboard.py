from turtle import Turtle, clear

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.player_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)

    def player_level(self):
        self.clear()
        self.goto(-230, 260)
        self.write(f"LEVEL:{self.level}", align="center", font=FONT)
    
    def level_increase(self):
        self.level += 1
        self.player_level()