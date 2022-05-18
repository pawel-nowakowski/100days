from turtle import Turtle
from time import sleep

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.ball_speed = 0.1
    # moves ball in a given direction, sleep added to slow down a game
    def moving(self, x, y):
        sleep(self.ball_speed)
        x_cor = self.xcor() + x
        y_cor = self.ycor() + y
        self.goto(x_cor, y_cor)

    # resets the ball position after it goes out of screen
    def reset(self):
        sleep(1)
        self.goto(0, 0)