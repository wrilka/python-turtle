from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
t.pensize(3)

def move_forward():
    t.forward(10)


def move_backward():
    t.backward(10)

def move_left():
    t.setheading(t.heading() + 10)

def move_right():
    t.setheading(t.heading() - 10)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(key = "s", fun = move_backward)
screen.onkey(key = "a", fun = move_left)
screen.onkey(key = "d", fun = move_right)
screen.onkey(clear, "c")
screen.exitonclick()