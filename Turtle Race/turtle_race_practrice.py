from turtle import Turtle, Screen
import random

length = [2, 10, 12, 20, 30]

tom = Turtle()
tom.shape("turtle")
tom.color("red")
tom.penup()
tom.backward(300)
tom.setheading(90)
tom.forward(100)
tom.setheading(0)
tom.pendown()


tam = Turtle()
tam.shape("turtle")
tam.color("green")
tam.penup()
tam.backward(300)
tam.setheading(0)
tam.pendown()

tim = Turtle()
tim.shape("turtle")
tim.color("blue")
tim.penup()
tim.backward(300)
tim.setheading(270)
tim.forward(100)
tim.setheading(0)
tim.pendown()


for _ in range(25):
    for _ in range(1):
        tim.forward(random.choice(length))
        tam.forward(random.choice(length))
        tom.forward(random.choice(length))


screen = Screen()
screen.exitonclick()