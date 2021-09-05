from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.goto(position)
        self.shape("square")
        self.penup()
        self.shapesize(5, 0.5)
        self.color("white")

    
    def up(self):
        self.goto(self.xcor(), self.ycor() + 60)

    
    def down(self):
        self.goto(self.xcor(), self.ycor() - 60)
    
    