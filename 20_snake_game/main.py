from turtle import Screen
from snake_game import Snake
from food import Food
from score import Scoreboard
from time import sleep
import config

SCREEN_WIDTH = int(config.SCREEN_WIDTH)
SCREEN_HEIGHT = int(config.SCREEN_HEIGHT)
# set up screen for snake game
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

# initialize snake, random food spawn and scoreboard
snake = Snake()
food = Food()
sb = Scoreboard()

snakes_head = snake.segments[-1]
screen.listen()
# key bindings for snake
screen.onkeypress(key=config.MOVE_UP, fun=snake.up)
screen.onkeypress(key=config.MOVE_DOWN, fun=snake.down)
screen.onkeypress(key=config.MOVE_LEFT, fun=snake.left)
screen.onkeypress(key=config.MOVE_RIGHT, fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()

    # consume a food if snake is nearby
    if snakes_head.distance(food) < 15:
        food.new_food()
        snake.snake_body_increment()
        sb.score()

    # collision with wall
    if snakes_head.xcor() > 280 or snakes_head.xcor() < -280 or snakes_head.ycor() > 280 or snakes_head.ycor() < -280:
        sb.print_game_over()
        snake.move(False)
        game_is_on = False

    # collision with tail
    for i in snake.segments[:-1]:
        if snakes_head.distance(i) < 10:
            sb.print_game_over()
            snake.move(False)
            game_is_on = False


screen.exitonclick()

