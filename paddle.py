from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("red", "green")
        self.shape("square")
        self.goto(0, -360)
        self.shapesize(stretch_len=5, stretch_wid=1)


    def move_right(self):
        self.setheading(0)
        self.forward(20)

    def move_left(self):
        self.setheading(180)
        self.forward(20)
