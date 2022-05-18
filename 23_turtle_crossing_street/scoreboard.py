from turtle import Turtle
FONT = ("Courier", 24, "normal")
GAME_OVER = ("Courier", 28, "bold")

# initalize scoreboard that tells current level
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-220, 260)
        self.level = 1
        self.write(f"Level: {self.level}", False, 'center', font=FONT)
        self.game_done = Turtle()
        self.game_done.hideturtle()

    # when triggered, increment text level
    def levelUp(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", False, 'center', font=FONT)

    # when triggered, write 'game over' at the middle of the screen
    def gameOver(self):
        self.game_done.penup()
        self.game_done.write("Game over", False, 'center', font=GAME_OVER)