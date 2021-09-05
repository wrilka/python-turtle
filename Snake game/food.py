from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed(0)
        self.refresh_food()

    def refresh_food(self):
        r_x_cor = random.randint(-280, 280)
        r_y_cor = random.randint(-280, 280)
        self.goto(r_x_cor, r_y_cor)