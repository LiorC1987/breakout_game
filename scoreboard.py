from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(170, 350)
        self.write("Score: 0", font=("Calibri", 30, "bold"))
        self.goto(-310, 350)
        self.write("Lives: 5", font=("Calibri", 30, "bold"))
        self.goto(-85, 345)
        self.write("LEVEL 1", font=("Calibri", 40, "bold"))
        self.hideturtle()
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.score = 0
        self.lives = 5
        self.level = 1

    def update(self):
        self.clear()
        self.goto(170, 350)
        self.write(f"Score: {self.score}", font=("Calibri", 30, "bold"))
        self.goto(-310, 350)
        self.write(f"Lives: {self.lives}", font=("Calibri", 30, "bold"))
        self.goto(-85, 345)
        self.write(f"LEVEL {self.level}", font=("Calibri", 40, "bold"))