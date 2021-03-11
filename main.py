from turtle import Turtle, Screen
from paddle import Paddle
from blocks import Block
from ball import Ball
from scoreboard import Scoreboard
import time

game_blocks = []
restart_ball = True
game_ends = False
ball_speed = 0.01
COLORS = ["BlueViolet", "chartreuse3", "DarkGoldenrod2", "DarkOrange1", "coral3", "DarkRed"]
screen = Screen()
screen.setup(width=700, height=800)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)


### CREATE INITIAL GAME BLOCKS
def create_blocks():
    global game_blocks
    game_blocks = []
    for color in COLORS:
        for n in range(0, 10):
            xloc = -315 + n * 70
            yloc = 220 + COLORS.index(color) * 25
            game_block = Block(color=color, xloc=xloc, yloc=yloc)
            game_blocks.append(game_block)


create_blocks()
scoreboard = Scoreboard()
ball = Ball()
paddle = Paddle()
screen.update()
screen.listen()

while not game_ends:
    screen.update()

    ### THE BALL ATTACHED TO THE PADDLE AS GAME BEGINS
    while restart_ball:
        screen.update()
        ball.restart_ball()
        if ball.ycor() == -340:
            ball.goto(paddle.xcor(), -340)
        elif ball.ycor() > -340 and scoreboard.lives > 0:
            restart_ball = False
        if scoreboard.lives > 0:
            screen.onkeypress(ball.move, "Up")
            screen.onkeypress(paddle.move_left, "Left")
            screen.onkeypress(paddle.move_right, "Right")
    ball.move()
    time.sleep(ball_speed)

    ### WHEN THE BALL BOUNCE OFF THE WALL
    if ball.xcor() < -338 or ball.xcor() > 338:
        ball.bounce_wall()

    ### WHEN THE BALL FALLS BELOW THE PADDLE
    if ball.ycor() < -400:
        ball.goto(paddle.xcor(), -340)
        restart_ball = True
        scoreboard.lives -= 1
        scoreboard.update()

    ### WHEN THE BALL HITS A BLOCK
    for block in game_blocks:
        if abs(ball.ycor() - block.ycor()) < 20 and abs(ball.xcor() - block.xcor()) < 34:
            ball_speed /= 2
            block.hideturtle()
            block.goto(1000, 1000)
            ball.bounce_block()
            game_blocks.remove(block)
            print(len(game_blocks))
            scoreboard.score += 1
            scoreboard.update()

    ### WHEN THE BALL BOUNCE OFF THE PADDLE
    # if abs(ball.ycor() - paddle.ycor()) < 20 and abs(ball.xcor() - paddle.xcor()) < 49:
    #     ball.bounce_paddle(-1, 1)


    ### WHEN THE BALL BOUNCE OFF THE PADDLE - DEPENDING ON WHERE IT HITS THE PADDLE
    if abs(ball.ycor() - paddle.ycor()) < 20 and 0 < (ball.xcor() - paddle.xcor()) < 20:
        print("1")
        ball.bounce_paddle(1, 1)
    if abs(ball.ycor() - paddle.ycor()) < 20 and 0 > (ball.xcor() - paddle.xcor()) > -20:
        print("2")
        ball.bounce_paddle(-1, 1)
    if abs(ball.ycor() - paddle.ycor()) < 20 and 26 < (ball.xcor() - paddle.xcor()) < 55:
        print("3")
        ball.bounce_paddle(1, 1.5)
    if abs(ball.ycor() - paddle.ycor()) < 20 and -55 < (ball.xcor() - paddle.xcor()) < -26:
        print("4")
        ball.bounce_paddle(-1, 1.5)

    ### WHEN THE BALL BOUNCE OFF CEILING
    if ball.ycor() > 395:
        ball.bounce_block()

    ### WHEN ALL BLOCKS HAVE BEEN TAKEN OUT
    if not game_blocks:
        scoreboard.level += 1
        ball.restart_ball()
        ball.goto(paddle.xcor(), -340)
        restart_ball = True
        scoreboard.update()
        create_blocks()

    ### GAME OVER CONDITIONS
    if scoreboard.lives == 0:
        scoreboard.goto(-215,-20)
        scoreboard.write("GAME OVER", font=("Calibri", 60, "bold"))

    screen.onkeypress(paddle.move_left, "Left")
    screen.onkeypress(paddle.move_right, "Right")
    time.sleep(ball_speed)

screen.update()

screen.exitonclick()
