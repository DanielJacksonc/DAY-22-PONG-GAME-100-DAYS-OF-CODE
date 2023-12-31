from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600 )
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((360, 0))
r_paddle.color("yellow")
l_paddle = Paddle((-360, 0))


ball = Ball()
score = Score()



screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

Game_on = True
while Game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.moving_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
#detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() <-340:
        ball.bounce_x()
    #
    # #This defines right sided paddle misss
    if ball.xcor() > 380:
        ball.reset_ball()
        score.l_point()
    #
    if ball.xcor() < -380:
        ball.reset_ball()
        score.r_point()



























screen.exitonclick()