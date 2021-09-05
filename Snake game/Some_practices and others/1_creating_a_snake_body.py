from turtle import Turtle, Screen


screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("Nokia Snake Game Returns!")
all_position = [(0,0), (-20, 0), (-40, 0)]

for position in all_position:
    a_turtle = Turtle("square")
    a_turtle.speed(0)
    a_turtle.color("white")
    a_turtle.goto(position)









screen.exitonclick()