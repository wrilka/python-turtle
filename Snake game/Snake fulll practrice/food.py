from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.refreh_food()
        

    def refreh_food(self):
        x_cor = random.randint(-230, 230)
        y_cor = random.randint(-230, 230)
        self.goto(x_cor, y_cor)