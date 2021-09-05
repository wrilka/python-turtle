from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Python Snake Game?")
all_postitions = [(0, 0), (-20, 0), (-40, 0)]
snake_segments = []
screen.tracer(0)


for pos in all_postitions:
    segment = Turtle()
    segment.penup()
    segment.color("white")
    segment.shape("square")
    segment.goto(pos)
    snake_segments.append(segment)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.2)
    
    for seg in range(len(snake_segments) - 1, 0, -1):
        x_cor = snake_segments[seg - 1].xcor()
        y_cor = snake_segments[seg - 1].ycor()
        snake_segments[seg].goto(x_cor, y_cor)
   
    snake_segments[0].forward(20)












screen.exitonclick()