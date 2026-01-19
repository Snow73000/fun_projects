from turtle import Turtle

WALL_HEIGHT = 290 # should be half screen height -10 (to make walls visible)
WALL_WIDTH = 390 # should be half screen width -10 (to make walls visible)
WALL_COLOR = "red"
LINE_COLOR = "white"
MOVE_SPEED = "fastest"
DOWN = 270

class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(MOVE_SPEED)
        self.hideturtle()
        self.penup()

    def draw_wall(self):
        self.setposition(WALL_WIDTH, WALL_HEIGHT)
        self.pendown()
        self.color(WALL_COLOR)
        self.goto(WALL_WIDTH, -WALL_HEIGHT)
        self.color(LINE_COLOR)
        self.goto(-WALL_WIDTH, -WALL_HEIGHT)
        self.color(WALL_COLOR)
        self.goto(-WALL_WIDTH, WALL_HEIGHT)
        self.color(LINE_COLOR)
        self.goto(WALL_WIDTH, WALL_HEIGHT)
        self.penup()

    def draw_mid_line(self):
        self.setposition(0, WALL_HEIGHT)
        self.setheading(DOWN)
        self.color(LINE_COLOR)
        while self.ycor() > -WALL_HEIGHT:
            self.pendown()
            self.forward(WALL_HEIGHT / 10.5)
            self.penup()
            self.forward(WALL_HEIGHT / 10.5)