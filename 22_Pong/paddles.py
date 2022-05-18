from turtle import Turtle

class Paddle(Turtle):

    # allows to initialize the paddle, will be used to add paddle to left and right side of the screen
    def __init__(self, x_pos):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = 0
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(self.x_pos, self.y_pos)

    # moves paddle up by the number specified in self.y_pos
    def moveUp(self):
        if self.y_pos <= 220:
            self.y_pos += 20
            self.goto(self.x_pos, self.y_pos)

    # moves paddle down by the number specified in self.y_pos
    def moveDown(self):
        if self.y_pos >= -220:
            self.y_pos -= 20
            self.goto(self.x_pos, self.y_pos)

    # returns current xcor of the paddle
    def x_cord(self):
        self.xcor()

    # returns current ycor of the paddle
    def y_cord(self):
        self.ycor()