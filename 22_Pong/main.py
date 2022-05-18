from turtle import Screen
from paddles import Paddle
from ball import Ball
from score import Score

# ball speed definied
BALL_SPEED = 10

# set up the screen for the game
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# create two paddles, ball and scoreboard to play
pad_one = Paddle(350) # right paddle
pad_two = Paddle(-350) # left paddle
ball = Ball()
score = Score()

game_is_on = True
screen.update()
screen.listen()
# key binding for p1 and p2
screen.onkeypress(key="Up", fun=pad_one.moveUp)
screen.onkeypress(key="Down", fun=pad_one.moveDown)
screen.onkeypress(key="w", fun=pad_two.moveUp)
screen.onkeypress(key="s", fun=pad_two.moveDown)

# x, y cords
y = BALL_SPEED
x = BALL_SPEED

while game_is_on:
    ball.moving(x, y)
    screen.update()

    # bounce the ball from up and down
    if ball.ycor() == 290:
        y *= -1
    if ball.ycor() == -290:
        y *= -1

    # bounce off the paddle
    if ball.xcor() == pad_one.xcor() - 20 and pad_one.ycor() + 50 >= ball.ycor() >= pad_one.ycor() - 50 or ball.xcor(
    ) == pad_two.xcor() + 20 and pad_two.ycor() + 50 >= ball.ycor() >= pad_two.ycor() - 50:
        ball.ball_speed *= 0.9 # increases ball speed by reducing sleep time
        x *= -1

    # resets the ball if it goes out of screen and give a 1 point to a player
    if ball.xcor() >= 410 or ball.xcor() <= -410:
        if ball.xcor() >= 410:
            score.score_player_two()
            x *= -1
        elif ball.xcor() <= -410:
            score.score_player_one()
            x *= -1
        ball.ball_speed = 0.1 # resets the ball speed
        ball.reset()
        ball.moving(x, y)

screen.exitonclick()