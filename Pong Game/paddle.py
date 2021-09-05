from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.goto(position)
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(5, 0.4)
    

    def up(self):
        y_cor = self.ycor() + 50
        self.goto(self.xcor(), y_cor)
    
    def down(self):
        y_cor = self.ycor() - 50
        #if self.ycor < -290:
        self.goto(self.xcor(), y_cor)