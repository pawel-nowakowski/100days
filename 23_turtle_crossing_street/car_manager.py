from turtle import Turtle
from random import choice
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREASE = 10

# initalize car that move in x axis from right to left
class CarManager:

    def __init__(self, xPos):
        self.car = Turtle("square")
        self.car.penup()
        self.car.shapesize(stretch_len=2, stretch_wid=1)
        self.car.color(choice(COLORS))
        self.car.setheading(180)
        yPos = randint(-260, 260)
        self.car.goto(xPos, yPos)

    # cause car to move at the given speed
    def carMoving(self, speed):
        self.car.forward(speed)

    # return x coordinate of car
    def xPos(self):
        return self.car.xcor()

    # return y coordinate of car
    def yPos(self):
        return self.car.ycor()
