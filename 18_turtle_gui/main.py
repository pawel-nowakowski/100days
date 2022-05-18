import turtle
from random import randint

turtle_tim = turtle.Turtle()
turtle_tim.shape("turtle")
color_list = ["blue", "green", "red", "purple", "pink", "yellow", "orange", "brown"]
turtle.colormode(255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b

# draw dashed line
def dashed_line():
    for _ in range(30):
        turtle_tim.pendown()
        turtle_tim.forward(3)
        turtle_tim.penup()
        turtle_tim.forward(3)


# draw from triangle to decagon
def polygons():
    for i in range(11)[3:]:
        turtle_tim.color(color_list[i - 3])
        for _ in range(i):
            turtle_tim.forward(100)
            turtle_tim.right(360/i)


def random_walk():
    turtle_tim.width(5)
    # turtle_tim.pensize
    # turtle_tim.speed
    '''steps = int(input("How many steps for random walk? Max is 50."))
    if steps > 50:
        steps = 50'''
    for i in range(100):
        color = random_color()
        turtle_tim.pencolor(color)
        a = randint(0, 3)
        if a == 0:
            turtle_tim.forward(30)
        elif a == 1:
            turtle_tim.backward(30)
        elif a == 2:
            turtle_tim.left(90)
            turtle_tim.forward(30)
        elif a == 3:
            turtle_tim.right(90)
            turtle_tim.forward(30)

def spirograph():
    i = 8
    j = int(360/i)
    turtle_tim.speed(0)
    for _ in range(j):
        turtle_tim.tilt(i)
        turtle_tim.right(i)
        turtle_tim.circle(50)


spirograph()
screen = turtle.Screen()
screen.exitonclick()

# import colorgram
#
# colors = colorgram.extract('spots.jpg', 40)
# list_of_colors = []
# for i in colors:
#     tuple_palette = (i.rgb[0], i.rgb[1], i.rgb[2])
#     list_of_colors.append(tuple_palette)
#
# print(list_of_colors)
# ctrl + /

list_of_colors = [(253, 251, 248), (254, 250, 252), (232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189),
                  (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16),
                  (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8),
                  (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239),
                  (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40),
                  (218, 87, 49), (174, 178, 231), (237, 169, 164), (6, 245, 223), (247, 9, 42), (10, 79, 112),
                  (16, 54, 243), (240, 16, 16)]