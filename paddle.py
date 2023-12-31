from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        self.position = position
        super(). __init__()

        self.shape("square")
        self.color("white")
        # paddle.hideturtle()
        self.turtlesize(stretch_len=0.7, stretch_wid=4)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
