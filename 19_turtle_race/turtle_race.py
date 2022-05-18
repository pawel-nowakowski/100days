from turtle import Turtle, Screen
from random import randint
screen = Screen()
screen.setup(width=500, height=400)
names = ["tim", "jim", "bim", "kim", "sim", "zim"]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput(title="Make your bet.",
                            prompt="Chose a color of turtle who you think will win: ")
i = 0  # colors index
j = 100 # y position

for index, name in enumerate(names):
    names[index] = Turtle(shape="turtle")
    names[index].color(colors[i])
    names[index].penup()
    names[index].goto(x=-230, y=j)
    i += 1
    j -= 40

x = -230
while x < 230:
    for i in range(len(names)):
        rand_nr = randint(1, 10)
        names[i].forward(rand_nr)
        x = int(names[i].pos()[0])
        if x >= 230:
            if user_bet == colors[i]:
                print("Congratulations, your turtle has won.")
            else:
                print(f"Turtle with {colors[i]} color won.")
            break

screen.exitonclick()