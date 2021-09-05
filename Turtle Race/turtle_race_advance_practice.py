from turtle import Turtle, Screen, width
import random

screen = Screen()
screen.setup(1000, 600)


race_on = False
all_cor = [50, 90, 130, 170, 210, 250]
all_color = ["red", "blue", "green", "purple", "yellow", "orange"]
all_turtles = []


for index_turtle in range(0, 6):
    st = Turtle(shape="turtle")
    st.speed("normal")
    st.color(all_color[index_turtle])
    st.penup()
    st.goto(-470, all_cor[index_turtle])
    all_turtles.append(st)


u_guess = screen.textinput("Which Turtle Will Win The Race?", "Which Color do you wanna Choose?")

if u_guess:
    race_on = True

while race_on:
    for e_turtle in all_turtles:
        e_turtle.forward(random.randint(0, 10))
        if e_turtle.xcor() > 457:
            e_turtle.setheading(270)
            e_turtle.forward(random.randint(0, 10))
            if e_turtle.ycor() > -257:
                race_on = False
                win_color = e_turtle.pencolor()
                if win_color == u_guess:
                    print(f"'YAY' Your Turtle Won the Race! Which was {win_color.title()} Turtle.")
                else:
                    print(f"You Lose! {win_color.title()} Turtle Won the Race!!.")




screen.exitonclick()
