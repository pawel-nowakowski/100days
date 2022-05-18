from turtle import Turtle
from config import HIGH_SCORE, new_high_score

FONT = ('Arial', 18, 'normal')
HIGH_SCORE = int(HIGH_SCORE)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score_is = -1
        self.goto(0, 275)
        self.score()


    def score(self):
        # print statement, move, align, font
        self.clear()
        self.score_is += 1
        self.write(f"Your score is {self.score_is}      High score is {HIGH_SCORE}", False, 'center', font=FONT)

    def print_game_over(self):
        if self.score_is > HIGH_SCORE:
            new_high_score(self.score_is)
        gameover = Turtle()
        gameover.goto(0, 0)
        gameover.hideturtle()
        gameover.color("white")
        gameover.hideturtle()
        gameover.penup()
        gameover.write("Game over", False, "center", font=FONT)