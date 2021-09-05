from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time 


screen = Screen()
screen.bgcolor("black")
screen.setup(500, 500)
screen.title("My FIrst Snake Game! ")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_over = False
while game_over != True:
    screen.update()
    time.sleep(0.01)
    snake.move()

    if snake.head.distance(food) < 15:
        snake.extend_segment()
        food.refreh_food()
        scoreboard.increase_score()

    if snake.head.xcor() > 250 or snake.head.xcor() < -250 or snake.head.ycor() > 250 or snake.head.ycor() < -250:
        scoreboard.game_finish()
        game_over = True
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_finish()
            game_over = True














screen.exitonclick()