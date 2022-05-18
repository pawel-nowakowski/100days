from turtle import Turtle

# constants
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.x_pos = 0
        self.snake_body()

    # creates default snake body
    def snake_body(self):
        for _ in range(3):
            snake = Turtle("square")
            snake.penup()
            snake.color("white")
            snake.goto(self.x_pos, 0)
            self.x_pos -= 20
            self.segments.insert(0, snake)

    # returns position on every single part of snake body except head
    # last elements of the snake body list is head and 0th element of the list is the last part created
    def snake_position(self):
        for i in self.segments[:-1]:
            yield i.pos()

    # adds body body square to food
    def snake_body_increment(self):
        new_pos = self.segments[0].pos()
        snake = Turtle("square")
        snake.penup()
        snake.color("white")
        snake.goto(new_pos)
        self.segments.insert(0, snake)

    # move up if not going down
    def up(self):
        if self.segments[-1].heading() != DOWN:
            self.segments[-1].setheading(UP)

    # move down if not going up
    def down(self):
        if self.segments[-1].heading() != UP:
            self.segments[-1].setheading(DOWN)

    # turn left if not going right
    def left(self):
        if self.segments[-1].heading() != RIGHT:
            self.segments[-1].setheading(LEFT)

    # turn right if not going left
    def right(self):
        if self.segments[-1].heading() != LEFT:
            self.segments[-1].setheading(RIGHT)

    # if input is_moving is false it stops the snake (after game over) and abort this function
    # else it uses index out of range error to move snake's head (as its last element of the list) and then moves
    # rest of the body to new position
    def move(self, is_moving=True):
        if is_moving == False:
            self.dont_move()
            return None
        for pos, seg in enumerate(self.segments):
            try:
                new_pos = self.segments[pos + 1].pos()
                seg.goto(new_pos)
            except (IndexError):
                seg.forward(20)

    # stops moving
    def dont_move(self):
        for seg in self.segments:
            seg.forward(0)


