import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager, STARTING_MOVE_DISTANCE, MOVE_INCREASE
from scoreboard import Scoreboard
from random import randint

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
scoreboard = Scoreboard()
cars = []

# create 12 cars at the start in random position
for i in range(12):
    xPos = randint(-180, 300)
    car = CarManager(xPos)
    cars.append(car)

game_is_on = True

screen.update()
screen.listen()
# key binding for p1 and p2
screen.onkeypress(key="Up", fun=turtle.moveUp)
screen.onkeypress(key="Down", fun=turtle.moveDown)


while game_is_on:
    n = randint(1, 12)
    time.sleep(0.1)
    screen.update()
    for car in cars:
        car.carMoving(STARTING_MOVE_DISTANCE)
        # disable unused cars
        if car.xPos() <= -320:
            cars.remove(car)
        # if car is too close to turtle the game is over, there is issue that moving backwards will close distance
        # too soon
        if abs(turtle.xcor() - car.xPos()) < 20 and abs(turtle.ycor() - car.yPos()) < 20:
            scoreboard.gameOver()
            game_is_on = False
            break
    # creates random cars, minimum 11 at play
    if n % 9 == 0 or len(cars) < 11:
        car = CarManager(320)
        cars.append(car)
    # if turtle crosses top, reset its position and speed up the cars
    if turtle.ycor() >= FINISH_LINE_Y:
        scoreboard.levelUp()
        turtle.turtleReset()
        STARTING_MOVE_DISTANCE += MOVE_INCREASE
    print(len(cars))

screen.exitonclick()

