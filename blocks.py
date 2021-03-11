from turtle import Turtle


class Block(Turtle):
    def __init__(self, color, xloc, yloc):
        super().__init__()
        self.penup()
        self.color(color)
        self.shape("square")
        self.goto(xloc, yloc)
        self.shapesize(stretch_len=3.4, stretch_wid=1)
