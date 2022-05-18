from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        random_x = randint(-275, 275)
        random_y = randint(-275, 275)
        self.goto(random_x, random_y)

    # spawns random food after the first one was eaten
    def new_food(self):
        random_x = randint(-275, 275)
        random_y = randint(-275, 275)
        self.goto(random_x, random_y)