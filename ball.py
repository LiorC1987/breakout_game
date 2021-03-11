from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("red", "green")
        self.shape("circle")
        self.goto(0, -340)
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.x_direction = 10
        self.y_direction = 10

    def move(self):
        x_cor = self.xcor() + self.x_direction
        y_cor = self.ycor() + self.y_direction
        self.goto(x_cor, y_cor)

    def bounce_wall(self):
        self.x_direction = -1 * self.x_direction

    def bounce_block(self):
        self.y_direction = -1 * self.y_direction

    def bounce_paddle(self, direction, intensity):
        self.y_direction = -1 * self.y_direction
        self.x_direction = intensity * direction * 10

    def restart_ball(self):
        self.x_direction = 10
        self.y_direction = 10