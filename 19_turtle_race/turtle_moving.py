from turtle import Turtle, Screen

torkoal = Turtle()
screen = Screen()

def forward():
    torkoal.forward(10)

def backward():
    torkoal.backward(10)

def turn_left():
    torkoal.left(10)

def turn_right():
    torkoal.right(10)

def clear():
    torkoal.clear()
    torkoal.penup()
    torkoal.setpos(0, 0)
    torkoal.pendown()

screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
