from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# initialize turtle that player moves
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.setheading(90)
        self.goto(STARTING_POSITION)

    # move up given move_distance
    def moveUp(self):
        if self.ycor() < FINISH_LINE_Y:
            self.forward(MOVE_DISTANCE)

    # move down given move_distance
    def moveDown(self):
        if self.ycor() < FINISH_LINE_Y:
            self.backward(MOVE_DISTANCE)

    # turtle moves to its starting position
    def turtleReset(self):
        self.goto(STARTING_POSITION)