from turtle import Turtle, xcor 

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(1)
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.05

    def move_ball(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_ball(self):
        self.ball_speed = 0.05
        self.goto(0, 0)
        self.x_move *= -1

    def score(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center")
