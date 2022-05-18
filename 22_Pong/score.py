from turtle import Turtle

# initalizes font
FONT = ('Tahoma', 40, 'normal')

class Score:

    # initalize scoreboard at the top of the screen
    def __init__(self):
        self.score_one = Turtle()
        self.score_two = Turtle()
        self.score_one.hideturtle()
        self.score_two.hideturtle()
        self.score_one.color("white")
        self.score_two.color("white")
        self.score_one.penup()
        self.score_two.penup()
        self.score_p_one = 0
        self.score_p_two = 0
        self.score_one.goto(40, 235)
        self.score_two.goto(-40, 235)
        self.score_table()

    # writes current table score
    def score_table(self):
        self.score_one.write(f"{self.score_p_one}", False, 'center', font=FONT)
        self.score_two.write(f"{self.score_p_two}", False, 'center', font=FONT)

    # grants 1 point to player one
    def score_player_one(self):
        self.score_one.clear()
        self.score_p_one += 1
        self.score_table()
    
    # grants 1 point to player two
    def score_player_two(self):
        self.score_two.clear()
        self.score_p_two += 1
        self.score_table()