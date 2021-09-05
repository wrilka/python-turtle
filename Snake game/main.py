from turtle import Screen
from snake import Snake
from food import Food
from score_board import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("Nokia Snake Game Returns!")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh_food()
        scoreboard.increase_score()
        snake.extend()
    
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.reset_score_board()
        snake.reset_snake()

    for segment in snake.segments[1:len(snake.segments) - 1]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_score_board()
            snake.reset_snake()



screen.exitonclick()