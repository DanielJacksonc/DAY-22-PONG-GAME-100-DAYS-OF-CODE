from turtle import Turtle


class Score(Turtle):
    def __init__ (self):
        super(). __init__()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 215)
        self.write(self.l_score, align="center", font=("courier", 60, "normal"))
        self.goto(100, 215)
        self.write(self.r_score, align="center", font=("courier", 60, "normal"))



    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()








