import turtle
from random import choice

list_of_colors = [(253, 251, 248), (254, 250, 252), (232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189),
                  (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16),
                  (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8),
                  (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239),
                  (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40),
                  (218, 87, 49), (174, 178, 231), (237, 169, 164), (6, 245, 223), (247, 9, 42), (10, 79, 112),
                  (16, 54, 243), (240, 16, 16)]

torkoal = turtle.Turtle()
torkoal.hideturtle()
turtle.colormode(255)
torkoal.pensize(15)
torkoal.penup()
torkoal.setpos(-100, -100)
for i in range(10):
    torkoal.setpos(-100, i * 30 - 100)
    for j in range(10):
        torkoal.pendown()
        color_ = choice(list_of_colors)
        torkoal.pencolor(color_)
        torkoal.forward(0)
        torkoal.penup()
        torkoal.forward(30)


screen = turtle.Screen()
screen.exitonclick()