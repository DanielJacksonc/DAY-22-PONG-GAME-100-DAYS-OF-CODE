from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super(). __init__()

        self.color("white")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1


    def moving_ball(self):
        x_position = self.xcor() + self.x_move
        y_position = self.ycor() + self.y_move
        self.goto(x_position, y_position)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_ball(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()
        time.sleep(2)




