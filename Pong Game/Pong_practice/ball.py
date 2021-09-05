from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.move_x = 10
        self.move_y = 10
        self.ball_speed = 0.05
    

    def move_ball(self):
        self.goto(self.xcor() + self.move_x, self.ycor() + self.move_y)
    
    def move_ball_y(self):
        self.move_y *= -1
    
    def move_ball_x(self):
        self.ball_speed *= 0.9
        self.move_x *= -1
    
    def another_turn(self):
        self.ball_speed = 0.05
        self.goto(0, 0)
        self.move_x *= -1