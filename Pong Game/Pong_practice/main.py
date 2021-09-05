from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard
import time

screen = Screen()
screen.setup(1000, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((470, 0))
l_paddle = Paddle((-470, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")



game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.move_ball_y()

    if ball.distance(r_paddle) < 60 and ball.xcor() > 445 or ball.distance(l_paddle) < 60 and ball.xcor() < -445:
        ball.move_ball_x()

    if ball.xcor() > 490:
        scoreboard.l_scored()
        ball.another_turn()
    
    if ball.xcor() < -490:
        scoreboard.r_scored()
        ball.another_turn()

    if scoreboard.r_score >= 5 or scoreboard.l_score >=5:
        scoreboard.game_finish()
        game_on = False









screen.exitonclick()