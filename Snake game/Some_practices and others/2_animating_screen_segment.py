from turtle import Turtle, Screen, xcor
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("Nokia Snake Game Returns!")
screen.tracer(0)


all_position = [(0,0), (-20, 0), (-40, 0)]
segments = []

for position in all_position:
    s_snake = Turtle("square")
    s_snake.penup()
    s_snake.color("white")
    s_snake.goto(position)
    segments.append(s_snake)


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments) - 1, 0, -1):
        x_cor = segments[seg_num - 1].xcor()
        y_cor = segments[seg_num - 1].ycor()
        segments[seg_num].goto(x_cor, y_cor)
    segments[0].forward(20)






screen.exitonclick()